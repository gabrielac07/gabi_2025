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

<p>This button takes you to a jupyter notebook about my interests:</p>
<button class="animated-button" onclick="window.location.href='http://127.0.0.1:4100/gabi_2025/interests/'">Click here</button><br><br>

<p>This button takes you to a game using a javascript cell:</p>
<button class="animated-button" onclick="window.location.href='http://127.0.0.1:4100/gabi_2025/game/'" >Play now</button> <br><br>

<p>This button takes you to a Notebook where I describe what I did:<p>
<button class="animated-button" onclick="window.location.href='http://127.0.0.1:4100/gabi_2025/process/'">Click here</button> <br><br>


<img src="https://media0.giphy.com/media/XuL4Zlq33sCTC/giphy.gif?cid=6c09b952roqx9x1uhiur86tdfrwrq0q7egmey7t2b4mz51p1&ep=v1_gifs_search&rid=giphy.gif&ct=s" alt="mario">









