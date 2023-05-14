import wikipedia as wk
from .get_image import image
import time, random
from sources.name_patterns import sorry
from .translate import translate , para_wise 
from .voice import voice
def explain(word,lang_):
        if word == 'python' or word == 'Python':
            word = 'Python (programming language)'
        if word == 'C' or word == 'C programming':
            word = 'C Programming Language'   
    # try:
        key = word
        img = image(word)
        try :
            value = wk.summary(word)
        except:
            value = random.choice(sorry)
            img = 'none'
        try:
            extra = wk.search(word)
            if word in extra:
                extra.remove(word)
        except:
            extra = None
        if extra is not None:
            extras = 'You may search about these lines also...\n\n'
        try:
            if len(extra) > 6 and extra is not None:
                extra = extra[0:10]
        except:
            pass
        # if extra is not None:
        #     for val in extra:
        #         extras += val + ', \n'
        #     extra = extras

        value = translate(value, lang_) 
        key2 = translate(key, lang_)
        
        if key2 in value or key2.title() in value:
            value = value.replace(key, f'<span class="text-white font-extrabold text-xl">{key}</span>')
            value = value.replace(key.title(), f'<span class="text-white font-extrabold font-mono text-xl">{key.title()}</span>')
        
        try:
            value = para_wise(value)
        except:
            pass
        
        data = {
        'id':str(time.time()),
        'key':key,
        'img':img,
        'value':value,
        'extra':extra,
        # 'audio': voice('what is programming language')
        }
        return data
    # except:
    #     return None                
#print(explain('what is programming language)'))


