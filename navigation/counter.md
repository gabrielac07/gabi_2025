---
layout: page
title: Cookie Counter
description: Click the button to get more cookies. Buy workers to automatically increase.
permalink: /counter/
---
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cookie Clicker</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background-color: #f0f0f0;
            margin-top: 50px;
        }

        .game-container {
            background-color: #fff;
            padding: 20px;
            border-radius: 10px;
            width: 300px;
            margin: auto;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }

        button {
            padding: 10px 20px;
            font-size: 18px;
            cursor: pointer;
        }

        #cookie-button {
            font-size: 24px;
        }

        .shop {
            margin-top: 20px;
        }

        p {
            font-size: 18px;
        }
    </style>
</head>
<body>
    <div class="game-container">
        <h1>Cookie Clicker</h1>
        
        <!-- Cookie button -->
        <button id="cookie-button">
            <img src="../images/cookie.png" alt="Cookie">
        </button>
        
        <!-- Display for the cookie count -->
        <p>Cookies: <span id="cookie-count">0</span></p>

        <!-- Shop to buy workers -->
        <div class="shop">
            <h2>Shop</h2>
            <button id="buy-worker">Buy Worker (Cost: 10 Cookies)</button>
            <p>Workers: <span id="worker-count">0</span></p>
        </div>
    </div>

    <!-- Audio for clicking sound -->
    <audio id="click-sound" preload="auto">
        <source src="../navigation/click-sound.mp3" type="audio/mpeg">
        Your browser does not support the audio element.
    </audio>

    <script>
        // Variables
        let cookieCount = 0;
        let workerCount = 0;
        let workerCost = 10;
        let cookiesPerSecond = 0;

        // DOM Elements
        const cookieButton = document.getElementById('cookie-button');
        const cookieCountDisplay = document.getElementById('cookie-count');
        const workerCountDisplay = document.getElementById('worker-count');
        const buyWorkerButton = document.getElementById('buy-worker');
        const clickSound = document.getElementById('click-sound');

        // Cookie click event
        cookieButton.addEventListener('click', () => {
            cookieCount++;
            cookieCountDisplay.innerText = cookieCount;

            // Play click sound
            clickSound.currentTime = 0; // Reset sound to start
            clickSound.play();
        });

        // Buy worker event
        buyWorkerButton.addEventListener('click', () => {
            if (cookieCount >= workerCost) {
                workerCount++;
                cookieCount -= workerCost;
                workerCost = Math.floor(workerCost * 1.15); // Increase cost progressively

                // Update displays
                cookieCountDisplay.innerText = cookieCount;
                workerCountDisplay.innerText = workerCount;

                // Increase passive cookie production
                cookiesPerSecond += 1;

                // Update button text with new worker cost
                buyWorkerButton.innerText = `Buy Worker (Cost: ${workerCost} Cookies)`;
            }
        });

        // Passive cookie generation from workers
        setInterval(() => {
            cookieCount += cookiesPerSecond;
            cookieCountDisplay.innerText = cookieCount;
        }, 1000);
    </script>
</body>
</html>
