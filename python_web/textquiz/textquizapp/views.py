
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
        selecttext += f'<a href="../create/{keyword.strip()}">{keyword.strip()}</a> | '
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


def get_word_meaning(request, word=None):
    url = f'https://krdict.korean.go.kr/api/search?key=9909E04870761033EC73F940D86C0382&q={word}&advanced=y&method=exact&translated=y&trans_lang=1'
    xml_data = requests.get(url, timeout=5, verify=False).text
    soup = BeautifulSoup(xml_data, "html.parser")
    definition_list = [definition.get_text()
                       for definition in soup.find_all('definition')]
    meaning = ''
    for i, definition in enumerate(definition_list):
        definition_list[i] = definition.replace('<b>', '').replace('</b>', '')
        meaning += f'{i+1}. {definition_list[i]}<br>'
    return render(request, 'textquizapp/index.html', {'word': word, 'meaning': meaning})


def create(request, keyword=None, word=None):
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
    if word:
        result = get_word_meaning(word)
    else:
        result = ''

    ai_text = context['article']
    word_in_text = word_of_text(ai_text)
    wordlinks = []
    for word in word_in_text:
        link = f'<a href="../word/{word.strip()}">{word.strip()}</a>'
        wordlinks.append(link)
    word_link = ', '.join(wordlinks)
    article = f'<h5>[{keyword}]로 생성한 짧은 글</h5><p>{ai_text}</p>'
    return render(request, 'textquizapp/index.html', {'selecttext': selecttext, 'article': article, 'word_in_text': word_in_text, 'word_link': word_link, 'meaning': result})
