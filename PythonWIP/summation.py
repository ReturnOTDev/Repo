import time

inp1 = input("Please enter a number here: ")
inp2 = input("Please input your second number: ")

def timer(func):
    def wrap(*args):
        start = time.time()
        func(*args)
        end = time.time()
        print("\nThis process took " + str(((end-start) * 1000)) + " milliseconds.")
        time.sleep(1.5)
    return wrap

@timer
def adder(a, b):

    while len(a) < len(b):
        a = "0" + a
    while len(b) < len(a):
        b = "0" + b

    # turning a and b into reversed lists of integers, because binary is calculated right to left
    a = list(map(lambda x: int(x), a))[::-1]
    b = list(map(lambda x: int(x), b))[::-1]

    # setting count and an empty text file for use later
    text = ""


    # iterating through a range of the length of a (to use for any bit size)
    for i in range(len(a)):

        # setting up both and xor boolean functions ("Logic Gates - Composite") for use later
        both = a[i] and b[i]
        xor = (not a[i] and b[i]) or (not b[i] and a[i])

        # running through the first binary numbers using a Half-Adder
        if i == 0:

            # creating the Half-Adder using boolean functions ("Composite and Elementary Logic Gates")
            if both:
                sum = 0
                count = 1
            elif xor:
                sum = 1
                count = 0
            elif not both:
                sum = 0
                count = 0
            
             # adds the sum (worked out in adder), to the final text
            text += str(sum)

        # implements the Full-Adder when adding the next binary numbers in the sequence
        else:

            # Full-Adder implemented using boolean functions.

            if both and count:
                sum = 1
                count = 1
            elif both and not count:
                sum = 0
                count = 1
            elif xor and count:
                sum = 0
                count = 1
            elif xor and not count:
                sum = 1
                count = 0
            elif (not both) and count:
                sum = 1
                count = 0
            else:
                sum = 0
                count = 0
            
            # adds the sum of the two binary numbers to the final text, the count is passed on
            text += str(sum)
    
    # the main function returns the final, printed boolean number
    # reverses the order back
    if count > 0 :
        return print("\n\n\nThe final number is: " + str(count) + text[::-1])
    else:
        return print("\n\n\nThe final number is: " + text[::-1])
    


adder(inp1, inp2)
