# Iterator 객체 --> iterable 객체 (반복자를 가지고 있는 객체)
# 커스텀 클래스 생성 확인
# 이미 Iterator 객체를 가지고 있는 객체들 살펴보기
# 내장함수 dir() : 객체가 가지는 변수와 메서드를 리스트로 알려줌.
num=[11,22,33,55]

# print(dir(num))

# # _ 변수=데이터 
# # 저장되는 데이터에 따라서 변수명 지정하는데
# # 이변수명은 특별한 의미는 없고 문법상 필요한 경우
# for _ in dir(num):
#     print(_)

#리스트에서 반복자(Iterator) 추출 : __iter__()
iteriter=num.__iter__()
print(iteriter.__next__())
print(iteriter.__next__())
print(iteriter.__next__())

#내장함수 iter(반복가능한객체) : 객체의 존재하는 반복자를 추출
iter=iter(num)
print(iter.__next__())
















