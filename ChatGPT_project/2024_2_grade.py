import pandas as pd
import openai 
from dotenv import dotenv_values
config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]

# 프롬프트에 따라 결과 문장을 생성하는 함수
def execute_prompt(prompt):
    # 챗봇 모델을 사용하여 프롬프트 실행
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "당신은 고도로 훈련된 교사입니다. 당신은 평가내용을 토대로 학생들의 성취내용을 만드는데 능숙합니다."},
            {"role": "user", "content": prompt}
        ]
    )
    
    # 여기서 response.choices[0].message.content 를 반환하도록 하세요
    # 이 예제에서는 response 객체의 구조를 정확히 모르므로
    # 실제 응답 구조에 맞게 접근해야 할 수 있습니다.
    return response['choices'][0]['message']['content']

# Excel 파일 읽기
excel_path = '/Users/hanseungryun/Desktop/2024_2_grade.xlsx'  # 앞서 업로드한 파일 경로
df = pd.read_excel(excel_path)

# '프롬프트' 열의 각 행에 대해 프롬프트 실행 함수 적용
df['성취내용(결과)'] = df['프롬프트'].apply(execute_prompt)

# 필요한 열을 가진 새로운 DataFrame 생성
final_df = df[['과목', '평가내용', '성취내용(결과)']]

# 새로운 Excel 파일로 최종 DataFrame 저장
output_excel_path = '/Users/hanseungryun/Desktop/final_achievements.xlsx'
final_df.to_excel(output_excel_path, index=False)

print(f"생성된 문장을 {output_excel_path}에 저장했습니다.")