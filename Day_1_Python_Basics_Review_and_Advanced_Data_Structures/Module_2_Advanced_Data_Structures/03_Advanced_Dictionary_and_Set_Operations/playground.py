
# Generate a list of elements where range 1 to 50, only odd numbers

odd_numers = [i for i in range(1,51) if i%2!=0]
# [expression  Loops   Condition ]
print(odd_numers)

odd_number_square = [i**2 for i in range(1,51) if i%2!=0]
# [expression  Loops   Condition ]
print(odd_numers)

odd_even = [i+i if i%2==0 else i*i for i in range(1,51)]
print(odd_even)

