#!/usr/bin/python3

def find_item(list, item):

  list = sorted(list)
  #Returns True if the item is in the list, False if not.
  if len(list) == 0:
    return False

  #Is the item in the center of the list?
  middle = len(list)//2
  # print(middle)
  # print(list[middle-1])
  if list[middle-1] == item:
    return True

  #Is the item in the first half of the list?
  if item < list[middle-1]:
    #Call the function with the first half of the list
    # print('First half')
    # print(list[:middle])
    return find_item(list[:middle], item)
  else:
    #Call the function with the second half of the list
    # print('Last half')
    # print(list[middle:])
    return find_item(list[middle:], item)

  return False

#Do not edit below this line - This code helps check your work!
list_of_names = ["Parker", "Drew", "Cameron", "Logan", "Alex", "Chris", "Terry", "Jamie", "Jordan", "Taylor"]

print(find_item(list_of_names, "Alex")) # True
print(find_item(list_of_names, "Andrew")) # False
print(find_item(list_of_names, "Drew")) # True
print(find_item(list_of_names, "Jared")) # False
