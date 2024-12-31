import json

# JSON 파일 경로
file_path = "strings.json"  # JSON 파일 경로

# JSON 파일 읽기
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# 홀수 번째 값만 추출
odd_items = [item for index, item in enumerate(data) if (index + 1) % 2 == 1]

# 결과 확인용 출력
print("홀수 번째 값:")
print(json.dumps(odd_items, ensure_ascii=False, indent=2))

# 필요한 경우, 홀수 값을 새 파일에 저장
output_path = "CustomStrings.json"
with open(output_path, "w", encoding="utf-8") as file:
    json.dump(odd_items, file, ensure_ascii=False, indent=2)

print(f"홀수 번째 데이터가 '{output_path}'에 저장되었습니다.")
