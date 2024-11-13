'''
Define function net_annual_income.
Function will pass gross pay as argument, select appropriate tax deduction,
calcute net pay using appropiate reduction and return net pay.

'''
def net_annual_income(gross):


    net = 0
    # Deductions determined from equal or greater if selections.
    if gross >= 45000:
        net = gross * (1 - 0.5) # All deductions use same formula (1 - n) for percentage reduction.
    
    elif gross >= 30000:
        net = gross * (1 - 0.3)

    else:
        net = gross * (1 - 0.15)
    
    return net

'''
Test values...
45000, 44999, 30000, 29999.
Values will test boundaries of all if selctions for tax deductions.
'''
print('Your net annual salary wil be: £', net_annual_income(45000)) #Your net annual salary wil be: £22500
print('Your net annual salary wil be: £', net_annual_income(44999)) #Your net annual salary wil be: £34999.3
print('Your net annual salary wil be: £', net_annual_income(30000)) #Your net annual salary wil be: £21000
print('Your net annual salary wil be: £', net_annual_income(29999)) #Your net annual salary wil be: £25499.15
