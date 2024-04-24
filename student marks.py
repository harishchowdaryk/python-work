# take student marks of 5 subject and print percentage display grade 
sub1=float(input())
sub2=float(input())
sub3=float(input())
sub4=float(input())
sub5=float(input())
total=(sub1+sub2+sub3+sub4+sub5)
print(total)
percentage =total/5
print(percentage,"%")
if(percentage>=75):
  print('grade A')
elif(percentage>=60 and percentage<=74 ):
  print('grade B')
elif(percentage>=35 and percentage<=59):
  print('grade C')
else:
  print('fail')







