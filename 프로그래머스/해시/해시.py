# 장르 배열
genres = ["game", "music", "game", "game", "music"]
# 좋아요 배열
likeds = [500, 600, 150, 800, 2500]
# > (파싱)
# 고유 번호와 좋아요 수
liked_dict = {k:v for k,v in enumerate(likeds)}
print(liked_dict) # {0: 500, 1: 600, 2: 150, 3: 800, 4: 2500}
# 장르로 묶어주기
genre_dict = {}
for i in range(len(genres)):
    if genres[i] in genre_dict:
        genre_dict[genres[i]].append(i)
    else:
        genre_dict[genres[i]] = [i]
print(genre_dict) # {'game': [0, 2, 3], 'music': [1, 4]}
# 장르별 좋아요
genre_liked = {}
for i in range(len(genres)):
    if genres[i] in genre_liked:
        genre_liked[genres[i]] += likeds[i]
    else:
        genre_liked[genres[i]] = likeds[i]
print(genre_liked) # {'game': 1450, 'music': 3100}
# 장르 정렬 (오름차순, 기준:좋아요)
sorted_genre = sorted(genre_liked, key=lambda x: genre_liked[x], reverse=True)
print(sorted_genre) # ['music', 'game']
games = sorted(genre_dict["game"], key=lambda x: (-liked_dict[x], x))
print(games) # [3, 0, 2] 좋아요가 높은 순으로 game에서