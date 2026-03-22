# DECLARATION of Array
# Declaration of 1D
'''
DECLARE a: ARRAY[5] OF INTEGER
DECLARE b: ARRAY[10] OF REAL
DECLARE name: ARRAY[5] OF STRING
'''

#DECLARE a: ARRAY[1:5] OF INTEGER
''' 1 -> lower bound
 5 -> upper bound
 '''

# Example: Array Input and Output
'''DECLARE a: ARRAY[0:4] OF INTEGER

FOR i := 0 TO 4
    READ a[i]
ENDFOR

FOR i := 0 TO 4
    PRINT a[i]
ENDFOR
'''
a = [0] * 5

for i in range(5):
    a[i] = int(input(f"Enter element for index {i}: "))

print("The array elements are:")
for i in range(5):
    print(a[i])

# SUM OF ARRAY ELEMENTS
'''
DECLARE sum: INTEGER
SET sum := 0

FOR i := 0 TO 4
    READ a[i]
ENDFOR

FOR i := 0 TO 4
    sum := sum + a[i]
ENDFOR

PRINT sum
'''
a = [0] * 5
sum_val = 0

# Input Loop
for i in range(5):
    a[i] = int(input(f"Enter element {i}: "))

# Calculation Loop
for i in range(5):
    sum_val = sum_val + a[i]

print("The sum of all elements is:", sum_val)

# Maximum of Array---------------
'''
DECLARE a: ARRAY[5] OF INTEGER
DECLARE max: INTEGER

FOR i := 0 TO 4
    READ a[i]
ENDFOR

SET max := a[0]

FOR i := 0 TO 4
    IF a[i] > max THEN
        max := a[i]
    ENDIF
ENDFOR

PRINT max
'''
a = [0] * 5

for i in range(5):
    a[i] = int(input(f"Enter element {i}: "))

max_val = a[0]
for i in range(5):
    if a[i] > max_val:
        max_val = a[i]

print("Maximum value is:", max_val)

# Pro-tip: Can also just use: print(max(a))

# Minimum Value of Array----------------------
'''
DECLARE a: ARRAY[5] OF INTEGER
DECLARE min: INTEGER

FOR i := 0 TO 4
    READ a[i]
ENDFOR

SET min := a[0]

FOR i := 0 TO 4
    IF a[i] < min THEN
        min := a[i]
    ENDIF
ENDFOR

PRINT min
'''
a = [0] * 5

# Input Loop
for i in range(5):
    a[i] = int(input(f"Enter element {i}: "))

# Comparison Logic
min_val = a[0]
for i in range(5):
    if a[i] < min_val:
        min_val = a[i]

print("Minimum value is:", min_val)

##### DECLERATION OF 2D ARRAY ######
'''
DECLARE x: ARRAY[2][2] OF INTEGER

 OR using range notation----

DECLARE x: ARRAY[0:1][0:1] OF INTEGER

 OR short hand----

Integer x[2][2]
Integer y[3][3]



DECLARE x: ARRAY[2][2] OF INTEGER

FOR r := 0 TO 1        # r stands for Rows
    FOR c := 0 TO 1    # c stands for Columns
        # Array access happens here: x[r][c]
    ENDFOR
ENDFOR

'''
