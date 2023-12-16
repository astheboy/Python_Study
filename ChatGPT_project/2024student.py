import pandas as pd

# 엑셀 파일 경로 설정
excel_file_path = '/Users/hanseungryun/Desktop/2024_student.xlsx'  # 실제 파일 경로로 변경해주세요.

# 데이터프레임으로 엑셀 파일 읽기
df = pd.read_excel(excel_file_path, sheet_name='Sheet1')  # 'Sheet1'을 실제 시트 이름으로 변경해주세요.

# 성적 순으로 학생들 정렬
df_sorted = df.sort_values(by='성적', ascending=False)

# 그룹 할당을 위한 초기 설정
group_assignments = {1: [], 2: [], 3: []}
group_gender_count = {1: {'남': 0, '여': 0}, 2: {'남': 0, '여': 0}, 3: {'남': 0, '여': 0}}
conflict_tracker = {}
total_students = len(df_sorted)
students_per_group = total_students // 3
extra_students = total_students % 3

# 각 그룹에 최대 학생 수 설정
max_students_per_group = total_students // 3 + (1 if total_students % 3 else 0)

# 그룹 할당
for _, row in df_sorted.iterrows():
    name = row['이름']
    gender = row['성별']
    conflict = row['충돌학생']

    # 할당할 그룹 찾기
    assigned_group = None
    possible_groups = [1, 2, 3]
    for _ in range(3):
        # 가장 적은 학생 수를 가진 그룹 찾기
        min_group = min(possible_groups, key=lambda x: (len(group_assignments[x]), -x))
        if len(group_assignments[min_group]) < students_per_group + (1 if min_group == 1 and extra_students > 0 else 0):
            if (conflict == "" or conflict_tracker.get(conflict, None) != min_group) and \
               group_gender_count[min_group][gender] <= group_gender_count[min_group]['남' if gender == '여' else '여']:
                assigned_group = min_group
                break
        # 최적의 그룹을 찾지 못한 경우 다음 그룹으로 이동
        possible_groups.remove(min_group)

    # 최적의 그룹을 찾지 못한 경우, 첫 번째 그룹에 할당
    if assigned_group is None:
        assigned_group = 1

    # 그룹 할당 및 성별 카운트, 충돌 학생 추적 업데이트
    group_assignments[assigned_group].append(name)
    group_gender_count[assigned_group][gender] += 1
    conflict_tracker[name] = assigned_group

    
# 그룹별 학생 수 재조정 (필요한 경우)
for group in group_assignments:
    while len(group_assignments[group]) > max_students_per_group:
        # 재조정할 학생 선택
        student_to_move = group_assignments[group].pop()
        # 다른 그룹으로 이동
        for target_group in group_assignments:
            if len(group_assignments[target_group]) < max_students_per_group:
                group_assignments[target_group].append(student_to_move)
                break
            
# 결과 출력
# for group, students in group_assignments.items():
#     print(f"그룹 {group}: {students}")

# 그룹 정보를 원본 데이터프레임에 추가
df['새 그룹'] = ''
for group, students in group_assignments.items():
    for student in students:
        df.loc[df['이름'] == student, '새 그룹'] = group

# 결과 표1 (반/번호/이름/성별/새 그룹) - 반과 번호 기준 오름차순 정렬
result_table1 = df.sort_values(['반', '번호'])

# 결과 표2 (새 그룹/반/번호/이름/성별) - 새 그룹과 이름 기준 오름차순 정렬
result_table2 = df[['새 그룹', '반', '번호', '이름', '성별']].sort_values(['새 그룹', '이름'])

# 엑셀 파일로 결과 저장
with pd.ExcelWriter('grouped_students.xlsx') as writer:
    result_table1.to_excel(writer, index=False, sheet_name='Grouped by Class')
    result_table2.to_excel(writer, index=False, sheet_name='Grouped by New Group')

print("그룹 편성 결과가 엑셀 파일로 저장되었습니다.")