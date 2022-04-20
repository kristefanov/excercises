#Write a program that prints multiple numbers from 1 to 20
#But for multiples of 3 print "Fizz" instead of the number and for the multipliers of 5 print "Buzz"
#For numbers which are multiples both 3 and 5 print "FizzBuzz"
s = int(input())

for n in range(1,s+1):
    string = ""
    if n % 3 == 0:
        string += "Fizz"
    if n % 5 == 0:
        string += "Buzz"
    if n % 3 != 0 and n % 5 != 0:
        string += str(n)
    print(string)