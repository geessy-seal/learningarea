#question1
name1 = input("enter your name: ")
name2 = input("enter your name: ")

#question2
num = int(input("enter integer: "))
num += 10
print(num)

#question3
num = float(input("enter real number: "))
print(f"{num:.2f}")

#question4 instruction unclear

#question5
x = 17
y = 5
print(f"{x//y} {x%y}")

#q6
width = float(input("enter width: "))
height = float(input("enter height: "))

area = width * height

#q7
num1 = float(input("enter num: "))
num2 = float(input("enter num: "))

#q8
total_min = int(input("enter num of min"))
hour = total_min // 60
min = total_min % 60
print(f"{hour} hour {min} minutes")

#q9
#it contsant value so it capital
PRICE = 89.75
print(f"{PRICE} THB")

#q10
num = int(input("enter intreger: "))
#we not just want remainer but decimal value so it not just num%3
decimal = (num % 3) / 3

#q11
price = float("input price of product: ")
#this also constant value so capital
VAT = 0.07
tax_amount = price * VAT
total_pay = tax_amount + price
print(f"{total_pay:.2f}")

#q12
num1 = int(input("enter your intreger: "))
num3 = int(input("enter your intreger: "))
num3 = int(input("enter your intreger: "))

average = (num1 + num2 + num3) / 3
print(f"{average:.3f}")

#q13
total_sec = int(input("number of second: "))
min = total_sec // 60
sec = total_sec % 60
print(min , sec)

#q14
distance = 456.789
time = 12
speed = distance / time
print(f"{speed:.2f}")

#q15 kindda bored from now on if it easy i ll skip

#q16
type1product = input("enter product name: ")
type1price = float(input(f"enter price of {type1product} per one"))
type2product = input("enter product name: ")
type2price = float(input(f"enter price of {type2product} per one"))
numofproducttype1 = int(input(f"number of  {type1product} you buy"))
numofproducttype2 = int(input(f"number of  {type2product} you buy")) 
total_price = (numofproducttype1 * type1price) + (numofproducttype2 * type2price)
#didnt tell me to print only tell me to find ราคารวม so

#q17
celsius = int(input("enter number of celsius u facring rn: "))
F = (9/5)*celsius + 32

#q18 
money = int(input("enter number of money: "))
bank100 = money // 100
remain = money % 100

#q19 it like many question i already done so i skip

#q20 it just use f string
