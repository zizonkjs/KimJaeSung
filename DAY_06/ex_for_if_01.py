#-----------------------------------------------------
# 제어문 - 반복문과 조건문 혼합사용.
#-----------------------------------------------------
# 숫자 1~50까지의 데이터가 있음. => 숫자%3==0
# 해당 데이터에서 3의 배수는 제곱을 하고, 나머지 숫자는 그대로 해서 모두 더해서 합계 출력.
datas=range(1,51)
total=0
for data in datas:
    # 3의 배수 여부 검사
    if data%3:
        total=total+data
    else:
        total=total+(data*data)

print(f"합계 : {total}")

#-----------------------------------------------------
# 제어문 - 반복문과 조건문 혼합사용.
#-----------------------------------------------------
# 메시지에서 알파벳과 숫자를 구분해서 처리할거임.
# 알파벳은 ★, 숫자는 ♥로 변경해서 출력.
#-----------------------------------------------------
msg="Good 2024"
msg2=''
for a in msg:
    if 'a'<=a<='z' or 'A'<=a<='Z': # 알파벳 여부 조건
        msg2=msg2+"★"
        print("★", end='')
    elif '0'<=a<='9': # 숫자 여부 조건
        msg2=msg2+"♥"
        print("♥", end='')
    else:
        msg2=msg2+a
        print(a, end='') # 그외 문자처리
print(f'저장된 msg2 : {msg2}')

