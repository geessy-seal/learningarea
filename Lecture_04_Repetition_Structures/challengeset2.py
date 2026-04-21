"""
Challenge 2 จาก 5 🔥

เขียนโปรแกรมรับเลขจำนวนเต็มบวก 1 จำนวน n

จากนั้นหาว่า:

มีกี่จำนวนระหว่าง 1 ถึง n ที่หารทั้ง 2 และ 5 ลงตัว

แล้วแสดงผลรวมของเลขเหล่านั้นด้วย

ตัวอย่าง

ถ้า n = 30

เลขที่เข้าเงื่อนไขคือ:

10 20 30

ผลลัพธ์:

count = 3
sum = 60
"""
n = int(input("enter an integer: "))
divisible = 0
sum_of_divisible = 0
for i in range(1, n+1):
    if (i % 2 == 0) and (i % 5 == 0):
        divisible += 1
        sum_of_divisible += i
print("count =", divisible)
print("sum =", sum_of_divisible)
#since it too easy let try brute force with while loop
n = int(input("enter an integer: "))

start = 1
divisible = 0
sum_of_divisible = 0
while start <= n:
    current_num = start
    if (current_num % 2 == 0) and (current_num % 5 == 0):
        divisible += 1
        sum_of_divisible += current_num
    start += 1
print("count =", divisible, "\n", "sum =", sum_of_divisible)
