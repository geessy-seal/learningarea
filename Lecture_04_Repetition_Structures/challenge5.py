"""
Challenge 5 จาก 5 (ข้อปิดบท) 🔥

ข้อนี้รวมของจริงทั้งหมด

เขียนโปรแกรมรับจำนวนเต็มบวก n

แสดง pattern แบบนี้:

ถ้า n = 5

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
แต่เงื่อนไขเพิ่ม:

ถ้าตัวเลขหาร 4 ลงตัว → พิมพ์ *

ดังนั้น n = 5 ต้องได้:

1
2 3 
* 5 6 
7 * 9 10
11 * 13 14 15
กติกาเพิ่ม
ต้องมีช่องว่างระหว่างตัว
running number ต่อเนื่อง
ห้าม reset
"""
#fuck this dont work when 2 deit number come into play and even for 1 degit why i even try to overcomplicait it
n = int(input("i said enter an fking integer not float: "))
num = 1
kee = 1
for i in range(n):
    for j in range(1 ,kee+1):
        if j % 2 == 0:
            print(" ", end="")
        elif num % 4 != 0:
            print(num, end="")
        else:
            print("*", end="")
        num += 1
    kee += 2
    print()
#tbh am a person who like logic staright foward so i like this more
#elif num % 4 == 0:
    #print("*", end="")
#else:
    #print(num, end="")




#this version work    
n = int(input("enter integer: "))
num = 1

for i in range(n):
    for j in range(i + 1):
        if num % 4 == 0:
            print("*", end=" ")
        else:
            print(num, end=" ")
        num += 1
    print()


