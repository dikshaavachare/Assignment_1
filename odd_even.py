list =[1,2,3,4,5,6,7,8,9]
total_odd = 0
total_even = 0
for number in list:
    if(number % 2 == 0):
        total_even = total_even + 1
    else:
        total_odd = total_odd + 1

print('total odd number = ',total_odd)
print('total even number = ',total_even)