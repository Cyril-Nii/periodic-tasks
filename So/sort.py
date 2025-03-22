ls = input("Enter your numbers seperated by comma(e.g. 3,4,5,6,7)\n")

ls = ls.split(",")

dig = ls[0]

for x in ls:
    if x<dig:
        dig = x
    
print("\nLowest number:",dig)