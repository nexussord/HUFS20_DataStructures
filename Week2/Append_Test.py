def append(value):
    global capacity, n, count, A, B, move
    # 전역변수 capacity(리스트의 용량), n(현재 리스트에 저장된 값의 개), 리스트 A, 리스트 B 선언
    if n == capacity:   # 원소의 개수가 리스트의 용량과 같다면
        capacity = capacity * 2    # 용량을 나타내는 변수 capacity를 두 배로 늘려주고
        B = [None] * capacity   # capacity만큼의 용량을 가진 비어있는 리스트 B를 생성
        for i in range(n):
            B[i] = A[i]    # 리스트 A의 내용을 리스트 B로 이동
            count += 1  # 이사 비용 카운트
            move += 1
        del A   # 이사가 끝났다면 기존의 리스트 A는 삭제
        A = B   # 리스트 A에 리스트 B를 대입
    A[n] = value    # A의 n번째 항에 value값을 대입
    n = n + 1   # n의 값을 1 증가 (저장된 값의 개수를 1 증가)
    count += 5  # 이사 비용 이외에 5번의 기본 연산이 필요하다고 가정


move = 0
count = 0   # 누적된 기본연산의 횟수
capacity = 1    # 리스트의 초기 용량은 1
n = 0   # 초기에 저장된 값의 개수는 0

N = int(input("Number of append operations = "))    # append 함수를 몇 번 실행할것인지 N값에 대입
A = [None]   # 원소가 비어있는 리스트 A를 생성
B = []   # 리스트 B 선언
for i in range(N):
    append(i)   # 입력받은 횟수 N번만큼 append 함수 실행
print(N, "append operations need", count, "basic operations in total, so average cost per append is", count / N)
print(move, 'times moved')
# N번의 append 함수는 count번의 기본연산을 필요로 하며, apeend 함수별로 필요한 평균 연산 횟수는 count / N이다.

