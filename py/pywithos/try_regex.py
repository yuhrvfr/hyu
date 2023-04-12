#!/usr/bin/env python3
import re
def check_aei (text):
  result = re.search(r"a.e.i", text)
  print(result)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True

re.search(r"a.e.i","academia")


print(re.search(r'p.ng','Pangaea', re.IGNORECASE))

fn = 'st_csv_n.txt'

with open(fn) as file:
    for idx, line in enumerate(file):
        voo = re.search(r'^voo',line, re.IGNORECASE)
        fund = re.search(r'fund',line, re.IGNORECASE)
        e96 =  re.search(r'96$',line)
        if voo != None:
            print("VOO  Case idx:{} voo: {}".format(idx,line))
        if fund != None:
            print(fund)
            print("FUND Case Idx:{} Fund:{}".format(idx,line))
        if e96 != None:
            print(e96)
            print("E96  Case idx:{} e96: {}".format(idx,line))



#range of character matching

def check_punctuation (text):
  result = re.search(r"[,.:;?!]", text)
  return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False

print(re.search(r'[a-c]$','tabac'))

print(re.search(r'[a-c]$','car'))
print(re.search(r'[a-c]','car'))
print(re.search(r'^[a-c]','car'))

print(re.search(r'[a-c]$','highway'))
print(re.search(r'[a-c]$','mama'))

print(re.search(r'[a-c0-9]$','MAMA'))
print(re.search(r'[a-c0-9]$','F12'))

re.search(r'[^a-z0-9]','il etait une fois!')
# <re.Match object; span=(2, 3), match=' '>

re.search(r'[^a-z0-9 ]','il etait une fois!')
# <re.Match object; span=(17, 18), match='!'>

re.search(r'fruit|veggie','i like to eat fruits')
# <re.Match object; span=(14, 19), match='fruit'>

re.search(r'fruit|veggie','i like to eat veggies')
# <re.Match object; span=(14, 20), match='veggie'>

re.search(r'fruit|veggie','i like to eat both fruits and veggies')
# <re.Match object; span=(19, 24), match='fruit'>

re.findall(r'fruit|veggie','i like to eat both fruits and veggies')
# ['fruit', 'veggie']



print('--- Repetitive matches------')

import re

re.search(r'Py.*n','Python programming is fun and useful!')
# <re.Match object; span=(0, 28), match='Python programming is fun an'>

re.search(r'Py[a-z]*n','Python programming is fun and useful!')
# <re.Match object; span=(0, 6), match='Python'>

re.search(r'Py[a-z]*n','Pyn!')
# <re.Match object; span=(0, 3), match='Pyn'>

re.search(r'c+a+','je fais caca mince')
# <re.Match object; span=(8, 10), match='ca'>

re.search(r'ca+','je fais caca mince')
# <re.Match object; span=(8, 10), match='ca'>

re.search(r'o+l+','Je vais a Hollywood!')
# <re.Match object; span=(11, 14), match='oll'>


print(re.search(r'o+l+','goldfish'))
# <re.Match object; span=(1, 3), match='ol'>

print(re.search(r'o+l+','woolly'))
# <re.Match object; span=(1, 5), match='ooll'>

print(re.search(r'o+l+','boil'))
# None

print(re.search(r'p?each','To each of their own'))
#<re.Match object; span=(3, 7), match='each'>

print(re.search(r'p?each','I like peaches'))
#<re.Match object; span=(7, 12), match='peach'>

print(re.search(r'p?each','I like to teach'))
#<re.Match object; span=(11, 15), match='each'>


def repeating_letter_a(text):
  result = re.search(r"a.*a", text,re.IGNORECASE)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True




print('----- Escape character \ -----------')

print(re.search(r'.com','welcome'))
<re.Match object; span=(2, 6), match='lcom'>

print(re.search(r'\.com','welcome'))
None

print(re.search(r'\.com','oracle.com'))
<re.Match object; span=(6, 10), match='.com'>



print('il\netait\nune\nfois')
il
etait
une
fois

#     r means raw string
print(r'il\netait\nune\nfois')
il\netait\nune\nfois


text = "there is a\nnext line"
print(re.search(r'\n',text))
<re.Match object; span=(10, 11), match='\n'>

print(re.search('\w*', 'This is exactly that.'))
<re.Match object; span=(0, 4), match='This'>

print(re.search('\w*', 'This_is_exactly_that.'))
<re.Match object; span=(0, 20), match='This_is_exactly_that'>


import re
def check_character_groups(text):
  result = re.search(r"\w+ \w+", text)
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False


import re
def check_sentence(text):
  result = re.search(r"^[A-Z][a-z ]+[.?!]$", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True

# Country start with A and finsihing with a
pattern = r'A.*a'
re.search(pattern,'Argentina')
<re.Match object; span=(0, 9), match='Argentina'>

re.search(pattern,'Azerbajian')
<re.Match object; span=(0, 9), match='Azerbajia'>

pattern = r'^A.*a$'
re.search(pattern,'Argentina')
<re.Match object; span=(0, 9), match='Argentina'>

print(re.search(pattern,'Azerbajian'))
None

# Regex pattern for python variable cannot start with numbers, can start with _, cannot have spaces
pn = r'^[a-zA-Z_][a-zA-Z0-9_]*$'

print(re.search(pn,'_variable+'))
None

print(re.search(pn,'_variable1'))
<re.Match object; span=(0, 10), match='_variable1'>

print(re.search(pn,'This Variable'))
None

print(re.search(pn,'This_Variable'))
<re.Match object; span=(0, 13), match='This_Variable'>

print('----------------')

pn1=r'^\W[a-z]+[A-Z]+$'

print(re.search(pn1,'?vA'))
<re.Match object; span=(0, 3), match='?vA'>

print(re.search(pn1,'vA'))
None


# --------

import re
def check_web_address(text):
  pattern = r'\w+\.[a-zA-Z]+$'
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True

import re
def check_time(text):
  pattern = r'[0-1]?[0-9]:[0-5][0-9]\s*[AaPp][Mm]'
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False
print(check_time("6:02am"))

re.search(r'[0-1\s][0-2]','6')


import re
def contains_acronym(text):
  pattern = r'\([A-Z]|[0-9][a-zA-Z0-9 ]*\)'
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True

import re
def check_zip_code (text):
  result = re.search(r"[a-zA-Z0-9 ] [0-9][0-9][0-9][0-9][0-9]", text)
  return result != None

print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
print(check_zip_code("90210 is a TV show")) # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.")) # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.")) # False
