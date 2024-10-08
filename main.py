import xml.etree.ElementTree as ET

# Load the XML data from the file
tree = ET.parse('books.xml')
root = tree.getroot()

# Print the root element tag (i.e., 'bookstore')
print(f"Root tag: {root.tag}")

# Loop through each 'book' element
for book in root.findall('book'):
    # Get the category attribute of the book
    category = book.get('category')
    
    # Find and extract the details of each book
    title = book.find('title').text
    author = book.find('author').text
    genre = book.find('genre').text
    price = book.find('price').text
    publish_date = book.find('publish_date').text
    lang = book.find('title').get('lang')  # Extract the 'lang' attribute from the 'title' element

    # Print book details
    print("\nBook Details:")
    print(f"Category: {category}")
    print(f"Title: {title} (Language: {lang})")
    print(f"Author: {author}")
    print(f"Genre: {genre}")
    print(f"Price: ${price}")
    print(f"Publish Date: {publish_date}")
