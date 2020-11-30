#Name: average_of_ints
#Purpose: Given a list which contains different types of objects
#including ints.Create a new list that has in
#position 0 the average of ints in the original list and in
#position 1 the list of all ints.
#Precondition: The list contains different types of objects. The int must to be true.
#Input Parameters(s)
#      my_list: a list contains different tupes of objects or the empty list
#Return Value(s)
#        -- if the input parameter is an empty list or don't contains ints, returna list of [0. []]
#        -- else return a list with the 0th index position containing the
#           average of all ints and the 1st index position containing the list of the ints themselves
#           te average should be rounded and then forced to be an int.
#====================================================================================
def average_of_ints(mylist):
    intlist = []
    sumint = 0
    avg = 0
    a = 0 #number of ints
    for i in mylist:
        x = isinstance(i,int)
        if x == True:
            a += 1                       
            sumint += i
            avg = int(round(sumint/a))
            intlist.append(i)
            
    return [avg,intlist]