# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

#안녕이게 원레포
#송가현 202101828 컴퓨터공학부
# touched by 제2의 송가현!
'''
for문을 사용해서 사이 년도를 다 돌아야하는데, 해당 년도가 윤년인지 아닌지에 따라 더하는 수가 달라진다. 따라서 윤년을 구하는 함수를 만들어서 사용하였다.
'''
print("오늘은 금요일입니다.")
def isYoon(a):	#윤년인지 구하는 함수
	if (a%4==0 and a%100!=0) or a%400==0:	#윤년의 조건을 만족하면, True를 반환
		return True
	else:	#윤년이 아니면 False를 반환
		return False

'''
day라는 리스트 변수에 모든 요일을 차례로 저장하고(일요일부터 시작하는지, 월요일부터 시작하는지는 상관없다.)yy1년도 1월 1일의 요일의 인덱스 값을 day1_index 변수에 저장한다. yy1년도와 yy2년 사이의 일수를 계산하여 day1_index 변수에 더해준 뒤, 7로 나눈 나머지에 해당하는 index를 가진 요소가 yy2년 1월 1일의 요일이 됨을 이용하였다. 
'''
day=['일','월','화','수','목','금','토']

year=list(map(int,input().split()))
# day1=day.index(input())
day1=input("day1:")
day1_index=day.index(day1)
yy1,yy2=year[0],year[1]
days=0
for i in range(yy1,yy2):
	if isYoon(i):
		days+=366
	else:
		days+=365
day1_index+=days
day1_index%=7
print("day[day1_index]: ",day[day1_index])	#day의 index값이 day1_index인 요소(요일)를 출력한다.
