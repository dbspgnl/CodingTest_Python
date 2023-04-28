from collections import defaultdict
def solution(genres, plays):
    # 고유번호, 재생 수, 장르, 장르별 재생수
    play_dict = {}
    genre_dict = {}
    genre_play = {}
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        play_dict[i] = play
        if genre not in genre_dict:
            genre_dict[genre] = [i] # 해당 장르로 고유 번호 배열 만들기
            genre_play[genre] = play
        else:
            genre_dict[genre].append(i)
            genre_play[genre] += play

    sort_genre = sorted(genre_play, key=lambda x: genre_play[x], reverse=True)

    answer = []
    for genre in sort_genre:
        songs = genre_dict[genre]
        songs = sorted(songs, key=lambda x: (-play_dict[x], x))
        answer += [x for x in songs[:2]]
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])) # [4, 1, 3, 0]