
# # # # #first = "shah"
# # # # #last = "alam"
# # # # #full = first + " " + last
# # # # # print(full)
# # # # #same = f"{print(first)} {last}"
# # # # # print(same)
# # # # #import math
# # # # #from math import ceil
# # # # #from re import X


# # # # #class1 = "  math maTics"
# # # # # print(class1)
# # # # # print(class1.upper())
# # # # # print(class1.lower())
# # # # # print(class1.title())
# # # # # print(class1.strip())
# # # # # print(class1.find("th"))
# # # # #print(class1.replace("m", "S"))
# # # # # print(class1.find("m"))
# # # # #print("ma" in class1)
# # # # #print("ma" not in class1)

# # # # #print(20 + 3)
# # # # #print(20 - 3)
# # # # #print(20 * 3)
# # # # #print(20 / 3)
# # # # # print(20/3)
# # # # #print(20 ** 3)
# # # # #print(20 // 3)
# # # # #print(20 % 3)
# # # # #x = 10
# # # # #x /= x
# # # # # print(x)
# # # # # print(round(2.4))
# # # # # print(round(2.6))
# # # # # print(abs(-6.9))
# # # # # print(ceil(3.1))
# # # # # print(math.degrees(5))

# # # # #x = input("x: ")
# # # # # print(type(x))
# # # # #y = int(x) + 1
# # # # #print(f"x: {x}, y: {y}")
# # # # # print(bool(0))
# # # # # print(bool(9))
# # # # # print(bool(""))
# # # # # print(bool("Flase"))
# # # # fruit = "Mango fruit"
# # # # print(fruit[1])
# # # # print(fruit[1:-0])
# # # # print(fruit[0:10])
# # # # print(20 % 4)
# # # # print("Roni\" \"Sardar")
# # # speed = 15
# # # if speed >= 50:
# # #     print("Please Be Careful")
# # #     print("!!! Reduce Your Speed !!!")
# # # elif    speed <= 20:
# # #         print("Please Be fast")
# # #         print("Or you will be late")
# # # else:
# # #             print("Its Okay Man")
# # #             print("Be Confident")
# # # print("Done")


# # rating = 60
# # if rating >= 65:
# #     message = "Watch This Movie"
# # elif rating <= 50:
# #     message = "Watching it will be a waste o9f time"
# # print(message)

# rating = 90
# if rating >= 70:
# #    message="watch it"
#     print("watch it")
# #elif rating <= 70:
# else:
# #    message="no"
#     print("no")
# #message = "Watch This Movie" if rating >= 65 else "no information"
# #print(message)



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