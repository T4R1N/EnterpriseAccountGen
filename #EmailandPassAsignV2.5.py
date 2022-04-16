#EmailandPassAsign
from random import randint
import random
import string

#Choose Name

with open('C:/Users/tarin/Downloads/test.txt','r') as f:
    list1 = f.readlines()
    names = [x.replace('\n', '') for x in list1]
    print(names)
f.close()
my_dict = {}
max = len(names) - 1

#Initialize lists
emails = list()
passes = list()
name1s = list()
users = list()

#Create username and email
for x in names:
    bob = False
    chosen = x

    #print("Name: " + chosen)


    lch = chosen.lower()
    lchs = lch.split()
    firsix = lchs[1][0:6]
    firone = lchs[0][0]
    name1 = firone + firsix
    numm = 1
    #user = name1 + str(numm)
    user = name1 + str(numm)
    email = user + "@xinmail.net" 
    while bob == False:
        
        if email in my_dict:
            numm += 1
            user = name1 + str(numm) 
            email = user + "@xinmail.net" 
        else:
            my_dict[email] = x
            bob = True
                    
    


    #print("E-Mail: " + email)

    #PasswordGenerator

    total = string.ascii_letters + string.digits

    length = 16

    password = "".join(random.sample(total, length))

    #print("Password: " + password + "\n")

    emails.extend([email]) #Add email to listW
    passes.extend([password]) #Add password to list
    users.extend([user]) #Add user to list
    name1s.extend([name1]) #Add username without number to list 
    # open file
    with open("C:/Users/tarin/Downloads/test2.txt", "a") as file:
        # set a list of lines to add:
        # write to file and add a separator
        file.writelines(chosen + ': ')
        file.writelines(email + ' - ')
        file.writelines(password)
        file.writelines('\n')
print(my_dict.keys())


 
#open and read the file after the appending:
with open("C:/Users/tarin/Downloads/test2.txt", "r") as file:
    print(file.read())
