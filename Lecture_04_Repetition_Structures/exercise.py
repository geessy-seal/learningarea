"""
Practice Question

เขียนโปรแกรม Python สำหรับคำนวณ sales commission โดยมีเงื่อนไขดังนี้:

ให้ผู้ใช้กรอกยอดขาย (sales)
ให้ผู้ใช้กรอกอัตราค่าคอมมิชชัน (commission rate)
คำนวณค่าคอมมิชชันจากสูตร:
commission=sales x commission rate
แสดงผลค่าคอมมิชชันโดยแสดงทศนิยม 2 ตำแหน่ง
หลังคำนวณเสร็จ ให้ถามผู้ใช้ว่าต้องการคำนวณอีกหรือไม่
ถ้าพิมพ์ y ให้ทำซ้ำ
ถ้าไม่ใช่ y ให้จบโปรแกรม

Output example
Enter the amount of sales: 50000
Enter the commission rate: 0.1
The commission is $5000.00
Do you want to calculate another commission (Enter y for ye
"""

loop = "y"
while loop == "y":
    sale = float(input("enter amount of sale: "))
    commission_rate = float(input("enter number of commissionrate: "))

    comission = sale * commission_rate

    print(f"the comission is ${comission:.2f}")

    loop = input("Do you want to calculate another commission (Enter y for yes): ")

"""
Practice Question

เขียนโปรแกรมช่วยตรวจสอบอุณหภูมิของสารชนิดหนึ่ง โดยมีเงื่อนไขดังนี้:

กำหนดอุณหภูมิสูงสุดที่ยอมรับได้เป็น 102.5 องศาเซลเซียส
ให้ผู้ใช้กรอกค่าอุณหภูมิเริ่มต้น
ถ้าอุณหภูมิสูงกว่า 102.5
แจ้งว่าอุณหภูมิสูงเกินไป
ให้ลด thermostat ลง
รอ 5 นาที
กรอกอุณหภูมิใหม่
ทำซ้ำจนกว่าอุณหภูมิจะไม่เกิน 102.5
เมื่ออุณหภูมิอยู่ในช่วงที่ยอมรับได้ ให้แสดงข้อความว่า:
temperature acceptable
check again in 15 minutes
"""
MAXIMUM_HEAT = 102.5
celcius = float(input("enter celcius: "))
while celcius > MAXIMUM_HEAT:
    #i know the way i print is odd but i just learn this so i want to use it
    print("hey it too hot too high temp\n", "decrease thermostat\n", "wait 5 min\n", sep= "")
    celcius = float(input("enter celcius again: "))
print("temperature acceptable")
print("check again in 15 min")


"""
Practice Question

เขียนโปรแกรม Python เพื่อแสดงตารางตัวเลขตั้งแต่ 1 ถึง 10 พร้อมค่ากำลังสองของแต่ละตัวเลข โดยมีเงื่อนไขดังนี้:

แสดงหัวตารางคำว่า:
Number    Square
แสดงเส้นคั่นใต้หัวตาราง
ใช้ loop แสดงตัวเลขตั้งแต่ 1 ถึง 10
ในแต่ละรอบ:
คำนวณค่ากำลังสองของตัวเลขนั้น
แสดงตัวเลขกับค่ากำลังสองในบรรทัดเดียวกัน
Output ที่ต้องได้ประมาณนี้
1   1
2   4
3   9
...
10  100
"""

print("Number\tSquare")
print("----------------------")

for number in range (1,11):
    square = number ** 2
    print(f"{number}\t{square}")

"""
Practice Question

เขียนโปรแกรม Python แสดงตารางตัวเลขและค่ากำลังสอง โดยมีเงื่อนไขดังนี้:

แจ้งผู้ใช้ว่าโปรแกรมนี้จะแสดงตัวเลขเริ่มจาก 1 และค่ากำลังสองของมัน
ให้ผู้ใช้กรอกว่าต้องการให้แสดงถึงเลขใด (end)
แสดงหัวตาราง:
Number    Square
ใช้ loop แสดงตัวเลขตั้งแต่ 1 ถึงค่าที่ผู้ใช้กรอก
ในแต่ละรอบ:
คำนวณ square
แสดงตัวเลขกับ square
"""
print("this program with start with 1 and it square")
end = int(input("choose the number of end"))
print("Number\tSquare")
for number in range(1, end + 1):
    square = number ** 2
    print(number, square, sep="\t")


"""
Practice Question

เขียนโปรแกรม Python เพื่อหาผลรวมของตัวเลข 5 ตัวที่ผู้ใช้กรอก โดยมีเงื่อนไขดังนี้:

แจ้งผู้ใช้ว่าโปรแกรมนี้จะคำนวณผลรวมของตัวเลข 5 ตัว
ใช้ loop รับค่าตัวเลขทีละตัวจำนวน 5 ครั้ง
ในแต่ละรอบ:
รับค่าตัวเลขจากผู้ใช้
นำไปบวกสะสมกับค่ารวม
หลังจบ loop ให้แสดงผลรวมทั้งหมด
Output ที่ต้องได้ประมาณนี้
Enter a number: 1
Enter a number: 2
Enter a number: 3
Enter a number: 4
Enter a number: 5
The total is 15
"""

print("this program will show result of 5 number u enter combine")

sum_value = 0
for i in range(5):
    number = int(input("enter an integer: "))
    sum_value += number

print("the total is", sum_value)


"""
Practice Question

เขียนโปรแกรม Python คำนวณภาษีทรัพย์สิน โดยมีเงื่อนไขดังนี้:

กำหนดอัตราภาษีคงที่ (tax factor) = 0.0065
ให้ผู้ใช้กรอกหมายเลข lot number
ถ้าผู้ใช้กรอก 0 ให้จบโปรแกรมทันที
ถ้าไม่ใช่ 0:
รับมูลค่าทรัพย์สิน (property value)
คำนวณภาษี:
tax=property value×0.0065
แสดงภาษีที่ได้
ถาม lot number ถัดไป
ทำซ้ำจนกว่าจะกรอก 0
สิ่งที่โจทย์นี้กำลังฝึกจริง ๆ
"""

TAX_FACTOR = 0.0065
lot_number = int(input("enter 0 if u want to stop: "))
while lot_number != 0:
    property_value = float(input("enter property value: "))
    tax = property_value * TAX_FACTOR
    print(tax)
    lot_number = int(input("enter 0 if u want to stop: "))

"""
Reverse engineer จากรูปนี้ → โจทย์ฝึก
Practice Question

เขียนโปรแกรม Python คำนวณราคาขายสินค้า โดยมีเงื่อนไขดังนี้:

กำหนดอัตราคูณราคาขาย (markup) = 2.5
ให้ผู้ใช้กรอกราคาต้นทุนสินค้า (wholesale cost)
ถ้าผู้ใช้กรอกค่าติดลบ:
แสดง error
ให้กรอกใหม่จนกว่าจะเป็นค่าที่ถูกต้อง
เมื่อได้ค่าถูกต้องแล้ว:

คำนวณราคาขาย:

retail=wholesale x 2.5
แสดงราคาขาย
ถามผู้ใช้ว่ามีสินค้าอีกไหม (y = ทำต่อ)
ถ้าตอบ y ให้ทำซ้ำ
"""


MARKUP = 2.5
again = "y"
while again == "y":
    wholesale_cost = float(input("enter your cost price: "))
    while wholesale_cost < 0:
        print("error cost cant be negative value")
        wholesale_cost = float(input("enter your cost price: "))

    retail = wholesale_cost * MARKUP

    print(retail)
    again = input("enter y if u still have other product: ")

"""
    Practice Question

เขียนโปรแกรม Python เพื่อคำนวณค่าเฉลี่ยคะแนนสอบของนักเรียนหลายคน โดยมีเงื่อนไขดังนี้:

ถามจำนวน students
ถามจำนวน test scores ต่อ student
สำหรับนักเรียนแต่ละคน:
แสดง student number
รับคะแนนสอบตามจำนวนที่กำหนด
รวมคะแนนทั้งหมด
คำนวณ average ของนักเรียนคนนั้น
แสดง average
ทำซ้ำจนครบทุก student
"""

num_of_student = int(input("enter number of student in class: "))
num_of_test = int(input("enter how many quiz u have taken"))

for student_num in range(1, num_of_student + 1):
    print("student number", student_num)
    sum_of_score = 0
    for test_num in range(1, num_of_test):
        score = float(input(f"enter your score for test {test_num}"))
        sum_of_score += score
    average = sum_of_score / num_of_test
    print(f"the average of student number {student_num} is {average}")

"""
Rectangle Pattern
Practice Question

เขียนโปรแกรม Python ให้ผู้ใช้กรอก:

จำนวนแถว (rows)
จำนวนคอลัมน์ (cols)

แล้วแสดงสี่เหลี่ยมของ *

Output ตัวอย่าง
*****
*****
*****
"""

rows = int(input("enter number of rows: "))
cols = int(input("enter number of cols: "))

for i in range(rows):
    for j in range(cols):
         print("*", end="")
    print()
"""
Practice Question

เขียนโปรแกรมแสดง triangle pattern โดยมีฐาน 8 แถว

แถวแรกมี 1 ดาว
แถวถัดไปเพิ่มทีละ 1 ดาว

Output ตัวอย่าง
*
**
***
****
"""

for rows in range(1, 9):
    for columb in range(rows):
        print("*", end="")
    print()

#or better way
for i in range(8):
    for j in range(i + 1):
        print("*", end="")
    print()
"""
Stair Step Pattern
Practice Question

เขียนโปรแกรมแสดง stair-step pattern จำนวน 6 ขั้น โดยใช้ #

แต่ละแถว:

มีช่องว่างเพิ่มขึ้นทีละ 1
แล้วตามด้วย #
Output ตัวอย่าง
#
 #
  #
   #
"""
#when i reread this why i over complicait so much
for rows in range(1, 7):
    for colum in range(rows - 1):
        print(" ", end="")
    print("#")
#or better way
for i in range(6):
    for j in range(i):
        print(" ", end="")
    print("#")