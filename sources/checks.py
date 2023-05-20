import re , calendar
from . import cal_time_date_funtions
from . import horoscope_funtions
from . import fake_funtions
from . import my_funtions
from . import text_funtions
from .joke_funtions import get_joke
import time
from response.extras.word_explanation import explain
from .name_patterns import fake_vars
from .name_patterns import joke_categories
from . import number_funtions
from .patterns import *
import pytz
import pandas as pd
import datetime , random
days_list = calendar.day_name[0:]
fake_vars_list = fake_vars
timezones = pytz.all_timezones

current_date = datetime.datetime.now().date().day
current_month = datetime.datetime.now().date().month
current_year = datetime.datetime.now().date().year

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

def check_name(string):
    df = pd.read_csv('names_final.csv')
    for word in string.split():
        if word in df['names']:
            return True
    return False
    
    

def check(promt,lang):
    promt = promt.lower().strip()
    if (promt == 'datetime' or promt == 'current datetime' or promt =='today date') or promt == 'what is the time' or promt == "What's the time" or promt == 'Do you know what time it is' or promt == 'Can you tell me the time' or re.search(current_datetime_pattern, promt, re.IGNORECASE):
        data = {
        'id':str(time.time()),
        'key':'Current Date & Time',
        'img':'no-img',
        'value':cal_time_date_funtions.current_datetime(),
        'copy':cal_time_date_funtions.current_datetime(),
        'extra':['sample'+str(x) for x in range(1,6)],
        }
        return data

    elif 'time for' in promt and 'timezone' in promt or re.search(timezone_pattern, promt, re.IGNORECASE) or re.search(timezone_pattern2, promt, re.IGNORECASE):
            timezone = 'Asia/Kolkata'
            for word in promt.split():
                if word in timezones:
                    timezone = word            
            data = {
            'id':str(time.time()),
            'key':f"time for {timezone} timezone",
            'img':'no-img',
            'value':cal_time_date_funtions.time_in_zone(timezone),
            'copy':cal_time_date_funtions.time_in_zone(timezone),
            'extra':['sample'+str(x) for x in range(1,6)],
            }
            return data        
    
    elif promt == 'date' or promt == 'current date' or promt == 'today date'  or re.search(current_date_pattern, promt, re.IGNORECASE):
        data = {
        'id':str(time.time()),
        'key':'Current Date',
        'img':'no-img',
        'value':cal_time_date_funtions.current_date(),
        'copy':cal_time_date_funtions.current_date(),
        'extra':['sample'+str(x) for x in range(1,6)],
        }
        return data

    elif promt == 'time'  or promt == 'current time' or promt == 'today time' or promt == 'present time' or promt =='now' or promt == 'what is the time' or promt == "what's the time" or promt == 'do you know what time it is' or promt == 'can you tell me the time'  or re.search(current_time_pattern, promt, re.IGNORECASE):
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

    elif ('weekday' in promt and len(promt.split(' ')) == 4) or ('week day' in promt and len(promt.split(' ')) == 5) or ('week day for' in promt and len(promt.split(' ')) == 6) or ('weekday for' in promt and len(promt.split(' ')) == 5) or re.search(weekday_pattern, promt, re.IGNORECASE):
        date = re.findall(r'\b(\d{4})[-\/\s\.](\d{1,2})[-\/\s\.](\d{1,2})\b', promt)
        if len(date) != 0:
            # year, month, date = date[0]
            date = ' '.join(date[0])
        else:
            date = [str(current_year), str(current_month), str(current_date)]
            date = ' '.join(date)

        data = {
            'id':str(time.time()),
            'key':f"Week day for {date}",
            'img':'no-img',
            'value':cal_time_date_funtions.weekday(date),
            'copy':cal_time_date_funtions.weekday(date),
            'extra':['sample'+str(x) for x in range(1,6)],
            }
        return data
    
    elif ('difference between dates' in promt) or re.search(date_difference_pattern , promt, re.IGNORECASE):
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
                
    elif ('next' in promt and len(promt.split(' ')) > 1 and promt.split(' ')[1].title() in days_list ) or re.search(next_day_pattern, promt, re.IGNORECASE):
            words = promt.split()
            day = ''
            for word in words:
                if word.title() in days_list:
                    day = word
                    break
            data = {
            'id':str(time.time()),
            'key':f"Next {day.title()}",
            'img':'no-img',
            'value':cal_time_date_funtions.next_day(day),
            'copy':cal_time_date_funtions.next_day(day),
            'extra':['sample'+str(x) for x in range(1,6)],
            }
            return data

    elif ('days' in promt and 'till' in promt) and len(promt.split()) < 6 or re.search(days_until_pattern, promt, re.IGNORECASE) :
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
            
    elif 'current week no' in promt or re.search(week_pattern , promt, re.IGNORECASE):

            data = {
            'id':str(time.time()),
            'key':f"Current week number",
            'img':'no-img',
            'value':cal_time_date_funtions.get_week_no(),
            'copy':cal_time_date_funtions.get_week_no(),
            'extra':['sample'+str(x) for x in range(1,6)],
            }
            return data        


    elif 'check leap year for' in promt or 'check leapyear for' in promt or re.search(leap_year_pattern, promt, re.IGNORECASE):
        year = re.findall(r'\b(\d+)\b', promt)
        if len(year) == 1:
            year = year[0]
        else:
            year = current_year    
        data = {
        'id':str(time.time()),
        'key':f"Leap year cheking for {year}",
        'img':'no-img',
        'value':cal_time_date_funtions.leap(int(year)),
        'copy':cal_time_date_funtions.leap(int(year)),
        'extra':['sample'+str(x) for x in range(1,6)],
        }
        return data        
  
    
    elif 'calendar for year' in promt or re.search(calendar_pattern, promt, re.IGNORECASE):
        try:
            value = ''
            date = re.findall(r'\b(\d{4})[-\/\s\.](\d{1,2})\b', promt)
            if len(date) == 0:            
                date = re.findall(r'\b(\d+)\b', promt)
                if len(date) == 0:
                    value = cal_time_date_funtions.whole_year(2023)
                else:
                    value = cal_time_date_funtions.whole_year(int(date[0]))
            else:
                year, month = date[0]
                value = cal_time_date_funtions.whole_month(int(year), int(month))
                                
            data = {
            'id':str(time.time()),
            'key':f"Calendar for specific month",
            'img':'no-img',
            'value':value,
            'copy':value,
            'extra':['sample'+str(x) for x in range(1,6)],
            }
            return data        
        except:
            data = {
            'id':str(time.time()),
            'key':f"Calendar for specific month",
            'img':'no-img',
            'value':'If you are trying to get the calendar for in specific year and month, you can send a message in the following format: <br> <center>calendar for yyyy mm </center> <br>where "<b>yyyy</b>" is the year and "<b>mm</b>" is the month. This message will tell the program to retrieve the calendar for specific year and month. <br> <br> However,<br> <span style="color:red;">"I could not find the calendar because the given year or month is invalid.</span>',
            'copy':'',
            'extra':['sample'+str(x) for x in range(1,6)],
            }
            return data
             

    # elif 'calendar for year' in promt or re.search(timezone_pattern, promt, re.IGNORECASE):
    #     try:
    #         date = re.findall(r'\b(\d+)\b', promt)
    #         year = date[0]
    #         data = {
    #         'id':str(time.time()),
    #         'key':f"Calendar for specific year",
    #         'img':'no-img',
    #         'value':cal_time_date_funtions.whole_year(int(year)),
    #         'copy':cal_time_date_funtions.whole_year(int(year)),
    #         'extra':['sample'+str(x) for x in range(1,6)],
    #         }
    #         return data
    #     except:
    #         return 'If you are trying to get the calendar for in specific year, you can send a message in the following format: <br> <center>calendar for year yyyy</center> <br>where "<b>yyyy</b>" is the year. This message will tell the program to retrieve the calendar for specific year. <br> <br> However,<br> <span style="color:red;">"I could not find the calendar because the given year is invalid.</span>'
    
    
                    #Name & Birthday
    
    
    elif ('name' in promt and 'birthday' in promt) or re.search(name_age_pattern, promt, re.IGNORECASE):
        try:
            date = re.findall(r'\b(\d{4})[-\/\s\.](\d{1,2})[-\/\s\.](\d{1,2})\b', promt)
            year, month, date = date[0]
            name = ''
            df = pd.read_csv('sources\\names_final.csv')
            for word in promt.split():
                if word in list(df['names']):
                    name = word
            
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
            data = {
            'id':str(time.time()),
            'key':f"Name-Birthdate Info",
            'img':'no-img',
            'value':'Soo sorry i actually i could not find your name. Because i am asumming this name is invalid. Soon i will give response if it is valid name.',
            'copy':'nothing',
            'extra':['sample'+str(x) for x in range(1,6)],
            }
            return data        
        
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
     
     
    elif promt == 'Do you know any jokes' or promt == 'How about a joke' or promt == 'Give me a joke' or promt == 'Make me laugh' or promt == 'I need cheering up' or re.search(joke_pattern, promt, re.IGNORECASE): 
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
    
    elif 'explain' in promt or 'desc' in promt and 'number' in promt and check_num(promt) or re.search(number_info_pattern, promt, re.IGNORECASE):        
        numbers = re.findall(r'\d+', promt)
        if len(numbers) == 1:
            num = numbers[0]
        else:
            num = random.randint(0, 1000)
        data = {
                'id':str(time.time()),
                'key':f"Describing Number {num}",
                'img':'no-img',
                'value':number_funtions.explain_number(num),
                'copy':'',
                'extra':['sample'+str(x) for x in range(1,6)],
            }
        return data
    
    elif 'even' in promt and 'numbers' in promt and (('from' in promt and 'to' in promt) or ('-' in promt ) or ('between' in promt )) and check_num(promt) or re.search(even_numbers_pattern , promt, re.IGNORECASE):
        numbers = re.findall(r'\d+', promt)
        if len(numbers) > 0:
            a = int(min(numbers))
            b = int(max(numbers))
        else:
            a = 0
            b = 100

        data = {
                'id':str(time.time()),
                'key':f"Even Numbers Between {a} to {b}",
                'img':'no-img',
                'value':number_funtions.even_numbers(a,b),
                'copy':number_funtions.even_numbers(a,b),
                'extra':['sample'+str(x) for x in range(1,6)],
            }
        return data
    
    elif 'odd' in promt and 'numbers' in promt and (('from' in promt and 'to' in promt) or ('-' in promt ) or ('between' in promt )) and check_num(promt) or re.search(odd_numbers_pattern, promt, re.IGNORECASE):
        numbers = re.findall(r'\d+', promt)
        if len(numbers) > 0:
            a = int(min(numbers))
            b = int(max(numbers))
        else:
            a = 0
            b = 100

        data = {
                'id':str(time.time()),
                'key':f"Odd Numbers Between {a} to {b}",
                'img':'no-img',
                'value':number_funtions.odd_numbers(a,b),
                'copy':number_funtions.odd_numbers(a,b),
                'extra':['sample'+str(x) for x in range(1,6)],
            }
        return data
    
    elif 'prime' in promt and 'numbers' in promt and (('from' in promt and 'to' in promt) or ('-' in promt ) or ('between' in promt )) and check_num(promt) or re.search(prime_numbers_pattern, promt, re.IGNORECASE):
        numbers = re.findall(r'\d+', promt)

        if len(numbers) > 0:
            a = int(min(numbers))
            b = int(max(numbers))
        else:
            a = 0
            b = 100

        data = {
                'id':str(time.time()),
                'key':f"Prime Numbers Between {a} to {b}",
                'img':'no-img',
                'value':number_funtions.prime_numbers(a, b),
                'copy':number_funtions.prime_numbers(a,b),
                'extra':['sample'+str(x) for x in range(1,6)],
            }
        return data
    
    elif 'fibonacci' in promt and 'numbers' in promt and (('from' in promt and 'to' in promt) or ('-' in promt ) or ('between' in promt )) and check_num(promt) or re.search(fibonacci_numbers_pattern , promt, re.IGNORECASE):
        numbers = re.findall(r'\d+', promt)

        if len(numbers) > 0:
            a = int(min(numbers))
            b = int(max(numbers))
        else:
            a = 0
            b = 100

        data = {
                'id':str(time.time()),
                'key':f"Fibonacci Numbers Between {a} to {b}",
                'img':'no-img',
                'value':number_funtions.fibonacci_numbers(a,b),
                'copy':number_funtions.fibonacci_numbers(a,b),
                'extra':['sample'+str(x) for x in range(1,6)],
            }
        return data
    
                            #my funtions
                            
    elif 'table' in promt and 'math' in promt or 'write' in promt or 'generate' in promt or re.search(math_table_pattern , promt, re.IGNORECASE):
        num = re.findall(r'\d+', promt)
        if len(num):
            num = int(num[0])
        else:
            num = random.randint(2, 500)
        data = {
                'id':str(time.time()),
                'key':f"Math Table for {num}",
                'img':'no-img',
                'value':number_funtions.table(num),
                'copy':'',
                'extra':['sample'+str(x) for x in range(1,6)],
            }
        
        return data
    
    elif 'roll dice' == promt or re.search(dice_pattern , promt, re.IGNORECASE):
        data = {
                'id':str(time.time()),
                'key':f"Dice",
                'img':'no-img',
                'value':my_funtions.dice(),
                'copy':'',
                'extra':['sample'+str(x) for x in range(1,6)],
            }
        return data
    
    elif 'toss' == promt or 'spin coin' in promt or 'heads or tales' in promt or 'heads and tales' in promt or re.search(toss_pattern , promt, re.IGNORECASE):
        data = {
                'id':str(time.time()),
                'key':f"Toss",
                'img':'no-img',
                'value':my_funtions.toss(),
                'copy':'',
                'extra':['sample'+str(x) for x in range(1,6)],
            }
        return data
    
    elif 'random card' == promt or 'pick a random card' in promt or ('card' in promt and 'get' in promt or 'select' in promt or 'pick' in promt or 'show' in promt or 'random' in promt) or re.search(deck_of_patterns , promt, re.IGNORECASE):
        data = {
                'id':str(time.time()),
                'key':f"Random Card",
                'img':'no-img',
                'value':my_funtions.card(),
                'copy':'',
                'extra':['sample'+str(x) for x in range(1,6)],
            }
        return data
    
    
                        #text funtions
    elif 'convert text' in promt or re.search(translate_pattern , promt, re.IGNORECASE):
        try:
            text = re.findall(r'[\'"](.*?)[\'"]', promt)[0]
        except:
            text = None 
        language_dict = {
    'Afrikaans': 'af',
    'Amharic': 'am',
    'Arabic': 'ar',
    'Azerbaijani': 'az',
    'Belarusian': 'be',
    'Bulgarian': 'bg',
    'Bengali': 'bn',
    'Bosnian': 'bs',
    'Catalan': 'ca',
    'Cebuano': 'ceb',
    'Czech': 'cs',
    'Welsh': 'cy',
    'Danish': 'da',
    'German': 'de',
    'Greek': 'el',
    'English': 'en',
    'Esperanto': 'eo',
    'Spanish': 'es',
    'Estonian': 'et',
    'Basque': 'eu',
    'Persian': 'fa',
    'Finnish': 'fi',
    'French': 'fr',
    'Irish': 'ga',
    'Scottish Gaelic': 'gd',
    'Galician': 'gl',
    'Gujarati': 'gu',
    'Hausa': 'ha',
    'Hawaiian': 'haw',
    'Hindi': 'hi',
    'Hmong': 'hmn',
    'Croatian': 'hr',
    'Haitian Creole': 'ht',
    'Hungarian': 'hu',
    'Armenian': 'hy',
    'Indonesian': 'id',
    'Igbo': 'ig',
    'Icelandic': 'is',
    'Italian': 'it',
    'Hebrew': 'iw',
    'Japanese': 'ja',
    'Javanese': 'jv',
    'Georgian': 'ka',
    'Kazakh': 'kk',
    'Khmer': 'km',
    'Kannada': 'kn',
    'Korean': 'ko',
    'Kurdish': 'ku',
    'Kyrgyz': 'ky',
    'Latin': 'la',
    'Luxembourgish': 'lb',
    'Lao': 'lo',
    'Lithuanian': 'lt',
    'Latvian': 'lv',
    'Malagasy': 'mg',
    'Maori': 'mi',
    'Macedonian': 'mk',
    'Malayalam': 'ml',
    'Mongolian': 'mn',
    'Marathi': 'mr',
    'Malay': 'ms',
    'Maltese': 'mt',
    'Burmese': 'my',
    'Nepali': 'ne',
    'Dutch': 'nl',
    'Norwegian': 'no',
    'Chichewa': 'ny',
    'Punjabi': 'pa',
    'Polish': 'pl',
    'Pashto': 'ps',
    'Portuguese': 'pt',
    'Romanian': 'ro',
    'Russian': 'ru',
    'Kinyarwanda': 'rw',
    'Sindhi': 'sd',
    'Sinhala': 'si',
    'Slovak': 'sk',
    'Slovenian': 'sl',
    'Samoan': 'sm',
    'Shona': 'sn',
    'Somali': 'so',
    'Albanian': 'sq',
    'Serbian': 'sr',
    'Sesotho': 'st',
    'Sundanese': 'su',
    'Swedish': 'sv',
    'Swahili': 'sw',
    'Tamil': 'ta',
    'Telugu': 'te',
    'Tajik': 'tg',
    'Thai': 'th',
    'Filipino': 'tl',
    'Turkish': 'tr',
    'Ukrainian': 'uk',
    'Urdu': 'ur',
    'Uzbek': 'uz',
    'Vietnamese': 'vi',
    'Xhosa': 'xh',
    'Yiddish': 'yi',
    'Yoruba': 'yo',
    'Chinese': 'zh',
    'Chinese (Traditional)': 'zh-TW',
    'Zulu': 'zu'
}
        language = 'te'
        for word in promt.split():
            if word.title() in language_dict.keys():
                language = word                
        data = {
                'id':str(time.time()),
                'key':f"Random Card",
                'img':'no-img',
                'value':text_funtions.language_convert(text, language),
                'copy':'',
                'extra':['sample'+str(x) for x in range(1,6)],
            }
        return data
    elif 'correct' in promt or re.search(correction_patterne , promt, re.IGNORECASE):
        try:
            text = re.findall(r'[\'"](.*?)[\'"]', promt)[0]
        except:
            text = None 
        data = {
                'id':str(time.time()),
                'key':f"Random Card",
                'img':'no-img',
                'value':text_funtions.correct_text(text),
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
    
    
    
    
    