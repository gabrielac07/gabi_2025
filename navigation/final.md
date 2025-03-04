---
toc: true
layout: page
title: "Final Exam Retrospective"
permalink: /final/
---

## Table of Contents
* TOC
{:toc}

## About My Feature:
The feature that I worked on for the past few weeks is a reading list displayed on the profile. Users are able to add books to their list, and are able to mark each book as you progress through it. They are also able to see the date they added the book, and to check if the book is available to be checked out. You can also delete the book if you don't want it anymore. It gets the books from the main book database, and adds the books to the Wishlist table. It has all the CRUD operations, fulfills all the CB requirements, and API's that function properly on the deployed website.

# 5 things I accomplished over 12 Weeks:
- making a table within a database using Model
- learning how to use token_required and returning a list unique to each user
- using multiple API routes for my feature and testing them on Postman
- learning how to communicate on a team and how to enhance cohesion and unity
- the importance of planning with kanban boards, burn downs, etc.

[Kanban Board](https://github.com/users/gabrielac07/projects/2)
This kanban board helped our group get tasks done and check our progress.

[Burn Down](https://github.com/gabrielac07/bookworms/issues/2) 
This burn down was specific to my feature, and I added to it when I wanted to change something and checked things off when I completed them.

[Figma Board](https://www.figma.com/board/ffwEjQVQMWAX5a4YbyKMuW/Bookworms-planning?node-id=0-1&p=f)
This flowchart is one of our planning documents and it provides a visual so that our group understands how the code is supposed to function.

# N@tM Event + Feedback

![img](../images/natm_selfie.jpg)

At N@TM, I got to share with many students and parents our Bookworms website, and we were able to get some feedback on it. Overall, people agreed that our styling was good and our website was cohesive. The things we can work on are mostly formatting issues and improving our talk.

### Things we did well:

![img](../images/natm_positives.png)

### Things we could improve on:

![img](../images/natm_improvements.png)

### Other Projects:
I took an interest in two other CSP projects, including Michelle's group about travel places and Prajna's group about food.

I liked the website about traveling because it's a functional website that can be used in real life, and it had cool features such as recommended vacation spots that are good for travelers.

![img](../images/natm_places.jpg)

The project about food and food rating was interesting to me because it can display food from all around the world, and the user can provide their own review of it, similar to Yelp. I was also able to provide feedback on it and interact with their project.

![img](../images/natm_food.jpg)

![img](../images/natm_feedback.jpg)

# CPT requirements:

#### Input:
 The user enters the book they would like to read through a dropdown menu, and also edit their progress through the book.

Dropdown list of books:
```html
<label for="bookDropdown">Select a Book: </label>
<select id="bookDropdown">
  <option value="">--Choose a book--</option>
</select>
<button id="addToWishlistButton">Add to reading list</button>
```

Reading status dropdown:
```javascript
const statusDropdown = document.createElement('select');
['for later', 'in progress', 'finished'].forEach((status) => {
  const option = document.createElement('option');
  option.value = status;
  option.textContent = status;
  if (status === book.status) {
    option.selected = true;
  }
  statusDropdown.appendChild(option);
});
statusDropdown.onchange = () => {
  const newStatus = statusDropdown.value;
  const newAvailability = book.availability;
  updateBookInWishlist(book.id, newStatus, newAvailability);
};
```

#### List: 
I use a list of dictionaries to create a list of books that eventually get displayed in the dropdown menu.

```python
    books_list = [{'id': book.id, 'title': book.title, 'author': book.author} for book in books]
```
 #### Sequencing: 
 My code uses sequencing because the code executes line by line, importing modules, defining the blueprint, and declaring routes

 ```python
 # Create a Blueprint for the wishlist functionality
wishlist_api = Blueprint('wishlist_api', __name__, url_prefix='/api/wishlist')
```

#### Selection: 
I include if statements that handle conditions, such as JSON requests in the function `add_book_to_wishlist`

```python
if not book_id:
    return jsonify({"error": "Missing book_id"}), 400
```

#### Iteration: 
This is present in `get_user_wishlist` where the code loops over each item and appends it to `books_in_wishlist`

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
#### Calls to procedure: 
The function `get_wishlist` is called in the `get_user_wishlist` route. It retrieves all the books in their reading list by passing their _uid.

```python
wishlist_items = get_wishlist(current_user._uid)
```

#### Output:
I have conditional output that is based off of selection. It adjusts the JSON output depending on the request:

```python
if wishlist_item:
    return jsonify({"availability": wishlist_item.availability}), 200
else:
    return jsonify({"error": "Book not found in wishlist"}), 404
```

# College Board MC:
#### Score: 61/67
[Download PDF](../images/mc_topics.pdf)

## Questions I got wrong:

![img](../images/mc_results.png)

## My first MC:

![img](../images/mc_1.png)

### Topics I had trouble with:
This time was mostly unit 3, but also 2 and 5. This means that I need to focus on:
- 2.3: Extracting Information from Data
- 3.7: Nested Conditionals
- 3.11: Binary Search
- 3.17: Algorithmic Efficiency
- 5.6: Safe Computing

### Questions I missed in both MC's:
- algorithm efficiency and runtime
- comparing code sets and algorithms

### Things that I improved on:
- NAND logic gates
- completing code and using if statements
- citizen science

## Longest Questions:

![img](../images/mc_time.png)

The types of questions that took me the longest were mostly topic 3, which is algorithms and programming. Most of these took longer because they are more complex and require a lot of thinking, but I need to work on being more efficient with my time. A couple questions I got wrong and they took me a long time, which means I need to review them more. This topic is data selection, which is about constraints and limits of a certain program.

## Quiz Corrections:
### Question 15: Consider the two programs below. The figure presents two programs, labeled Program A and Program B, each with two blocks of code that consist of 4 lines. Throughout the second block of code in each program there are nested blocks of code, as follows. 
Which of the following best compares the values displayed by programs A and B?
My answer: Program A and program B display the same number of values, but the values differ.
Correct answer: Program A and program B display identical values in the same order.
Explanation: The two programs aren't in the same order, but they both display the numbers from 1-10. 

### Question 21: Which of the following observations is most consistent with the information in the circle graph?
My answer: Over 75% of the files stored are at least 100 KB in size.
Correct answer: Over 75% of the files stored are 10 MB in size or less.
Explanation: The files at least 100 KB are only 59%, while the files up to 10 MB are 76%.

### Question 30: In the following program, assume that the variable n has been initialized with an integer value. The figure presents 2 blocks of code that consist of 14 total lines. Throughout the code there are nested blocks of code. Which of the following is NOT a possible value displayed by the program?
My answer: too low
Correct answer: out of range
Explanation: Correct. The string "out of range" could only be displayed if the condition n ≥ 1 was false. If the initial value of n is at least 0, then n will be incremented by 1, making n at least 1. Therefore the condition n ≥ 1 will be true and "out of range" will not be displayed. If the initial value of n is negative, then n will be multiplied by -1, making n at least 1. Therefore the condition n ≥ 1 will be true and "out of range" will not be displayed.

### Question 40: Which of the following best explains how a certificate authority is used in protecting data?
My answer: A certificate authority certifies the safety of a particular Web site so that users know that it does not contain any viruses.
Correct answer: A certificate authority verifies the authenticity of encryption keys used in secured communications.
Explanation: Certificate authorities issue digital certificates that certify the ownership of public keys.

### Question 47: The procedure BinarySearch (`numList`, `target`) correctly implements a binary search algorithm on the list of numbers `numList`. The procedure returns an index where `target` occurs in `numList`, or -1 if target does not occur in `numList`. Which of the following conditions must be met in order for the procedure to work as intended?
My answer: The list `numList` must not contain any duplicate values
Correct answer: The values in `numList` must be in sorted order.
Explanation: Correct. In order for a binary search on a list to work as intended, the list must be sorted.

### Question 50: Consider the following algorithms. Each algorithm operates on a list containing n elements, where n is a very large integer.
1. . An algorithm that accesses each element in the list twice
2. An algorithm that accesses each element in the list n times
3. An algorithm that accesses only the first 10 elements in the list, regardless of the size of the list
### Which of the algorithms run in reasonable time?
My answer: 3 only
Correct answer: 1, 2, and 3
Explanation: for an algorithm to run in reasonable sum, it has to take a number of steps less than or equal to a polynomial function. 1 accesses elements 2n times, 2 accesses n^2 times, and 3 accesses 10 elements.


# Self-Grading

| **Topic**                                                                 | **Grade** | **Explanation**                                                                                                                                                                                                                                         | **Total** |
|---------------------------------------------------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| 5 things you did over 12 weeks, Issues, burndown, presentation            | 5/5     | I have 5 distinct things I learned over the trimester, including proof of burndown lists and planning.                                                                                                         | 4.5     |
| Full Stack Project Demo, including CPT requirement highlights, and N@tM feedback | 2/2       | My project works full stack, with all CRUD operations and CPT requirements clearly demonstrated and explained well. I went to N@tM and received helpful feedback, as well as taking interest in other groups. | 2       |
| Project Feature blog write-up, using CPT/FRQ language                     | 0.95/1    | I wrote about the function of my project feature, as well as how it meets the CPT requirements for College Board. One thing I could've done was use a bit more programming language in my explanation.      | 0.95    |
| MCQ                                                                       | 1/1       | I did a good job of understanding the questions I got wrong and correcting them, as well as analyzing weaker topics and questions that took longer, which is helpful when studying for the exam.              | 1       |
| 10th point                                                                | 0.5/1     | I took interest in N@tM projects and blogged about them, as well as practicing with a new person. I also sent a summary of my talking points a day in advance and had a self-scoring rubric, but I didn't reflect on my strengths and weaknesses or think about my next steps. | 0.5     |
| **Total**                                                                 | **9/10** |                                                                                                                                                                                                                 | **8.95** |
