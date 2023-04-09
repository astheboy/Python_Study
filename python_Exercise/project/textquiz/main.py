import openai
import random
import os

openai.api_key = "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"

# 텍스트 문서에서 주제를 추출하는 함수


def extract_keywords_from_file(file):
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "topics.txt")
    with open(file_path, "r") as f:
        text = f.read()
    keywords = text.strip().split(",")
    return [keyword.strip() for keyword in keywords]

# 텍스트 생성 함수


def generate_text(keyword):
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

    # prompt = f"생성한 글에서 올바른 중심 문장 1개와 잘못된 중심문장 3개를 만들어 사지선다형 퀴즈로 제시해 주세요. "
    # response = openai.Completion.create(
    #     engine="text-davinci-003",
    #     prompt=prompt,
    #     temperature=0.5,
    #     max_tokens=1000,
    #     n=1,
    #     stop=None,
    #     timeout=10,
    # )
    # question = response.choices[0].text.strip()

    # result = article + question
    return article

# 생성한 글의 중심 문장을 ai가 찾는 함수


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


# 사용자와 상호작용하는 함수
while True:
    file = "topics.txt"
    topic_select = input("자동으로 무작위 주제의 글을 만들겠습니까?(Y/N)")
    if topic_select.lower() == "y":
        keywords = extract_keywords_from_file(file)
        keyword = random.sample(keywords, 2)
    else:
        keyword = input("당신이 생성하고 싶은 글에 들어갈 단어나 키워드를 입력해 주세요. : ")
    article = generate_text(keyword)
    summary_ai = summarize_text(article)
    print("생성 된 글:")
    print(article)
    summary = input("글을 보고 중심문장을 찾아봅시다. : ")
    validation_prompt = f"Would you say the following sentence is at least 50% of the way to being a key sentence in your article? If yes, please say yes or no. Sentence: '{summary}' Article: '{article}'"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=validation_prompt,
        temperature=0.5,
        max_tokens=1,
        n=1,
        stop=None,
        timeout=10,
    )

    if response.choices[0].text.strip() == "Yes":
        print("중심문장을 잘 찾았습니다.")
    else:
        print("중심문장을 다시 찾아보면 좋겠습니다.")

    print("내가 생각한 중심문장은 다음과 같습니다.")
    print(summary_ai)
    another_article = input("다른 글을 생성하여 다시 중심 문장을 찾아보겠습니까? (Y/N)")
    if another_article.lower() != "y":
        break
