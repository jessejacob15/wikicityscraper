from bs4 import BeautifulSoup #need package for html scraping
import requests               #need to search the web                
from csv import writer        #need to write csv file


# function takes the wikipedia link from each city and searches its table for mayor, timezone,
# elevation, website, demonym and area code
# function returns list containing city's data from its individual wiki page
def local(link):                                                    
    inner = requests.get(link)                                          #local response link
    alpha = BeautifulSoup(inner.text, 'html.parser')                    #soup variable
    table = alpha.find(class_='infobox geography vcard')                #find css class where the city's data table is stored
    tr_tags = table.find_all('tr')                                      #list of all <tr> tags where each data element is stored
    addinfo = []                                                        #array for 

    for tr in tr_tags:                                                  #loop to find each element in tr tag
        if ('Mayor' in tr.get_text() and 'Type' not in tr.get_text()):  
            td = tr.find('td')
            mayor = td.get_text()
            if ('(' in mayor):
                cut = mayor.find('(')
                mayor = mayor[0:cut]
            addinfo.append(mayor)
        if ('Time zone' in tr.get_text()):
            td = tr.find('td')
            tz = td.get_text()
            addinfo.append(tz)
        if ('Elevation' in tr.get_text()):
            td = tr.find('td')
            elev = td.get_text().replace('\xa0', '')
            addinfo.append(elev)
        if ('Website' in tr.get_text()):
            td = tr.find('td')
            web = td.find('a')['href']
            addinfo.append(web)
        if ('Demonym' in tr.get_text()):
            td = tr.find('td')
            demon = td.get_text()
            addinfo.append(demon)
        if ('Area code' in tr.get_text()):
            td = tr.find('td')
            ac = td.get_text()
            addinfo.append(ac)

        
    return addinfo


response = requests.get('https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population')  #main wikipedia response
soup = BeautifulSoup(response.text, 'html.parser')                                                   #main wikipedia soup variable

table = soup.find(class_= 'wikitable sortable')                                                     #find table in article CSS

la = table.find_all('td')                                                                           #find all <td> tags in article where data is stored

i = 0                                                                                               #i and j loop variables where j can be changed for ammount of states to scrape, 
j =  int(input("please input the number of cities to collect data on? (30 maximum): "))                  # i is to control the ammount of data scraped, right now it takes all feilds from wiki table for each city
all_city_info = [] #superlist of all cities data lists

while (j > 30 or j < 0):
    j = int(input("please enter number between 0 and 30: "))
            
print("fetching data on the top " +  str(j) + " cities...")


for k in range (j):
    city_info = []
    for i in range(i, i + 11):
        add_info_local = []
        #data from main wiki
        data_item = (la[i].get_text().replace('\n', '').replace('\xa0', '').
                           replace('\xb0', '').replace('\u2032', '').replace('\u2033', '').replace('\ufeff', '').replace('/km2', '')
                         .replace('/sqmi', '').replace('sqmi', '').replace('km2',''))
        if ('[' in data_item):
            cut = data_item.find('[')
            data_item = data_item[0:cut]
        city_info.append(data_item)
        #data from each individual page, looks for city link from css in the name
        if (i%11 == 1):                                                                                 
            link = 'https://en.wikipedia.org' + la[i].find('a')['href']
            addinfo_local = local(link)
    #add each intem from city page to its list
    for item in addinfo_local:
        city_info.append(item.replace('\u2212', ''))
    i = i + 1
    #add completed city list to a superlist of all cities
    all_city_info.append(city_info)


#writes the csv file
with open ('cities.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Rank', 'City Name', 'State', '2018 Population', '2010 Population', 'Population increase', 'Square miles',
               'Square Kilometers', 'Population per Square Mile', 'Population per Square Kilometer', 'Coordinates',
               'Mayor', 'Elevation', 'Demonym[s]', 'Timezone[s]', 'Area Code[s]', 'Website']
    csv_writer.writerow(headers)

    #loops through each city's list and writes row in the table
    for citylist in all_city_info:
        cityrow = []
        for data in citylist:
            cityrow.append(data)
        csv_writer.writerow(cityrow)


    

    
