from bs4 import BeautifulSoup
import requests
#import pandas
#import numpy
def GetHouseList(pages_from,pages_to):
    data=[]
    #df=pandas.DataFrame(columns=['title','price','location','property_type','bedrooms','bathrooms','area'])
    for pageNo in range(pages_from,pages_to):
        url="https://www.olx.com.eg/en/properties/apartments-duplex-for-sale/cairo/?search%5Bfilter_enum_ad_type%5D%5B0%5D=1&search%5Bfilter_enum_type%5D%5B0%5D=1&search%5Bfilter_enum_payment_options%5D%5B0%5D=1&page={}".format(pageNo+1)
        print(pageNo+1)
        r = requests.get(url)
        content = r.content
        soup = BeautifulSoup(content,features="lxml")
        for d in soup.findAll('div', attrs={'class':'ads__item'}):
            try:
                 #get details
                #detailsUrl= d.find('a', attrs={'class':'ads__item__ad--title'}).text
                detailsUrl=d.find_all('a', href=True)
                print(detailsUrl)
                break
                #detailsUrl=find('a').contents[0]
                detialRequest = requests.get('https://www.propertyfinder.eg'+str(detailsUrl[0]['href']))
                detailContent = detialRequest.content
                detailSoup = BeautifulSoup(detailContent,features="lxml")
                amenities=[]
                for amenity in detailSoup.findAll('div', attrs={'class':'property-amenities__list'}):
                    #print(amenity.text)
                    amenities.append(amenity.text.strip())


                price = d.find('span', attrs={'class':'card__price-value'}).text
                title = d.find('h2', attrs={'class':'card__title card__title-link'}).text
                location = d.find('span', attrs={'class':'card__location-text'}).text
                property_type = d.find('p', attrs={'class':'card__property-amenity card__property-amenity--property-type'}).text
                bedrooms = d.find('p', attrs={'class':'card__property-amenity card__property-amenity--bedrooms'}).text
                bathrooms = d.find('p', attrs={'class':'card__property-amenity card__property-amenity--bathrooms'}).text
                area = d.find('p', attrs={'class':'card__property-amenity card__property-amenity--area'}).text
               
                #print('amenities:',amenities)
                createDate=detailSoup.findAll('div', attrs={'class':'property-page__legal-list'})[1].text
                data.append([title,price,location,property_type,bedrooms,bathrooms,area,amenities,createDate])
            except :
                #print('Error')
                continue
    return data
GetHouseList(1,2)











    


