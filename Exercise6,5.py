# Write a function that gets a list of integers as a parameter. The function returns a second list that is otherwise the same as the original list except that all uneven numbers have been removed. For testing, write a main program where you create a list, call the function, and then print out both the original as well as the cut-down list.


def odd_removal(int_list):
    filtered_list = []
    for each in int_list:
        if each%2 == 0:
            filtered_list.append(each)
    
    return filtered_list



def main():
    int_list = [1,2,3,44,333,4,5,6,7,11,9]
    int_filtered_list = odd_removal(int_list)
    print(f"The original list is {int_list} and filtered list is {int_filtered_list}")

main()

