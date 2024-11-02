def is_even(number):
    return True if number % 2 == 0 else False

def calculate_area(length, width):
    return length * width

def classify_triangle(a, b, c):
    if a == b == c:
        return 'equilateral'
    elif a == b or a == c or b == c:
        return 'isosceles'
    else:
        return 'versatile'



