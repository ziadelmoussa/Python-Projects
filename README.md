# Python Projects 

This repository consolidates a collection of functional Command Line Interface (CLI) applications built to practice core software development concepts, file management, API integration, and version control.

## Technical Skills Covered
* Core Python: Functions, loops, nested dictionaries, lists, and exception handling.
* Data Persistence: File handling, CRUD operations, and reading/writing data using JSON.
* Integrations and Regex: Interacting with external REST APIs (OpenWeatherMap API) and text parsing with Regular Expressions (Regex).
* Workflow: Input validation, defensive error handling, and structured Git/GitHub workflows.

---

## Repository Directory
Each project is self-contained within its own directory:
* ./Calculator-Project — CLI Arithmetic Calculator
* ./contact-book — Contact book featuring JSON storage and Regex email verification
* ./expense-tracker — Financial tracker with multi-category spending analytics
* ./number-guessing-game — Multi-difficulty guessing game
* ./quiz-app — Interactive multiple-choice quiz dashboard
* ./todo-app — Automated persistent task management application
* ./Weather-App — Live weather client pulling data from the OpenWeatherMap API

---

## Projects Index

<details>
<summary>1. Weather App (API Integration)</summary>

### Overview
This application retrieves real-time weather information for a requested city using the OpenWeatherMap API.

### Main Functions
* `get_weather(city)`: Retrieves live JSON payloads from the API.
* `display_weather(weather)`: Parses and presents the weather metrics inside a cleanly structured console panel.
* `main()`: Houses core runtime execution loops and controls menu behaviors.

### App Interaction Example
```text
****************
Weather App
****************
1. Get Weather
2. Exit

Choose option: 1
Enter city: Dammam

=================
Weather Report
=================
City: Dammam
Temperature: 38°C
Humidity: 55%
Wind Speed: 14 km/h
Condition: Sunny
```

### Setup and Execution
1. Open the application script file.
2. Locate the line: `API_KEY = "PUT_YOUR_API_KEY_HERE"` and swap it with your custom OpenWeatherMap API key token.
3. Launch the app via the terminal:
   ```bash
   python Weather-App/weather_app.py
   ```

### Error Handling
* Invalid city names
* Network or internet downtime issues
* Unauthorized or invalid API keys
* Malformed responses or empty payloads

---
</details>

<details>
<summary>2. Contact Book App (JSON Storage & Regex)</summary>

### Overview
A CRUD management application handling contact records locally inside a structured persistent JSON store.

### Features
* Create new entries, read database logs, modify existing details, and delete entries.
* Validates user input formatting with standard Python structure checks.
* Validates email strings leveraging Regular Expressions (Regex).
* Allows menu navigation rollbacks using the '<' character.
* Fields Tracked: Name, Phone Number, and Email Address.

### Code Organization
* main.py: Drives core menu operational pathways and entry transformations.
* contacts.json: Serves as the database flat-file storage hub.

### Setup and Execution
```bash
cd contact-book
python main.py
```
---
</details>

<details>
<summary>3. Expense Tracker (Data Analytics & CRUD)</summary>

### Overview
A CLI tracking asset designed to record expenditures, compute total metrics, and group spending records by custom categories.

### Features
* Record asset expenditure logs (Amount, Category, and Description).
* Review historical logs or delete line items explicitly.
* Compute automated cumulative calculations.
* Filter data segments to aggregate spending records across active targets.

### Code Organization
* main.py: Drives dashboard interfaces and algorithmic computations.
* expenses.json: Retains persistent spending logs across runtime sessions.

### Setup and Execution
```bash
cd expense-tracker
python main.py
```
---
</details>

<details>
<summary>4. To-Do List App (Persistent Task Tracker)</summary>

### Overview
A task utility engineered to manage, view, process, and clear active operations with background JSON synchronization.

### Features
* Add new items and monitor complete processing state values.
* Toggle line items to Complete flags.
* Delete obsolete entries seamlessly.
* Automated loading and background saves tracking modifications.

### Code Organization
* main.py: Drives application operations and standard structural adjustments.
* tasks.json: Backs system data states persistently across instances.

### Setup and Execution
```bash
cd todo-app
python main.py
```
---
</details>

<details>
<summary>5. Quiz App (Data Trees & Score Management)</summary>

### Overview
An interactive trivia console parsing multi-tier evaluation models using layered data models.

### Features
* Dynamic category classification paths (Science, Math, and Geography parameters).
* Multiple-choice quiz selection structures.
* Maintains metrics trackers calculating percentages and overall point values.
* Seamless loops facilitating immediate restart capabilities.

### Setup and Execution
```bash
cd quiz-app
python main.py
```
---
</details>

<details>
<summary>6. CLI Calculator (Input Control & Logic Processing)</summary>

### Overview
A terminal engine structured to manage core arithmetic queries while preventing runtime drops.

### Features
* Handles foundational arithmetic (Addition, Subtraction, Multiplication, Division).
* Robust entry handling parsing logic against value inputs.
* System structural fallback controls intercepting Division by Zero attempts.
* Maintains calculation loops continuously until user prompts explicit close commands.

### Setup and Execution
```bash
cd Calculator-Project
python main.py
```
---
</details>

<details>
<summary>7. Number Guessing Game (Randomization & Conditionals)</summary>

### Overview
A random number engine parsing numeric inputs against active logic configurations.

### Features
* Dynamic background target generation using the Python standard `random` library.
* Adjustable settings controlling target windows.
* Tracks user attempt performance metrics throughout runtime operations.
* Ensures smooth terminal restarts via quick entry paths.

### Setup and Execution
```bash
cd number-guessing-game
python main.py
```
</details>
