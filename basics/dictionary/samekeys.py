#=========================================================================================================
# Name: sameKeys
# Purpose: looks for keys that are found in both dictionaries and returns a new dictionary that contains key:
#          value pairs where the key in the new dictionary is the key found in both dictionaries, diction1 and diction2,
#          and the new key’s value being a list of the values of diction1.key and diction2.key values concatenated together.
# Precondition: There can be any type of objects for the values of the keys.
#               The order of the keys in the returned dictionary will be dictated by the
#               hashing function of the system so order does not matter of the keys.
# Input parameter(s): this function will take into two parameters, dictinary 1 and dictionary 2, and There can be any type
#                     of objects for the values of the keys.All types of objects
# return Value(s): value pairs where the key in the new dictionary is the key
#                  found in both dictionaries, diction1 and diction2, and the new key’s value
#                  being a list of the values of diction1.key and diction2.key values concatenated together.
#==========================================================================================================
def sameKeys(diction1, diction2):
    newdict= {}
    list1 = diction1.keys()
    list2 = diction2.keys()
    for i in list1:
        if i in list2:
            newdict[i]= [diction1[i], diction2[i]]            
    return newdict