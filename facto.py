
# factorial of  n
#n x n-1 x n-2, where n-i, i+=1
#I used while loop
#school homework: Pratyush Saha Class 10
#Kendriya Vidyalaya Sangathan

i = 1


n = int(input("Enter a number: "))
p = 1
while i <= n:
    p*=i
    i+=1
print(p)
