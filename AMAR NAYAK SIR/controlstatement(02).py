'''
### SELECTION:------
    1.IF:------

         IF condition THEN 
               statements
               ENDIF

    2.SWITCH:--------
'''
######################################################################################
'''    
Q1=Greatest of two

DECLARE a:INTEGER
DECLARE b:INTEGER
READ a,b:
IF a>b THEN
       PRINT "a is greater."
ELSE 
    PRINT "b is greater."
ENDIF
'''
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

if a > b:
    print("a is greater.")
else:

    print("b is greater.")

######-------------------------------------------------------------
'''
Q2=EVEN/ODD
DECLARE a:=INTEGER
READ a
IF a%2==0 THEN 
    PRINT "a is even number."
ELSE 
    PRINT"a is odd number."
'''    
 # CODE
a = int(input("Enter a number: "))

if a % 2 == 0:
    print("a is even number.")
else:
    print("a is odd number.")   
    
#-------------------------------------------------
''' Q3=IS INTEGER 
 DECLARE a:=INTEGER 
 READ a
 IF a>0 THEN
    PRINT "POSITIVE"
ELSEIF a<0 THEN
    PRINT "NEGETIVE"
ELSE
    PRINT "ZERO"
ENDIF
 '''   
# Read input and convert to integer
a = int(input("Enter a number: "))

if a > 0:
    print("POSITIVE")
elif a < 0:
    print("NEGETIVE")
else:
    print("ZERO")    
      



#### NESTED IF ########:-------------------

'''
EXAMPLE:
DECALRE UID: String
DECALRE Pass:String
READ UID 
READ Pass
IF UID=="ADMIN" THEN
    IF Pass=="ADMIN" THEN 
    PRINT"WELCOME"
    ELSE
        PRINT"WRONGPASS"
    ENDIF
ELSE
    PRINT"WRONG UID"
ENDIF
    '''
#ACTUAL CODE
uid = input("Enter UID: ")
password = input("Enter Pass: ")

if uid == "ADMIN":
    if password == "ADMIN":
        print("WELCOME")
    else:
        print("WRONGPASS")
else:
    print("WRONG UID")


'''EXAMPLE:
DECLARE cn,cd,pm,dbms,ml:INTEGER
READ cn,cd,pm,dbms,ml
DECLARE per:REAL
per:((n+cd+pm+dbms+ml)/5)
IF per>=90 THEN 
   PRINT"A+"
ELSEIF per>=80 THEN
   PRINT"A"
ELSEIF per>=70 THEN
   PRINT"B+"
ELSEIF per>=50 THEN 
    PRINT"B"
ELSEIF per>=30 THEN
    PRINT"C"
ELSE
    PRINT"FAIL"
ENDIF
'''



####### CASE  STATEMENT #############:--------

'''####SYNTAX####
DECLARE X:INTEGER
READ X
CASE OF X:
1:PRINT"ONE"
2:PRINT"TWO"
3:PRINT"THREE"
ELSE|OTHREWISE
PRINT"WRONG"
ENDCASE
'''
# QUESTION:-
'''
INTEGER P,Q,R
SET P=9,Q=6,R=10
if((Q^P^R)>(R^Q))
 R=(11&12)+Q
ENDIF
IF((Q^6^8)>P^4)
P=(R+3)&R
ENDIF
PRINT P+Q+R 
'''

# QUESTION:-
'''
INTEGER A,B,C
SET A=2,B=4,C=7
B=7+A
IF(C>B)
B=B+B
ENDIF
B=6+A
IF((A+B)<(B-A)||( <A))

B=(C+4)+C
ELSE
A=C+B
ENDIF
C=(C+9)^A
PRINT A+B+C
'''

######## LOOP/ITERATION ################
'''##### SYNTAX ####
REPEAT
S+S
 UNTIL CONDITION
 INTEGER X
 SET X:=1
 REPEAT
    PRINT X
    INCRREMENT X
UNTIL X<=10
'''

###### WHILE LOOP:--------------
''' SYNTAX ####
WHILE CONDITION LOOP
    STATEMENTS
    ENDWHILE
'''
# -------------------------------------
'''EXAMPLE######
INTEGER X
SET X:=1
WHILE X<=10 LOOP
    PRINT X
    INCREMENT X
ENDWHILE
'''

##### FOR LOOP:---------------------
'''
FOR Variable := Start TO End LOOP
    S + S
ENDFOR
'''


#-----------------------------
'''EXAMPLE######
FOR i := 1 TO 10 LOOP STEP 1
    PRINT i
ENDFOR
'''
# 1 to 10
for i in range(1, 11, 1):
    print(i)
'''
EXAMPLE#####
FOR i := 10 TO 1 LOOP STEP -1
    PRINT i
ENDFOR
'''
# 10 to 1
for i in range(10, 0, -1):
    print(i)
'''
EXAMPLE#######
FOR i := 1 TO 10 LOOP STEP 2
    PRINT i
ENDFOR
# Note: Increment with 2
'''
# 1 to 10 with step 2
for i in range(1, 11, 2):
    print(i)

#QUESTION:-- SUM OF FIRST (N) NATURAL NUMBERS
'''
DECLARE num: INTEGER
INTEGER i, sum

SET sum := 0

READ num

FOR i := 1 TO num LOOP
    sum := sum + i
ENDFOR

PRINT sum
'''
# ACTUAL CODE
num = int(input("Enter a number: "))
sum_val = 0

for i in range(1, num + 1):
    sum_val = sum_val + i

print("The sum is:", sum_val)

'''
DECLARE num: INTEGER
DECLARE n: INTEGER
INTEGER i

i := 1

READ n

FOR i := 1 TO n LOOP
    PRINT n * (n + 1) / 2
ENDFOR
'''
#ACTUAL CODE 
n = int(input("Enter n: "))
for i in range(1, n + 1):
    # This prints the final sum calculation 'n' times
    print(n * (n + 1) // 2)

#QUESTION:- SUM OF THE SQUARE OF THE FIRST (N) NATURAL NUMBEERS
'''
DECLARE num: INTEGER
INTEGER i, sum

SET sum := 0

READ num

FOR i := 1 TO num LOOP
    sum := sum + i * i
ENDFOR

PRINT sum
'''
#ACTUAL CODE
num = int(input("Enter num: "))
sum_val = 0

for i in range(1, num + 1):
    sum_val = sum_val + (i * i)

print("The sum of squares is:", sum_val)


#### FACTORIAL ####
'''
# FACTORIAL
DECLARE num: INTEGER
INTEGER i, fact

SET fact := 1

READ num

FOR i := num TO 1 LOOP STEP -1
    fact := fact * i
ENDFOR

PRINT fact
'''
#ACTUAL CODE 
num = int(input("Enter number for factorial: "))
fact = 1

# From num down to 1
for i in range(num, 0, -1):
    fact = fact * i

print("Factorial is:", fact)