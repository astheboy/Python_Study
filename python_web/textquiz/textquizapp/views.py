
import openai
import os
from django.shortcuts import render, HttpResponse
from django.template import RequestContext
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

file = "topics.txt"


# topics.txt 파일에서 키워드를 추출하는 함수
def extract_keywords_from_file(file):
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, file)
    with open(file_path, "r") as f:
        text = f.read()
    keywords = text.strip().split(",")
    selecttext = ''
    for keyword in keywords:
        selecttext += f'<a href="/creat/{keyword.strip()}">{keyword.strip()}</a> | '
    return selecttext

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

# 사용자가 입력한 주제의 텍스트를 생성하는 함수


def submit_message(request):
    selecttext = extract_keywords_from_file(file)
    context = {'article': '', 'summary': ''}
    if request.method == 'POST':
        text = request.POST.get('comment', '')
        print(f"내가 생각한 주제: {text}")
        if not text:
            context = {'오류': '주제를 입력해주세요.'}
        else:
            response = generate_text(text)
            if not response:
                context = {'오류': '죄송합니다. 이용이 불가능합니다. 잠시 후 다시 시도해 주세요.'}
            else:

                # context['내가 생각한 주제'] = text
                context['article'] = response['article']
                context['summary'] = response['summary']
    else:
        context = {'article': '', 'summary': ''}
    return render(request, 'textquizapp/index.html', {'selecttext': selecttext, 'context': context})


def index(request):
    selecttext = extract_keywords_from_file(file)
    article = ''
    return render(request, 'textquizapp/index.html', {'selecttext': selecttext, 'article': article})


def creat(request, keyword):
    context = {'article': '', 'summary': ''}
    context = generate_text(keyword)
    ai_text = context['article']
    article = f'<h5>[{keyword}]로 생성한 짧은 글</h5><p>{ai_text}</p>'
    return render(request, 'textquizapp/index.html', {'article': article})


def read(request, id):
    return HttpResponse("Read"+id)
