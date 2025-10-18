#과제 11
a = list(map(int,input("숫자 5개 입력: ").split()))
b = int(input("추가할 숫자: "))
a.append(b)
print(a)

#과제 12
a = list(map(int,input("숫자 5개 입력: ").split()))
b = a.pop()
b = a.pop()
print(a)

#과제 13
a = list(map(int,input("숫자 5개 입력: ").split()))

for index, value in enumerate(a, start = 101):
    print(index, value)

#과제 14
a = [10, 20, 30, 40, 30, 20, 10]
b = a.count(20)
print(b)

#과제 15
a = list(map(int,input("숫자 10개 입력: ").split()))
min_value = min(a)
max_value = max(a)

print(min_value, " and ", max_value)

#과제 16
a = list(map(int,input("숫자 10개 입력: ").split()))
a.remove(min(a))
a.remove(max(a))

sum = sum(a)
print(sum)

#과제 17
a = [10, 20, 30, 40, 30, 20, 10]

while 20 in a:
    a.remove(20)

print(a)

#과제 18
a = list(i + 1 for i in range(5))
print(a)

#과제 19
a = list(i * 2 + 1 for i in range(10))
print(a)

#과제 20
a, b = map(int,input("두 개의 정수 입력: ").split())
power = list(2 ** i for i in range(a, b+1))

del power[1]
del power[-2]

print(power)

#과제 21
sting_var = "Hello, world!"
print(sting_var.replace('Hello','Hi'))

#과제 22
sting_var = input('문자 4개 입력: ').split()
sting_var = " / ".join(sting_var)
print(sting_var)

#과제 23
name = input('영어 성 : ')
last_name = name.lower()
new_sting = last_name.rjust(10)
print(new_sting)

#과제 24
prices = list(map(int,input("물품 가격: ").split(';')))
prices.sort(reverse = True)

for price in prices:
    print(str(price).rjust(9))