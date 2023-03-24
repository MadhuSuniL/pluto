from googletrans import Translator

translator = Translator()

#telugu - te
#hindi - hi
#english - en
#tamil - tamil
#chinese - zh-cn
#kannada - kn
#malayalam - ml
#tukish - tr
#urdu - ur
#arbic - ar

# import googletrans
# print(googletrans.LANGUAGES)


def translate(text,to_lang):
    if 'en' in to_lang:
        return text
    safe = to_lang
    to_lang = to_lang.split(' ')
    try:
        translated_text = translator.translate(text, src='en', dest = to_lang[0])
    except:
        return 'Server is busy..! try after sometime.'
    # print(f"The Actual Text was {text}")
    # print(f"The Translated Text is: {translated_text.text}")
    # print(f"The Translated Text pronunciation is {translated_text.pronunciation}")

    if(translated_text.text.lower() == text.lower() or translated_text.pronunciation.lower() == text.lower()):
        return translate('Could not translated..!', safe)

    if(to_lang[1] == 'n'):
        return translated_text.text
    else:
        return translated_text.pronunciation
    
# a = translate('Hello how are you', 'ur n')

# print(a)



def para_wise(text):
    para_length = 830
    para_range = range(para_length-100 ,len(text))
    final_paras_list = []
    while True:
        if len(text) >= para_length:
            para = ''
            index = 0
            for char in text:
                try:
                    first = text[index-1].isnumeric()
                    second = text[index+1].isnumeric()
                except:
                    first = False
                    second = False
                if len(para) in para_range and char == '.' and (not first and not second):
                    final_paras_list.append(para+'.')
                    text = text.replace(para+'.', '')
                    break
                else:
                    para += char
                
                index += 1
                    
            # break
        else:
            final_paras_list.append(text)
            break
            
    final_text = '<br><br>&nbsp;&nbsp;&nbsp;&nbsp;'.join(final_paras_list)
    
    return '&nbsp;&nbsp;&nbsp;&nbsp;'+final_text
    
    
    
    
# print(para_wise("""Hyderabad ( (listen) HY-dər-ə-bad; Telugu: [ˈɦaɪ̯daraːbaːd], Urdu: [ˈɦɛːdəɾaːbaːd]) is the capital and largest city of the Indian state of Telangana and the de jure capital of Andhra Pradesh. It occupies 650 km2 (250 sq mi) on the Deccan Plateau along the banks of the Musi River, in the northern part of Southern India. With an average altitude of 542 m (1,778 ft), much of Hyderabad is situated on hilly terrain around artificial lakes, including the Hussain Sagar lake, predating the city's founding, in the north of the city centre. According to the 2011 Census of India, Hyderabad is the fourth-most populous city in India with a population of 6.9 million residents within the city limits, and has a population of 9.7 million residents in the metropolitan region, making it the sixth-most populous metropolitan area in India. With an output of US$74 billion, Hyderabad has the fifth-largest urban economy in India.
# Muhammad Quli Qutb Shah established Hyderabad in 1591 to extend the capital beyond the fortified Golconda. In 1687, the city was annexed by the Mughals. In 1724, Asaf Jah I, the Mughal viceroy, declared his sovereignty and founded the Asaf Jahi dynasty, also known as the Nizams. Hyderabad served as the imperial capital of the Asaf Jahi's from 1769 to 1948. As capital of the princely state of Hyderabad, the city housed the British Residency and cantonment until Indian independence in 1947. Hyderabad was annexed by the Indian Union in 1948 and continued as a capital of Hyderabad State from 1948 to 1956. After the introduction of the States Reorganisation Act of 1956, Hyderabad was made the capital of the newly formed Andhra Pradesh. In 2014, Andhra Pradesh was split to form the state of Telangana, and Hyderabad became the joint capital of the two states with a transitional arrangement scheduled to end in 2024. Since 1956, the city has housed the Rashtrapati Nilayam, the winter office of the president of India.
# Relics of the Qutb Shahi and Nizam eras remain visible today; the Charminar has come to symbolise the city. By the end of the early modern era, the Mughal Empire had declined in the Deccan, and the Nizam's patronage attracted men of letters from various parts of the world. A distinctive culture arose from the amalgamation of local and migrated artisans, with Painting, handicraft, jewellery, literature, dialect and clothing are prominent still today. Through its cuisine, the city is listed as a creative city of gastronomy by UNESCO. The Telugu film industry based in the city was the country's second-largest producer of motion pictures as of 2012.
# Until the 19th century Hyderabad was known for the pearl industry and was nicknamed the "City of Pearls", and was the only trading centre for Golconda diamonds in the world. Many of the city's historical and traditional bazaars remain open. Hyderabad's central location between the Deccan Plateau and the Western Ghats, and industrialisation throughout the 20th century attracted major Indian research, manufacturing, educational and financial institutions. Since the 1990s, the city has emerged as an Indian hub of pharmaceuticals and biotechnology4. The formation of the special economic zones of Hardware Park and HITEC City, dedicated to information technology, has encouraged leading multinationals to set up operations in Hyderabad."""))
