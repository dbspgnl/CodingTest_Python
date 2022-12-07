array = [5,7,9,0,3,1,6,2,4,8]
def quick_sort(array, start, end): # 배열과 시작인덱스, 끝인덱스
    if start >= end: # 원소가 하나면 종료
        return
    pivot = start
    left = start+1
    right = end
    while(left<=right): # 아래 찾기가 교차하는 순간 종료
        while(left<=end and array[left] <= array[pivot]): #피벗보다 큰 수 찾기
            left+=1
        while(right > start and array[right] >= array[pivot]): #피벗보다 작은 수 찾기
            right-=1
        if(left > right): # 교차 이후 작은 수와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 교차 된 게 없다면 작은 수로
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right-1) # 기준5보다 왼쪽으로 처리
    quick_sort(array, right+1, end) # 기준5보다 오른쪽으로 처리
quick_sort(array, 0, len(array)-1)
print(array)