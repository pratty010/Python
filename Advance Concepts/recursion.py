# normal factorial loop function
def fact(x):
    fac = 1
    for i in range(x):
        fac *= (i+1)
    
    return fac

# factorial function - recurrsively
def rec_fact(x):
    if x == 1:
        return 1
    else:
        return x * rec_fact(x-1)

# loop fibonacci funtion - return the nuumber at input index
def fib(x):
    a = 0
    b = 1
    
    fibl = [0, 1]
    
    for i in range(x - 2):
        b = fibl[i] + fibl[i+ 1]
        fibl.append(b)

    return fibl[-1]

# recurrsive funtion to do the same as fib()
def rec_fib(x):
    if x == 1:
        return 0
    elif x == 2:
        return 1
    else:
        return rec_fib(x - 1) + rec_fib(x - 2)
        


def main():
    
    # factorial function calls
    print(fact(7))
    print(rec_fact(7))
    
    # fibonacci function calls
    print(fib(5))
    print(rec_fib(5))
    
if __name__ == '__main__':
    main()        