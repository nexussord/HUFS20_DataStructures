import time, random

def prefixSum1(X, n):
    # code for prefixSum1
    S = [0 for _ in range(n)]
    for i in range(0, n):
        S[i] = 0
        for j in range(i):
            S[i] += X[j]


def prefixSum2(X, n):
    # code for prefixSum2
    S = [0 for _ in range(n)]
    S[0] = X[0]
    for i in range(1, n):
        S[i] = S[i - 1] + X[i]


random.seed()  # random 함수 초기화
# n 입력받음
n = int(input('type n : '))

# 리스트 X를 randint를 호출하여 n개의 랜덤한 숫자로 채움
X = []
for i in range(n + 1):
    temp = random.randint(-999, 999)
    X.append(temp)

before = time.process_time()
# prefixSum1 호출
prefixSum1(X, n)
after = time.process_time()
prefixSum1Time = after - before

before = time.process_time()
# prefixSum2 호출
prefixSum2(X, n)
after = time.process_time()
prefixSum2Time = after - before

# 두 함수의 수행시간 출력
print(prefixSum1Time, prefixSum2Time)