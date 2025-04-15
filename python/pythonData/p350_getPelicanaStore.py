from itertools import count
from p340_ChickenUtil import ChickenStore

brandName = 'pelicana'
base_url = 'https://www.pelicana.co.kr/store'

def getData():
    savedData = []

    for page_idx in count():
        url = base_url + '?page=' + str(page_idx + 1)
        print(url)
        chknStore = ChickenStore(brandName, url)
        soup = chknStore.getSoup()
        