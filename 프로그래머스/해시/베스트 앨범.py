# 장르 기준 많이 재생된 순으로
# 장르 내에서 많이 재생된 순으로 2개 선정
# 만약 장르 내 재생 수가 같다면 고유 번호가 낮은 노래를 우선

def solution(genres, plays):
    playDict = {} # 고유 번호와 재생 수 {0: 500, 1: 600, 2: 150, 3: 800, 4: 2500}
    genreDict = {} # 고유 번호와 장르 {0: classic, 1: pop ...}
    genrePlay = {} # 장르별 재생 수 {classic: 1450, pop: 3100}
    for i in range(len(genres)): # 초기화
        genre = genres[i] # 고유번호
        play = plays[i] # 플레이수
        playDict[i] = play # 고유 번호와 재생 수 초기화
        if genre not in genreDict: # 새로 만들어주기
            genreDict[genre] = [i] # 고유 번호로 장르 만들어주기
            genrePlay[genre] = play # 장르별 재생 수
        else: # 있으면 기존에 넣기
            genreDict[genre].append(i) # 기존에 추가
            genrePlay[genre] += play # 장르별 재생 수 누적
    # 장르 정렬 (재생 수 기준)
    sortedGenre = sorted(genrePlay, key=lambda x: genrePlay[x], reverse=True)
    # 각 장르에서 가장 많이 재생된 노래 2개씩 answer에 추가
    answer = []
    for genre in sortedGenre:
        songs = genreDict[genre]
        # print(songs)
        songs = sorted(songs, key=lambda x: (-playDict[x], x)) # 오름차순
        # print(songs)
        answer += [x for x in songs[:2]] # 2개까지만
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])) # [4, 1, 3, 0]

"""
def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer
    
    
def solution(genres, plays):
    answer = []
    
    dic1 = {}
    dic2 = {}
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [(i, p)]
        else:
            dic1[g].append((i, p))
    
        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p
    
    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)
    
    return answer  

"""