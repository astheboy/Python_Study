
import openai
import os
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render, HttpResponse
from django.template import RequestContext
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

file = "topics.txt"
keyword = ''

# topics.txt 파일에서 키워드를 추출하는 함수


def extract_keywords_from_file(file):
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, file)
    with open(file_path, "r") as f:
        text = f.read()
    keywords = text.strip().split(",")
    selecttext = ''
    for keyword in keywords:
        selecttext += f'<a href="../creat/{keyword.strip()}">{keyword.strip()}</a> | '
    return selecttext

# 글에서 주요 단어을 chatgpt에 물어 리스트로 추출하는 함수


def word_of_text(text):
    prompt = f"Please separate the text into words and display only nouns in Korean (regardless of duplication). : '{text}'"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=400,
        n=1,
        stop=None,
        timeout=10,
    )
    words = response.choices[0].text.strip()

    # words를 ,로 나누어서 리스트로 만들기
    words = words.split(',')
    return words

# 각 단어의 국어 사전 검색 결과를 가져오는 함수


def get_word_meaning(word):

    url = f"https://ko.dict.naver.com/search.nhn?sLn=kr&searchOption=all&query={word}"
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, 'html.parser')
    if soup.select_one('span.txt_box') is not None:
        meaning = soup.select_one('span.txt_box').text
    else:
        meaning = '뜻을 찾을 수 없습니다.'
    return meaning

# 생성한 텍스트에서 중심 문장을 추출하는 함수


def summarize_text(text):
    prompt = f"Find the center sentence of the following text.: '{text}'"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=200,
        n=1,
        stop=None,
        timeout=10,
    )
    summary = response.choices[0].text.strip()
    return summary

# 텍스트 생성 함수


def generate_text(keyword):
    context = {'article': '', 'summary': ''}
    prompt = f"다음 키워드를 주제로 한 짧은 글을 생성해 주세요. 키워드: '{keyword}' "
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=1000,
        n=1,
        stop=None,
        timeout=10,
    )
    article = response.choices[0].text.strip()
    summary = summarize_text(article)
    if not article:
        context = {'오류': '죄송합니다. 이용이 불가능합니다. 잠시 후 다시 시도해 주세요.'}
    else:
        # context['내가 생각한 주제'] = text
        context['article'] = article
        context['summary'] = summary

    return context


def index(request):
    selecttext = extract_keywords_from_file(file)
    article = ''
    return render(request, 'textquizapp/index.html', {'selecttext': selecttext, 'article': article})


def word(request, word=None):
    meaning = get_word_meaning(word)
    return render(request, 'textquizapp/word.html', {'word': word, 'meaning': meaning})


def creat(request, keyword=None):
    selecttext = extract_keywords_from_file(file)
    context = {'article': '', 'summary': ''}
    if keyword:
        context = generate_text(keyword)
    else:
        if request.method == 'POST':
            text = request.POST.get('comment', '')
            print(f"내가 생각한 주제: {text}")
            if not text:
                context = {'오류': '주제를 입력해주세요.'}
            else:
                response = generate_text(text)
                # codiga-disable
                if not response:
                    context = {'오류': '죄송합니다. 이용이 불가능합니다. 잠시 후 다시 시도해 주세요.'}
                else:
                    # context['내가 생각한 주제'] = text
                    keyword = text
                    context['article'] = response['article']
                    context['summary'] = response['summary']

    ai_text = context['article']
    word_in_text = word_of_text(ai_text)
    wordlinks = []
    for word in word_in_text:
        link = f'<a href="../word/{word.strip()}">{word.strip()}</a>'
        wordlinks.append(link)
    result = ', '.join(wordlinks)
    article = f'<h5>[{keyword}]로 생성한 짧은 글</h5><p>{ai_text}</p>'
    return render(request, 'textquizapp/index.html', {'selecttext': selecttext, 'article': article, 'word_in_text': word_in_text, 'word': result})
