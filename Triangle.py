
def classifyTriangle(a, b, c):
    # require that the input values be >= 0 and <= 200
    if (a > 200 or a <= 0) or (b > 200 or b <= 0) or (c > 200 or c <= 0):
        return 'InvalidInput'
    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    elif not(isinstance(a, int) or isinstance(b, int) or isinstance(c, int)):
        return 'InvalidInput'
    elif (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'

# now we know that we have a valid triangle
    elif a == b and b == c and a == c:
        return 'Equilateral'
    elif ((a ** 2) + (b ** 2)) == (c ** 2) or ((c ** 2) + (b ** 2)) == (a ** 2) or ((a ** 2) + (c ** 2)) == (b ** 2):
        return 'Right'
    elif (a != b) and (b != c) and (a != c):
        return 'Scalene'
    else:
        return 'Isosceles'

