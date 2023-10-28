import random
# TODO: Step 1 - return shape from user input (it can't be blank and must be a valid shape!)     
def get_shape():
    shape = input("shape: ").lower().strip()
    if shape not in ["triangle","square","pyramid"]:
        return get_shape()
    else:
        return shape


# TODO: Step 2 - return height from user input (it must be int!)
#       The maximum possible height must be 80
def get_height():
    height = int(input("height: "))
    if height > 80:
        return get_height()
    else:
        return height


# TODO: Step 3 Complete the required shapes below
#       with reference to the unittests
def draw_square(height):
    for i in range(height):
        for j in range(height):
            print("*",end="")
        print()


def draw_triangle_reversed(height):
    for i in range(height):
        for _ in range(i,height):
            print(i+1, end=" ")
        print()


def draw_triangle(height):
    for i in range(1,height+1):
        for j in range(1,i+1):
            print(j, end=" ")
        print()



def draw_triangle_multiplication(height):

    for i in range(1,height+1):
        for j in range(1,i+1):
            print(j*i, end=" ")
        print()


def draw_pyramid(height):
    for i in range(height):
        for j in range(height-i-1):
            print(" ",end="")
        for j in range(2*i+1):
            print("*",end="")
        print()



def draw_triangle_prime(height):
    '''filter out prime rturn '''
    def is_prime(num):
        for i in range(2,num):
            if num % i == 0:
                return False
        return True
    init_prime = 2
    for k in range(1, height+1):
        for _ in range(k):
            while not is_prime(init_prime):
                init_prime += 1
            print(init_prime, end=" ")
            init_prime += 1
        print()
         
                
# TODO: Step 4 - add support for other shapes
def draw(shape, height):
    if shape == "pyramid":
        draw_pyramid(height)
    if shape == "square":
        draw_square(height)
    if shape == "triangle":
        draw_triangle(height)
    if shape == "triangle multiplaction":
        draw_triangle_multiplication(height)
    if shape == "triangle prime":
        draw_triangle_prime(height)
    if shape == "pyramid":
        draw_pyramid(height)


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
    k = []
    if n == 1:
        return [('A', 'C')]
    else:
        for i in range(n*2):
            k.append((random.choice((auxiliary,source,target),2)))
        return k
    # else:
    #     k.append(((source,)))
        


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    draw(shape_param, height_param)