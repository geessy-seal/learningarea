"""
Challenge 4 จาก 5 🔥

เขียนโปรแกรมรับจำนวนเต็มบวก n

แล้วแสดง pattern:

ถ้า n = 4

1
23
456
78910
แต่เงื่อนไขเพิ่ม:

ถ้าตัวเลข > 5 ให้พิมพ์ #

ดังนั้น n = 4 จะได้

1
23
45#
####
"""
n = int(input("enter an integer: "))
num = 1
for i in range(n):
    for j in range(i+1):
        if num > 5:
            print("#", end="")
        else:
            print(num, end="")
        num += 1
    print()