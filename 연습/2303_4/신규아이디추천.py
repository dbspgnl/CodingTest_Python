def solution(new_id):
    answer = ""
    # 1단계: 소문자로 치환
    new_id = new_id.lower()
    # 2단계: 소문자, 숫자, -_. 만 허용
    for c in new_id:
        if c.isalnum() or c in "-_.":
            answer += c
    # 3단계: 마침표 중복은 한 번으로 처리
    while ".." in answer:
        answer = answer.replace("..", ".")
    # 4단계: 마침표 처음과 끝이면 제거
    if answer and answer[0] == ".": answer = answer[1:]
    # or answer[0:1] == ".": answer = answer[1:]
    if answer and answer[-1] == ".": answer = answer[:-1]
    # or answer[-1:0] == ".": answer = answer[1:]
    # 5단계: 빈 문자열이면 a로 치환
    if answer == "": answer = "a"
    # 6단계: 마침표가 마지막에 없게
    answer = answer[:15]
    if answer[-1] == ".": answer = answer[:-1]
    # 7단계: 길이가 2자 이하는 불가능
    while len(answer) < 3:
        answer += answer[-1]
    return answer
print(solution("...!@BaT#*..y.abcdefghijklm")) # bat.y.abcdefghi