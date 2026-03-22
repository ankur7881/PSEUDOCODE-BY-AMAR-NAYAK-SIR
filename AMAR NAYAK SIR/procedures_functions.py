# Procedures - does not return value
'''
PROCEDURE add (x: INTEGER, y: INTEGER)
    PRINT x + y
END PROCEDURE
'''
# Functions - return value 
# (group of statements to perform specific task)
'''FUNCTION add (x: INTEGER, y: INTEGER) RETURN INTEGER
    RETURN x + y
END FUNCTION

# Example call:
CALL add (12, 8)
'''
# -----------------------------------------------------------------

# SIMPLE INTEREST BY PROCEDURES
'''
PROCEDURE simint (pa: INTEGER, roi: REAL, noy: REAL)
    DECLARE si: REAL
    
    si := (pa * roi * noy) / 100
    
    PRINT si
END PROCEDURE

CALL simint (100, 2.3, 1.2)
'''
def simint(pa, roi, noy):
    
    si = (pa * roi * noy) / 100
    print(f"Simple Interest: {si}")

simint(100, 2.3, 1.2)

# 1. Cube of a Number
'''
PROCEDURE cube(a: INTEGER)
    DECLARE cube: INTEGER
    cube := a * a * a
    PRINT cube
END PROCEDURE

CALL cube(5)
'''
def cube(a):
    print(f"Cube: {a**3}")
cube(5)


# 2. Area of a Triangle
'''PROCEDURE artri(b: REAL, h: REAL)
    DECLARE artri: REAL
    artri := 1/2 * b * h
    PRINT artri
END PROCEDURE

CALL artri(2.4, 3.0)
'''

def artri(b, h):
    area = 0.5 * b * h
    print(f"Area of Triangle: {area}")

artri(2.4, 3.0)


# 3. Find Max of Two Numbers
'''PROCEDURE max(a: REAL, b: REAL)
    DECLARE max: REAL
    IF a > b THEN
        PRINT a
    ELSE
        PRINT b
    ENDIF
END PROCEDURE

CALL max(12, 5)
'''
def max_procedure(a, b):
    if a > b:
        print(f"Max is: {a}")
    else:
        print(f"Max is: {b}")

max_procedure(12, 5)
# -------------------------------------------------


# 1. Simple Interest Function
'''FUNCTION simint (pa: INTEGER, roi: REAL, noy: REAL) RETURN REAL
    DECLARE si: REAL
    si := (pa * roi * noy) / 100
    RETURN si
END FUNCTION

PRINT simint (12, 3, 4)
'''
def simint(pa, roi, noy):
    return (pa * roi * noy) / 100
print(f"SI: {simint(12, 3, 4)}")



# 2. Cube Function
'''FUNCTION cube (a: INTEGER) RETURN INTEGER
    DECLARE cube: INTEGER
    cube := a * a * a
    RETURN cube
END FUNCTION

PRINT cube (5)
'''

def cube(a):
    return a ** 3
print(f"Cube: {cube(5)}")




# 3. Area of Triangle Function
'''FUNCTION ArTriangle (b: REAL, h: REAL) RETURN REAL
    DECLARE ArTriangle: REAL
    ArTriangle := 0.5 * b * h
    RETURN ArTriangle
END FUNCTION

PRINT ArTriangle (2.0, 3.0)
'''
def ar_triangle(b, h):
    return 0.5 * b * h
print(f"Area: {ar_triangle(2.0, 3.0)}")


# 1. Function to find Maximum of Two Numbers
'''FUNCTION max (a: INTEGER, b: INTEGER) RETURN INTEGER
    DECLARE c: INTEGER
    IF a > b THEN
        c := a
    ELSE
        c := b
    ENDIF
    RETURN c
END FUNCTION

PRINT max(23, 6)
'''
def max_function(a, b):
    if a > b:
        c = a
    else:
        c = b
    return c
print(f"Max: {max_function(23, 6)}")



# 2. Function to find Absolute Value
'''FUNCTION AbsValue (a: INTEGER) RETURN INTEGER
    IF a > 0 THEN
        RETURN a
    ELSE
        RETURN -a
    ENDIF
END FUNCTION

PRINT AbsValue(5)
PRINT AbsValue(-5)
'''

def abs_value(a):
    if a > 0:
        return a
    else:
        return -a

print(f"Abs 5: {abs_value(5)}")
print(f"Abs -5: {abs_value(-5)}")