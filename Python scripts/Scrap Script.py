from bs4 import BeautifulSoup
import requests
#import pandas
#import numpy
def GetHouseList(pages):
    data=[]
    #df=pandas.DataFrame(columns=['title','price','location','property_type','bedrooms','bathrooms','area'])
    for pageNo in range(pages):
        url="https://www.propertyfinder.eg/en/search?c=1&l=2254&ob=mr&page={}&t=1".format(pageNo+1)
        print(pageNo+1)
        r = requests.get(url)
        content = r.content
        soup = BeautifulSoup(content,features="lxml")
        for d in soup.findAll('div', attrs={'class':'card-list__item'}):  
            try:
                price = d.find('span', attrs={'class':'card__price-value'}).text
                title = d.find('h2', attrs={'class':'card__title card__title-link'}).text
                location = d.find('span', attrs={'class':'card__location-text'}).text
                property_type = d.find('p', attrs={'class':'card__property-amenity card__property-amenity--property-type'}).text
                bedrooms = d.find('p', attrs={'class':'card__property-amenity card__property-amenity--bedrooms'}).text
                bathrooms = d.find('p', attrs={'class':'card__property-amenity card__property-amenity--bathrooms'}).text
                area = d.find('p', attrs={'class':'card__property-amenity card__property-amenity--area'}).text
                data.append([title,price,location,property_type,bedrooms,bathrooms,area])
            except:
                continue
    print('Data Scrapped successfully')
    return data








    


