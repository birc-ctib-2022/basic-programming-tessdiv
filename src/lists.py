import sys

# This reads all of stdin and converts it into a list of integers.
# This *only* works if there are no non-integers in the input.
# You can learn how to deal with errors later...
x = [int(a) for a in sys.stdin.read().split()]

# if you have a list of integers you want to write to stdout in the same
# space separated format, you cannot use print(x) since that will add the
# square brackets and the commas, but you can use
#
# print(" ".join(str(i) for i in x))
#
# to first translate the integers into strings, (str(i) for i in x),
# and then merge them with spaces between them, " ".join(...).
#
# In the exercises where you need to print lists, that is what
# we need to do, but you can use this function to make the code
# a little more readable:


def print_list(x):
    print(" ".join(str(i) for i in x))


# We haven't covered functions yet, it is a few weeks away, but all
# you have to do to print a list, `y`, is to write `print_list(y)`.

# In sys.argv we find the command-line arguments a Python program
# receives. The first, `sys.argv[0]`, is just the name of the
# program, so the first real argument is `sys.argv[1]`. We use that
# to distinguish between which of the three operations we want to
# execute. If `sys.argv[1]` is "mean", we want to use your first
# exercise, if it is "times", it is the second exercise, and if it is
# "even" it is the third. Any other option is an error.


if len(sys.argv) < 2:
    print("Incorrect number of arguments.", file=sys.stderr)
    sys.exit(1)

match sys.argv[1]:
    case "mean":
        sum = [] #create the empty list to add data to
        for i in x: #no need to put list, the list is x which will be a standard input 
            sum += i # adds each value in list 
        mean = sum/len(x) #defines mean 
        print(mean)

    case "times":
        # Put your solution to the second exercise here
        times_three = [] 
        for i in x: 
            times_three.append(i*3) #multiplies each value in list by 3
        print_list(times_three)

    #also works 
    #[3*i for i in x]

    case "even":
        # Put your solution to the third exercise here
        even = []
        for i in x: 
            if i % 2 ==0: #applies to only values in list that are evenly divisible by 2
                even.append(i) #appends them to the new list even 
        print_list(even)
        #[i for i in x if i % 2 ==0]

        print_list(even)

    case _:
        print(f"Incorrect command {sys.argv[1]}.", file=sys.stderr)
        sys.exit(1)