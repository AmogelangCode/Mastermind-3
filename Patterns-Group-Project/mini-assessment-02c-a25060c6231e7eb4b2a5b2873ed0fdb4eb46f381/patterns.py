def get_shape():
    """
    function to get shape from user
    must be a valid shape
    """
    shape = input("Shape: ").lower().strip()
    if shape not in ["triangle","square","pyramid"]:
        return get_shape()
    return shape



def get_height():
    """
    function to get height::integer
    """
    height = int(input("height: "))
    if height > 80:
        return get_height()
    return height


def draw_square(height):
    """
    func to draw square shaped astercs
    """
    for i in range(height):
        for _ in range(height):
            print("*",end="")
        print()


def draw_triangle_reversed(height):
    """
    function to draw a reversed triangle
    """
    for i in range(height):
        for _ in range(i,height):
            print(i+1,end=" ")
        print()


def draw_triangle(height):
    """
    function that draws an increamenting triangle
    """
    for i in range(1,height+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()


def draw_triangle_multiplication(height):
    """
    function that draws an increamenting triangles of multiplication
    """
    for i in range(1,height+1):
        for j in range(1,i+1):
            print(j*i,end=" ")
        print()


def draw_pyramid(height):
    """
    function that draws a pyramid
    """
    for i in range(height):

        for _ in range(height-i-1):
            print(" ",end="")

        for _ in range(2*i+1):
            print("*",end="")
        print()



def draw(shape, height):
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
    return ""


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    draw(shape_param, height_param)