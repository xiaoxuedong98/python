def subtractFor(total, num, times):
    for X in range(times):
        total = total - num
    return total


import math
def main():
    total = int(input("Please enter the current total:  "))
    num = int(input("What number will be suntracted?  "))
    times = int(input("How many times should we subtract?  "))
    output = total - ( num * times )
    print("Answer:  ", total ,"-", "(", num ,"*", times ,")", "=", output)

main()