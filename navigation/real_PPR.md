---
layout: page
title: Personalized Project Reference
permalink: /real_PPR/
---

## Procedure:
Capture and paste two program code segments you developed during the administration of this task that contain a student-developed procedure that implements an algorithm used in your program and a call to that procedure.

### i. The first program code segment must be a student-developed procedure that:
- Defines the procedure's name and return type (if necessary)
- Contains and uses one or more parameters that have an effect on the functionality of the procedure
- Implements an algorithm that includes sequencing, selection, and iteration

### ii. The second program code segment must show where your student-developed procedure is being called in your program.

i. This is the `get_user_wishlist()` function. It:
- Defines a procedure named `get_user_wishlist()` with a return type of JSON.
- Uses the current_user parameter indirectly via `g.current_user` for user-specific access.
- Implements an algorithm with Sequencing, Selection, and Iteration to retrieve and format the user's wishlist items.

**Sequencing:** The function executes a series of steps in a specific order, starting with fetching the current user and their wishlist items, then iterating over each item to retrieve the corresponding book details, and finally appending the formatted book details to the `books_in_wishlist` list.

**Selection:** The function uses an `if` statement to check if a book exists for each wishlist item. If the book exists, it is added to the `books_in_wishlist` list.

**Iteration:** The function uses a `for` loop to iterate over each item in the `wishlist_items` list, processing each item to retrieve and format the book details.

```python
@wishlist_api.route('/', methods=['GET'])
@token_required()
def get_user_wishlist():
    """Retrieve all books in the user's wishlist."""
    current_user = g.current_user
    wishlist_items = get_wishlist(current_user._uid)  # Fetch all wishlist entries for the current user
    books_in_wishlist = []
    for item in wishlist_items:
        book = Book.query.get(item.book_id)
        if book:  # Selection
            books_in_wishlist.append({
                'id': item.id,
                'book_id': book.id,
                'title': book.title,
                'author': book.author,
                'status': item.status,
                'date_added': item.date_added.strftime('%Y-%m-%d'),  # Format date to exclude time
                'availability': item.availability
            })  # Sequencing & Iteration
    return jsonify(books_in_wishlist)
```

ii. This code segment shows the `get_user_wishlist()` function being called whenever a user makes a GET request to the /api/wishlist/ endpoint. The function is decorated with `@wishlist_api.route` and `@token_required` to ensure it is properly routed and secured.

```python
@wishlist_api.route('/', methods=['GET'])
@token_required()
def get_user_wishlist():
    # ...existing code...
```

## List:
Capture and paste two program code segments you developed during the administration of this task that contain a list (or other collection type) being used to manage complexity in your program.

### i. The first program code segment must show how data have been stored in the list.

### ii. The second program code segment must show the data in the same list being used, such as creating new data from the existing data or accessing multiple elements in the list, as part of fulfilling the program's purpose.

i. This code segment shows the `books_list` variable storing all books retrieved from the database. The books are stored as dictionaries in a list, each containing the book's id, title, and author.

```python
@wishlist_api.route('/books', methods=['GET'])
def get_books():
    """Retrieve all books from the database to display in a dropdown menu."""
    books = Book.query.all()  # Retrieves all books from the database
    books_list = [{'id': book.id, 'title': book.title, 'author': book.author} for book in books]
    return jsonify(books_list)
```

ii. This code segment shows the `books_in_wishlist` list being created by iterating over the `wishlist_items` and appending books to the list. Each book is retrieved from the database and added to the list as a dictionary containing the book's details.

```python
books_in_wishlist = []
for item in wishlist_items:
    book = Book.query.get(item.book_id)
    if book:
        books_in_wishlist.append({
            'id': item.id,
            'book_id': book.id,
            'title': book.title,
            'author': book.author,
            'status': item.status,
            'date_added': item.date_added.strftime('%Y-%m-%d'),
            'availability': item.availability
        })
```

## Comments

<div id="utterances-comments"></div>
<script src="https://utteranc.es/client.js"
        repo="gabrielac07/gabi_2025"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>