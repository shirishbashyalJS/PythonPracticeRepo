# Write a function that gets a list of integers as a parameter. The function returns the sum of all the numbers in the list. For testing, write a main program where you create a list, call the function, and print out the value it returned.


def sum_list(int_list):
    return sum(int_list)




def main():
    int_list = [1,2,3,4,5,6,7,8,9,10]
    total = sum_list(int_list)

    print("The sum is "+str(total))

main()



