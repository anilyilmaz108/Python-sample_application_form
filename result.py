import form as f
import pandas as pd

print(f)
all_data = [f.date,f.first_name,f.last_name,f.age,f.phone_number,f.mail,f.lic,f.cert,f.refer,f.lang,f.prog,f.add]

requested = ["english","python","javascript"]
employee = []
exist = []
grade = 0

employee.append(f.languages)
employee.append(f.programming)

for i in employee:
    if i in requested:
        exist.append(i)

condition_1 = len(exist) * 20
condition_2 = len(f.lang) * 5
condition_3 = len(f.prog) * 7.5
condition_4 = len(f.cert) * 2.5

grade = condition_1 + condition_2 + condition_3 + condition_4

if grade > 60:
    print(f"{f.first_name}, You can attend the interview.")
else:
    print(f"{f.first_name}, Thanks for applying")

df = pd.DataFrame(all_data, columns = ["Variables"], index = ["First Name",
    "Last Name","Date","Age","Phone Number","E-mail Adresses",
    "Languages","Licenses","Certificates","References","Programming Languages",
    "Additional"])
print(df)




