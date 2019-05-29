# Wikipedia city scraper

This project is a python program that scrapes a  [wikipedia](https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population) article for data on the top cities in the United States.  

### Prerequisites

To run this project, beautifulsoup4 must be installed as well as python requests.
Beautifulsoup is used to scrap HTML pages and requests will look up a url.  
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install beautifulsoup4 and requests in terminal.

```bash
pip install requests
pip install bs4
```



## Code explanation

Firstly the code puts every city's data from the original wikipedia cite into a list. It does this by initializing a request variable and a beautifulsoup variable and finds the class with the table, "wikitable sortable".  It then finds all of the <td> tags where each data element is stored in the table.  The data is put into a list, "city_info", and the cities individual website is found by looking for the <a>[href] tag at the index the link is located.  

The method "local" is used to scrape each individual wikipedia cite for all of the cities.  It's parameter is the link to the url of the individual city page.  The method initializes its own request and beautifulsoup variables and searches the html for the city's first table on the page.  All cities have the same table with the tag "infobox geography vcard".  Each data element in the table is stored in a <tr> tag so the method then collects all of the <tr> tags using beautifulsoup's "find_all" method.  The method than looks for <td> tags within the <tr> tag to find data on "Mayor", "Timezone", "Elevation", "Website", "Demonym" and "Area code" and adds the data to an array that is returned.  Some data elements must me stripped of python special characters or links in brackets or parenthesis.  

The cities individual data is added to "city_info" and put into a superlist with all the cities information, "all_city_info".  The ammount of cities to scrape can be changed by the user when prompted (30 was chosen as the max as the code can run quite slowly especially if internet connection is slow).   "all_city_info" is looped through and written into rows of a csv file.  

## Built With

Python3



## Author

**Jesse Jacob** 


