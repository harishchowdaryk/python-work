a=int(input())


if(a%400==0 or a%100!=0 and a%4==0):
    print(a,"is",'leap year')
else:
    print(a,"is","not a leap year")


'''if(a%100==0 and a%400==0):
    print('leap year')
elif(a%100!=0 and a%4==0):
    print('leap year')
else:
    print('not a leap year')'''