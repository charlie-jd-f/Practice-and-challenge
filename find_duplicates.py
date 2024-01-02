# Create a function to find duplicates and returns list with
# any duplicates
#
# use for loop to look at each element in order
# loop through each element in the list
# if the element shows up again, break the loop, and append the value to a list

def find_duplicate(list):
    new_list = []
    for n in list:

        if n in new_list:
            continue
        else:
            counter = 0
            for x in list:
                if x == n:
                    counter += 1
                    if counter >= 2:
                        new_list.append(n)
                        break
    return new_list

list = [1, 2, 3, 2, 4, 5, 6, 1]

result = find_duplicate(list)
print(result)

# improved code is to include sets
