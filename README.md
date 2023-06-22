# Web_Scrape_using_Python
Web Scrape using Python and Beautiful Soup

Perform web scraping on the website "https://www.waktusolat.my/pulau-pinang" to extract prayer time data for a specific location (Pulau Pinang in this case). I uses the `requests` library to connect to the website and retrieve the HTML content. Then, utilizes the `BeautifulSoup` library for parsing and navigating the HTML structure.

The code specifically targets a table on the webpage that contains prayer time information. It extracts the table headers and the data in each column of the table. It then writes the extracted data to a CSV file named "waktusolat.csv".

In summary, the code scrapes the prayer time data from the website and saves it in a CSV file for further analysis or usage.
