"""
Exercise: Electricity
Normal monthly rate for electricity usage exceeding 150 units per
month (excluding VAT):
Write a program to calculate the electricity bill by specifying that the
user enters the electricity usage data as an integer. The program will
output the data as the electricity bill, service charge, VAT (7% of the
total electricity bill (electricity bill plus service charge)) and the total
amount to be paid, with 2 decimal places.
"""
UNIT_RATE1 = 3.2484
UNIT_RATE2 = 4.2218
UNIT_RATE3 = 4.4217
SERVICE_FEE = 24.62
VAT = 0.07
consume_energy = int(input("Enter the energy consumption (kilowatt-hours): "))

if consume_energy <= 150:
    electricitybill = consume_energy * UNIT_RATE1
elif consume_energy <= 400:
    electricitybill = 150 * UNIT_RATE1 + (consume_energy - 150) * UNIT_RATE2
else: 
    electricitybill = 150 * UNIT_RATE1 + 250 * UNIT_RATE2 + (consume_energy - 400) * UNIT_RATE3

sub_total = electricitybill + SERVICE_FEE
vat_amount = sub_total * VAT

total_pay = sub_total + vat_amount

#to fking lazy to do the f string and.2f print