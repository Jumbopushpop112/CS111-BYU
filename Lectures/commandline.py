import sys
print(sys.argv)

def calculate_pay(rate, hours):
    return rate * hours

calc_pay_text1 = sys.argv[1]
rate = float(sys.argv[2])
calc_pay_text2 = sys.argv[3]
hours = float(sys.argv[4])
calc_pay_text3 = sys.argv[5]

print(f'{calc_pay_text1} ${rate:.2f} {calc_pay_text2} {hours} {calc_pay_text3}, the amount paid will be ${calculate_pay(rate, hours):.2f}.') 