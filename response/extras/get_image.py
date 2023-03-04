from googleapiclient import discovery
def image(word):
    try:
        api_key = "AIzaSyDLvY11fFe_speSTQiRTozh8a8wJJiwsyo"
        resource = discovery.build("customsearch", 'v1', developerKey=api_key).cse()
        result = resource.list(q=word,searchType='image', cx='2157080c00f934f39').execute()
        return result['items'][0]['link'] 
    except:
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Flag_of_None.svg/2560px-Flag_of_None.svg.png'
