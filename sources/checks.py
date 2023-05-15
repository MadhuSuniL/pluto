import re , calendar
from . import cal_time_date_funtions
from . import horoscope_funtions
from . import fake_funtions
from . import my_funtions
from .joke_funtions import get_joke
import time
from response.extras.word_explanation import explain
from .name_patterns import fake_vars
from .name_patterns import joke_categories
from . import number_funtions

days_list = calendar.day_name[0:]
fake_vars_list = fake_vars

def fake_exist(string):
    string = string.replace(' ','_')
    for var in fake_vars_list:
        if var in string:
            return True
        else:
            pass
    return False

def check_num(string):
    for i in range(0,9):
        if str(i) in string:
            return True
    return False

def check(promt,lang):
    promt = promt.lower().strip()
    if (promt == 'datetime' or promt == 'current datetime' or promt =='today date'):
        data = {
        'id':str(time.time()),
        'key':'Current Date & Time',
        'img':'no-img',
        'value':cal_time_date_funtions.current_datetime(),
        'copy':cal_time_date_funtions.current_datetime(),
        'extra':['sample'+str(x) for x in range(1,6)],
        }
        return data

    elif promt == 'date' or promt == 'current date' or promt == 'today date' or promt == 'present date':
        data = {
        'id':str(time.time()),
        'key':'Current Date',
        'img':'no-img',
        'value':cal_time_date_funtions.current_date(),
        'copy':cal_time_date_funtions.current_date(),
        'extra':['sample'+str(x) for x in range(1,6)],
        }
        return data

    elif promt == 'time'  or promt == 'current time' or promt == 'today time' or promt == 'present time' or promt =='now':
        data = {
        'id':str(time.time()),
        'key':'Current Time',
        'img':'no-img',
        'value':cal_time_date_funtions.current_time(),
        'copy':cal_time_date_funtions.current_time(),
        'extra':['sample'+str(x) for x in range(1,6)],
        }
        # print(data)
        return data
    
    elif promt == 'date all' or promt == 'current date all' or promt == 'today date all' or promt == 'present date all':
        data = {
        'id':str(time.time()),
        'key':'Current Date in different formats',
        'img':'no-img',
        'value':cal_time_date_funtions.current_date_all(),
        'copy':cal_time_date_funtions.current_date_all(),
        'extra':['sample'+str(x) for x in range(1,6)],
        }
        return data
             
    elif promt == 'time all' or promt == 'current time all' or promt == 'today time all' or promt == 'present time all':
        data = {
        'id':str(time.time()),
        'key':'Current Date in different formats',
        'img':'no-img',
        'value':cal_time_date_funtions.current_time_all(),
        'copy':cal_time_date_funtions.current_time_all(),
        'extra':['sample'+str(x) for x in range(1,6)],
        }
        return data

    elif ('weekday' in promt and len(promt.split(' ')) == 4) or ('week day' in promt and len(promt.split(' ')) == 5) or ('week day for' in promt and len(promt.split(' ')) == 6) or ('weekday for' in promt and len(promt.split(' ')) == 5):
        data = {
        'id':str(time.time()),
        'key':f"Week day for {promt.replace('week','').replace('day','').replace('for','').strip().replace(' ','-')}",
        'img':'no-img',
        'value':cal_time_date_funtions.weekday(promt.replace('week','').replace('day','').replace('for','').strip()),
        'copy':cal_time_date_funtions.weekday(promt.replace('week','').replace('day','').replace('for','').strip()),
        'extra':['sample'+str(x) for x in range(1,6)],
        }
        return data
    
    elif ('difference between dates' in promt):
        try:
            promt = promt.replace('difference between','').replace('and','').strip()
            dates = re.findall(r'\b(\d{4})[-\/\s\.](\d{1,2})[-\/\s\.](\d{1,2})\b', promt)
            year1, month1, date1 = dates[0]
            year2, month2, date2 = dates[1]
            data = {
            'id':str(time.time()),
            'key':f"Differnece between two dates",
            'img':'no-img',
            'value':cal_time_date_funtions.difference_between_dates(int(year1),int(month1),int(date1),int(year2),int(month2),int(date2)),
            'copy':cal_time_date_funtions.difference_between_dates(int(year1),int(month1),int(date1),int(year2),int(month2),int(date2)),
            'extra':['sample'+str(x) for x in range(1,6)],
            }
            return data
        except:
            data = {
            'id':str(time.time()),
            'key':f"Differnece between two dates",
            'img':'no-img',
            'value':'If you are trying to get the difference between two dates, you can send a message in the following format: <br> <center>"difference between <b>yyyy mm dd</b> and <b>yyyy mm dd</b>"</center> <br>where "<b>yyyy</b>" is the year, "<b>mm</b>" is the month, and "<b>dd</b>" is the day of the month for the dates you want to find the difference between. This message will tell the program to retrieve the difference between the specified dates. <br> <br> However,<br> <span style="color:red;">"I could not find the difference between the given dates because the given date(s) is(are) invalid.</span>',
            'copy':'',
            'extra':['sample'+str(x) for x in range(1,6)],
            }
            return data
                
    elif ('next' in promt and len(promt.split(' ')) > 1 and promt.split(' ')[1].title() in days_list ):
            data = {
            'id':str(time.time()),
            'key':f"Next {promt.split()[1]}",
            'img':'no-img',
            'value':cal_time_date_funtions.next_day(promt.split()[1]),
            'copy':cal_time_date_funtions.next_day(promt.split()[1]),
            'extra':['sample'+str(x) for x in range(1,6)],
            }
            return data


    elif ('days' in promt and 'till' in promt) and len(promt.split()) < 6:
        try:
            date = re.findall(r'\b(\d{4})[-\/\s\.](\d{1,2})[-\/\s\.](\d{1,2})\b', promt)
            year, month, date = date[0]
            data = {
            'id':str(time.time()),
            'key':f"Days till specific date",
            'img':'no-img',
            'value':cal_time_date_funtions.days_till(int(year), int(month), int(date)),
            'copy':cal_time_date_funtions.days_till(int(year), int(month), int(date)),
            'extra':['sample'+str(x) for x in range(1,6)],
            }
            return data
        except:
            return 'If you are trying to get the count of days till specific date, you can send a message in the following format: <br> <center>"next days till yyyy mm dd</center> <br>where "<b>yyyy</b>" is the year, "<b>mm</b>" is the month, and "<b>dd</b>" is the day of the month. This message will tell the program to retrieve the count of days till specific date. <br> <br> However,<br> <span style="color:red;">"I could not find the count because the given date is invalid.</span>'
                
    elif 'time for' in promt and 'timezone' in promt:
            data = {
            'id':str(time.time()),
            'key':f"time for {promt.split()[2]} timezone",
            'img':'no-img',
            'value':cal_time_date_funtions.time_in_zone(promt.split()[2]),
            'copy':cal_time_date_funtions.time_in_zone(promt.split()[2]),
            'extra':['sample'+str(x) for x in range(1,6)],
            }
            return data        
            
    elif 'current week no' in promt:

            data = {
            'id':str(time.time()),
            'key':f"Current week number",
            'img':'no-img',
            'value':cal_time_date_funtions.get_week_no(),
            'copy':cal_time_date_funtions.get_week_no(),
            'extra':['sample'+str(x) for x in range(1,6)],
            }
            return data        


    elif 'check leap year for' in promt or 'check leapyear for' in promt:
        year = promt.strip()[::-1][0:4][::-1]
        data = {
        'id':str(time.time()),
        'key':f"Leap year cheking for {year}",
        'img':'no-img',
        'value':cal_time_date_funtions.leap(int(year)),
        'copy':cal_time_date_funtions.leap(int(year)),
        'extra':['sample'+str(x) for x in range(1,6)],
        }
        return data        
  
    
    elif 'calendar for month' in promt:
        try:
            date = re.findall(r'\b(\d{4})[-\/\s\.](\d{1,2})\b', promt)
            year, month = date[0]
            data = {
            'id':str(time.time()),
            'key':f"Calendar for specific month",
            'img':'no-img',
            'value':cal_time_date_funtions.whole_month(int(year), int(month)),
            'copy':cal_time_date_funtions.whole_month(int(year), int(month)),
            'extra':['sample'+str(x) for x in range(1,6)],
            }
            return data        
        except:
            return 'If you are trying to get the calendar for in specific year and month, you can send a message in the following format: <br> <center>calendar for yyyy mm </center> <br>where "<b>yyyy</b>" is the year and "<b>mm</b>" is the month. This message will tell the program to retrieve the calendar for specific year and month. <br> <br> However,<br> <span style="color:red;">"I could not find the calendar because the given year or month is invalid.</span>'

    elif 'calendar for year' in promt:
        try:
            date = re.findall(r'\b(\d+)\b', promt)
            year = date[0]
            data = {
            'id':str(time.time()),
            'key':f"Calendar for specific year",
            'img':'no-img',
            'value':cal_time_date_funtions.whole_year(int(year)),
            'copy':cal_time_date_funtions.whole_year(int(year)),
            'extra':['sample'+str(x) for x in range(1,6)],
            }
            return data
        except:
            return 'If you are trying to get the calendar for in specific year, you can send a message in the following format: <br> <center>calendar for year yyyy</center> <br>where "<b>yyyy</b>" is the year. This message will tell the program to retrieve the calendar for specific year. <br> <br> However,<br> <span style="color:red;">"I could not find the calendar because the given year is invalid.</span>'
    
    
                    #Name & Birthday
    
    
    elif ('name:' in promt and 'birthday:' in promt) or ('name :' in promt and 'birthday :' in promt):
        try:
            date = re.findall(r'\b(\d{4})[-\/\s\.](\d{1,2})[-\/\s\.](\d{1,2})\b', promt)
            year, month, date = date[0]
            base = alphabets_with_space = [chr(x) for x in range(97, 123)] + [' ']
            name = ''
            for char in promt.replace('name:','').replace('name :','').replace('birthday:','').replace('birthday :',''):
                if char in base:
                    name+=char
            data = {
            'id':str(time.time()),
            'key':f"Name-Birthdate Info",
            'img':'no-img',
            'value':horoscope_funtions.horoscope(name,int(year),int(month),int(date)+1),
            'copy':'nothing',
            'extra':['sample'+str(x) for x in range(1,6)],
            }
            return data        
        except :
            return "n-none"
        
        
                                # Fake Values
        
        
        
    elif 'fake' in promt and fake_exist(promt):
        promt = promt.replace(' ','_')
    
        for var in fake_vars:
            if var in promt:
                res = fake_funtions.generate_fake_value(var)
                return {
                'id':str(time.time()),
                'key':f"Fake-{var.title().replace('_',' ')}",
                'img':'no-img',
                'value':res[0],
                'copy':str(res[1]),
                'extra':['sample'+str(x) for x in range(1,6)],
                }
            else:
                pass
        return {
                'id':str(time.time()),
                'key':f"fake-value generate",
                'img':'no-img',
                'value':'no-content',
                'copy':'',
                'extra':['sample'+str(x) for x in range(1,6)],
                }   
     
     
                # Jokes 
     
     
    elif 'tell' in promt or 'say' in promt and 'joke' in promt:
        for cat in joke_categories:
            if cat.lower() in promt:
                data = {
                    'id':str(time.time()),
                    'key':f"Joke on {cat.title()}",
                    'img':'no-img',
                    'value':get_joke(cat.title()),
                    'copy':'',
                    'extra':['sample'+str(x) for x in range(1,6)],
                }
                return data 
            else:
                data = {
                    'id':str(time.time()),
                    'key':f"Joke on Random Category",
                    'img':'no-img',
                    'value':get_joke(None),
                    'copy':'',
                    'extra':['sample'+str(x) for x in range(1,6)],
                }
                return data
            
            
                    # number funtions
    elif 'explain' in promt or 'desc' in promt and 'number' in promt and check_num(promt):        
        numbers = re.findall(r'\d+', promt)
        data = {
                'id':str(time.time()),
                'key':f"Describing Number {numbers[0]}",
                'img':'no-img',
                'value':number_funtions.explain_number(numbers[0]),
                'copy':'',
                'extra':['sample'+str(x) for x in range(1,6)],
            }
        return data
    
    elif 'even' in promt and 'numbers' in promt and (('from' in promt and 'to' in promt) or ('-' in promt ) or ('between' in promt )) and check_num(promt):
        numbers = re.findall(r'\d+', promt)
        data = {
                'id':str(time.time()),
                'key':f"Even Numbers Between {int(min(numbers))} to {int(max(numbers))}",
                'img':'no-img',
                'value':number_funtions.even_numbers(int(min(numbers)), int(max(numbers))),
                'copy':number_funtions.even_numbers(int(min(numbers)), int(max(numbers))),
                'extra':['sample'+str(x) for x in range(1,6)],
            }
        return data
    
    elif 'odd' in promt and 'numbers' in promt and (('from' in promt and 'to' in promt) or ('-' in promt ) or ('between' in promt )) and check_num(promt):
        numbers = re.findall(r'\d+', promt)
        data = {
                'id':str(time.time()),
                'key':f"Odd Numbers Between {min(numbers)} to {max(numbers)}",
                'img':'no-img',
                'value':number_funtions.odd_numbers(int(min(numbers)), int(max(numbers))),
                'copy':number_funtions.odd_numbers(int(min(numbers)), int(max(numbers))),
                'extra':['sample'+str(x) for x in range(1,6)],
            }
        return data
    
    elif 'prime' in promt and 'numbers' in promt and (('from' in promt and 'to' in promt) or ('-' in promt ) or ('between' in promt )) and check_num(promt):
        numbers = re.findall(r'\d+', promt)
        data = {
                'id':str(time.time()),
                'key':f"Prime Numbers Between {min(numbers)} to {max(numbers)}",
                'img':'no-img',
                'value':number_funtions.prime_numbers(int(min(numbers)), int(max(numbers))),
                'copy':number_funtions.prime_numbers(int(min(numbers)), int(max(numbers))),
                'extra':['sample'+str(x) for x in range(1,6)],
            }
        return data
    
    elif 'fibonacci' in promt and 'numbers' in promt and (('from' in promt and 'to' in promt) or ('-' in promt ) or ('between' in promt )) and check_num(promt):
        numbers = re.findall(r'\d+', promt)
        data = {
                'id':str(time.time()),
                'key':f"Fibonacci Numbers Between {min(numbers)} to {max(numbers)}",
                'img':'no-img',
                'value':number_funtions.fibonacci_numbers(int(min(numbers)), int(max(numbers))),
                'copy':number_funtions.fibonacci_numbers(int(min(numbers)), int(max(numbers))),
                'extra':['sample'+str(x) for x in range(1,6)],
            }
        return data
    
                            #my funtions
                            
    elif 'table' in promt and 'math' in promt or 'write' in promt or 'generate' in promt:
        num = re.findall(r'\d+', promt)
        num = int(num[0])
        data = {
                'id':str(time.time()),
                'key':f"Math Table for {num}",
                'img':'no-img',
                'value':number_funtions.table(num),
                'copy':'',
                'extra':['sample'+str(x) for x in range(1,6)],
            }
        
        return data
    
    elif 'roll dice' == promt:
        data = {
                'id':str(time.time()),
                'key':f"Dice",
                'img':'no-img',
                'value':my_funtions.dice(),
                'copy':'',
                'extra':['sample'+str(x) for x in range(1,6)],
            }
        return data
    
    elif 'toss' == promt or 'spin coin' in promt or 'heads or tales' in promt or 'heads and tales' in promt:
        data = {
                'id':str(time.time()),
                'key':f"Toss",
                'img':'no-img',
                'value':my_funtions.toss(),
                'copy':'',
                'extra':['sample'+str(x) for x in range(1,6)],
            }
        return data
    
    elif 'random card' == promt or 'pick a random card' in promt or ('card' in promt and 'get' in promt or 'select' in promt or 'pick' in promt or 'show' in promt or 'random' in promt):
        data = {
                'id':str(time.time()),
                'key':f"Random Card",
                'img':'no-img',
                'value':my_funtions.card(),
                'copy':'',
                'extra':['sample'+str(x) for x in range(1,6)],
            }
        return data
    
    
    else:
        return explain(promt,lang)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def GetRes(key,lang):
    try:
        data = {
            'id':str(time.time()),
            'key':f"{key} = ?",
            'img':'no-img',
            'value':f'After solving the given expression the answers is ,<br> <h1 class="text-2xl">{key} = <b>{eval(key)}</b></h1><br><br> <i>One more thing users should notice is that I am solving this using the <b>"BODMAS"</b> rule.</i>',
            'copy':eval(key),
            'extra':['sample'+str(x) for x in range(1,6)],
            }
        sam = eval(key)+10
        print(data)
        return data
    except:
        data = check(key, lang)
        # if len(data['value']) < 110:
        #     data['value'] = '<h1 class="text-2xl">'+ data['value'] +"</h1>"
        return data
    
    
    
    
    