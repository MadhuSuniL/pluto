import requests 
from bs4 import BeautifulSoup


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




def get_today_news():
    headlines = []
    images = []
    contents = []

    url = 'https://www.indiatoday.in/world'
    domain = 'https://www.indiatoday.in'



    page = requests.get(url).text
    # print(len(page))
    html = BeautifulSoup(page,'lxml')

    articles = html.find_all('article')

    for article in articles:
        try:
            # for headlines
            headline = article.find('a')
            if headline != None:
                headline = headline.text
            if 'Watch' not in headline:        
                headlines.append(headline)
                #for url link
                link = article.find('a')
                if link is not None:
                    link = link['href']
                    new_page = requests.get(domain+link).text
                    # print(len(new_page))
                    new_html = BeautifulSoup(new_page,'lxml')
                    main = new_html.find('div',class_='jsx-99cc083358cc2e2d Story_story__content__body__qCd5E story__content__body widgetgap')
                    # for images
                    try:
                        image = main.find('img',attrs={'width':'690'})
                        if image is not None:
                            image = image['src']
                            # print(image)
                            images.append(image)
                        
                    except:
                        print(headline)
                    # for contents
                    content = main.find_all('p')
                    if content is not None:
                        text = ''
                        for cont in content:
                            text+=cont.text
                        content = para_wise(text) 
                        # print(content)
                        contents.append(content)
                    # adding
        except:
            pass

    data = {
        'headlines' : headlines,
        'images' : images,
        'contents' : contents
    }            
    # print(len(headlines))
    # print(len(images))
    # print(len(contents))
    return data       
       
# print(get_today_news())