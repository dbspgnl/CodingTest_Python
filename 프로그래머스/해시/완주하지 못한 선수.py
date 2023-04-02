# # 효율성 테스트 탈락
# def solution(participant, completion):
#     for i in completion:
#         participant.remove(i)
#     return participant[0]

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1] # 마지막꺼

print(solution(["leo", "kiki", "eden"],["eden", "kiki"])) #"leo"
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"])) #"vinko"
print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"])) #"mislav"

"""
import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
"""
