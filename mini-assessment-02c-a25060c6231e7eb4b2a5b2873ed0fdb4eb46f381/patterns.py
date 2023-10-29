
# TODO: Step 1 - return shape from user input (it can't be blank and must be a valid shape!)     
def get_shape():

    shape = input("Enter valid shape : ").lower()
    while shape not in ["square","triangle","pyramid"]:
        shape = input("Enter valid shape :").lower()
    return shape


# TODO: Step 2 - return height from user input (it must be int!)
#       The maximum possible height must be 80
def get_height():
    
    height = input("Enter valid height : ")
    while not height.isdigit() or int(height) > 80:
        height = input("Enter valid height : ")
    return int(height)

# TODO: Step 3 Complete the required shapes below
#       with reference to the unittests
def draw_square(height):
    output = ""
    for i in range(height):
        for j in range(height):
            print("*", end="")
        print()

def draw_triangle_reversed(height):
    for i in range(1, height + 1):
        for j in range((height + 1 -i)):
            print(i, end =" ")
        print()


def draw_triangle(height):
    for i in range(1,height + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


def draw_triangle_multiplication(height):
        for i in range(1, height+1):
            for j in range(i):
                print(i * (j +1),end=" ")
            print()



def draw_pyramid(height):
    for i in range(height):
        print(" " * (height - i - 1) + ("*" * (i + (i + 1))))



def draw_triangle_prime(height):
    """ 
    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    In Python, prime numbers are essential in various mathematical and computational applications. They play a
    fundamental role in number theory, cryptography, and data security.

    Prime numbers are characterized by the following properties:
    1. They are integers greater than 1.
    2. They have exactly two positive divisors: 1 and the number itself.
    3. They cannot be divided evenly by any other positive integer except 1 and itself.

    For example, some prime numbers are 2, 3, 5, 7, 11, 13, 17, and so on. Non-prime numbers are called composite
    numbers and have more than two positive divisors.
    
"""
    pass
         
                
# TODO: Step 4 - add support for other shapes
def draw(shape, height):
    if shape == "pyramid":
        draw_pyramid(height)
    if shape == "square":
        draw_square(height)
    if shape == "triangle":
        # draw_triangle_reversed(height)
        draw_triangle(height)



# TODO: Step 5 (standalone function) - Solve The Tower of Hanoi
def tower_of_hanoi(n, source, auxiliary, target):
    """
    Solve the Tower of Hanoi problem for n disks.

    Args:
        n (int): Number of disks to move.
        source (str): Name of the source peg.
        auxiliary (str): Name of the auxiliary peg.
        target (str): Name of the target peg.

    Returns:
        list: A list of moves to solve the Tower of Hanoi problem.

    Example:
    >>> tower_of_hanoi(3, 'A', 'B', 'C')
    [('A', 'C'), ('A', 'B'), ('C', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('A', 'C')]
    """
    return ""


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    draw(shape_param, height_param)