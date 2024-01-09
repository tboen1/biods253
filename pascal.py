from math import factorial

def get_nCk(n,k):
    return int(factorial(n)/(factorial(n-k)*factorial(k)))

def main():
    for i in range(1,10):
        line = ""
        for j in range(i):
            val = get_nCk(i,j)
            line = line + str(val) + " "
        print(line)

if __name__=="__main__": 
    main()

