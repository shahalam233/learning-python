#insert = 900
insert_salary = input("insert_salary: ")

insert_salary = int(insert_salary)
if insert_salary >= 1000:
    high_salary=True
else:
    high_salary=False
#print(type("insert"))
insert_credit = input("insert_credit: ")
insert_credit = int(insert_credit)
if insert_credit >=5000:
    high_credit=True
else:
    high_credit=False



#high_salary = False
#high_credit = True
#if high_salary == True and high_credit == True:
if high_credit and high_salary:
    print("Eligible")
else:
    print("Not eligible")