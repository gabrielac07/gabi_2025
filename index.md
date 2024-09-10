---
layout: base
title: Home 
description: Home Page
hide: true
---
<style>
  .animated-button {
    background-color: #155f91; 
    color: white;
    border: none;
    border-radius: 25px;
    padding: 12px 24px;
    font-size: 16px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
    transition: color 0.6s, background-color 0.4s; /* Add transition for background-color */
  }

  .animated-button::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 300%;
    height: 300%;
    background: rgba(21, 97, 143, 0.3);
    transition: width 0.4s, height 0.4s, top 0.4s, left 0.4s;
    border-radius: 50%;
    z-index: 0;
    transform: translate(-50%, -50%);
  }

  .animated-button:hover::before {
    width: 0;
    height: 0;
    top: 50%;
    left: 50%;
  }

  .animated-button:hover {
    color: white; 
    background-color: #15935d;
  }

  .animated-button span {
    position: relative;
    z-index: 1;
  }
</style>


<p>This button takes you to my partner's Github Page:</p>
<button class="animated-button" onclick="window.location.href='https://jowan3.github.io/Jowan_2025'">Jowan's page</button><br><br>

<p>This button lets you learn about my favorite sport, tennis:</p>
<button class="animated-button" onclick="window.location.href='http://127.0.0.1:4100/gabi_2025/tennis/'">Tennis</button><br><br>

<p>This button lets you learn about one of my favorite places to travel to:</p>
<button class="animated-button" onclick="window.location.href='http://127.0.0.1:4100/gabi_2025/brazil/'">Brazil</button> <br><br>

<p>This button takes you to learn about a dog breed:<p>
<button class="animated-button" onclick="window.location.href='http://127.0.0.1:4100/gabi_2025/spaniels/'">English Cocker Spaniels</button> <br><br>

<img src="https://media0.giphy.com/media/XuL4Zlq33sCTC/giphy.gif?cid=6c09b952roqx9x1uhiur86tdfrwrq0q7egmey7t2b4mz51p1&ep=v1_gifs_search&rid=giphy.gif&ct=s" alt="mario">


<br><br>







