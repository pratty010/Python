# var assignment and type conversion

# global variable
pi = 3.14


# var assignment
def assign():
    x = 10
    y ="Hello"
    z = 3.1453
    a = True
    b = "34"
    bt = b"Hello"


    di = {
        "hello": 1,
        "world": 2
    }
    s = {1,2,3}
    l = ['a', 'b', 'c']
    t = ("Hello", "World", 3.14)
    r = range(10)

    # basic data type
    print(x, type(x))
    print(y, type(y))
    print(z, type(z))
    print(a, type(a))
    print(bt, type(bt))


    print(b,type(b))
    # type casting - forceful conversion
    b = int(b) 
    print(b,type(b))

    # collection type
    print(di, type(di))
    print(s, type(s))
    print(l, type(l))
    print(t, type(t))
    print(r, type(r))
    
    # print global var - avaible to all funtions
    print(pi)
    


def main():
    # function call
    assign()
    # print global var
    print(pi)
    
if __name__ == '__main__':
    main()