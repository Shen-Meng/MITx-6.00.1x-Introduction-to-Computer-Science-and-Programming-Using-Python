#problem 1
pay = 10
while True:
    ub = balance
    for x in range(12):
        ub -= pay
        ub += ub*(annualInterestRate/12.0)
    if ub <= 0:
        print('Lowest Payment: ' + str(pay))
        break
    else:
        pay += 10


#problem 2
x = balance
low = balance/12.0
high = balance * (1+annualInterestRate/12.0)**12 / 12.0
while abs(x) > 0.01:
    p=(low + high) / 2.0
    x = balance
    for count in range(12):
        x = (x - p) * (1 + annualInterestRate / 12.0)
    if x > 0:
        low = p
    else:
        high = p
print 'Lowest Payment: %.2f' % p