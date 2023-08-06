# function to show try, except and finally blocks --> catch errors
def error_handler(x, y):
    try:
        print("Dividing {} by {}".format(x, y))
        print(x/y)
    except ValueError:
        print("Error related to value assigment")
    except TypeError:
        print("Error related to data type assigment")
        print("values can only be of int datatype")
    except ZeroDivisionError:
        print("not possible to divide by 0")
        print("Correct answer --> {}".format(x/1))
    else:
        print("other errors not accounted for")
    finally:
        print("All Errors handled")

# raise and assert to raise local test exceptions
def raise_error(x, y):
    if x != y:
        raise Exception("Help me understand this condition.")
    
    # assert(x > y)
    
def main():
    
    error_handler(-1, 0)
    error_handler("text", 1)
    raise_error(100 , 200)
    
    
if __name__ == '__main__':
    main()