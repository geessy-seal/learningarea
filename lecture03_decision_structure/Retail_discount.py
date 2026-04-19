"""
A software company sells a package that retails for 99 baht.
Quantity discounts are given according to the following table:
Write a program that asks the user to enter the number of
packages purchased. The program should then display the
amount of the discount (if any) and the total amount of the
purchase after the discount.
"""

RETAIL = 99
packnum = int(input("enter the number of packages purchased: "))

if packnum >= 100:
    discount_rate = 0.4
elif packnum >= 50:
    discount_rate = 0.3
elif packnum >= 20:
    discount_rate = 0.2
elif packnum >= 10:
    discount_rate = 0.1
else: 
    discount_rate = 0

sub_total = packnum * RETAIL
amount_discount =  sub_total* discount_rate
total_pay = sub_total - amount_discount

#can use \n instead or the best way would be use print func 3 time because it easy to read
print(f"""Normal amount: {sub_total:,.2f} Baht
Discount amount: {amount_discount:.2f} Baht
Total amount: {total_pay:,.2f} Baht""")