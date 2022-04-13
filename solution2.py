def solution(n,d):
    return list(int(i) for i in str(n)[-d:]) if d > 0 else []
print(solution(1234,0))
