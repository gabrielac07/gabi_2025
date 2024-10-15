---
layout: page
title: Sprint 2 
permalink: /sprint2/
---
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Big Idea 3: Algorithms and Programming</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f4f4f4;
        }
        h1 {
            color: #2c3e50;
            text-align: center;
        }
        h2 {
            color: #2980b9;
        }
        p {
            font-size: 1.1em;
            line-height: 1.6;
        }
        ul {
            list-style-type: square;
        }
        li {
            margin-bottom: 10px;
        }
        .container {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Big Idea 3: Algorithms and Programming</h1>
        
        <h2>1. Algorithm Design and Analysis</h2>
        <p>
            <strong>Definition:</strong> An algorithm is a precise, step-by-step procedure for solving a problem.
        </p>
        <p>
            <strong>Importance:</strong> Algorithms form the backbone of programming and computational problem-solving.
        </p>
        <p>
            <strong>Efficiency:</strong> Students evaluate algorithms' efficiency, often considering time and space complexity.
        </p>

        <h2>2. Developing Programs</h2>
        <p>
            <strong>Abstraction:</strong> Abstraction simplifies problems by focusing on essential aspects and breaking down complexity.
        </p>
        <p>
            <strong>Program Development:</strong> Students write clear, correct, and efficient programs using different languages and tools.
        </p>
        <p>
            <strong>Documentation:</strong> Effective documentation ensures code is understandable and maintainable.
        </p>

        <h2>3. Programming Concepts</h2>
        <ul>
            <li><strong>Control Structures:</strong> Conditional statements (if-else), loops, and functions allow dynamic, responsive programs.</li>
            <li><strong>Variables and Data Types:</strong> Understanding variables to store data and using different data types (integers, strings, lists, etc.).</li>
            <li><strong>Modularity:</strong> Functions and procedures promote reusable, modular code for complex problem-solving.</li>
        </ul>

        <h2>4. Testing and Debugging</h2>
        <p>
            Students use techniques to test and debug programs, ensuring they work correctly under various conditions. Iterative development and debugging cycles are key for refining solutions.
        </p>

        <h2>5. Impact of Programming</h2>
        <p>
            Programming allows for creative problem-solving and innovation across industries like healthcare, education, and entertainment.
        </p>
        <p>
            Ethical considerations are discussed, emphasizing responsible programming and the societal implications of algorithms.
        </p>
    </div>
</body>
</html>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sprint 2</title>
    <style>
        nav ul {
            list-style-type: none;
            margin: 0;
            padding: 0;
            overflow: hidden;
            background-color: #15935d;
            position: relative;
            z-index: 100;
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

        /* Submenu CSS */
        nav ul ul {
            display: none;
            position: absolute;
            background-color: #155f91;
            top: 100%;
            left: 0;
            box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.2);
            opacity: 0;
            transition: all 0.3s ease;
        }

        nav ul li:hover > ul {
            display: block;
            opacity: 1;
            transform: translateY(10px);
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

        /* Adding hover effects and shadow to GIF */
        img {
            transition: transform 0.3s ease;
            border-radius: 12px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        }

        img:hover {
            transform: scale(1.05);
        }

        /* Spotify iframe effects */
        iframe {
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }

        iframe:hover {
            transform: scale(1.03);
        }

        /* Adding a cool hover effect for menu links */
        nav li a:before {
            content: '';
            position: absolute;
            width: 100%;
            height: 4px;
            background-color: white;
            bottom: 0;
            left: 0;
            transform: scaleX(0);
            transform-origin: bottom right;
            transition: transform 0.3s ease-out;
        }

        nav li a:hover:before {
            transform: scaleX(1);
            transform-origin: bottom left;
        }

    </style>
</head>
<body>

<nav>
    <ul>
        <li><a href="https://nighthawkcoders.github.io/portfolio_2025/csp/big-idea/p3/fundamentals">Sprint 2 Resources</a>
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

<br><br><br>


</body>
</html>