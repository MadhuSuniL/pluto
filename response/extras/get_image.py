from googleapiclient import discovery
import random
def image(word):
    try:
        api_key = "AIzaSyDLvY11fFe_speSTQiRTozh8a8wJJiwsyo"
        resource = discovery.build("customsearch", 'v1', developerKey=api_key).cse()
        result = resource.list(q=word,searchType='image', cx='2157080c00f934f39').execute()
        # print(result['items'])
        return result['items'][0]['link'] 
    except:
        # none_images = ['https://www.google.co.in/url?sa=i&url=https%3A%2F%2Fwww.shutterstock.com%2Fvideo%2Fsearch%2F404-page-not-found-robot&psig=AOvVaw0FLEeCwYt5tAkB-7a_ae-N&ust=1683542325911000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCIiD9YSC4_4CFQAAAAAdAAAAABAF','https://www.google.co.in/url?sa=i&url=https%3A%2F%2Fwww.freepik.com%2Fpremium-vector%2Fwebsite-page-found-wrong-url-address-error-broken-robot-character-keeps-socket-off-site-crash_29091796.htm&psig=AOvVaw0FLEeCwYt5tAkB-7a_ae-N&ust=1683542325911000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCIiD9YSC4_4CFQAAAAAdAAAAABAK','https://www.google.co.in/url?sa=i&url=https%3A%2F%2Fwww.redbubble.com%2Fi%2Fart-board-print%2FError-404-No-Image-Found-by-Jientifelmalti%2F50491116.5E8EA&psig=AOvVaw1BzRB9Jg73lAtRWwTkMfwf&ust=1683542579758000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCNjDx_2C4_4CFQAAAAAdAAAAABAE','https://www.google.co.in/url?sa=i&url=https%3A%2F%2Fwww.redbubble.com%2Fi%2Fart-board-print%2FError-404-No-Image-Found-by-Jientifelmalti%2F50491116.5E8EA&psig=AOvVaw1BzRB9Jg73lAtRWwTkMfwf&ust=1683542579758000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCNjDx_2C4_4CFQAAAAAdAAAAABAE','https://www.google.co.in/url?sa=i&url=https%3A%2F%2Fwww.redbubble.com%2Fi%2Fart-board-print%2FError-404-No-Image-Found-by-Jientifelmalti%2F50491116.5E8EA&psig=AOvVaw1BzRB9Jg73lAtRWwTkMfwf&ust=1683542579758000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCNjDx_2C4_4CFQAAAAAdAAAAABAE']
        return 'https://ih1.redbubble.net/image.1316918305.1116/st,small,845x845-pad,1000x1000,f8f8f8.jpg'
