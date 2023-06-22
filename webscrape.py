import requests
from bs4 import BeautifulSoup

url = 'https://www.waktusolat.my/pulau-pinang'

# Connect to the URL
response = requests.get(url)

# Process the result
result = response.text

processor = BeautifulSoup(result, 'html.parser')

# Get table properties
table = processor.table

rows = table.findAll('tr')

headers = []  # To store the table headers
whole_columns = []  # To store the data in each column

# Loop through each row in the table
for row in rows:
    headers_column = row.findAll('th')  # Find all the header columns
    columns = row.findAll('td')  # Find all the regular columns

    if len(headers_column):
        # If there are header columns, add their text to the headers list
        for i in range(len(headers_column)):
            if i == 0:
                headers.append('Tarikh')
            else:
                headers.append(headers_column[i].text)
    else:
        # If there are regular columns, add their text to the whole_columns list
        columns_text = []
        for column in columns:
            columns_text.append(column.text)
        whole_columns.append(columns_text)

with open('waktusolat.csv', mode='w') as csvfile:
    writer = csv.writer(csvfile, delimiter='.', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    writer.writerow(headers)  # Write the headers to the CSV file
    for column_array in whole_columns:
        writer.writerow(column_array)  # Write each row of data to the CSV file
