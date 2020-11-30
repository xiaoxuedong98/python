def subtractWhile(total, num, times):
    while times > 0:
        total = total - num
        times = times - 1
    return total

def main():

    total = int(input("Please enter the current total:  "))
    num = int(input("What number will be suntracted?  "))
    times = int(input("How many times should we subtract?  "))
    print("Answer:  ",total, "- (", num, "*", times, ")", "=", subtractWhile(total, num, times) )
    
main()