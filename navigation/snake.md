---
layout: page
title: Snake
description: Move the arrow keys to move the snake and eat the apples.
permalink: /snake/
---
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Snake Game</title>
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
        }

        canvas {
            background-color: #333;
            display: block;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
            border-radius: 10px;
        }

        h1 {
            position: absolute;
            top: 20px;
            color: white;
            font-size: 2rem;
        }
    </style>
</head>
<body>

    <h1>Snake Game</h1>
    <canvas id="gameCanvas" width="400" height="400"></canvas>

    <script>
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');

        const box = 20;
        let snake = [{ x: 9 * box, y: 10 * box }];
        let food = {
            x: Math.floor(Math.random() * 19 + 1) * box,
            y: Math.floor(Math.random() * 19 + 1) * box
        };
        let score = 0;
        let d;

        document.addEventListener("keydown", direction);

        function direction(event) {
            if (event.keyCode === 37 && d !== "RIGHT") {
                d = "LEFT";
            } else if (event.keyCode === 38 && d !== "DOWN") {
                d = "UP";
            } else if (event.keyCode === 39 && d !== "LEFT") {
                d = "RIGHT";
            } else if (event.keyCode === 40 && d !== "UP") {
                d = "DOWN";
            }
        }

        function collision(head, array) {
            for (let i = 0; i < array.length; i++) {
                if (head.x === array[i].x && head.y === array[i].y) {
                    return true;
                }
            }
            return false;
        }

        function draw() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            // Draw Snake
            for (let i = 0; i < snake.length; i++) {
                ctx.fillStyle = (i === 0) ? "#4caf50" : "#76ff03";
                ctx.fillRect(snake[i].x, snake[i].y, box, box);

                ctx.strokeStyle = "#2a5298";
                ctx.strokeRect(snake[i].x, snake[i].y, box, box);
            }

            // Draw Food
            ctx.fillStyle = "#ff5722";
            ctx.fillRect(food.x, food.y, box, box);

            // Move Snake
            let snakeX = snake[0].x;
            let snakeY = snake[0].y;

            if (d === "LEFT") snakeX -= box;
            if (d === "UP") snakeY -= box;
            if (d === "RIGHT") snakeX += box;
            if (d === "DOWN") snakeY += box;

            // Snake eats the food
            if (snakeX === food.x && snakeY === food.y) {
                score++;
                food = {
                    x: Math.floor(Math.random() * 19 + 1) * box,
                    y: Math.floor(Math.random() * 19 + 1) * box
                };
            } else {
                snake.pop();
            }

            let newHead = { x: snakeX, y: snakeY };

            // Game Over
            if (
                snakeX < 0 || snakeX >= canvas.width ||
                snakeY < 0 || snakeY >= canvas.height ||
                collision(newHead, snake)
            ) {
                clearInterval(game);
                alert("Game Over! Your score: " + score);
                location.reload();
            }

            snake.unshift(newHead);

            // Display score
            ctx.fillStyle = "white";
            ctx.font = "20px Arial";
            ctx.fillText("Score: " + score, box, 1.5 * box);
        }

        let game = setInterval(draw, 100);
    </script>

</body>
</html>
