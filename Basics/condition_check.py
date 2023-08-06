# func to get input from user
def inpu():
    a = input("Input First Number -->")
    b = input("Input Second Number -->")
    
    return a, b

# func to use if, elif and else
def if_con(a, b):
    if a > b:
        print("{} is greater than {}.".format(a, b))
    elif a < b:
        print("{} is less than {}.".format(a, b))
    else:
        print("{} = {}.".format(a, b))

# main func
def main():
    a, b = inpu()
    if_con(a, b)
   
    
if __name__ == '__main__':
    main()

        