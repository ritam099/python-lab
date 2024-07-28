def giveDays(month):
    months = ("January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December")
    days = [31, "leap", 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    month = month.capitalize()  # Standardize input
    if month in months:
        index = months.index(month)
        if days[index] == "leap":
            year = int(input("Enter the year: "))
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                return 29
            else:
                return 28
        else:
            return days[index]
    else:
        return "Bad input"


print(giveDays("September"))  
