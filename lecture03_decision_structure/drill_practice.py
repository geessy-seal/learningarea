"""drill from crash royal need nerf
เขียนโปรแกรมรับจำนวนเต็ม 1 จำนวน แล้วตรวจว่าเป็น เลขคู่ หรือไม่

เงื่อนไข:

ต้องใช้ int(input(...))
ต้องใช้ if
ต้องใช้ %
ถ้าเป็นเลขคู่ ให้พิมพ์ even
ถ้าไม่เป็นเลขคู่ ยังไม่ต้องทำอะไร ในข้อนี้

ตัวอย่าง:

Enter an integer: 8
even
"""
num = int(input("enter integer: "))

if num % 2 == 0:
    print("even")



"""
Small Drill 1.1

เขียนโปรแกรมรับจำนวนเต็ม 1 จำนวน แล้วพิมพ์ตามนี้:

ถ้าเลขนั้น มากกว่า 0 ให้พิมพ์ positive
ถ้าไม่มากกว่า 0 ยังไม่ต้องทำอะไร
"""
num = int(input("enter integer: "))
if num > 0:
    print("positive")

"""
Small Drill 1.2

เขียนโปรแกรมรับจำนวนเต็ม 1 จำนวน แล้ว:

ถ้าเลขนั้นหาร 3 ลงตัว ให้พิมพ์ multiple of 3
"""

num = int(input("enter integer: "))
if num % 3 == 0:
    print("mutiple of 3")

"""
1.
รับจำนวนเต็ม 1 จำนวน

ถ้าเป็นเลขคี่ ให้พิมพ์: odd
"""
num = int(input("enter integer: "))
if num % 2 != 0:
    print("odd")

"""
2.
รับจำนวนเต็ม 1 จำนวน

ถ้าเลขนั้นมากกว่าหรือเท่ากับ 10 ให้พิมพ์:
two digits or more
"""
num = int(input("enter integer: "))
if num >= 10:
    print("two degits or more")

"""
3.
รับจำนวนเต็ม 1 จำนวน

ถ้าเลขนั้นหาร 5 ลงตัว ให้พิมพ์:

multiple of 5
"""
num = int(input("enter integer: "))
if num % 5 == 0:
    print("mutiple of 5")

"""
4.
รับจำนวนเต็ม 1 จำนวน

ถ้าเลขนั้นอยู่ระหว่าง 1 ถึง 100 (รวมขอบ) ให้พิมพ์:

in range
"""
num = int(input("enter integer: "))
if 0 < num < 101:
    print("in range")
# other ver for if
#if 1 <= num <= 100:
#if num >= 1 and num <= 100:

"""
5.
รับจำนวนเต็ม 1 จำนวน

ถ้าเลขนั้นเป็นเลขคู่ และ มากกว่า 20 ให้พิมพ์:

valid even
"""

num = int(input("enter integer: "))
#could use parentness for cleaner but am confident with operator precedence
if num % 2 == 0 and num > 20:
    print("valid even")

"""
ข้อ 6

รับจำนวนเต็ม 1 จำนวน

ถ้าเลขนั้นหารทั้ง 2 และ 3 ลงตัว ให้พิมพ์:

divisible by 2 and 3
"""
num = int(input("enter integer: "))
#is there way to write to make it easiler to read? like add ()
if num % 2 == 0 and num % 3 == 0:
    print("divisible by 2 and 3")

"""
ข้อ 7

รับจำนวนเต็ม 1 จำนวน

ถ้าเลขนั้น ไม่ใช่เลขคู่ ให้พิมพ์:

not even
"""
num = int(input("enter integer: "))
#and is not nessary both way work as check if it even
if (num % 2 == 1) and (num % 2 != 0):
    print("not even")

"""
ข้อ 8

รับจำนวนเต็ม 1 จำนวน

ถ้าเลขนั้นอยู่นอกช่วง 10 ถึง 20 ให้พิมพ์:

outside range
"""

num = int(input("enter integer: "))
if not (10 <= num <= 20):
    print("outside range")

"""
ข้อ 9

รับจำนวนเต็ม 1 จำนวน

ถ้าเลขนั้นเป็นเลขคู่ หรือ มากกว่า 50 ให้พิมพ์:

accepted
"""
num = int(input("enter integer: "))
if num % 2 == 0 or num > 50:
    print("accepted")

"""
ข้อ 10 — String Comparison

รับชื่อ 2 ชื่อ แล้วถ้า name1 มากกว่า name2 ตามลำดับตัวอักษร ให้พิมพ์:

name1 comes later

(ใช้ comparison ของ string ตรง ๆ)
"""
name1 = input("entr name 1: ")
name2 = input("enter name2: ")

if name1 > name2:
    print("name1 come before name 2")

"""
ข้อ 11 — not operator

รับจำนวนเต็ม 1 จำนวน

ถ้าเลขนั้น ไม่อยู่ในช่วง 50 ถึง 100

ให้พิมพ์:

outside

ข้อนี้ตั้งใจให้ลองใช้ not
"""
num = int(input("enter a number: "))
if not (50 <= num <= 100):
    print("outside")


"""
ข้อ 12 — Boolean flag เบื้องต้น

รับคะแนนสอบ 1 ค่า

สร้างตัวแปร passed

ถ้าคะแนน >= 50 → passed = True
ถ้าไม่ใช่ → passed = False

แล้วถ้า passed เป็นจริง ให้พิมพ์:

pass
"""
point = float(input("enter your score: "))

passed = False

if point >= 50:
    passed = True

if passed:
    print("pass")


"""
Small Drill ต่อ (ข้อ 13–14)
ข้อ 13 — String + if-else

รับ password 1 ค่า

ถ้าตรงกับ "python123" → พิมพ์ accepted
ถ้าไม่ตรง → พิมพ์ wrong password
"""
password = input("enter your password: ")
if password == "python123":
    print("accepted")
else:
    print("wrong password")

"""
ข้อ 14 — Boolean flag + range + else

รับคะแนน 1 ค่า

สร้าง flag ชื่อ high_score

ถ้าคะแนน >= 80 → True
ถ้าไม่ใช่ → False

จากนั้น:

ถ้า high_score → พิมพ์ high score
ไม่งั้น → พิมพ์ normal
"""
score = float(input("enter your score: "))
high_score = False
if score >=80:
    high_score = True

if high_score:
    print("high score")
else:
    print("normal")

"""
ข้อ 15
รับคะแนนสอบ 1 ค่า

เงื่อนไข:

ถ้าคะแนน >= 80 พิมพ์ A
ถ้าคะแนน >= 70 แต่ < 80 พิมพ์ B
ถ้าคะแนน >= 60 แต่ < 70 พิมพ์ C
ต่ำกว่านั้น พิมพ์ F
เงื่อนไขเพิ่ม:

ใช้ if-elif-else เท่านั้น
"""
score = float(input("enter your score: "))

if score >= 80:
    print("A")
elif score >= 70:
    print("B")
elif score >= 60:
    print("C")
else:
    print("F")

"""
Combine Problem ข้อ 16

รับจำนวนเต็ม 1 จำนวน

เงื่อนไข:

ถ้าหาร 2 ลงตัว และ หาร 5 ลงตัว → พิมพ์ divisible by 2 and 5
ถ้าหาร 2 ลงตัวอย่างเดียว → พิมพ์ divisible by 2 only
ถ้าหาร 5 ลงตัวอย่างเดียว → พิมพ์ divisible by 5 only
ไม่เข้าเลย → พิมพ์ neither
"""
num = int(input("enter a number: "))
if (num % 2 == 0) and (num % 5 == 0):
    print("divisivle by 2 and 5")
elif num % 2 == 0:
    print("divisible by 2")
elif num % 5 == 0:
    print("divisible b 5")  
else:
    print("Nither")

"""
17 รับชื่อ 2 ชื่อ

ถ้า name1 มาก่อน name2 ตาม alphabet:

พิมพ์:

correct order

ไม่งั้นพิมพ์:

swap
"""
name1 = (input("enter name #1 "))
name2 = (input("enter name #2 "))

if name1 < name2:
    print("correct order")
else:
    print("swap")

"""
18
รับจำนวนเต็ม 3 จำนวน

พิมพ์ค่าที่มากที่สุดออกมา

ตัวอย่าง:

Enter 3 numbers: 8 15 3
15

⚠️ เงื่อนไข:

ใช้ if / elif / else เท่านั้น
ยังไม่ใช้ max()
"""
num1 = int(input("enter integer#1: "))
num2 = int(input("enter integer#2: "))
num3 = int(input("enter integer#3: "))

maximum = num1
if num2 > maximum:
    maximum = num2

if num3 > maximum:
    maximum = num3

print(maximum)

"""
19
รับอายุ 1 ค่า

เงื่อนไข:

ต่ำกว่า 13 → child
13 ถึง 19 → teen
20 ขึ้นไป → adult

⚠️ ใช้ if-elif-else
"""
age = int(input("your age: "))
if age >= 20:
    print("adult")
elif age >= 13:
    print("teen")
else:
    print("child")

"""
20
ขียนโปรแกรมรับข้อมูล 3 ค่า:

username (string)
password (string)
age (int)

กติกา:

ถ้า username ไม่เท่ากับ "admin" → พิมพ์ unknown user
ถ้า username ถูก แต่ password ไม่เท่ากับ "python123" → พิมพ์ wrong password
ถ้า username และ password ถูก แต่ age < 18 → พิมพ์ access denied
ถ้าถูกทั้งหมด → พิมพ์ access granted
เงื่อนไข
ใช้ if-elif-else หรือ nested if ก็ได้
ยังไม่ต้องใช้ loop
อย่าใช้ function อื่นนอกจาก input, int, print
"""
username = input("enter your username: ")
password = input("enter your password: ")
age = int(input("enter your age: "))
correct_username = False
correct_password = False
correct_age = False
if username != "admin":
    print("unknown user")
else:
    correct_username = True

if correct_username and password == "python123":
    correct_password = True

elif correct_username and password != "python":
    print("wrong password")

if  correct_username and correct_password and age > 18:
    print("acess granted")
elif correct_username and correct_password and age < 18:
    print("accept denied")

#what am i writing above overcomplicait here better way
if username != "admin":
    print("unknown user")
elif password != "python123":
    print("wrong password")
elif age < 18:
    print("access denied")
else:
    print("acess granted")

"""
21
รับเลขจำนวนเต็ม 1 ค่า

กติกา:

ถ้าหาร 2 ลงตัว และ หาร 3 ลงตัว → divisible by both
ถ้าหาร 2 ลงตัวอย่างเดียว → divisible by 2
ถ้าหาร 3 ลงตัวอย่างเดียว → divisible by 3
ถ้าไม่เข้าเลย → neither

⚠️ ข้อนี้ดูว่า:

คุณจัดลำดับ if / elif ถูกไหม
คุณรู้ไหมว่า case ไหนต้องเช็คก่อน

ส่งมาได้เลย ✍️
"""
num = input("enter a number: ")
if num % 2 == 0 and num % 3 == 0:
    print("divisible by both")
elif num % 2 == 0:
    print("divisible by 2")
elif num % 3 == 0:
    print("divisible by 3")
else:
    print("neither")

"""
22.
เขียนโปรแกรมรับ:

username
password
age

เงื่อนไข:

ถ้า username ไม่ใช่ "admin" → "unknown user"
ถ้า username ถูก แต่ password ไม่ใช่ "python123" → "wrong password"
ถ้าถูกทั้งสอง:
age >= 18 → "access granted"
age < 18 → "access denied"
"""
username = input("enter your username: ")
password = input("enter your password: ")
age = int(input("enter your age: "))

if username == "admin":
    if password == "python123":
        if age >= 18:
            print("acess granted")
        else:
            print("acess denied")
    
    else:
        print("wrong password")
else:
    print("unknow user")


"""
23.
Choosing between nested vs logical operator

ข้อนี้สำคัญกว่าเขียน syntax เยอะ เพราะคือ “เลือกโครงสร้างให้ถูก”

รับค่า:

score
attendance

เงื่อนไข:

ถ้า score >= 50 และ attendance >= 80
→ "pass"
ถ้า score >= 50 แต่ attendance < 80
→ "attendance too low"
ถ้า score < 50
→ "fail"
กติกา

เขียน 2 แบบ

แบบ A:

nested

แบบ B:

logical operator (and / elif)
"""
# A ver
score = int(input("enter ur score: "))
attendance = int(input("enter ur attendance: "))

if score >= 50:
    if attendance >= 80:
        print("pass")
    else:
        print("attendance too low")
else:
    print("fail")

#B ver
score = int(input("enter ur score: "))
attendance = int(input("enter ur attendance: "))

if score >= 50 and attendance >= 80:
    print("pass")
elif score >= 50:
    print("attendace too low")
else:
    print("fail")

"""
24.รับค่า:

username
password
member (yes/no)

เงื่อนไข:

ถ้า username ถูก (admin) และ password ถูก (python123)
→ ให้ตั้ง flag ว่า login สำเร็จ
ถ้า login สำเร็จแล้ว:
member = yes → "premium access"
member = no → "basic access"
ถ้า login ไม่สำเร็จ → "login failed"
"""

username = input("enter username: ")
password = input("enter password: ")
member = input("yes/no: ")
login = False
if username == "admin" and password == "python123":
    login = True
else:
    print("login failed")

if login:
    if member == "yes":
        print("premium acess")
    else:
        print("basic acess")

"""
24.เขียนโปรแกรมรับ:

username
password
score

เงื่อนไข:

ถ้า username ไม่ใช่ "student"
→ "unknown user"
ถ้า username ถูก แต่ password ไม่ใช่ "abc123"
→ "wrong password"
ถ้า login ถูก:
score >= 80 → "grade A"
score >= 70 → "grade B"
score >= 60 → "grade C"
score ต่ำกว่า 60 → "fail"
ข้อกำหนด

ข้อนี้ ห้ามเขียน nested ลึกเกินจำเป็น

คือ:

ใช้ nested เท่าที่ควร
แต่ grade part ควร flatten ให้สวย
"""
username = input("enter username: ")
password = input("enter password: ")
score = int(input("enetr your score"))
if username != "student":
    print("unknow user")
elif password != "abc123":
    print("wrong password")
elif score >= 80:
    print("grade A")
elif score >= 70:
    print("grade B")
elif score >= 60:
    print("grade C")
else:
    print("fail")

"""
25.
รับค่า:

username
password
member (yes/no)
score

เงื่อนไข:

ถ้า username หรือ password ผิด → "login failed"
ถ้า login ถูก:
ถ้า member = yes:
score >= 70 → "premium passed"
score < 70 → "premium failed"
ถ้า member = no:
score >= 80 → "basic passed"
score < 80 → "basic failed"
ข้อนี้ตั้งใจให้คุณเลือกเอง:
nested
logical
flag
หรือ mix
"""
#i treat them as constant 
CORRECT_USERNAME = "student"
CORRECT_PASSWORD = "abc123"

username = input("enter username: ")
password = input("enter password: ")
member = input("yes/no: ")
score = int(input("enetr your score"))

if (username != CORRECT_USERNAME) or (password != CORRECT_PASSWORD):
    print("login fail")
elif member == "yes":
    if score >= 70:
        print("premium passed")
    else:
        print("premium fail")
elif member == "no":
    if score >= 70:
        print("basic passed")
    else:
        print("baisc fail")
else:
    print("invalid member")

"""
26.
โจทย์: Electricity Bill + Membership Discount ⚡

รับค่า:

units จำนวนหน่วยไฟ
member (yes/no)

กติกา:

คิดค่าไฟ
0–100 หน่วย → หน่วยละ 5 บาท
101–200 หน่วย → หน่วยละ 7 บาท
มากกว่า 200 หน่วย → หน่วยละ 10 บาท
หลังจากคิดค่าไฟแล้ว
ถ้าเป็น member → ลด 10%
หลังลดแล้ว
ถ้ายอดสุดท้ายเกิน 1500 → "high bill"
ถ้าไม่เกิน → "normal bill"
"""
UNIT_RATE1 = 5
UNIT_RATE2 = 7
UNIT_RATE3 = 10


unit = float(input("enter electricity unit u consume"))
member = input("are u member? (type yes/no): ")

if 0 < unit <= 100:
    electricity_bill = unit * UNIT_RATE1
elif unit <= 200:
    electricity_bill = (100 * UNIT_RATE1) + (unit - 100) * UNIT_RATE2
elif unit > 200:
    electricity_bill = (100 * UNIT_RATE1) + 100 * (UNIT_RATE2) + (unit - 200) * UNIT_RATE3
else:
    electricity_bill = 0
    print("hey who told u unit can be negative value?")

if member == "yes":
    discount = electricity_bill * 0.1
    electricity_bill = electricity_bill - discount


if electricity_bill > 1500:
    print("high bill")
else:
    print("nomal bill")

"""

"""