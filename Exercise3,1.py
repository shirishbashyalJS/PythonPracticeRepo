# Write a program that asks a fisher the length of a zander in centimeters. If the zander does not fulfill the size limit, the program instructs to release the fish back into the lake and notifies the user of how many centimeters below the size limit the caught fish was. A zander must be 42 centimeters or longer to meet the size limit.

Length_zander = float(input("Enter the length of zander: "))
size_limit = 42

if(Length_zander >= size_limit):
    print("The size limit fulfilled")
else:
    print(f"Release the fish back into the lake because the fish was {size_limit - Length_zander} cm short.")