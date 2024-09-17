---
layout: page
title: Click Counter
description: Click the button to get more money. Buy workers to automatically increase.
permalink: /counter/
---
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Button Click Game</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background: linear-gradient(135deg, #1e3c72, #2a5298);
            font-family: 'Arial', sans-serif;
            color: white;
        }
        
        .container {
            text-align: center;
            padding: 20px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
        }

        h1 {
            font-size: 2.5rem;
            margin-bottom: 20px;
            letter-spacing: 2px;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.4);
        }

        #countDisplay {
            font-size: 3rem;
            margin: 20px 0;
            font-weight: bold;
        }

        .click-btn {
            padding: 15px 30px;
            font-size: 1.5rem;
            background: linear-gradient(45deg, #ff416c, #ff4b2b);
            border: none;
            border-radius: 50px;
            color: white;
            cursor: pointer;
            transition: transform 0.3s, box-shadow 0.3s;
        }

        .click-btn:hover {
            transform: scale(1.1);
            box-shadow: 0 10px 20px rgba(255, 64, 108, 0.6);
        }

        .click-btn:active {
            transform: scale(1.05);
        }

        .reset-btn {
            margin-top: 20px;
            padding: 10px 20px;
            font-size: 1rem;
            background-color: #555;
            color: white;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            transition: background 0.3s ease;
        }

        .reset-btn:hover {
            background-color: #777;
        }

        .shop-item {
            margin-top: 20px;
            padding: 10px 20px;
            font-size: 1rem;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            transition: background 0.3s ease;
        }

        .shop-item:hover {
            background-color: #66BB6A;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Button Click Game with Shop</h1>
        <div id="countDisplay">0</div>
        <button class="click-btn" onclick="incrementCount()">Click Me!</button>
        <br />
        <button class="reset-btn" onclick="resetCount()">Reset</button>
        <br />
        <div>
            <button class="shop-item" onclick="buyWorker()">Buy Worker (Cost: 10)</button>
        </div>
        <p id="workerCount">Workers: 0</p>
    </div>

    <!-- Sound Effect for Click -->
    <audio id="clickSound">
        <source src="https://www.soundjay.com/button/sounds/button-16.mp3" type="audio/mp3">
    </audio>

    <script>
        let count = 0;
        let workers = 0;
        let workerCost = 10;
        let passiveIncrement = 0;

        // Sound effect for the button click
        const clickSound = document.getElementById("clickSound");

        // Function to increment the count when the button is clicked
        function incrementCount() {
            count++;
            document.getElementById('countDisplay').innerText = count;
            clickSound.play();  // Play sound on click
        }

        // Function to reset the count
        function resetCount() {
            count = 0;
            workers = 0;
            passiveIncrement = 0;
            document.getElementById('countDisplay').innerText = count;
            document.getElementById('workerCount').innerText = "Workers: 0";
        }

        // Function to buy a worker
        function buyWorker() {
            if (count >= workerCost) {
                workers++;
                count -= workerCost;
                passiveIncrement += 1;
                document.getElementById('workerCount').innerText = "Workers: " + workers;
                document.getElementById('countDisplay').innerText = count;
            } else {
                alert("Not enough clicks to buy a worker!");
            }
        }

        // Passive increment logic
        setInterval(function() {
            count += passiveIncrement;
            document.getElementById('countDisplay').innerText = count;
        }, 1000);  // Increment the count every second based on the number of workers
    </script>
</body>
</html>
