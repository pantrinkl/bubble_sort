# defining functions

# decide whether number or text
def is_number(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

# load input data
def load_numbers(file_name):
    try:
        with open(file_name, 'r') as h:
            content = h.readlines() 
        list_nums = []
        for line in content:
            # if delimiter is comma, replaced with space
            line.replace(',',' ')
            # divide line to parts by spaces
            for i in line.split(): 
                # if item in line is a number, add to list of numbers
                if is_number(i) == True: 
                    list_nums.append(float(i))
        return list_nums
    except FileNotFoundError:
        exit("Nenalezen vstupní soubor.")
    except PermissionError:
        exit("Nemám přístup k vstupnímu souboru.")

# save sorted numbers to file: vystup.txt
def save_nums(sorted_nums):
    try:
        with open('vystup.txt','w') as k:
            for i in sorted_nums:
                k.write("{:g} ".format(i))
    except PermissionError:
        exit("Nemám přístup k výstupnímu souboru vystup.txt")

# main program

# get name of input file from user
input_name = str(input("Zadejte název vstupního souboru: "))

# get ascending or descending order
p=1
while p==1: 
    order = str(input("Zadejte zda vzestupné(asc) nebo sestupné(desc) třídění: "))
    if order != "desc" and order != "asc":
        print("Špatně zadané desc nebo asc.")
    else:
        p+=1

# load numbers from 
num_list = load_numbers(input_name)

# sort loaded numbers with bubble sort method - ascending
if order == "asc":
    p=0
    while p == 0:
        p = 1
        for i in range(len(num_list)-1):
            if num_list[i]>num_list[i+1]:
                a=num_list[i]
                num_list[i]=num_list[i+1]
                num_list[i+1]=a
                p=0

# sort loaded numbers with bubble sort method - descending      
if order == "desc":
    p=0
    while p == 0:
        p = 1
        for i in range(len(num_list)-1):
            if num_list[i]<num_list[i+1]:
                a=num_list[i]
                num_list[i]=num_list[i+1]
                num_list[i+1]=a
                p=0
                
# save sorted numbers
save_nums(num_list)