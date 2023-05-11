import datetime , calendar , pytz

#global vars
days_list = calendar.day_name[0:]



def current_datetime():
    # datetime
    current_date = str(datetime.datetime.now().date())
    current_time = str(datetime.datetime.now().time())
    return f'Today Date is <b>{current_date}</b><br> Current Time is <b>{current_time}</b>' 

def current_date():
    # date
    current_date = str(datetime.datetime.now().date())
    return f'Today Date is <b>{current_date}</b>' 

def current_time():
    # time
    current_time = str(datetime.datetime.now().time())
    return f'Current Time is <b>{current_time}</b>' 

def current_date_all():
    # date all

    current_date = datetime.date.today()
    return f"""Current date (YYYY-MM-DD): <b>{current_date.strftime('%Y-%m-%d')}</b><br>
       Current date (MM/DD/YYYY): <b>{current_date.strftime('%m/%d/%Y')}</b><br>
       Current date (DD-MMM-YY): <b>{current_date.strftime('%d-%b-%y')}</b><br>
       Current date (Month Day, Year): <b>{current_date.strftime('%B %d, %Y')}</b><br>
       """
       
def current_time_all():
    # time all
    
    current_time = datetime.datetime.now().time()
    return f"Current time (24-hour format): <b>{current_time.strftime('%H:%M:%S')}</b><br>" \
       f"Current time (12-hour format): <b>{current_time.strftime('%I:%M:%S %p')}</b><br>" \
       f"Current time (microseconds): <b>{current_time.strftime('%f')}</b><br>"

def weekday(string):
    # weekday for 'yyyy mm dd'
    try:
        # print(string)
        year, month, date = string.split()
        # print(year,month,date)
        day = calendar.weekday(int(year), int(month), int(date))
        return f'The week day for <b>{year}-{month}-{date}</b> is <b>{days_list[day]}</b>'    
    except:
        return 'If you are trying to get the weekday of a specific date, then you can send a message in the following format: <br> <b><center>"weekday for yyyy mm dd"</center></b> <br>where "<b>yyyy</b>" is the <b>year</b>, "<b>mm</b>" is the <b>month</b>, and "<b>dd</b>" is the <b>day</b> of the month for the date you want to find the weekday for. This message will tell the program to retrieve the weekday of the specified date.<br><br> However,<br> <span class="text-red-400">I could not find weekday because given date is invalid </span>'

def difference_between_dates(year1,month1,date1,year2,month2,date2):
    # differnece between dates yyyy mm dd and yyyy mm dd
    try:    
        date1_ = datetime.datetime(year1,month1,date1)
        date2_ = datetime.datetime(year2,month2,date2)
        return f"differnece between {year1}-{month1}-{date1} and {year2}-{month2}-{date2} is <b>{str(date1_-date2_).replace('-', '').split(',')[0]}</b>"
    except:
        return 'If you are trying to get the difference between two dates, you can send a message in the following format: <br> <center>"difference between <b>yyyy mm dd</b> and <b>yyyy mm dd</b>"</center> <br>where "<b>yyyy</b>" is the year, "<b>mm</b>" is the month, and "<b>dd</b>" is the day of the month for the dates you want to find the difference between. This message will tell the program to retrieve the difference between the specified dates. <br> <br> However,<br> <span class="text-red-400">"I could not find the difference between the given dates because the given date(s) is(are) invalid.</span>'
    

def next_day(day):
    #next monday
    
    try:
        weekday = days_list.index(day.title())

        # get the current date
        today = datetime.date.today()

        # calculate the next occurrence of the weekday
        days_until_weekday = (weekday - today.weekday() + 7) % 7
        if days_until_weekday == 0:
            next_weekday = today + datetime.timedelta(days=days_until_weekday+7)
            return f"The next {calendar.day_name[weekday]} is on <b>{next_weekday}</b>"
        elif days_until_weekday == 1:
            next_weekday = today + datetime.timedelta(days=days_until_weekday) 
            return f"The next {calendar.day_name[weekday]} is on <b>{next_weekday} (Tomorrow)</b>"         
        elif days_until_weekday == 2:
            next_weekday = today + datetime.timedelta(days=days_until_weekday) 
            return f"The next {calendar.day_name[weekday]} is on <b>{next_weekday} (Day after tomorrow)</b>"
        else:
            next_weekday = today + datetime.timedelta(days=days_until_weekday) 
            return f"The next {calendar.day_name[weekday]} is on <b>{next_weekday}</b>"
    except:
        return 'If you are trying to get the next day, you can send a message in the following format: <br> <center>"next <b>name of the day</b></center> <br>where "name of the day will be" monday, tuesday, ....sunday "<b>dd<This message will tell the program to retrieve the next day occurence. <br> <br> However,<br> <span class="text-red-400">"I could not find the next day occurence because the given day name is invalid.</span>'
                     

def days_till(year,month,date):
    # days till yyyy mm dd
    try:    
        target_date = datetime.date(year, month, date)
        today = datetime.date.today()
        days_until = (target_date - today).days
        return (f"There are <b>{days_until}</b> days until {target_date}")
    except:
        return 'If you are trying to get the count of days till specific date, you can send a message in the following format: <br> <center>"next days till yyyy mm dd</center> <br>where "<b>yyyy</b>" is the year, "<b>mm</b>" is the month, and "<b>dd</b>" is the day of the month. This message will tell the program to retrieve the count of days till specific date. <br> <br> However,<br> <span class="text-red-400">"I could not find the count because the given date is invalid.</span>'

# def total_days(year, month):
#     # total days yyyy mm
#     try:
#         total_days = calendar.monthrange(year, month)[1]
#         return(f"The number of days in <b>{calendar.month_name[month]} {year}</b> is <b>{total_days}</b>")
#     except:
#         return 'If you are trying to get the total days in specific year and month, you can send a message in the following format: <br> <center>"total days in yyyy mm </center> <br>where "<b>yyyy</b>" is the year and "<b>mm</b>" is the month. This message will tell the program to retrieve the count of total days in specific year and month. <br> <br> However,<br> <span class="text-red-400">"I could not find the count because the given year or month is invalid.</span>'
        
        
def time_in_zone(zone):
    # time for zone timezone

    try:
        timezone = pytz.timezone(zone)
        current_time = str(datetime.datetime.now(timezone).time()).split('.')[0]
        return(f"The current time in <b>{timezone.zone}</b> is <b>{current_time}</b>")
    except:
        return 'If you are trying to get the time in specific timezone, you can send a message in the following format: <br> <center>time for "zone-name" timezone </center> <br>where "<b>zone</b>" is the name of the timezone ex. Asia/Kolkata.. This message will tell the program to retrieve the time for specific timezone. <br> <br> However,<br> <span class="text-red-400">"I could not find the time for given timezone because the given timezone is invalid.</span>'
        


def get_week_no():
    # current week no
    
    today = datetime.date.today()
    year, week_num, day_of_week = today.isocalendar()

    return(f"The current week number is {week_num}")


def leap(year):
    # check leapyear for yyyy

    try:
        if calendar.isleap(year):
            return(f"<b>{year}</b> is a leap year")
        else:
            return(f"<b>{year}</b> is not a leap year")        
    except:
        return 'If you are trying to find the specific year is leap year or not, you can send a message in the following format: <br> <center>check leap yyyy </center> <br>where "<b>yyyy</b>" is the year. This message will tell the program to retrieve the result of leap year for specific year.<br> <br> However,<br> <span class="text-red-400">"I could not find the result for given year because the given year is invalid.</span>'
        
        
        
def whole_month(year,month):
    # calendar for yyyy mm
    
    try:
        cal = calendar.HTMLCalendar()
        html_code = cal.formatmonth(year, month).replace('border="0"', 'border="1"').replace('cellpadding="0"', 'cellpadding="2"')
        return(html_code)
    except:
        return 'If you are trying to get the calendar for in specific year and month, you can send a message in the following format: <br> <center>calendar for yyyy mm </center> <br>where "<b>yyyy</b>" is the year and "<b>mm</b>" is the month. This message will tell the program to retrieve the calendar for specific year and month. <br> <br> However,<br> <span class="text-red-400">"I could not find the calendar because the given year or month is invalid.</span>'
    
def whole_year(year):
    # calendar for year yyyy 
    
    try:
        cal = calendar.HTMLCalendar()
        html_code = ''
        for i in range(1,13):
            html_code += cal.formatmonth(year, i).replace('border="0"', 'border="1"').replace('cellpadding="0"', 'cellpadding="2"')+'<br><br>'
        return(html_code)
    except:
        return 'If you are trying to get the calendar for in specific year, you can send a message in the following format: <br> <center>calendar for year yyyy</center> <br>where "<b>yyyy</b>" is the year. This message will tell the program to retrieve the calendar for specific year. <br> <br> However,<br> <span class="text-red-400">"I could not find the calendar because the given year is invalid.</span>'


