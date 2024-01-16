from math import factorial, ceil
import argparse
import timeit
import matplotlib.pyplot as plt

def get_nCk(n,k):
    return int(factorial(n)/(factorial(n-k)*factorial(k)))

def main(num):
    for i in range(num):
        line = ""
        for j in range(i+1):
            val = get_nCk(i,j)
            line = line + str(val) + " "
        print(line)

def plot_time(filename):
    time_vals = []
    line_vals = []
    for n in range(6):
        iter_num = 10
        this_line_num = ceil(10**(n/2))
        this_time = timeit.timeit(lambda: main(this_line_num), number=iter_num)
        time_vals.append(this_time/iter_num)
        line_vals.append(this_line_num)

    plt.plot(line_vals, time_vals)
    plt.yscale('log')
    plt.xscale('log')
    plt.title("Time to run Pascal's Triangle")
    plt.xlabel('Number of lines')
    plt.ylabel('Time (sec)')

    plt.savefig(filename)

if __name__=="__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('number_lines', help='Number of lines to print', type=int)
    parser.add_argument('-fn', '--filename', default='./plot_timing.jpg')

    args = parser.parse_args()
    main(args.number_lines)

    plot_time(args.filename)
