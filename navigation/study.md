---
layout: page
title: Personal Study Blog
author: Gabriela Connelly
permalink: /study/
---

# Big Ideas Summary + Study Blog
---

## Big Idea 5: Impact of Computing

### Beneficial vs Harmful Effects
- **Beneficial effects** can include:
  - Improved communication and access to information
  - Increased efficiency in tasks through automation
  - Medical advancements like telehealth and diagnostics
- **Harmful effects** can include:
  - Loss of privacy and data breaches
  - Spread of misinformation and fake news
  - Negative mental health effects from social media use
- Impacts can vary based on:
  - The user’s perspective
  - How a computing innovation is used
  - Long-term vs short-term outcomes

---

### Digital Divide
- Refers to unequal access to technology and the internet
- Factors contributing to the divide:
  - Socioeconomic status
  - Geographic location (e.g., rural vs urban)
  - Age, education level, and infrastructure availability
- Consequences:
  - Reduced educational and career opportunities
  - Limited access to vital services and information
- Solutions:
  - Expanding broadband access
  - Providing affordable devices
  - Digital literacy programs

---

### Computing Bias
- Occurs when algorithms or systems reflect human biases
- Causes:
  - Biased data used to train models
  - Lack of diversity in developer teams
  - Poor testing across user groups
- Real-world examples:
  - Facial recognition misidentifying people of color
  - Hiring algorithms favoring certain demographics
- Mitigation:
  - Diverse development teams
  - Transparent design/testing practices
  - Regular audits for bias

---

### Crowdsourcing
- Collecting data or ideas from a large online group
- Examples:
  - Wikipedia (collaborative knowledge base)
  - Foldit (protein folding game contributing to science)
  - Traffic apps like Waze
- Benefits:
  - Scalable and cost-effective
  - Taps into collective intelligence
- Challenges:
  - Data quality and reliability
  - Managing large-scale participation

---

### Legal and Ethical Concerns
- **Legal issues**:
  - Copyright and intellectual property
  - Data protection laws (e.g., GDPR)
  - Hacking and cybercrime
- **Ethical issues**:
  - Privacy and surveillance
  - AI decision-making without human oversight
  - Misuse of personal data for profit
- Importance of ethical computing:
  - Creating technology that benefits all users fairly
  - Holding developers and companies accountable

---

### Safe Computing
- Best practices for protecting devices and personal information:
  - Use strong, unique passwords and a password manager
  - Enable two-factor authentication
  - Avoid suspicious links and attachments
  - Keep software and devices updated
  - Use secure networks (avoid public Wi-Fi for sensitive tasks)
- Cybersecurity threats to watch for:
  - Phishing, malware, ransomware, identity theft

---

## Big Idea 3: Algorithms and Programming

### Binary Search Algorithm
- Searches for a target value in a **sorted list**
- Process:
  - Check the middle value
  - If it's the target, you're done
  - If target is smaller, search the left half
  - If target is larger, search the right half
- Time complexity: **O(log n)**
- Requirements:
  - List must be **sorted**
- More efficient than linear search for large datasets

---

### Lists and Filtering Algorithm
- **Lists**: Data structures used to store ordered collections (arrays)
- **Filtering**:
  - Creating a new list by selecting items that meet certain conditions
  - Example: filtering a list of temperatures for values > 90°F
- Common operations:
  - Traversing the list with loops
  - Using conditionals (`if` statements) to apply filters
- Useful in data analysis, UI rendering, game states, etc.

---

### Simulation, Games, and Random Algorithms
- **Simulations**:
  - Imitate real-world processes (e.g., climate models, traffic flow)
  - Help analyze outcomes without real-world testing
- **Games**:
  - Use simulations to model physics or decision-making
- **Random algorithms**:
  - Introduce unpredictability (e.g., dice roll in games)
  - Used in:
    - Password generation
    - AI behavior
    - Sampling techniques
- Benefits:
  - Test a range of possibilities
  - Add variability and realism

---

### Big O and Algorithm Efficiency
- **Big O notation** describes how the runtime of an algorithm scales with input size:
  - **O(1)** – Constant time (e.g., accessing a list element by index)
  - **O(n)** – Linear time (e.g., looping through a list)
  - **O(log n)** – Logarithmic time (e.g., binary search)
  - **O(n²)** – Quadratic time (e.g., nested loops)
- Importance:
  - Helps determine if an algorithm is practical for large datasets
  - Affects speed, memory use, and scalability
- Trade-offs:
  - Sometimes faster algorithms are more complex to implement
  - Choosing the right algorithm is essential for performance

---

### Undecidable Problems
- **Definition**: Problems for which no algorithm can determine the answer for all possible inputs.
- **Classic example**: The Halting Problem—determining whether an arbitrary program will finish running or loop forever.
- **Implications**:
  - Sets a boundary on what computers can solve.
  - Guides us toward approximation or domain-specific solutions.
- **Approaches when confronted with undecidability**:
  - Restrict the problem domain (e.g., only consider programs of a certain form).
  - Use semi-decision procedures that may run forever on “no” instances but halt on “yes.”

---

### Graphs and Graph Algorithms
- **Graphs**: Data structures composed of **vertices (nodes)** and **edges (connections)**.
  - Can be **directed** (edges have direction) or **undirected**.
  - Weighted vs. unweighted edges.
- **Common algorithms**:
  - **Breadth-First Search (BFS)**  
    - Explores neighbors level by level.  
    - Finds shortest path in unweighted graphs.  
    - Complexity: O(V + E).
  - **Depth-First Search (DFS)**  
    - Explores as far as possible along each branch before backtracking.  
    - Useful for cycle detection and topological sorting.  
    - Complexity: O(V + E).
  - **Dijkstra’s Algorithm**  
    - Finds shortest paths from a source to all nodes in a weighted graph (non-negative weights).  
    - Complexity: O((V + E) log V) with a priority queue.
  - **Minimum Spanning Tree (Kruskal’s or Prim’s)**  
    - Connects all vertices with minimal total edge weight.  
    - Applications in network design.
- **Applications**:
  - Social network analysis, routing, scheduling, dependency resolution.

---

### Heuristics
- **Definition**: Strategies or “rules of thumb” used to find good-enough solutions more quickly when exact methods are too slow.
- **Characteristics**:
  - Not guaranteed to find the optimal solution.
  - Often domain-specific.
  - Trade speed for solution quality.
- **Examples**:
  - **A\* Search** (graphs):  
    - Uses a heuristic function to estimate distance to the goal.  
    - Balances actual cost so far (g) and estimated remaining cost (h).  
    - Completeness and optimality depend on heuristic being admissible (never overestimates).
  - **Greedy algorithms**:  
    - Make the locally optimal choice at each step.  
    - Example: coin-change problem in U.S. currency.
  - **Genetic algorithms**:  
    - Inspired by natural selection.  
    - Use mutation, crossover, and selection to evolve solutions.
- **When to use heuristics**:
  - Large search spaces (e.g., puzzle solving, game AI).
  - NP-hard problems (e.g., the Traveling Salesperson Problem).
  - Real-time decision making where time is limited.

