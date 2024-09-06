no_of_items = 3
list = []
for i in range(int(no_of_items)):
    i = input(f"Enter item {i+1}: ")
    list.append(i)

search_item = input("Enter the item to search: ")

if search_item in list:
    index = list.index(search_item)
    print(f"Index of {search_item} is {index+1}.")
else:
    print(f"{search_item} not found in the list.")

# start_index = int(input("Enter the start index for slicing: "))
# end_index = int(input("Enter the end index for slicing: "))

# sliced_list = list[start_index-1:end_index]

# print(f"Sliced list from index {start_index} to {end_index}: {sliced_list}")

removed_item = input("Enter the item to remove: ")
if removed_item in list:
    list.remove(removed_item)
    print(f"{removed_item}  removed successfully.")
    print("Updated list:", list)
