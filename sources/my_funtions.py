import random
from num2words import num2words
from .name_patterns import coin_toss_patterns, dice_patterns, card_patterns, cards

def dice():
    value = num2words(random.randint(1, 6)).title() 
    return random.choice(dice_patterns).replace('{dice_value}', '<b class="text-3xl">'+value+'</b>')

def toss():
    value = random.choice(['Heads','Tales']) 
    return random.choice(coin_toss_patterns).replace('{outcome}', '<b class="text-3xl">'+value+'</b>')

def card():
    value = random.choice(cards)
    return random.choice(card_patterns).replace('{card_name}', '<b class="text-3xl">'+value+'</b>')





