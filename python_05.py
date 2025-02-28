# 리스트 언패킹
x, y, z = [1, 2, 3]
print(x, y, z)  # 1 2 3

# 리스트 확장 (리스트 + 리스트)
A = [1, 2, 3]
B = [*A, *[4, 5, 6]]
print(B)  # [1, 2, 3, 4, 5, 6]

# range 객체 언패킹
C = [*range(1, 11)]
print(C)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 집합(Set) 언패킹 (순서는 보장되지 않음)
D = [*{1, 2, 3}]
print(D)  # 예: [1, 2, 3] (순서가 다를 수도 있음)

# 딕셔너리 언패킹 (키 값만 리스트로 저장)
E = [*{"one": 1, "two": 2}]
print(E)  # ['one', 'two']

# 문자열 언패킹
F = [*"Hello"]
print(F)  # ['H', 'e', 'l', 'l', 'o']

# 개별 변수에 문자열 언패킹
a, b, c = "ABC"
print(a, b, c)  # A B C

# 리스트에 여러 개 언패킹
G = [*A, *"XYZ", *range(4, 7)]
print(G)  # [1, 2, 3, 'X', 'Y', 'Z', 4, 5, 6]


# 리스트 메서드
A = [0, 1, 2]
A.append(3)
print(f"A: {A}") # [0, 1, 2, 3]
A.clear()
print(f"A: {A}") # []

A.extend([0, 1, 2, 3])
print(f"A: {A}")

A.insert(0, -1)
print(f"A: {A}")

A.pop()
print(f"A: {A}")

A.pop(-2) # 뒤에서 두 번째 요소 반환 후 제거
print(f"A: {A}")

A = A * 2
print(f"A: {A}")
A.remove(2) # 처음 나오는 value 2를 제거
print(f"A: {A}")


# 얕은 복사
A = [0, [1, 2]]
B = A.copy()
print(f"A: {A}\nB: {B}")

A[1][0] = 10 # A[0]은 단일원소이기 때문에, 처음부터 깊은 복사
print(f"A[1][0]: {A[1][0]}\nB[1][0]: {B[1][0]}")


# 깊은 복사
import copy

A = [0, [1, 2]]
B = copy.deepcopy(A)
print(f"A: {A}\nB: {B}")

A[1][0] = 10
print(f"A[1][0]: {A[1][0]}\nB[1][0]: {B[1][0]}")