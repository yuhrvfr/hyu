mydict={}

def count_letters(i_sentence):
    d = {}
    for c in i_sentence:
        if c not in d:
            #print('exec11')
            d[c] = 1
        else:
            #print('exec')
            d[c] += 1
    return d


print(count_letters("aaaaa"))

def count_letters2(i_sentence):
    d = {}
    for c in i_sentence:
        if c in d:
            #print('exec2')
            d[c] += 1
        else:
            #print('exec21')
            d[c] = 1
    return d

def count_letters3(i_sentence):
    d = {}
    for c in i_sentence:
        if c not in d:
            d[c] = 0
        d[c] += 1
    return d

def recount_dic(i_dic):
    d = {}
    for k, v in i_dic.items():
        if k.upper() not in d:
            d[k.upper()]=0
        d[k.upper()] += v
    return d

def ins_upd_dic(i_dic, i_key, i_val):
    if i_key in i_dic:
        print("The {} [ {} ] current value is {} and will be updated to {}".format
        (i_dic, i_key, i_dic[i_key], i_val))
    else:
        print("The {} [ {} ] will be created with the value {}".format
        (i_dic, i_key, i_val))
    i_dic[i_key]=i_val


user_input = "GOD alone is my shield" #input('Enter the sentence 1: ')
d1 = count_letters(user_input)

user_input = "Our Father who arts in heaven" #input('Enter the sentence 2: ')
d2 = count_letters2(user_input)

user_input = "Hail Mary full of grace" #input('Enter the sentence 3: ')
d3 = count_letters3(user_input)


#print(count_letters("aaaaa"))
#print(count_letters2("aaaaa"))
#print(count_letters3("aaaaa"))
#d=count_letters("aaaaa")
#d2=count_letters2("bbbbbbb")
#d3=count_letters3("ccccccccc")

mydict.update(d1)
mydict.update(d2)
mydict.update(d3)

mydicts = dict(sorted(mydict.items()))
#mydictsk = dict(sorted(mydict.keys()))

print(mydict)
print(mydicts)
#print(mydictsk)

mdic = recount_dic(mydicts)
print(mdic)

ins_upd_dic(mdic, 'X', 3)

ins_upd_dic(mdic, 'O', 9)
print(mdic)

print(mdic['F'])

for k in mdic.items():
    print(k)

del mdic['Y']

print('--------')
for k in mdic.items():
    print(k)



l=[{"id":82,"name":"Oracle Applications","short_name":"OA","lien":"https://www.linkedin.com/in/herve-yu-20aa261/details/recommendations/?detailScreenTabIndex=0","special_instructions":"+ Expert in Oracle Financial and SCM applications TCA,AR,XLA,GL,CST,AP,PO,OM with 25+ years of experience."},
{"id":83,"name":"Web Apps","short_name":"WA","lien":"https://www.linkedin.com/in/herve-yu-20aa261/details/certifications/","special_instructions":"+ Expert on Oracle Technologies PLSQL, SQL, Forms. Working knowledge in Web Design and Web Apps HTML/CSS/JS, Google Angular through Coursera John-Hopkins-University"},
{"id":84,"name":"Artificial Intelligence","short_name":"AI","lien":"https://www.coursera.org/account/accomplishments/certificate/ECL9RQNDD27F","special_instructions":"+ Machine Learning, Deep Learning through Coursera-Stanford University and Duke Unversity"},
{"id":85,"name":"Management Accountant","short_name":"MA","lien":"https://www.imanet.org/","special_instructions":"+ Certified Managment Accountant (Certification# 43517) by the Institute Management Accountants IMA."}]



#for elt in l:
#    print(elt)

print(l[1]["lien"])
