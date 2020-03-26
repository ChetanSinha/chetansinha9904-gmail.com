import pandas as pd

doc = []
with open('dates.txt') as file:
    for line in file:
        doc.append(line)

df = pd.Series(doc)
df.tail(10)

def date_sorter():
    
    # Your code here
    one = df.str.extract(r'((?:\d{1,2})(?:(?:/|-)\d{1,2})(?:(?:/|-)\d{2,4}))')
    
    two = df.str.extract(r'((?:\d{,2}\s)?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*(?:-|\.|\s|,)\s?\d{,2}[a-z]*(?:-|,|\s)?\s?\d{2,4})')
    
    three = df.str.extract(r'((?:\d{1,2}(?:-|/))?(?:19|20)\d{2})')
    
    dates = one.fillna(two).fillna(three)
    
    date = list(dates)
    #preprocessing and cleaning data
    dates = data_preprocess(date)
    #data returned in the required format
    
    #(IMP) sort the date to year, month, day accordingly and returning the index from the sorted object.
    dates_index = [date[0] for date in sorted(enumerate(dates), key=lambda x: (int(x[1].split('/')[0]),int(x[1].split('/')[1]), int(x[1].split('/')[2])))]
    
    #converting list into pandas series
    dates_index = pd.Series(dates_index)
    
    return dates_index


def completeMonthName(month):
    if month == "Jan":
        return "1"
    elif month == "Feb":
        return "2"
    elif month == "Mar":
        return "3"
    elif month == "Apr":
        return "4"
    elif month == "May":
        return "5"
    elif month == "Jun":
        return "6"
    elif month == "Jul":
        return "7"
    elif month == "Aug":
        return "8"
    elif month == "Sep":
        return "9"
    elif month == "Oct":
        return "10"
    elif month == "Nov":
        return "11"
    elif month == "Dec":
        return "12"
        
def data_preprocess(dates):
    
    # list to hold the formatted dates
    formatted_dates = []
    
    for date in (dates):
        flag = 0
        date = date.strip()
        # split the dates acc. to the joiners present
        for char in ['/', '-', ' ']:
            if date.split(char)[0] == date:
                # if char type of joiner is not present in this date
                continue
            else:
                lst = date.split(char)
                if lst[0][0].isdigit():
                    # check if the date is month preceding or date
                    if len(lst) == 3:
                        #check if day number is present in the date or not
                        if lst[1][0].isdigit():
                            #check if the middle term in the date given is month or day
                            day, month, year = lst[1], lst[0].strip('.').strip(','), lst[2]
                        else:
                            day, month, year = lst[0], lst[1].strip('.').strip(','), lst[2]

                    elif len(lst) == 2:
                        day, month, year = '1', lst[0].strip('.').strip(','), lst[1]

                else:
                    if len(lst) == 3:
                        if len(lst[1]) > 3:
                            # handles the superscript part of a day i.e th, nd, st
                            lst[1] = lst[1].strip(',')[:-2]

                        day, month, year = lst[1].strip(','), lst[0].strip('.'), lst[2]

                    elif len(lst) == 2:
                        day, month, year = '1', lst[0].strip('.'), lst[1]
                flag = 1
            
        if not flag:
            # checks if only year is provided
            day, month, year = '1', '1', date
        
        if not month[0].isdigit():
            # converts month in string to numeric
            month = completeMonthName(month[:3])
        if int(month) > 12:
            return False
        
        if len(year) == 2:
            year = '19' + year
        lst = [year, month, day]
        formatted_dates.append("/".join(lst))
    return formatted_dates
    
