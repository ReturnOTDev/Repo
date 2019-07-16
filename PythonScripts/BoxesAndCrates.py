# This is a file that takes in the dimensions of any given crate and determines the maximum number of boxes that can fit inside it (given box dimensions)




# creating fit1 as a baseline for other fit functions (setting Z as 1 by default for 2D structures)
def fit1(X, Y, x, y):
    return (X // x) * (Y // y)


# creating fit2 by using fit1 but switching x and y as arguments
# Then creating a list containing no. of boxes and returning the max value
def fit2(X, Y, x, y):
    pos1 = fit1(X, Y, x, y)
    pos2 = fit1(X, Y, y, x)
    boxes = [pos1, pos2]
    return max(boxes)


# creating fit3 with same idea as fit2 except with the implementation of width/depth
# which brings along many more permutations.

def d3(X, Y, Z, x, y, z):
    return (X // x) * (Y // y) * (Z // z)


def fit3(X, Y, Z, x, y, z):
    pos1 = d3(X, Y, Z, x, y, z)
    pos2 = d3(X, Y, Z, y, x, z)
    pos3 = d3(X, Y, Z, y, z, x)
    pos4 = d3(X, Y, Z, z, y, x)
    pos5 = d3(X, Y, Z, x, z, y)
    pos6 = d3(X, Y, Z, z, x, y)
    boxes = [pos1, pos2, pos3, pos4, pos5, pos6]
    return max(boxes)


# creating fit_n with variables for crate and box dimensions
# it iterates through the number of dimensions, by creating a range of the list length
# then multiplies the variables boxes by the int division of box and crate dimension lengths
def fit_n(crate_dim, boxes_dim):
    boxes = 1
    for i in range(len(crate_dim)):
        boxes *= (crate_dim[i] // boxes_dim[i])
    return boxes
