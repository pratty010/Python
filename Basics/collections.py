
# non-mutable collection
def tuple_opr(mytuple):
    
    # copy tuple --> direct assignment changes both list (same pointer assignment)
    test_tuple = ('Hello', 'World', 1, 2, True, 3.21, b'Test', 'a')
    test_tuple = tuple(mytuple)
    
    # print tuple
    print(mytuple)
    print(test_tuple)
    
    # length operations
    l_n = len(mytuple)
    print("{} has length --> {}".format(mytuple, l_n))
    
    # access specific list indices
    print(mytuple[2])
    print(mytuple[-2])
    print(mytuple[2:5]) #splicing
    
    print("2 found {} times in tuple {}".format(mytuple.count(2), mytuple))
    print("1 found at iindex {} in tuple {}".format(mytuple.index(1), mytuple))
    
    # search in the tuple
    if 2 in mytuple:
        print("2 found in the tuple")
    else:
        print("Not Found")
        
    
    # adding to the tuple
    new_tuple  = mytuple + test_tuple # concat string
    print("Joined tuple --> {}".format(new_tuple))

    
    # add, manipulate and remove : tuple --> list --> oper --> tuple



# mutable collection
def list_opr(mylist):
    
    # copy list --> direct assignment changes both list (same pointer assignment)
    test_list = mylist.copy()
    test_list = list(mylist)
    
    num_list = [2, 5 , 1, 6, 3, 10]
    test_num_list = num_list.copy()
    
    # reversing a list
    test_list.reverse()
    
    # print list
    print(mylist)
    print(test_list)
    
    # sorting a list
    num_list.sort()
    print("{} in ascending order --> {}".format(test_num_list, num_list))
    num_list.sort(reverse=True)
    print("{} in descending order --> {}".format(test_num_list, num_list))

    # length operations
    l_n = len(num_list)
    print("{} has length --> {}".format(num_list, l_n))
    
    # access specific list indices
    print(mylist[2])
    print(mylist[-2])
    print(mylist[2:5]) #splicing
    
    k = num_list.count(2) # count operation for an element
    print("2 found in list {} --> {} time".format(num_list, k))
    
    # manipulating a particular index
    mylist[4] = 4
    print(mylist)    
    
    # search in the list
    if 2 in mylist:
        print("2 found in the list")
    else:
        print("Not Found")
        
    # adding to the list
    new_test_list = mylist + test_list # concat string
    
    new_list = mylist.copy()
    new_list.extend(test_list) # using extend operations
    print("Joined list --> {}".format(new_list))
    
    new_list.append(34) # apending element operations
    print("Joined list after appending to end --> {}".format(new_list))

    new_list.insert(0, "new start") # inserting element at a index
    print("Joined list after inserting in start --> {}".format(new_list))
    
    # removing elements from list
    new_list.pop()
    new_list.pop(4) # pop from particluar index
    print("{} after popping a element from the end --> {}".format(new_test_list, new_list))
    
    new_list.remove("new start") # remove from particular index
    print("{} after removing (new start) from the end --> {}".format(new_test_list, new_list))
    
    new_list.clear() # clear the list
    print("{} after clearing the list --> {}".format(new_test_list, new_list))  
 
 
   
# mutable with no duplicates and unordered.
def set_oper(myset):
    
    # copy set 
    test_set = myset.copy()
    test_set = set(myset)
    
    num_set = {2, 5 , 1, 6, 3, 10}
    test_num_set = num_set.copy()
    
    # print set
    print(test_set)
    print(num_set)
    
    # length operations
    l_n = len(test_set)
    print("{} has length --> {}".format(test_set, l_n))
    
    # search in the set - only access as the set is unordered. Accessing common and different elements.
    if 2 in myset:
        print("2 found in the set")
    else:
        print("Not Found")
    
    # common elements in two set
    test_set_1 = test_set.intersection(num_set)
    print(test_set_1)
    test_set_1.intersection_update(test_set)
    print(test_set_1)
    
    # inclusive operations
    print(test_set_1.issubset(test_set))
    print(test_set_1.issuperset(test_set))
    print(test_set.isdisjoint(test_num_set))
    
    
    # append operations
    test_set.add("me is smart")  
    print("{} after adding a element --> {}".format(myset, test_set))
    
    
    # removing elements from list
    test_num_set.pop()
    print("{} after popping a element--> {}".format(num_set, test_num_set))
    
    test_set.discard(3)
    print("{} after discarding (3) element--> {}. No effect and no error.".format(myset, test_set))
    
    test_set.remove(2) # remove from particular index
    print("{} after removing (2) from set --> {}".format(myset, test_set))
    
    
    # joining sets
    new_set = test_set.union(num_set)
    print("{} after concating with set {} --> {}".format(myset, num_set, new_set))

    test_set.update(num_set)
    print("{} after updating with set {} --> {}".format(myset, num_set, test_set))
    
    
    # clearing set
    test_set.clear() # clear the list
    print("{} after clearing the set --> {}".format(myset, test_set))  




# like maps in C++
def dict_oper(mydict):
    
    # creating a copy
    test_dict = mydict.copy()
    
    # printing dict
    print(mydict, test_dict)
    
    # access keys, values, items
    print("{} has brand key as {}".format(test_dict, test_dict["brand"]))
    print("{} has model key as {}".format(test_dict, test_dict.get("model")))
    print("{} has keys as {}".format(test_dict, test_dict.keys()))
    print("{} has values as {}".format(test_dict, test_dict.values()))
    print("{} has items as {}".format(test_dict, test_dict.items()))
    
    
    # search key in dict
    if 2 in mydict:
        print("2 found in the set")
    else:
        print("Not Found")
        
    
    # add and update to the dict
    
    test_dict["color"] = "red"
    print("{} after adding an intem {}".format(mydict, test_dict))
        
    test_dict.update({"model" : "Suzuki"})
    print("{} after updating an intem {}".format(mydict, test_dict))
    
    test_dict_1 = dict(test_dict)
    
    # removing elements from list
    test_dict.pop("color")
    print("{} after popping a color key--> {}".format(test_dict_1, test_dict))
    
    test_dict.popitem()
    print("{} after popping last item added-> {}".format(test_dict_1, test_dict))

    test_dict.clear()
    print("{} after clear dict-> {}".format(test_dict_1, test_dict))
    

    
# main function
def main():
    # var assignment
    mytuple = ("Hello", "World", 1, 2, True, 3.21, b'Test', 'a')
    mylist = ["Hello", "World", 1, 2, True, 3.21, b'Test', 'a']
    myset = {"Hello", "World", 1, 2, True, 3.21, b'Test', 'a'}

    mydict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
        }

    # funtions invoke
    list_opr(mylist)
    tuple_opr(mytuple)
    set_oper(myset)
    dict_oper(mydict)
    
    
if __name__ == '__main__':
    main()