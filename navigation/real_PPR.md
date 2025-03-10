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
- Implements an algorithm with Sequencing, Selection, and Iteration.

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

ii. Here, the `get_user_wishlist()` function is called whenever a user makes a GET request to the /api/wishlist/ endpoint.

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

i. The `books_list` variable stores all books retrieved from the database.

```python
@wishlist_api.route('/books', methods=['GET'])
def get_books():
    """Retrieve all books from the database to display in a dropdown menu."""
    books = Book.query.all()  # Retrieves all books from the database
    books_list = [{'id': book.id, 'title': book.title, 'author': book.author} for book in books]
    return jsonify(books_list)
```

ii. The `books_in_wishlist` list is created by iterating over the wishlist_items and appending books to the list.

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