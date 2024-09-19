---
layout: page
title: Calculator
description: This calculator includes an exponent, square root, and percent feature. It also includes history.
permalink: /calculator/
---
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Binary Calculator</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background: linear-gradient(135deg, #667eea, #764ba2);
            font-family: 'Arial', sans-serif;
        }

        .calculator {
            background-color: #333;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
            max-width: 300px;
        }

        .display, .history {
            width: 100%;
            background-color: #222;
            color: white;
            text-align: right;
            font-size: 1.5rem;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 10px;
        }

        .history {
            font-size: 1rem;
            max-height: 150px;
            overflow-y: auto;
            text-align: left;
        }

        .buttons {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 10px;
        }

        button {
            width: 100%;
            padding: 15px;
            font-size: 1.5rem;
            border: none;
            border-radius: 10px;
            background-color: #444;
            color: white;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        button:hover {
            background-color: #555;
        }

        .operator {
            background-color: #ff7f50;
        }

        .operator:hover {
            background-color: #ff6347;
        }

        .equal {
            background-color: #4caf50;
        }

        .equal:hover {
            background-color: #45a049;
        }

        .clear {
            background-color: #f44336;
        }

        .clear:hover {
            background-color: #e53935;
        }
    </style>
</head>
<body>

    <div class="calculator">
        <div class="display" id="display">0</div>
        <div class="history" id="history"></div>
        <div class="buttons">
            <!-- Standard Numbers and Operators -->
            <button onclick="appendNumber('7')">7</button>
            <button onclick="appendNumber('8')">8</button>
            <button onclick="appendNumber('9')">9</button>
            <button class="operator" onclick="chooseOperation('/')">÷</button>

            <button onclick="appendNumber('4')">4</button>
            <button onclick="appendNumber('5')">5</button>
            <button onclick="appendNumber('6')">6</button>
            <button class="operator" onclick="chooseOperation('*')">×</button>

            <button onclick="appendNumber('1')">1</button>
            <button onclick="appendNumber('2')">2</button>
            <button onclick="appendNumber('3')">3</button>
            <button class="operator" onclick="chooseOperation('-')">−</button>

            <button onclick="appendNumber('0')">0</button>
            <button onclick="appendNumber('.')">.</button>
            <button class="equal" onclick="compute()">=</button>
            <button class="operator" onclick="chooseOperation('+')">+</button>

            <!-- Additional Operations -->
            <button class="operator" onclick="chooseOperation('^')">^</button>
            <button class="operator" onclick="chooseOperation('√')">√</button>
            <button class="operator" onclick="chooseOperation('%')">%</button>

            <button class="clear" style="grid-column: span 2;" onclick="clearDisplay()">C</button>
            <button class="clear" style="grid-column: span 2;" onclick="deleteNumber()">DEL</button>
        </div>
    </div>

    <script>
        let currentInput = '';
        let previousInput = '';
        let operation = null;
        let history = [];

        function appendNumber(number) {
            if (number === '.' && currentInput.includes('.')) return;
            currentInput = currentInput.toString() + number.toString();
            updateDisplay();
        }

        function updateDisplay() {
            document.getElementById('display').innerText = currentInput || '0';
        }

        function clearDisplay() {
            currentInput = '';
            previousInput = '';
            operation = null;
            updateDisplay();
        }

        function deleteNumber() {
            currentInput = currentInput.toString().slice(0, -1);
            updateDisplay();
        }

        function chooseOperation(op) {
            if (currentInput === '') return;
            if (previousInput !== '') {
                compute();
            }
            operation = op;
            previousInput = currentInput;
            currentInput = '';
        }

        function compute() {
            let result;
            const prev = parseFloat(previousInput);
            const current = parseFloat(currentInput);
            if (isNaN(prev) || isNaN(current) && operation !== '√') return;

            switch (operation) {
                case '+':
                    result = prev + current;
                    break;
                case '-':
                    result = prev - current;
                    break;
                case '*':
                    result = prev * current;
                    break;
                case '/':
                    result = prev / current;
                    break;
                case '^':
                    result = Math.pow(prev, current);
                    break;
                case '√':
                    result = Math.sqrt(prev);
                    break;
                case '%':
                    result = (prev * current) / 100;
                    break;
                default:
                    return;
            }
            
            addToHistory(`${previousInput} ${operation} ${currentInput || ''} = ${result}`);
            currentInput = result.toString(2); // Convert result to binary
            operation = null;
            previousInput = '';
            updateDisplay();
        }

        // Adding history entries
        function addToHistory(entry) {
            history.push(entry);
            let historyElement = document.getElementById('history');
            historyElement.innerHTML = history.join('<br>');
        }
    </script>

</body>
</html>
