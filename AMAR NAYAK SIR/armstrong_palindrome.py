#### ARMSTRONG NUMBER ####
'''
DECLARE n: INTEGER
DECLARE num: INTEGER
DECLARE b: INTEGER
DECLARE a: INTEGER

SET b := 0

READ num

n := num

WHILE n > 0
    a := n mod 10
    n := n / 10
    b := b + a * a * a
ENDWHILE

IF b == num THEN
    PRINT "Armstrong"
ELSE
    PRINT "Not Armstrong"
ENDIF
'''
# ACTUAL CODE

num = int(input("Enter a number: "))
b = 0
n = num

while n > 0:
    a = n % 10       
    n = n // 10        
    b = b + (a ** 3)  

if b == num:
    print("Armstrong")
else:
    print("Not Armstrong")

#### PALINDROME NUMBER ####
'''
DECLARE n: INTEGER
DECLARE num: INTEGER
DECLARE b: INTEGER
DECLARE a: INTEGER

SET b := 0

READ num

n := num

WHILE n > 0
    a := n mod 10
    n := n / 10
    b := b * 10 + a
ENDWHILE

IF b == num THEN
    PRINT "Palindrome"
ELSE
    PRINT "NOT Palindrome"
ENDIF
'''
#ACTUAL CODE 

num = int(input("Enter a number: "))
b = 0
n = num

while n > 0:
    a = n % 10          # Get the last digit
    n = n // 10         # Remove the last digit
    b = b * 10 + a      # Build the reversed number

if b == num:
    print("Palindrome")
else:
    print("NOT Palindrome")


###### JUMP,,BREAK,,CONTINUE #####---------------------------------

# BREAK STATEMENT
'''DECLARE i: INTEGER

FOR i := 1 TO 10
    IF i == 5 THEN
        BREAK
    ENDIF
    PRINT i
ENDFOR
'''
for i in range(1, 11):
    if i == 5:
        break
    print(i)

# CONTINUE STATEMENT
'''
DECLARE i: INTEGER

FOR i := 1 TO 10
    IF i == 5 THEN
        CONTINUE
    ENDIF
    PRINT i
ENDFOR
'''
for i in range(1, 11):
    if i == 5:
        continue 
    print(i)

#QUESTION:- PRINT ALL ODD NUMBER-----
'''
# Question: Print all odd numbers
DECLARE i := INTEGER

FOR i := 1 TO 10
    IF i mod 2 == 0 THEN
        CONTINUE
    ENDIF
    PRINT i
ENDFOR
'''
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

#QUESTION:- PRINT PRIME OR NOT 
'''
# PRIME Numbers
DECLARE n: INTEGER
READ n

FOR i := 2 TO n - 1
    IF n mod i == 0 THEN
        PRINT "Not Prime"
        BREAK
    ENDIF
ENDFOR

IF n == i THEN
    PRINT "Prime"
ENDIF
'''
n = int(input("Enter a number: "))

if n < 2:
    print("Not Prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")

#### FIBBONACHI SERIES
'''
DECLARE n: INTEGER
DECLARE PREV: INTEGER
DECLARE NEXT: INTEGER
DECLARE SUM: INTEGER

SET PREV := 0
SET NEXT := 1
SET SUM := 0

PRINT PREV
PRINT NEXT

WHILE SUM <= n
    SUM := PREV + NEXT
    PRINT SUM
    PREV := NEXT
    NEXT := SUM
ENDWHILE
'''
n = int(input("Enter the limit n: "))

prev = 0
next_val = 1
sum_val = 0

print(prev)
print(next_val)

while True:
    sum_val = prev + next_val
    if sum_val > n:
        break
    print(sum_val)
    prev = next_val
    next_val = sum_val

#QUESTION:-ENTER A NUMBER AND A DIGIT AND FIND DIGIT IS PRESENT OR NOT IN GIVEN NUMBER
'''
DECLARE n : INTEGER
DECLARE b : INTEGER
DECLARE a : INTEGER
DECLARE d : INTEGER
SET found : BOOLEAN := FALSE

READ n
READ d

WHILE n > 0
    a := n mod 10
    n := n / 10
    IF a == d THEN
        found := TRUE
        BREAK
    ENDIF
ENDWHILE

IF found == TRUE THEN
    PRINT "Search Successfull."
ELSE
    PRINT "Search Unsuccessfull"
ENDIF
'''
n = int(input("Enter the number: "))
d = int(input("Enter the digit to search: "))
found = False

temp = n # Using a temporary variable to keep the original n intact
while temp > 0:
    a = temp % 10
    temp = temp // 10
    if a == d:
        found = True
        break

if found:
    print("Search Successfull.")
else:
    print("Search Unsuccessfull")


# Question: Enter a number and a digit and 
# find how many times the digit is present in a number.
'''
DECLARE n: INTEGER
DECLARE a: INTEGER
DECLARE b: INTEGER
DECLARE count := INTEGER

SET count := 0

READ n
READ b

WHILE n > 0
    a := n mod 10
    n := n / 10
    IF a == b THEN
        INCREMENT count
    ENDIF
ENDWHILE

PRINT count
'''
n = int(input("Enter the number: "))
digit = int(input("Enter the digit to count: "))
count = 0

temp = n 
while temp > 0:
    remainder = temp % 10
    temp = temp // 10
    if remainder == digit:
        count += 1

print(f"The digit {digit} appears {count} times.")
