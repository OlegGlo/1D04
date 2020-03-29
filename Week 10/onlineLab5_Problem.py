from calendar import monthrange

class Date:

    something = 1

    #jan 1
    #feb 2
    #mar 3
    #april 4
    #may 5
    #june 6 
    #july 7 
    #aug 8
    #sept 9  
    #oct 10
    #nov 11
    #dec 12

    def __init__(self, date, month, year):

        self.d = date
        self.m = month
        if date > self.daysInMonth(month, date):
            raise NameError("Non-existant date")
        self.y = year

    def getDay(self):
        return self.d  
        
    def getMonth(self):
        return self.m

    def getYear(self):
        return self.y

    def daysInMonth(self, month,year):
        x = monthrange(year,month)
        daysNum = int(x[1])

        return daysNum

    def stringConvert(self):

        strReturn = str(self.d) + "/" + str(self.m) + "/" + str(self.y)

        print(strReturn)

        return strReturn

    def Next(self):
        #normal case
        if self.d != self.daysInMonth(self.m,self.y):

            #return Date(days,months,year)
            return Date(self.d+1,self.m,self.y)

        #next months case
        elif self.d == self.daysInMonth(self.m,self.y) and self.m != 12:
            
            #return Date(days,months,year)
            return Date(1,self.m+1,self.y)

        #next year case
        elif  self.d == self.daysInMonth(self.m,self.y) and self.m == 12:
            
            #return Date(days,months,year)
            return Date(1,1,self.y+1)

        #for any other cases
        else:
            
            #error-ish:
            return Date(0,0,0)
        
    def Prev(self):
        #normal case
        if self.d != 1:

            return Date(self.d-1,self.m,self.y)
                  
        #prev months case
        elif self.d == 1 and self.m != 1:

            return Date(self.daysInMonth(self.m-1,self.y),self.m-1,self.y)
        #prev year case
        else:

            return Date(self.daysInMonth(12,self.y),12,self.y-1)
    
    def isBefore(self,d):

        #different year
        if self.y > d.y:
            return True

        #different month
        elif self.m > d.m and self.y == d.y:
            return True

        #date, same month
        elif self.d > d.d and self.m == d.m and self.y == d.y:
            return True

        #else
        else:
            return False

    def isAfter(self,d): #d is after self

        #different year
        if self.y < d.y:
            return True

        #different month
        elif self.m < d.m and self.y == d.y:
            return True

        #date, same month
        elif self.d < d.d and self.m == d.m and self.y == d.y:
            return True 

        #else
        else:
            return False

    def isEqual(self,d):

        if self.d == d.d and self.m == d.m and self.y == d.y:
            return True
        else:
            return False
    
    def add_days(self,n):

        numberAdded = n

        day = self.d
        month = self.m
        year = self.y

        condition = False

        while condition == False:

            day += 1
            numberAdded -= 1
            
            if day >= self.daysInMonth(month,year) and month == 12:

                day = 1
                numberAdded -= 1
                month = 1
                year += 1

            if day >= self.daysInMonth(month,year):

                day = 1
                numberAdded -= 1
                month += 1

            if numberAdded <= 0:
                condition = True

        return Date(day,month,year)
    
    def days_between(self, d):

        day1 = self.d
        month1 = self.m
        year1 = self.y

        day2 = d.d
        month2 = d.m
        year2 = d.y

        x1=0
        x2=0
        

        if month2 == month1 and year2 == year1: #simple case

            return abs(day1 - day2)

        if self.isAfter(d) == True:

            #adding days of the current month

            x1 = abs(self.daysInMonth(month1,year1) - day1)

            while month1 != month2:

                x2 += self.daysInMonth(month1,year1)

                month1 += 1

            return x1 + x2

        if self.isBefore(d) == True:
            pass

