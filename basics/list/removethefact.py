#Name: remove_the_fact
#Purpose: Given a list of strings, create a new list that has in
#position 0 the number of times “fact” was in the original list and in
#position 1, a list of all other strings in the original list that were
#not “fact”. There can be duplication of strings on the new list.
#Precondition: The list will only contain strings.
#Input Parameter(s)
#          my_list: a list containing only strings or the empty list
#Return Value(s)
#          -- if the input parameter is an empty list, return a list of [0, []]
#          -- else return a list with the 0th index position containing the
#             number of times “fact” was seen on the list and the 1st
#             index position containing the list of the strings that are
#             not “fact”. If there are no strings on the list, return
#             an empty list in that position.
#=========================================================================

def remove_the_fact(mylist):
    list1 = []
    a = 0
    for i in mylist:
        if i == "fact":
            a += 1
        else:
            list1.append(i)
    return [a, list1]