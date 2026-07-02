num = int (input("Enter a number = "))
rev = 0
while num > 0 :
    digits = num % 10
    rev = rev* 10 + digits
    num = num // 10 
    

print(rev)
