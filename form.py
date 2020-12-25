form = """
                                                             Date: {}
                   SAMPLE APPLICATION FORM
Please fill in the information in lower case letters.

PERSONAL DETAILS                            
First Name            : {}                 
Last Name             : {}                
Age                   : {}                
Phone Number          : {}                   
E-mail Addresses      : {}                

EXPERIENCES                                     
License               : {} 
Certificates          : {}  
Reference             : {}

SKILLS
Languages             : {}
Programming Languages : {}
Additional            : {}

"""
lang = [] 
lic = []
cert = []
refer = []
prog = []
add = []
x=1
first_name = input("First Name: ")
last_name = input("Last Name: ")
date = input("Date: ")
age = input("Age: ")
phone_number = input("Phone Number : ")
mail = input("E-mail addresses: ")

while x:
    languages = input("Languages: ")
    lang.append(languages)
    y = input("If there is no action to add, press 1. Otherwise, press anything and  you can continue writing.\n==>")
    if y == "1":
        break

while x:
    license_ = input("License: ")
    lic.append(license_)
    y = input("If there is no action to add, press 1. Otherwise, press anything and  you can continue writing.\n==>")
    if y == "1":
        break

while x:
    certificates = input("Certificates: ")
    cert.append(certificates)
    y = input("If there is no action to add, press 1. Otherwise, press anything and  you can continue writing.\n==>")
    if y == "1":
        break

while x:
    reference = input("Reference: ")
    refer.append(reference)
    y = input("If there is no action to add, press 1. Otherwise, press anything and  you can continue writing.\n==>")
    if y == "1":
        break
    
while x:
    programming = input("Programming Languages: ")
    prog.append(programming)
    y = input("If there is no action to add, press 1. Otherwise, press anything and  you can continue writing.\n==>")
    if y == "1":
        break

while x:
    additional = input("Additional: ")
    add.append(additional)
    y = input("If there is no action to add, press 1. Otherwise, press anything and  you can continue writing.\n==>")
    if y == "1":
        break
all_data = [date,first_name,last_name,age,phone_number,mail,lic,cert,refer,lang,prog,add]

print(form.format(date,first_name,last_name,age,
                  phone_number,mail,lic,cert,
                  refer,lang,prog,add))

def create(b,x):
    with open(b + ".txt","a") as dosya:
        print(dosya.write(x))      
b = input("Header: ")
create(b,form.format(date,first_name,last_name,age,
                  phone_number,mail,lic,cert,
                  refer,lang,prog,add))    