#!/usr/bin/env python3
with open("write.txt","w") as l_file:
    l_num = l_file.write("Why do people go to spread viruses in the public swimming pool,\naffecting others.")
print(str(l_num))

with open("write.txt","a") as l_file:
    l_file.write("\nNow I am in trouble, sick due to selfish folks.")

# with open("write.txt","a") as l_file:
#     l_file.write_line("\nStock to hold forever:")
#     l_file.write_line("\n1 VOO")

with open("write.txt","r+") as l_file:
    l_file.write("This is here:")


# ---------------------------

guests = open("guests.txt", "w")
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]

for i in initial_guests:
    guests.write(i + "\n")

guests.close()

new_guests = ["Sam", "Danielle", "Jacob"]

with open("guests.txt", "a") as guests:
    for i in new_guests:
        guests.write(i + "\n")

guests.close()

with open("guests.txt") as guests:
    for line in guests:
        print(line)


checked_out=["Andrea", "Manuel", "Khalid"]
temp_list=[]

with open("guests.txt", "r") as guests:
    for g in guests:
        temp_list.append(g.strip())

with open("guests.txt", "w") as guests:
    for name in temp_list:
        if name not in checked_out:
            guests.write(name + "\n")

with open("guests.txt") as guests:
    for line in guests:
        print(line)

guests_to_check = ['Bob', 'Andrea']
checked_in = []

with open("guests.txt","r") as guests:
    for g in guests:
        checked_in.append(g.strip())
    for check in guests_to_check:
        if check in checked_in:
            print("{} is checked in".format(check))
        else:
            print("{} is not checked in".format(check))
