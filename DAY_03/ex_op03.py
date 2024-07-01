# ---------------------------------------------------
# 객체비교연산자
# "객체" : 힙영역에 존재하는 데이터, 즉 저장된 데이터
#          Class를 기반으로 저장된다.
# ---------------------------------------------------
num1=10
num2=num1

# 2개의 변수가 동일한 객체를 저장하고 있는지 확인하는 연산자
# 객체 비교 연산자

print(f"num1 is(주소의 값을 비교) num2 똑같은 객체인지 비교 : {num1 is num2}")
print(id(num1))
print(id(num2))
print("-------------------------------------------------------------")
num2 = 10.0
print(f"num1 is num2 똑같은 주소의 값인 객체인지 비교 : {num1 is num2}")
print(id(num1))
print(id(num2))
print("-------------------------------------------------------------")
# 순수데이터 비교연산으로 출력해보기.
print(f"num1==(값 자체를 비교)num2 : {num1==num2}")

