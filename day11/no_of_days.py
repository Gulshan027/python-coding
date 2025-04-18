def leap(year):
    if(year%4==0):
        if(year%100==0):
            if(year%400==0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False
        
month_day=[31,28,31,30,31,30,31,31,30,31,30,31]
year=int(input("Year to: "))
month=int(input("Enter month: "))

check=leap(year)
def final(check,month):
    if(check==True and month==2):
        print("there are 29 days")
    elif(check==False and month==2):
        print("there are 28 days")
    else:
        print(f"{month_day[month+1]} is no of days")

final(check,month)
