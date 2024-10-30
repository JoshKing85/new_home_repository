'''
Define function calculate weekly_pay.

This function will pass hours worked in a week. The function will calcute wages for hours worked for a standard pay.
 If hours are greater than 35 the fuction will calculate over time hours
and add to standard hours worked. 
Total wages will be returned.

'''

def calculate_weekly_pay(hours):

    if hours <= 35:
        wages = hours*12
    
    else:
        over_time = hours - 35
        wages = (35*12) + (over_time*18)
    
    
    return wages


'''
Test values are...

32, 35, 56


Expected outputs in order are...

Gross weekly wage is: £384
Gross weekly wage is: £420
Gross weekly wage is: £798

'''

print('Gross weekly wage is: £', calculate_weekly_pay(32))
print('Gross weekly wage is: £', calculate_weekly_pay(35))
print('Gross weekly wage is: £', calculate_weekly_pay(56))
