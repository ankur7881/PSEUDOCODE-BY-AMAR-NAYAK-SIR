''' DECLARE a:INTEGER
 DECLARE b:INTEGER
 DECLARE C:INTEGER
 SET a:=8 ,b:=51, C:=2
     c:=(a^b)^a
     b:=b mod 4
     print a+b+c
     '''
#ACTUAL CODE
a = 8
b = 51
c = 2

c = (a ^ b) ^ a  
b = b % 4         

print(a + b + c) 






'''
DECLARE a:INTEGER
DECLARE b:INTEGER
DECLARE C:INTEGER
SET a:=1 ,b:=1
    a:=(a^1)+(1)+(b^1)+1
'''
#ACTUAL CODE
a = 1
b = 1
a = (a ^ 1) + 1 + (b ^ 1) + 1
print(a)








''' DECLARE a:,b:,c:=INTEGER
 SET c:=8,b:=2
     a:=c/b
     c:=b>>a
     print c
'''
#ACTUAL CODE

c = 8
b = 2

a = c // b  

c = b >> a 

print(c) 



