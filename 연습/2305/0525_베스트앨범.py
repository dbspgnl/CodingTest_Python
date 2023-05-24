def solution(genres, plays):
    playDict = {} # 0:500,
    genreDict = {} # class: [0,1,2],
    genrePlay = {} # class: 1400,
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        playDict[i] = play
        if genre not in genreDict:
            genreDict[genre] = [i]
            genrePlay[genre] = play
        else:
            genreDict[genre].append(i)
            genrePlay[genre] += play
    sortedGenre = sorted(genrePlay, key=lambda x: genrePlay[x], reverse=True)
    answer = []
    for genre in sortedGenre:
        songs = genreDict[genre] # 0,1,2
        songs = sorted(songs, key=lambda x: (-playDict[x],x))
        answer += [x for x in songs[:2]]
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])) # [4, 1, 3, 0]