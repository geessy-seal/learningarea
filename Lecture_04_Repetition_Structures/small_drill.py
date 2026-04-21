"""
small Drill 1.1

เขียนโปรแกรมรับจำนวนเต็ม 1 จำนวนชื่อ n

ให้พิมพ์เลขจาก 1 ถึง n

แต่มีเงื่อนไขว่า:

ถ้าเลขหาร 3 ลงตัว ให้พิมพ์ "skip-3" แทนเลขนั้น


"""

n = int(input("enter an integer: "))

for number in range(1, n + 1):
    if number % 3 == 0:
        print("skip-3")
    else:
        print(number)

"""
Small Drill 1.2

เขียนโปรแกรมรับจำนวนเต็ม 1 จำนวนชื่อ n

ให้พิมพ์เลขถอยหลังจาก n ลงมาถึง 1

แต่:

ถ้าเลขเป็นจำนวนคู่ ให้ต่อท้าย " even"
"""

n = int(input("enter an integer: "))

for i in range(n, 0, -1):
    print(i, end="")
    if i % 2 == 0:
        print(" even", end="")
    print()

"""
Small Drill 1.3

เขียนโปรแกรมรับจำนวนเต็ม 1 จำนวนชื่อ limit

ให้หาผลรวมของเลขตั้งแต่ 1 ถึง limit

แต่:

ถ้าตัวเลขหาร 4 ลงตัว ให้ ไม่เอามาบวก

ตัวอย่าง limit = 6

1+2+3+5+6 = 17

(จะ print แบบไหนก็ได้ ขอให้ logic ถูก)
"""
limit = int(input("enter an integer: "))
sum_of_num = 0
for number in range(1, limit+1):
    if (number % 4) != 0: 
        sum_of_num += number

print(sum_of_num)

"""
ข้อ 2.1

รับจำนวนเต็มบวก 1 จำนวนชื่อ n

ให้พิมพ์เลขจาก 1 ถึง n

แต่:

ถ้าหาร 2 และ 3 ลงตัวพร้อมกัน → พิมพ์ "both"
ถ้าหาร 2 ลงตัวอย่างเดียว → พิมพ์ "two"
ถ้าหาร 3 ลงตัวอย่างเดียว → พิมพ์ "three"
ไม่เข้าเงื่อนไข → พิมพ์เลขเดิม
"""

n = int(input("enter an integer: "))
for num in range(1, n + 1):
    if (num % 2 == 0) and (num % 3 == 0):
        print("both")
    elif num % 2 == 0:
        print("two")
    elif num % 3 ==0:
        print("three")
    else:
        print(num)
    

"""
ข้อ 2.2

รับจำนวนเต็มบวก 1 จำนวนชื่อ n

พิมพ์เลขถอยหลังจาก n ลงมาถึง 1

แต่:

ถ้าหาร 5 ลงตัว → ข้ามเลย ไม่พิมพ์
ถ้าเป็นเลขคี่ → ต่อท้าย " odd"
"""

n = int(input("enter an interger: "))

for num in range(n, 0, -1):
    if num % 5 == 0:
        continue
    print(num, end="")
    if num % 2 == 1:
        print(" odd", end="")
    print()

"""
ข้อ 2.3

รับจำนวนเต็มบวก 1 จำนวนชื่อ limit

หาผลรวมเฉพาะตัวเลขที่:

ไม่หาร 3 ลงตัว
และเป็นเลขคู่เท่านั้น

"""
limit = int(input("enter an interger: "))
sum_of_num = 0
for num in range(1, limit + 1):
    if (num % 3 != 0) and (num % 2 == 0):
        sum_of_num += num

print(sum_of_num)

"""
ข้อ 3.1

เขียนโปรแกรมรับจำนวนเต็มบวก 1 จำนวนชื่อ n

ใช้ while loop พิมพ์เลขจาก 1 ถึง n

แต่:

ถ้าเลขนั้นหาร 4 ลงตัว ให้พิมพ์ "four"
นอกนั้นให้พิมพ์เลขเดิม
"""

n = int(input("enter an integer: "))
repeat = 1
while repeat <= n:
    
    if repeat % 4 == 0:
        print("four")
    else:
        print(repeat)
    repeat += 1
"""
ข้อ 3.2

เขียนโปรแกรมรับจำนวนเต็มบวก 1 จำนวนชื่อ n

ใช้ while loop พิมพ์เลขถอยหลังจาก n ลงมาถึง 1

แต่:

ถ้าเลขนั้นหาร 3 ลงตัว ให้ข้ามไม่พิมพ์
ถ้าเลขนั้นไม่ถูกข้ามและเป็นเลขคู่ ให้ต่อท้าย " even"
"""

n = int(input("enter an integer: "))

while n >= 1:
    if n % 3 == 0:
        n -= 1
        continue

    if n % 2 == 0:
        print(n, "even")  
    else:
        print(n)
    n -= 1
#or i like this ver more
n = int(input("enter an integer: "))

while n >= 1:
    if n % 3 != 0:
        if n % 2 == 0:
            print(n, "even")      
        else:
            print(n)
    n -= 1

#or even but not so clean
n = int(input("enter an integer: "))

while n >= 1:
    if n % 3 != 0:
        print(n, end="")
        if n % 2 == 0:
            print(" even", end="")
        print()          
    n -= 1
    
    
    
    

"""

ข้อ 3.3

เขียนโปรแกรมรับจำนวนเต็มบวก 1 จำนวนชื่อ limit

ใช้ while loop หาผลรวมของเลขตั้งแต่ 1 ถึง limit

แต่ให้นำมาบวกเฉพาะเลขที่:

เป็นเลขคี่
และไม่หาร 5 ลงตัว

พิมพ์ผลรวมสุดท้ายออกมา
"""

limit = int(input("enter posiive integer: "))
loop = 1
sum_value = 0
while loop <= (limit):
    if (loop % 2 == 1) and (loop % 5 != 0):
        sum_value += loop
    loop += 1
print(sum_value)

"""
ข้อ 4.1

เขียนโปรแกรมรับจำนวนเต็มบวก 1 จำนวนชื่อ n

ใช้ while loop พิมพ์เลขจาก 1 ถึง n

แต่:

ถ้าเลขนั้นหาร 2 ลงตัว และหาร 5 ลงตัวพร้อมกัน ให้พิมพ์ "two-five"
ถ้าหาร 2 ลงตัวอย่างเดียว ให้พิมพ์ "two"
นอกนั้นให้พิมพ์เลขเดิม
"""
n = int(input("enter positive integer: "))
number = 1
while number <= n:
    if (number % 2 == 0) and (number % 5 == 0):
        print("two-five")
    elif number % 2 == 0:
        print("two")
    else:
        print(number)
    
    number += 1

#way 2 using nest if
n = int(input("enter positive integer: "))
number = 1
while number <= n:
    if number % 2 == 0:
        if number % 5 == 0:
            print("two five")
        else:
            print("two")
    else:
        print(number)
    number += 1
    
#way 3 use elif have to revert value can use both not or != idk i know my code wrong for sure on this ver
n = int(input("enter positive integer: "))
number = 1
while number <= n:
    if number % 2 != 0:
        print(number)
        number += 1
    elif number % 5 != 0:
        print("two")
        number += 1

    else:
        print("two five")
        number += 1

    
"""
ข้อ 4.2

เขียนโปรแกรมรับจำนวนเต็มบวก 1 จำนวนชื่อ n

ใช้ while loop พิมพ์เลขถอยหลังจาก n ลงมาถึง 1

แต่:

ถ้าเลขนั้นหาร 4 ลงตัว ให้ข้ามไม่พิมพ์
ถ้าเลขนั้นไม่ถูกข้าม และหาร 3 ลงตัว ให้ต่อท้าย " three"

ตัวอย่างถ้าเจอ 6:

6 three
"""

n = int(input("enter an integer: "))

while n >= 1:
    if  n % 4 == 0:
        n -= 1
        continue
    if n % 3 == 0:
        print(n, "three")
    else:
        print(n)
    n -= 1

#way2
n = int(input("enter an integer: "))

while n >= 1:
    if n % 4 != 0:
        if n % 3 == 0:
            print(n, "three")
        else:
            print(n)
        n -= 1
    else:
        n -= 1
# way 3
n = int(input("enter an integer: ")) 

while n >= 1:
    if n % 4 == 0:
        n -= 1
    elif n % 3 == 0:
        print(n, "three")
        n -= 1
    else:
        print(n)
        n-=1


"""
ข้อ 4.3

เขียนโปรแกรมรับจำนวนเต็มบวก 1 จำนวนชื่อ limit

ใช้ while loop หาผลรวมของเลขตั้งแต่ 1 ถึง limit

แต่ให้นำมาบวกเฉพาะเลขที่:

หาร 2 ลงตัว
และไม่หาร 4 ลงตัว

พิมพ์ผลรวมสุดท้ายออกมา
"""

limit = int(input("enter an positive integer: "))
number = 1
sum_total = 0
while number <= limit:
    if number % 2 == 0 and number % 4 != 0:
        sum_total += number
    number += 1

print(sum_total)

"""
5.1
ขียนโปรแกรมรับจำนวนเต็มไปเรื่อย ๆ

ถ้าผู้ใช้ป้อน 0 ให้หยุดรับทันที

ระหว่างนั้น:

ถ้าค่าที่รับมาเป็นเลขคู่ ให้พิมพ์ "even"
ถ้าเป็นเลขคี่ ให้พิมพ์ "odd"
"""

number = int(input("enter an integer and enter 0 if want to step: "))

while number != 0:
    if number % 2 == 0:
        print("even")
    else:
        print("ood")

    number = int(input("enter an integer and enter 0 if want to step: "))

"""
5.2
เขียนโปรแกรมรับจำนวนเต็มไปเรื่อย ๆ

ถ้าผู้ใช้ป้อน -1 ให้หยุด

ระหว่างนั้น:

รวมเฉพาะค่าที่มากกว่า 10

สุดท้ายพิมพ์ผลรวม
"""

number = int(input("enter an integer and enter -1 if want to step: "))
sum_of_num = 0
while number != -1:
    if number > 10:
        sum_of_num += number

    number = int(input("enter an integer and enter -1 if want to step: "))
print(sum_of_num)

"""
5.3
เขียนโปรแกรมรับจำนวนเต็มไปเรื่อย ๆ

ถ้าผู้ใช้ป้อนเลขที่หาร 7 ลงตัว ให้หยุดทันที (break)

แต่ก่อนหยุด:

ถ้าค่าที่รับมาไม่หาร 7 ลงตัว ให้พิมพ์ค่าที่รับมา
"""

number = int(input("enter an integer: "))

while True:
    if number % 7 == 0:
        break
    else:
        print(number)
    
    number = int(input("enter an integer: "))

"""
ข้อ 6.1

รับจำนวนเต็ม 1 จำนวน

ถ้าค่าน้อยกว่า 1 ให้รับใหม่เรื่อย ๆ จนกว่าจะได้ค่าที่มากกว่าหรือเท่ากับ 1

จากนั้นพิมพ์:

accepted
"""
number = int(input("enter integer"))

while number < 1:
    number = int(input("enter integer"))
print("accept")

"""
ข้อ 6.2

รับจำนวนเต็ม 1 จำนวน

ถ้าค่าไม่อยู่ในช่วง 10 ถึง 50 ให้รับใหม่เรื่อย ๆ

เมื่อได้ค่าที่ถูกต้องแล้ว:

พิมพ์เลขนั้นออกมา
"""
number = int(input("enter integer"))

while number < 10 or number > 50:
    number = int(input("enter integer"))
print(number)

"""
ข้อ 6.3

รับจำนวนเต็ม 1 จำนวน

ถ้าค่าเป็นเลขคี่ ให้รับใหม่เรื่อย ๆ จนกว่าจะได้เลขคู่

เมื่อได้เลขคู่แล้ว:

พิมพ์:

valid even number
"""

number = int(input("enter integer"))

while number % 2 == 1:
    number = int(input("enter integer"))
    if number % 2 ==0:
        print("valid output number")

"""
Subtopic Hard Problem 1

(Validation + Sentinel)

โจทย์

เขียนโปรแกรมรับจำนวนเต็มไปเรื่อย ๆ

กติกา:
ถ้าผู้ใช้ป้อน 0 → ให้หยุดโปรแกรมทันที
ถ้าค่าที่ป้อน น้อยกว่า 1 หรือมากกว่า 100
→ ให้ถือว่า invalid และรับใหม่ทันที
(ไม่เอาค่านี้ไปทำอะไร)
ถ้าค่าถูกต้อง:
ถ้าเป็นเลขคู่ → พิมพ์ "even"
ถ้าเป็นเลขคี่ → พิมพ์ "odd"
"""
num = int(input("enter an integer: "))
while num != 0:
    if num < 1 or num > 100:
        num = int(input("enter an integer: "))
    elif num % 2 == 0:
        print("even")
        num = int(input("enter an integer: "))
    else:
        print("odd")
        num = int(input("enter an integer: "))
#or

num = int(input("enter an integer: "))

while num != 0:
    if num >= 1 and num <= 100:
        if num % 2 == 0:
            print("even")
        else:
            print("odd")

    num = int(input("enter an integer: "))
"""
Subtopic Hard Problem 2

เขียนโปรแกรมรับจำนวนเต็มไปเรื่อย ๆ

กติกา:
ถ้าป้อน -1 → หยุดโปรแกรมทันที
ถ้าค่าติดลบ (แต่ไม่ใช่ -1) → ข้าม ไม่ต้องพิมพ์อะไร (continue)
ถ้าค่าเป็นจำนวนคู่ → พิมพ์ "even"
ถ้าค่าเป็นจำนวนคี่ → พิมพ์ "odd"
"""
num = int(input("enter an integer: "))

while num != -1:
    if num < 0:
        num = int(input("enter an integer: "))
        continue

    if num % 2 == 0:
        print("even")
    else:
        print("odd")
    
    num = int(input("enter an integer: "))


"""
Subtopic Hard Problem 3

เขียนโปรแกรมรับจำนวนเต็มไปเรื่อย ๆ

กติกา:
ถ้าป้อน 0 → หยุด
ถ้าค่าติดลบ → ข้าม ไม่เอาไปคิด
ถ้าค่าเป็นเลขคู่ → เอาไปรวมสะสม
ถ้าค่าเป็นเลขคี่ → ไม่รวม

สุดท้ายพิมพ์ผลรวมทั้งหมด

จุดฝึก

ตอนนี้มีครบ:

sentinel
continue
accumulator

ใน loop เดียว
"""

n = int(input("enter an integer: "))
sum_total = 0
while n != 0:
    if n < 0:
        pass
    elif n % 2 == 0:
        sum_total += n
    
    n = int(input("enter an integer: "))

print(sum_total)

# or u can while n != 0:
if n >= 0 and n % 2 == 0:
    sum_total += n

n = int(input("enter an integer: "))


"""
sub hard problem 4.1
111
222
333
"""

for i in range(1, 4):
    for j in range(3):
        print(i, end="")
    print()


"""
sub hard problem 4.2
111
222
333
"""
for i in range(3):
    print("12")

"""
sub hard problem 4.3
ใช้ nested loop พิมพ์:

123
123
123
"""
for i in range(3):
    print("123")

"""
sub hard problem 4.4


พิมพ์:

123
1234
12345
"""
for i in range(1, 4):
    for j in range(1, i + 3):
        print(j, end="")
    print()

"""
sub hard problem 4.5
พิมพ์:

1
22
333
4444
"""

for i in range(1, 5):
    for j in range(i):
        print(i, end="")
    print()

"""
sub hard problem 4.6
พิมพ์:
4321
4321
4321
"""

for i in range(4):
    for j in range(4, 0, -1):
        print(j, end="")
    print()

"""
subprob 4.7
พิมพ์:

1
12
123
1234
"""

for i in range(4):
    for j in range(1, i+2):
        print(j , end="")
    print()
#this easier to read
for i in range(1, 5):
    for j in range(1, i+1):
        print(j , end="")
    print()

"""
sub problem 4.8
พิมพ์:

4444
333
22
1
"""

for i in range(4 , 0, -1):
    for j in range(i):
        print(i, end="")
    print()
"""
sub problem 4.9
พิมพ์:
135
135
135
"""
for i in range(1, 4):
    for j in range(1, 6, 2):
        print(j, end="")
    print()

"""
subproblem 5.0
พิมพ์:

1234
123
12
1
"""
for i in range(4, 0, -1):
    for j in range(1 , i+1 ):
        print(j, end="")
    print()

"""
subproblem 6.1
พิมพ์:

1
23
456
"""
num = 1
for i in range(1,4):
    for j in range(i):
        print(num, end="")
        num += 1
    print()
"""
พิมพ์:
sub problem 6.2
****
***
**
*
"""
for i in range(4, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

"""
ข้อ M1

พิมพ์:

11
222
3333
"""
for i in range(1, 4):
    for j in range(i+1):
        print(i, end="")
    print()

"""
ข้อ M2

พิมพ์:

12
345
6789
"""
num = 1
for i in range(1, 4):
    for j in range(i+1):
        print(num, end="")
        num += 1
    print()
"""
ข้อ R2

พิมพ์:

321
32
3
"""
for i in range(3):
    for j in range(3, i, -1):
        print(j, end="")
    print()

"""
พิมพ์:

*
**
***
****
"""
for i in range(4):
    for j in range(i+1):
        print("*", end="")
    print()

"""
พิมพ์:

   *
  **
 ***
****

(มี space หน้าแต่ละแถว)
"""
space = 3
for i in range(4):
    for j in range(space):
        print(" ", end="")
    for k in range(i+1):
        print("*", end="")
    print()
    space -= 1
#
for i in range(1, 5):
    for j in range(4 - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()
"""
พิมพ์:

1111
 222
  33
   4
"""
#i dont know if the question is tricky or i overcompicait like 3 loop???
space = 0
for i in range(1, 5):
    for j in range(space):
        print(" ", end="")
    for k in range(space, 5):
        print(i, end="")
    print()
    space += 1

for i in range(1, 5):
    for j in range(i - 1):
        print(" ", end="")
    for k in range(5 - i):
        print(i, end="")
    print()
"""
ข้อ O3

พิมพ์:

1
 2
  3
   4
"""
for i in range(1, 5):
    for j in range(0, i-1):
        print(" ", end="")
    print(i)

"""
P1

พิมพ์:

   1
  22
 333
4444

(อันนี้ combine space + repeat number)
"""

for i in range(1,5):
    for j in range(4-i):
        print(" ", end="")
    for k in range(i):
        print(i, end="")
    print()

"""
P2

พิมพ์:

1
22
333
4444
333
22
1

(ขึ้นแล้วลง)
"""
#this is wrong funny when i comeback and read it
num = 1
for i in range(7):
    for j in range(num):
        print(num, end="")
    if num < 4:
        num += 1
    else:
        num -= 1
    print()
#or 
num = 1
direction = 1

for i in range(7):
    for j in range(num):
        print(num, end="")
    print()

    if num == 4:
        direction = -1

    num += direction
#or easiest to read
for i in range(1, 5):
    for j in range(i):
        print(i, end="")
    print()

for i in range(3, 0, -1):
    for j in range(i):
        print(i, end="")
    print()
"""
พิมพ์:

1234
 234
  34
   4
"""
num = 1
for i in range(1, 5):
    for j in range(i - 1):
        print(" ", end="")
    for k in range(num, 5):
        print(k, end="")
    num += 1
    print()

"""
เช่น:

1234
321
21
1

หรือ

4321
 321
  21
"""

for i in range(1, 5):
    if i == 1:
        for j in range(1,5):
            print(j, end="")
    else:
        for j in range(5-i, 0, -1):
            print(j, end="")
    print()

# ver 2
for j in range(1, 5):
    print(j, end="")
print()

for i in range(3, 0, -1):
    for j in range(i, 0, -1):
        print(j, end="")
    print()

#or
for i in range(4, 0, -1):
    for j in range(4-i):
        print(" ", end="")
    for k in range(i, 0, -1):
        print(k, end="")
    print()