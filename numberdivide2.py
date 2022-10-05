asknumber = input("Please submit a number: ")

try:
   newnum = int(asknumber)
except:
    print("Please submit a number")
    exit()

num = newnum/2

if num % 4 == 0:
  print("Your number is a multiple of 4,", num)
else:
  print("Your number divided by 2 is:", num)
