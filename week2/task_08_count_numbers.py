number = int(input("enteryour number"))
even = 0
odd = 0
total = 0
for i in range(1,number + 1):
  total +=i
  if i % 2 ==0:
    even += 1
 
  else:
    odd += 1
    

print(even)
print(odd)
print(total)