num=int(input("Enter the value:"))

if num>1:

for i in range(2,num):

if (num%i==0):

print("It is not a prime number.")

else:

print("It is a prime number.")

else:

print(num,'is not a prime number')