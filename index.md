---
layout: base
title: Home 
description: Home Page
hide: true
---
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My GitHub Page</title>
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
        <li><a href="#">Notebooks</a>        
            <ul>
                <li><a href="http://127.0.0.1:4100/gabi_2025/interests/">My interests</a></li>
                <li><a href="http://127.0.0.1:4100/gabi_2025/process/">Sprint 1 Summary</a></li>
                <li><a href="http://127.0.0.1:4100/gabi_2025/java_cell/">Java Cell</a></li>
            </ul>
        <li><a href="#">Games</a>
            <ul>
                <li><a href="http://127.0.0.1:4100/gabi_2025/counter/">Cookie Counter</a></li>
                <li><a href="http://127.0.0.1:4100/gabi_2025/calculator/">Binary Calculator</a></li>
                <li><a href="http://127.0.0.1:4100/gabi_2025/snake/">Snake Game</a></li>
            </ul>
        </li>
        <li><a href="https://gabrielac07.github.io/gabi_2025/sprint2/">Big Idea 3</a>
        </li>
         </li>
        <li><a href="https://gabrielac07.github.io/gabi_2025/sprint3/">Sprint 3</a>
        </li>
         <li><a href="https://gabrielac07.github.io/gabi_2025/2018_MCQ/">AP Classroom 2018 MCQ</a>
        </li>
        <li><a href="https://gabrielac07.github.io/gabi_2025/extra_credit/">Student Panel Extra Credit</a>
        </li>
        <li><a href="https://gabrielac07.github.io/gabi_2025/sprint4_PPR/">Sprint 4 PPR</a>
        </li>
        <li><a href="https://gabrielac07.github.io/gabi_2025/big_idea1/">Big Idea 1</a>
        </li>
        <li><a href="https://gabrielac07.github.io/gabi_2025/final/">Final Retrospective</a>
        </li>
    </ul>
</nav>

<br><br><br>
<img src="https://media0.giphy.com/media/XuL4Zlq33sCTC/giphy.gif?cid=6c09b952roqx9x1uhiur86tdfrwrq0q7egmey7t2b4mz51p1&ep=v1_gifs_search&rid=giphy.gif&ct=s" alt="mario">

<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/5XOGgDmdRe2CUHruz2l9TM?utm_source=generator&theme=0" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>

</body>
</html>
