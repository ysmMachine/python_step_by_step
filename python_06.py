# 집합 생성
A = { 1, 2, 3 }
B = set((1, 2, 3))
C = set(range(1, 4))
print(A == B == C)  # True

D = set("abc")
x, y, z = D  # 집합은 순서 보장 X
print(f"x, y, z = {x}, {y}, {z}")  # x, y, z = c, a, b

# 집합 연산
S = set(range(1, 11))
print(len(S))  # 집합 크기
print(1 in S)  # 1이 집합에 있는지 확인
print(S.isdisjoint([0, 11]))  # 배반사건이면 True
print(S | set((0, 11)))  # 합집합
print(S & set((1, 2, 3)))  # 교집합
print(S - set((1, 2)))  # 차집합
print(S ^ set((1, 2, 3)))  # 대칭 차집합

S.add(100)  # 원소 추가
S.remove(1)  # 원소 삭제
S.pop()  # 임의의 원소 삭제
S.clear()  # 집합 비우기

# dict 생성
A = { "Apple" : 1000, "Orange": 1200 }
B = dict(Orange = 1200, Apple = 1000)  # dict는 set과 마찬가지로 순서 없음
C = dict([("Apple", 1000), ("Orange", 1200)])
print(A == B == C)  # True

# OrderedDict 사용
import collections
A = collections.OrderedDict(Orange = 1000)
print(A["Orange"])  # 순서가 보장된 OrderedDict에서 값 접근
