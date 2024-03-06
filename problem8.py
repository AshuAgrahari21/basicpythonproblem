#write a python script to check a wheather a number is leap year or not.
year=int(input())
if year%4==0 and year%100!=0:
    print("this is leap year")
else:
    print("this is not leap year")