#---------------------------------------------------------------
# list/set/dict 자료형과 반복문, 조건부표현식 결합
# 메모리 사용량 감소를 위해서 사용 & 속도도 빠름
#---------------------------------------------------------------
# A 리스트의 데이터를 B리스트에 담기
# 단, A 리스트에서 짝수 값은 3을 곱하고, 홀수 값은 그대로
# B 리스트에 담기
a=[1,2,3,4,5,6]
b=[]
for num in a:
    if num%2:
        b.append(num)
    else:
        b.append(num*3)
print(f'a => {a}\nb=>{b}')

#모든 원소를 새로운 list c에 담기

c=[num for num in a]
print(f'a => {a}\nb=>{b}\nc=>{c}')

#짝수 데이터만 새로운 list c에 담기
# if not num%2: c.append(num*3)
c=[num*3 for num in a if not num%2]
print(f'a => {a}\nb=>{b}\nc=>{c}')

# 짝수 데이터는 3을 곱하고, 홀수 데이터는 그대로 리스트에 담기 list comperhesion 사용
# else: c.append(num)
c=[num*3 if not num%2 else num for num in a]
print(f'a => {a}\nb=>{b}\nc=>{c}')