# study list and tuple
# insert, update, delete

l = [('Herve','Yu','1966-01-22',''),
('Weizhen','Huang','1967-05-30',''),
('Gabrielle-Marthe','Yu','2000-06-17',''),
('Joseph','Yu','2003-02-04','')]



def birth_day(i_elt):
    l_fname, l_name, l_birthday, l_passday = i_elt
    return l_birthday

# Display the family

def display_civic_fam():
    l.sort(key=birth_day)
    print("===========================")
    for elt in l:
        surname, name, birthday, passday = elt
        if passday == '':
            print("{n:<10}, {s:<20} was born on {b} is still alive".format
            (n=name,s=surname,b=birthday))
        elif passday != '':
            print("{:<10}, {:<20} was born on {} passed on {}".
            format(name,surname,birthday,passday))
    print("---------------------------")

#display_civic_fam()


def upd_passday(i_name, i_firstname, i_passday):
    for l_idx, l_elt in enumerate(l):
        l_fname, l_name, l_bday, l_pday = l_elt
        if i_firstname == l_fname and i_name == l_name:
            l[l_idx] = (l_fname, l_name, l_bday, i_passday)

#display_civic_fam()


def add_member(i_name, i_firstname, i_birthday):
    for l_idx, l_elt in enumerate(l):
        l_firstname, l_name, l_birthday, l_passday = l_elt
        if l_firstname == i_firstname and l_name == i_name and l_birthday == i_birthday:
            print("{}, {} alreday in family register".format(i_name,i_firstname))
            return
    l.append((i_firstname, i_name, i_birthday, ''))


def pop_member(i_name,i_firstname):
    for l_idx, l_elt in enumerate(l):
        l_firstname, l_name, l_birthday, l_passday = l_elt
        if l_firstname == i_firstname and l_name == i_name:
            l.remove(l_elt)


# Gabrielle-Marthe pass on 10-03-2000
upd_passday('Yu','Gabrielle-Marthe','10-03-2000')
display_civic_fam()

#Joseph marries on 06-06-2026
add_member('Chu','Hilary','2004-03-06')
add_member('Yu','Herve','1966-01-22')
#display_civic_fam()
add_member('Yu','John','2029-03-06')
#display_civic_fam()
add_member('Yu','Szewah','1964-02-21')
add_member('Zheng','Xiaomin','1956-08-04')
display_civic_fam()

pop_member('Zheng','Xiaomin')
display_civic_fam()
