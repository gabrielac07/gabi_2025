---
layout: page
title: Sprint 2 
permalink: /sprint2/
---
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
</body>
</html>