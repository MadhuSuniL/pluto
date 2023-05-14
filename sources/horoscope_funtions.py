from nltk.corpus import wordnet
# nltk.download('wordnet')
from .name_patterns import patterns_list
from .name_patterns import qualities
import requests, datetime, math, random, pandas


pt = patterns_list
def name_sentence(name, meaning, gender, religion):
    
    patterns = list(set(pt))
    # print(type(o))
    sentences = []
    for pattern in patterns:
        sentence = pattern.replace("[Intro]", "Get ready for an amazing name!")
        sentence = sentence.replace("[Name]", name.title())
        sentence = sentence.replace("[Gender]", gender.strip())
        sentence = sentence.replace("[Religion]", religion.strip())
        sentence = sentence.replace("[Meaning]", meaning.strip())
        
        if meaning.lower().startswith("a") or meaning.lower().startswith("e") or meaning.lower().startswith("i") or meaning.lower().startswith("o") or meaning.lower().startswith("u"):
            sentence = sentence.replace("[Symbolism]", "the essence of an " + meaning.lower())
        else:
            sentence = sentence.replace("[Symbolism]", "the essence of a " + meaning.lower())
        
        sentences.append(sentence)
    return random.choice(sentences)


def get_word_info(word):
    synsets = wordnet.synsets(word)
    
    if not synsets:
        return "No information available for the word."
    
    # Retrieve information from the first synset
    first_synset = synsets[0]
    definition = first_synset.definition()
    examples = first_synset.examples()
    
    info = f"Word: {word}\nDefinition: {definition}\nExamples: {examples}"
    return info

def encounter(name, number):
    patterns = [
        f"I have observed {number} instances of people named {name}.",
        f"In my experience, I have come across {number} individuals named {name}.",
        f"{name} is a name that I have encountered {number} times.",
        f"Encountering {number} people named {name} has been a common occurrence for me.",
        f"I've had the opportunity to meet {number} individuals who share the name {name}.",
        f"It's remarkable that I have encountered {number} people with the name {name}.",
        f"Throughout my experience, {name} is a name that has appeared {number} times.",
        f"I have personally come across {number} occurrences of the name {name}.",
        f"{number} individuals named {name} have crossed my path.",
        f"Having encountered {number} people with the name {name}, it is a familiar name to me."
    ]

    sentences = random.choice(patterns)
    return sentences



def name_prob(name):
    try:
        response = requests.get(f"https://api.genderize.io/?name={name}")
        data = response.json()
        return f"The name {name} is {data['probability']*100:.0f}% likely to be associated with the {data['gender']} gender. "+encounter(name, data['count'])
    except:
        return ''
        

def name_describe(name):
    name_len = len(name)
    f = ''
    for char in name:
        index = name.index(char)
        size = len(qualities[char.upper()])
        pos = math.floor((index/name_len)*size)
        f+=f"<b class='text-xl'>{char.upper()}</b> <span  class='text-lg'>{qualities[char.upper()][pos]}</span><br>"
    return f

                                            ##Date



def age(year, month, date):
    birthdate = str(year)+'/'+str(month)+'/'+str(date)
    birthdate = datetime.datetime.strptime(birthdate, "%Y/%m/%d").date()
    today = datetime.date.today()
    age = today - birthdate

    years = age.days // 365
    months = (age.days % 365) // 30
    days = (age.days % 365) % 30
    
    return f"{years} years {months} months {days} days <br> or {years * 12 + months} months {days} days <br> or {age.days // 7} weeks {age.days % 7} days <br> or {age.days} days <br> or {age.days * 24} hours <br> or {age.days * 24 * 60} minutes <br> or {age.days * 24 * 60 * 60} seconds"


def calculate_zodiac_sign(day, month):
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    else:
        return "Invalid date"


def generate_zodiac_response(day, month):
    zodiac_sign = calculate_zodiac_sign(day, month)
    
    if zodiac_sign == 'Aries':
        return "You are an Aries. Aries individuals are known for their confidence and ambition. You have a pioneering spirit and are always ready to take on new challenges."

    elif zodiac_sign == 'Taurus':
        return "You are a Taurus. Taurus individuals are reliable and practical. You have a strong work ethic and value stability and material comforts."

    elif zodiac_sign == 'Gemini':
        return "You are a Gemini. Gemini individuals are sociable and intellectually curious. You have excellent communication skills and a versatile nature."

    elif zodiac_sign == 'Cancer':
        return "You are a Cancer. Cancer individuals are nurturing and intuitive. You form strong emotional connections and have a creative side."

    elif zodiac_sign == 'Leo':
        return "You are a Leo. Leo individuals are confident and passionate. You possess leadership qualities and have a desire for recognition and success."

    elif zodiac_sign == 'Virgo':
        return "You are a Virgo. Virgo individuals are analytical and practical. You pay attention to detail and have a strong sense of organization."

    elif zodiac_sign == 'Libra':
        return "You are a Libra. Libra individuals are diplomatic and harmonious. You value fairness and strive for balance and harmony."

    elif zodiac_sign == 'Scorpio':
        return "You are a Scorpio. Scorpio individuals are passionate and mysterious. You form deep emotional connections and have a determined nature."

    elif zodiac_sign == 'Sagittarius':
        return "You are a Sagittarius. Sagittarius individuals are adventurous and optimistic. You have a philosophical nature and a love for new experiences."

    elif zodiac_sign == 'Capricorn':
        return "You are a Capricorn. Capricorn individuals are responsible and ambitious. You have a strong sense of discipline and strive for success."

    elif zodiac_sign == 'Aquarius':
        return "You are an Aquarius. Aquarius individuals are independent and innovative. You have a humanitarian mindset and a desire to make a positive impact."

    elif zodiac_sign == 'Pisces':
        return "You are a Pisces. Pisces individuals are compassionate and imaginative. You have artistic talents and possess a deep sense of empathy."

    else:
        return "Invalid zodiac sign. Please provide a valid zodiac sign."

def events(date):
    headings = [
        "The most popular events on your birthday date are historical milestones and celebrations.",
        "Your birthday date has witnessed numerous significant events throughout history.",
        "Historically, your birthday date is associated with important events and memorable occasions.",
        "On your birthday date, noteworthy events and remarkable happenings have taken place.",
        "Throughout the years, your birthday date has been marked by notable events and festive occasions.",
        "Your birthday date holds a rich history of remarkable events and memorable moments.",
        "Significant historical events and renowned celebrations have occurred on your birthday date.",
        "On your special day, noteworthy occurrences and noteworthy festivities have been recorded.",
        "Celebrations and milestones are commonly observed on your birthday date.",
        "Your birthday date is renowned for witnessing prominent events and notable happenings."
    ]
    
    birth_date = date
    timestamp = int((datetime.datetime.strptime(birth_date, "%Y-%m-%d") - datetime.datetime(1970, 1, 1)).total_seconds() / (60 * 60 * 24))
    events_list = []
    for even in range(5):
        api_url = f"http://numbersapi.com/{timestamp}/date"
        response = requests.get(api_url)
        fun_fact = f'{even+1}. '+response.text
        events_list.append(fun_fact)
    
    return random.choice(headings)+' <br><br>'+"<br>\n".join(events_list)

        
        
def horoscope(name, year, month, date):
    name = name.lower().strip()
    names = pandas.read_csv('sources\\names_final.csv')
    if name in list(names['names']):
        index = list(names['names']).index(name)
        name_sentence_var = name_sentence(name, names['meanings'][index], names['genders'][index], names['religion'][index])
        name_prob_var = name_prob(name)
        name_describe_var = name_describe(name)
        generate_zodiac_response_var = generate_zodiac_response(date, month)
          
        res = f"""
        <h1 class='text-3xl text-cyan-400 font-bold my-4' style='text-align:center'>{name.title()}</h1>
        <p>
        &nbsp;&nbsp;&nbsp;&nbsp;{name_sentence_var} {name_prob_var} {generate_zodiac_response_var}
        </p>
        <br>
        <br>
        <p>
        <center class='flex flex-col items-center'>
        {name_describe_var}
        </center>
        </p>
        <br>
        <h1 class='text-xl text-cyan-400'>Your Age</h1>
        <br>
        <p>
        {age(year, month, date)}
        </p>
        <br>
        <h1 class='text-xl text-cyan-400'>Events</h1>
        <br>
        <p>
        {events(str(year)+'-'+str(month)+'-'+str(date+1))}
        </p>"""
        
        return res
    else:
        return 'no'
# print(horoscope('Madhu', 2000, 3, 28))
        
        
        


