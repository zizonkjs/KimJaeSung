#--------------------------------------------------------------
# 연산자 실습
#--------------------------------------------------------------
# [실습] 문자열 데이터 2개에 대한 논리 연산 수행 후 출력
# data1="Hello"
# data2='hello'
data1="Hello"
data2="hello"

print(f'{data1}<{data2} and {data1}=={data2} : {data1<data2 and data1==data2}')
print(f'{data1}<{data2} or {data1}=={data2} : {data1<data2 or data1==data2}')
print(f'not {data1}>{data2} : {not data1>data2}')



print("------------------------------------------------------------------")

#-----------------------------------------------------------
# [실습] 정수 1개와 문자열 1개에 대한 논리 연산 수행 후 출력
#        단 not 연산자만 사용
# num=-3.2, 0인 경우
# msg='원더우먼', ''인 경우 
#------------------------------------------------------------
num=-3.2
num1=0
msg='원더우먼'
print(f'not{num}=={num1} : {not num==num1}')
print(f'not{num1}<={num1} : {not num1<=num1}')

print(f'not {msg} : {not msg}')

num=0 # 0은 False로 본다. 0이외의 값은 True 출력함.
msg=''
print(f'not {num} : {not num}')
print(f'not {msg} : {not msg}')