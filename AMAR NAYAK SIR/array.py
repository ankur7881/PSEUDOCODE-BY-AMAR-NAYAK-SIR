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

#---------------------

DECLARE x: ARRAY[2][2] OF INTEGER

FOR r := 0 TO 1        # r stands for Rows
    FOR c := 0 TO 1    # c stands for Columns
        # Array access happens here: x[r][c]
    ENDFOR
ENDFOR
'''
x = [[0, 0], [0, 0]]

for r in range(2):
    for c in range(2):
        x[r][c] = int(input(f"Enter x[{r}][{c}]: "))

print("The Matrix is:")
for row in x:
    print(row)

#### SUM OF All ELEMENTS OF 2D ARRAY ####
'''
DECLARE x : ARRAY [3][3] OF INTEGER
DECLARE Sum : INTEGER

SET Sum := 0

FOR r := 0 TO 2
    FOR c := 0 TO 2
        READ x [r][c]
    ENDFOR
ENDFOR

FOR r := 0 TO 2
    FOR c := 0 TO 2
        Sum := Sum + x [r][c]
    ENDFOR
ENDFOR

PRINT Sum
'''
x = [[0 for _ in range(3)] for _ in range(3)]
sum_val = 0

for r in range(3):
    for c in range(3):
        x[r][c] = int(input(f"Enter element for [{r}][{c}]: "))

for r in range(3):
    for c in range(3):
        sum_val = sum_val + x[r][c]

print("The sum is:", sum_val)

#### COUNT TOTAL NO. OF EVEN ODD INSIDE METRIX ####
'''
DECLARE x: ARRAY [3][3] OF INTEGER
DECLARE even: INTEGER
DECLARE odd: INTEGER

SET even := 0, odd := 0

# Input Loop
FOR r := 0 TO 2
    FOR c := 0 TO 2
        READ x[r][c]
    ENDFOR
ENDFOR

# Processing Loop
FOR r := 0 TO 2
    FOR c := 0 TO 2
        IF x[r][c] mod 2 == 0 THEN
            even := even + 1
        ELSE
            odd := odd + 1
        ENDIF
    ENDFOR
ENDFOR

PRINT even
PRINT odd
'''
x = [[0 for _ in range(3)] for _ in range(3)]
even = 0
odd = 0

for r in range(3):
    for c in range(3):
        x[r][c] = int(input(f"Enter element for [{r}][{c}]: "))

for r in range(3):
    for c in range(3):
        if x[r][c] % 2 == 0:
            even += 1
        else:
            odd += 1

print(f"Even numbers: {even}")
print(f"Odd numbers: {odd}")

#### Addition of 3x3 Matrix ####
''''
DECLARE x: ARRAY[3][3] OF INTEGER
DECLARE y: ARRAY[3][3] OF INTEGER
DECLARE z: ARRAY[3][3] OF INTEGER

FOR r := 0 TO 2
    FOR c := 0 TO 2
        READ x[r][c]
        READ y[r][c]
    ENDFOR
ENDFOR

FOR r := 0 TO 2
    FOR c := 0 TO 2
        z[r][c] := x[r][c] + y[r][c]
    ENDFOR
ENDFOR

FOR r := 0 TO 2
    FOR c := 0 TO 2
        PRINT z[r][c]
    ENDFOR
ENDFOR
'''
x = [[0]*3 for _ in range(3)]
y = [[0]*3 for _ in range(3)]
z = [[0]*3 for _ in range(3)]

for r in range(3):
    for c in range(3):
        x[r][c] = int(input(f"Enter x[{r}][{c}]: "))
        y[r][c] = int(input(f"Enter y[{r}][{c}]: "))

for r in range(3):
    for c in range(3):
        z[r][c] = x[r][c] + y[r][c]

print("Matrix Z (Sum):")
for row in z:
    print(row)





