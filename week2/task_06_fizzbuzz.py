i = int(input("enter starting point"))
n = int(input("enter ending point"))
for i in range (i,n +1,1):
  if i % 3 == 0 and i % 5 ==0:
    print("FizzBuzz")
  elif i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz")
  
  else:
    print(i)