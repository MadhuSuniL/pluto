import requests , random

laughing_emojis = [
    "😂",
    "🤣",
    "😆",
    "😄",
    "😅",
    "😊😂",
    "😁",
    "😃",
    "😹",
    "😄🤣",
    "😆😂",
    "😂😅",
    "🤣😄",
    "😂😄",
    "😂🤣😄",
    "😂😆😅",
    "😂😹",
    "😂😃",
    "😂🙂",
    "😂😊"
]


def get_joke(cat):
    
    if cat == None:
        url = "https://v2.jokeapi.dev/joke/Any"
    else:
        url = f"https://v2.jokeapi.dev/joke/{cat}"
    response = requests.get(url)
    data = response.json()
    try:
        category = data['category']
    except:
        category = cat.title()
    patterns = [
    f"Oh, I've got a good one for you! This joke is from the {category} category. Here it goes:",
    f"Guess what? I found a hilarious joke in the {category} category. Prepare to laugh:",
    f"Ready for a joke? This one's from the {category} category. Brace yourself:",
    f"Time for some laughter! Here's a joke from the {category} category just for you:",
    f"I've got a joke to brighten your day, straight from the {category} category. Listen to this:",
    f"You're in for a treat! Here's a joke from the {category} category that I think you'll enjoy:",
    f"Hold on tight! I discovered a fantastic joke in the {category} category. Get ready to chuckle:",
    f"Get ready for a hilarious joke! This one falls under the {category} category. Here it comes:",
    f"I stumbled upon a great joke in the {category} category. Brace yourself for some laughter:",
    f"Knock, knock! I've got a joke from the {category} category that's bound to make you smile:",
    f"Listen up! I've found a fantastic joke in the {category} category. Prepare to be amused:",
    f"Here's a joke for you, fresh from the {category} category. Get ready to laugh out loud:",
    f"Hold onto your seat! I've discovered a side-splitting joke in the {category} category. Enjoy:",
    f"Ready to have a good chuckle? This joke is from the {category} category. Here you go:",
    f"I have a joke to brighten your day, and it's in the {category} category. Check this out:",
    f"Calling all joke enthusiasts! I've got a gem from the {category} category. Get ready to laugh:",
    f"In need of a smile? Here's a joke from the {category} category just for you:",
    f"Attention, everyone! I've uncovered a rib-tickling joke in the {category} category. Listen up:",
    f"Prepare yourself for a joke of epic proportions! This one's from the {category} category:",
    f"I bet you'll enjoy this one! It's a joke from the {category} category. Have a laugh:",
    f"Hold your breath! I've got a side-splitting joke from the {category} category. Here it is:",
    f"Get ready to laugh your socks off! This joke falls into the {category} category:",
    f"Looking for a joke that'll brighten your day? Look no further! It's from the {category} category:",
    f"I found a gem of a joke in the {category} category. Get ready to giggle uncontrollably:",
    f"Attention, joke lovers! I present to you a rib-tickling joke from the {category} category:",
    f"Need a little humor in your life? Here's a joke from the {category} category to make you smile:",
    f"Hold onto your funny bone! I've got a joke in the {category} category that'll crack you up:"
    ]


    if data["type"] == "single":
        return random.choice(patterns) +'<br><br>'+'<b>'+data["joke"]+'</b>'+random.choice(laughing_emojis)
    elif data["type"] == "twopart":
        return random.choice(patterns) +'<br><br>'+'<b>'+f"{data['setup']}\n{data['delivery']}"+'</b>'+random.choice(laughing_emojis)
    else:
        return "I'm sorry, I couldn't fetch a joke."

