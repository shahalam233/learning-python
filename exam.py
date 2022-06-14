# n = int(input().strip())
# if n % 2 != 0:
#         print("Weird")
# elif 2<= n >=5:
#         print("Not Weird")
# elif 6<= n >= 20:
#         print("Weird")
# elif n >= 20:
#         print("Not Weird")
n = int(input().strip())
if n%2 != 0:
        print('Weird')
elif n%2==0 and n in range(2,5):
        print('Not Weird')
elif n%2==0 and n in range(6,20):
        print('Weird')
elif n%2==0 and n>20:
        print('Not Weird')
