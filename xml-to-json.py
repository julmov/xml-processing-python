import xml.etree.ElementTree as ET
import json

# Parse the XML file
tree = ET.parse('books.xml')
root = tree.getroot()

# Create a list to store book data
books = []

# Loop through each book element and extract details
for book in root.findall('book'):
    # Get the category attribute of the book
    category = book.get('category')
    
    # Extract the details for each book
    title = book.find('title').text
    author = book.find('author').text
    genre = book.find('genre').text
    price = float(book.find('price').text)  # Convert price to float
    publish_date = book.find('publish_date').text
    lang = book.find('title').get('lang')  # Extract the 'lang' attribute from 'title'
    
    # Add book details to the list as a dictionary
    books.append({
        'category': category,
        'title': {
            'name': title,
            'lang': lang
        },
        'author': author,
        'genre': genre,
        'price': price,
        'publish_date': publish_date
    })

# Convert the list of books to JSON format
books_json = json.dumps(books, indent=4)

# Output the JSON data (you can also write it to a file)
print(books_json)

# Optional: Write the JSON data to a file
with open('books.json', 'w') as json_file:
    json_file.write(books_json)
