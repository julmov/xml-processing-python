import json

# Open and load the JSON data from the file
with open('books.json', 'r') as json_file:
    books_data = json.load(json_file)

# Print the entire JSON data to see the structure
print("All Books Data:")
print(json.dumps(books_data, indent=4))

# Loop through each book and print details
for book in books_data:
    category = book['category']
    title = book['title']['name']
    author = book['author']
    genre = book['genre']
    price = book['price']
    publish_date = book['publish_date']
    lang = book['title']['lang']

    # Print book details
    print("\nBook Details:")
    print(f"Category: {category}")
    print(f"Title: {title} (Language: {lang})")
    print(f"Author: {author}")
    print(f"Genre: {genre}")
    print(f"Price: ${price}")
    print(f"Publish Date: {publish_date}")
