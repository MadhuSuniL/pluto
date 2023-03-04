import wikipedia as wk
from .get_image import image

def explain(word):
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
            value = "I am sorry i could't found the result. Please check spellings or try in another way(with new words)."
            img = 'none'
        try:
            extra = wk.search(word)
        except:
            extra = None
        if extra is not None:
            extras = 'You can search about these things also...\n\n'
        if len(extra) > 6 and extra is not None:
            extra = extra[0:10]
        # if extra is not None:
        #     for val in extra:
        #         extras += val + ', \n'
        #     extra = extras

        data = {
        'key':key,
        'img':img,
        'value':value,
        'extra':extra
        }
        return data
    # except:
    #     return None                
#print(explain('what is programming language)'))


