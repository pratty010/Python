# normal while loop
def while_loop(a):
    i = 1
    while i < a:
        print(i)
        i += 1

# condition controlled while loop
def while_ctrl_loop(c):
    while c < 10:
        c += 1
        if c % 3 == 0:
            print("{} divisible by 3. Skipping".format(c))
            continue
        else:
            print(c)
    
       
# normal for loop 
def for_loop(a):
    for i in range(a):
        print(i)


# condition controlled for loop
def for_ctrl_loop(d):
    for i in range(2, d):
        if i < 7:
            print("{} is less than threshold".format(i))
        else:
            print("{} is more than threshold".format(i))


# main funtion            
def main():
    # single line var assignment
    a, b, c, d= 10, 5, 0, 12
    
    # loop invoke
    while_loop(a)
    print("\n")
    while_ctrl_loop(c)
    print("\n")
    for_loop(b)
    print("\n")
    for_ctrl_loop(d)
    print("\n")

    
if __name__ == '__main__':
    main()
