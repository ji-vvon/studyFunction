#예제1) 리턴문, 인자 모두 없는 함수
def printHello():
    print("Hello, user")

# printHello()

#예제2) 리턴문이 없는 함수
def printHi(name):
    print("Hi,", name)

# name = input()
# printHi(name)

#예제3) 리턴문이 있는 함수
def printWelcome(user):
    word = "Welcome, " + str(user)
    return word

# user = int(input())
# print(printWelcome(user))

#예제4) 세 개의 값을 동시에 리턴하는 함수
def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3

a, b, c = func_mul(10)
# print(a, b, c)

#참고
def func_mul3(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3] #리스트로 반환
    #return (y1, y2, y3) #튜플로 반환

list = func_mul3(10)
# print(list)

#문자열 안에 우리가 원하는 값을 쉽게 삽입 ->formatting
#파이썬에는 여러 문자열 formatting 방법이 있음
#여기서는 format함수를 사용한 formatting만 알고 넘어가보도록 하겠습니다
#더 자세한 방법을 알고 싶다면 https://wikidocs.net/13 을 참고해주세요

#1_문자열에 숫자 바로 대입하기
print("저는 덕성 멋사 {}기 입니다.".format(9))

#2_문자열에 문자열을 입력받아 대입하기
fruit = input("당신이 좋아하는 과일은? ")
print("내가 좋아하는 과일은 {}입니다.".format(fruit))

#3_2개 이상의 값 넣기(숫자는 인덱스, 문자는 이름으로 대입)
print("저는 {0}학번 {major}과 입니다.".format(18, major="it미디어공학"))