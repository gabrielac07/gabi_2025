---
layout: page
title: Sprint 2 
permalink: /sprint2/
---
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Part 1 - Fundamentals</title>
    <style>
        nav ul {
            list-style-type: none;
            margin: 0;
            padding: 0;
            overflow: hidden;
            background-color: #15935d;
        }

        nav li {
            float: left;
            position: relative;
        }

        nav li a {
            display: block;
            color: white;
            text-align: center;
            padding: 14px 16px;
            text-decoration: none;
            transition: all 0.3s ease;
            font-weight: bold;
        }

        nav li a:hover {
            background-color: #155f91;
            transform: scale(1.1);
        }

        /* Submenu styling */
        nav ul ul {
            display: none;
            position: absolute;
            background-color: #155f91;
            top: 100%;
            left: 0;
            box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.2);
            opacity: 0;
            transition: opacity 0.3s ease, transform 0.3s ease;
        }

        /* Show submenu on hover */
        nav li:hover > ul {
            display: block;
            opacity: 1;
            transform: translateY(0px); /* Removed translateY(10px) */
        }

        nav ul ul li {
            float: none;
            position: relative;
        }

        nav ul ul a {
            padding: 10px 16px;
        }

        /* Add transition effect to submenu items */
        nav ul ul li a:hover {
            background-color: #15935d;
            transform: translateX(10px);
        }

    </style>
</head>

<body>
<nav>
    <ul>
        <li><a href="#">Sprint 2 Resources</a>
            <ul>
                <li><a href="https://nighthawkcoders.github.io/portfolio_2025/csp/big-idea/p3/fundamentals">Period 3 Lessons</a></li>
                <li><a href="https://docs.google.com/spreadsheets/d/1eHGWIXPmFyhhdkjCYhULZZxweWrCLLZLY0NlReUTi7c/edit?gid=0#gid=0">Period 3 Schedule</a></li>
                <li><a href="https://docs.google.com/spreadsheets/d/14h1omXeuwfE-chlK-InGmzPGwLkhnY1mPBVatxFL13c/edit?usp=sharing">3.2 Grades</a></li>
                <li><a href="https://nighthawkcoders.github.io/portfolio_2025/csse/javascript/fundamentals/for-loops/">JavaScript For Loops and Sprites</a></li>  
            </ul>
        </li>
        <li><a href="https://nighthawkcoders.github.io/portfolio_2025/csp/big-idea/p3/fundamentals">Sprint 2 Homework</a>
            <ul>
                <li><a href="https://gabrielac07.github.io/gabi_2025/hacks-3.1-3.4/">3.1 and 3.4</a></li>
                <li><a href="https://gabrielac07.github.io/gabi_2025/hacks-3.3-3.5/">3.3 and 3.5</a></li>
                <li><a href="https://gabrielac07.github.io/gabi_2025/hacks-3.6-3.7/">3.6 and 3.7</a></li>
                <li><a href="https://gabrielac07.github.io/gabi_2025/hacks-3.8/">3.8</a></li>
                <li><a href="https://gabrielac07.github.io/gabi_2025/hacks-3.10/">3.10</a></li>
                <li><a href="https://gabrielac07.github.io/gabi_2025/hacks-3.10/">3.10</a></li>
                <li><a href="https://gabrielac07.github.io/gabi_2025/hacks-final/">Final Hacks</a></li>
            </ul>
        </li>
    </ul>
</nav>

<h1>Part 1 - Fundamentals</h1>

<div class="container">
    <h2>This Unit Overview</h2>
    <p>In this unit, you will cover the foundational concepts of programming, which are crucial for understanding how to develop and think about algorithms and logic in coding. Here are the key topics:</p>

    <ul>
        <li><strong>3.1 Variables:</strong> Learn about variables, which are used to store data that can be reused and manipulated throughout the program.</li>
        <li><strong>3.2 Data Abstraction:</strong> Data abstraction involves using variables and data structures to manage and simplify the complexity of programs.</li>
        <li><strong>3.3 Mathematical Expressions:</strong> Understand how to use operators and expressions to perform calculations and manipulate data.</li>
        <li><strong>3.4 Strings:</strong> Learn about string data types and how to manipulate text within your programs.</li>
        <li><strong>3.5 Booleans:</strong> Dive into Boolean logic, which helps make decisions in your code using true or false values.</li>
        <li><strong>3.6 Conditionals:</strong> Explore conditionals, which allow your program to make decisions based on specific criteria.</li>
        <li><strong>3.7 Nested Conditionals:</strong> Learn how to use conditionals inside other conditionals to handle more complex decision-making.</li>
        <li><strong>3.8 Iteration:</strong> Understand loops and iteration, which allow for repetitive tasks to be automated and executed multiple times.</li>
        <li><strong>3.10 Lists:</strong> Study how to use lists (arrays) to store and manage collections of data within your program.</li>
    </ul>
</div>

</body>
</html>


<script src="https://utteranc.es/client.js"
        repo="nighthawkcoders/portfolio_2025"
        issue-term="title"
        label="blogpost-comment"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
