def CMYK_to_RGB(C,M,Y,K):
    C = C / 100           #convert the percentages into their decimal equivalent
    M = M / 100
    Y = Y / 100
    K = K / 100
    R = 255 * (1-C) * (1-K)
    G = 255 * (1-M) * (1-K)
    B = 255 * (1-Y) * (1-K)
    R = int(round(R))
    G = int(round(G))      #round the floats to integers
    B = int(round(B))     
    return [R,G,B]

def main():
    C = int(input("Cyan component: "))
    M = int(input("Magenta component: "))
    Y = int(input("Yellow component: "))
    K = int(input("Blak(Key) component: "))
    #0,1,2 represent the first, second, third value in the list.
    print("RGB representation: ", CMYK_to_RGB(C,M,Y,K)[0],CMYK_to_RGB(C,M,Y,K)[1],CMYK_to_RGB(C,M,Y,K)[2])

if __name__ == '__main__':
    main()
