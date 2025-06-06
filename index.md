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
    <p>This site showcases my work with notebooks, projects, games, and reflections from the 2024-2025 school year. Click around and explore!</p>

    <h2>Virtual Business Card</h2>
  <img src="/images/frame.png" alt="Contact info" width="300px" height="200px">


    <h2>About</h2>
    <div class="button-grid">
      <a class="btn" href="/about">About Me</a>
      <a class="btn" href="https://github.com/gabrielac07" target="_blank">GitHub</a>
      <a class="btn" href="https://www.linkedin.com/in/gabriela-connelly-701687365" target="_blank">Linkedin</a>
      <a class="btn" href="https://cs-p-hq.slack.com/team/U07HRPRKQHL" target="_blank">Slack</a>
    </div>

    <h2>Explore My Work</h2>
    <div class="button-grid">
      <a class="btn" href="https://gabrielac07.github.io/gabi_2025/projects/">📁 Classwork & Projects</a>
      <a class="btn" href="https://gabrielac07.github.io/gabi_2025/my_interests/">💖 My Interests</a>
      <a class="btn" href="https://gabrielac07.github.io/gabi_2025/college_board/">🧠 College Board Content</a>
    </div>

    <div class="media">
      <img src="https://media0.giphy.com/media/XuL4Zlq33sCTC/giphy.gif?cid=6c09b952roqx9x1uhiur86tdfrwrq0q7egmey7t2b4mz51p1&ep=v1_gifs_search&rid=giphy.gif&ct=s" alt="mario">
  </section>

  <footer>
    <p>Made with 💻 by Gabrielac | © 2025</p>
  </footer>
</body>
</html>
