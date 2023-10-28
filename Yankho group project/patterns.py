# TODO: Step 1 - return shape from user input (it can't be blank and must be a valid shape!)     
def get_shape():
    '''prompt the user for an input and return that input'''
    

    shapes = ["square", "triangle", "pyramid"]
    while True:
        shape= input("Enter a shape: ").lower()
        if shape not in shapes:
            shape = ("Enter a shape: ").lower
        else:
            return shape




# TODO: Step 2 - return height from user input (it must be int!)
#       The maximum possible height must be 80
def get_height():
    '''prompt the user for an input that is an integer with a limit of 80'''


    height = input("Enter height: ")
    while not height.isdigit and int(height)>80:
        height = input("Enter height: ")

    return int(height)
    


    # TODO: Step 3 Complete the required shapes below
#       with reference to the unittests
def draw_square(height):
    '''args:
        height
        
        return a 2d square shape using asterisks'''


    for row in range(height):
        for column in range(height):
            print("*", end = "")
        print()
    


def draw_triangle(height):
    '''args:
        height
        
        return a 2d triangle shape using dollar signs'''
    
    for row in reversed(range(height)):
        for column in range(1,height-row+1):
            print("$", end = "")
        print()
    


def draw_pyramid(height):
    '''args:
        height
        
        return a 2d shape of a pyramid using asterisks'''


    k = height-1
    for y in range(1,height*2,2):
        print(" "*k+"*"*y)
        k-=1




# TODO: Step 4 - add support for other shapes
def draw(shape, height):
    '''args:
        shape, height
        
        return the specific function that will draw a shape according to the input'''


    if shape == "pyramid":
        draw_pyramid(height)

    elif shape == "square":
        draw_square(height)

    elif shape == "triangle":
        draw_triangle(height)

    # if shape == "tower of hanoi":
    #     tower_of_hanoi(height)   


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


    if n == 1:
        # Base case: If there's only one disk, move it from the source to the target peg.
        return [(source, target)]
    else:
        # Recursive case:
        # 1. Move n-1 disks from the source peg to the auxiliary peg using the target peg.
        # 2. Move the largest disk from the source peg to the target peg.
        # 3. Move the n-1 disks from the auxiliary peg to the target peg using the source peg.
        # Combine all the moves and return them as a list.
        moves = []
        moves += tower_of_hanoi(n - 1, source, target, auxiliary)  # Step 1
        moves.append((source, target))  # Step 2
        moves += tower_of_hanoi(n - 1, auxiliary, source, target)  # Step 3
        return moves



if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    draw(shape_param, height_param)