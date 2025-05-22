---
layout: base
title: Home 
description: Home Page
hide: true
---

<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Gabi’s GitHub Page</title>
  <style>
    body {
      
      font-family: 'Segoe UI', sans-serif;
      margin: 0;
      padding: 0;
      background: #f8f9fa;
      color: #333;
    }

    section {
      max-width: 900px;
      margin: 40px auto;
      padding: 0 20px;
    }

    h1, h2 {
      text-align: center;
      color: #155f91;
    }

    .button-grid {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 12px;
      margin: 16px 0;
    }

    .btn {
      background: linear-gradient(to right, #15935d, #155f91);
      border: none;
      padding: 12px 20px;
      border-radius: 10px;
      color: white;
      font-weight: bold;
      text-decoration: none;
      transition: transform 0.2s ease, background 0.3s ease;
      text-align: center;
    }

    .btn:hover {
      background: #147050;
      transform: scale(1.05);
    }

    .dropdown {
      position: relative;
      display: inline-block;
    }

    .dropdown-content {
      display: none;
      position: absolute;
      background-color: white;
      min-width: 200px;
      box-shadow: 0 4px 8px rgba(0,0,0,0.2);
      z-index: 1;
      border-radius: 10px;
      overflow: hidden;
    }

    .dropdown-content a {
      color: #155f91;
      padding: 12px 16px;
      display: block;
      text-decoration: none;
      font-weight: bold;
    }

    .dropdown-content a:hover {
      background-color: #f0f0f0;
    }

    .dropdown:hover .dropdown-content {
      display: block;
    }

    .dropdown .btn {
      cursor: pointer;
    }

    .media {
      display: flex;
      flex-direction: column;
      align-items: center;
      margin-top: 40px;
    }

    img {
      width: 280px;
      border-radius: 16px;
      box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
      transition: transform 0.3s ease;
    }

    img:hover {
      transform: scale(1.05);
    }

    iframe {
      margin-top: 20px;
      border-radius: 12px;
      width: 100%;
      max-width: 600px;
      height: 352px;
      box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    }

    footer {
      margin-top: 40px;
      text-align: center;
      font-size: 0.9rem;
      color: #555;
    }
  </style>
</head>

<body>
  <section>
    <h1>Welcome to Gabi’s GitHub Portfolio!</h1>
    <p>This site showcases my work with notebooks, projects, games, and reflections from the 2025 school year. Click around and explore!</p>

    <h2>About</h2>
    <div class="button-grid">
      <a class="btn" href="gabi_2025/about">About Me</a>
      <a class="btn" href="https://github.com/gabrielac07" target="_blank">My GitHub Profile</a>
    </div>

    <h2>Interests</h2>
    <div class="button-grid">
      <a class="btn" href="gabi_2025/brazil">Brazil</a>
      <a class="btn" href="gabi_2025/spaniels">Spaniels</a>
      <a class="btn" href="gabi_2025/tennis">Tennis</a>
      <a class="btn" href="gabi_2025/random">Random</a>
      <a class="btn" href="gabi_2025/interests">My Interests</a>
    </div>

    <h2>College Board – AP Computer Science Principles</h2>
    <div class="dropdown">
      <div class="btn">College Board Content ▼</div>
      <div class="dropdown-content">
        <a href="gabi_2025/base64">Base64</a>
        <a href="gabi_2025/2021_MCQ">2021 MCQ</a>
        <a href="gabi_2025/study">Study Blog</a>
        <a href="gabi_2025/big_idea1">Big Idea 1</a>
        <a href="gabi_2025/3.1_and_3.4_hacks">Big Idea 3.1 and 3.4</a>
        <a href="gabi_2025/3.3_and_3.5_hacks">Big Idea 3.3 and 3.5</a>
        <a href="gabi_2025/3.6_and_3.7_hacks">Big Idea 3.6 and 3.7</a>
        <a href="gabi_2025/3.10_hacks">Big Idea 3.10</a>
        <a href="gabi_2025/3.8_hacks">Big Idea 3.8</a>
        <a href="gabi_2025/ComputingBias">Computing Bias</a>
        <a href="gabi_2025/binary_search">Binary Search</a>
        <a href="gabi_2025/random">Simulations</a>
        <a href="gabi_2025/safe_computing">Safe Computing</a>
        <a href="gabi_2025/2018mcq">2018 MCQ</a>
        <a href="gabi_2025/PPR">PPR</a>
      </div>
    </div>

    <h2>Classwork and Projects</h2>
    <div class="dropdown">
      <div class="btn">Class Projects ▼</div>
      <div class="dropdown-content">
        <a href="gabi_2025/sprint2">Sprint 2</a>
        <a href="gabi_2025/final_hack">Sprint 2 Notebook</a>
        <a href="gabi_2025/sprint3">Sprint 3</a>
        <a href="gabi_2025/sprint4">Sprint 4</a>
        <a href="gabi_2025/tri3_blog">Tri 3 Blog</a>
        <a href="gabi_2025/cybersecurity">Cybersecurity Panel</a>
        <a href="gabi_2025/extra_credit_blog">CS Student Panel</a>
        <a href="gabi_2025/real_PPR">Real PPR</a>
        <a href="gabi_2025/final">Final Project</a>
        <a href="gabi_2025/calculator">Calculator</a>
        <a href="gabi_2025/counter">Counter</a>
        <a href="gabi_2025/snake">Snake Game</a>
        <a href="gabi_2025/tools">Tools</a>
        <a href="gabi_2025/process">GitHub Pages</a>
        <a href="gabi_2025/java">Coding with Java</a>
      </div>
    </div>

    <div class="media">
      <img src="https://media0.giphy.com/media/XuL4Zlq33sCTC/giphy.gif?cid=6c09b952roqx9x1uhiur86tdfrwrq0q7egmey7t2b4mz51p1&ep=v1_gifs_search&rid=giphy.gif&ct=s" alt="mario">
      <iframe src="https://open.spotify.com/embed/playlist/5XOGgDmdRe2CUHruz2l9TM?utm_source=generator&theme=0" frameBorder="0" allowfullscreen allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
    </div>
  </section>

  <footer>
    <p>Made with 💻 by Gabrielac | © 2025</p>
  </footer>
</body>
</html>
