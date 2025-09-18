# Simple Quiz Application 

A simple Python-based quiz application that fetches questions from external API and provide an interactive with scroing and timing features.

---

## Project Structure

### `fetch_questions.py` 

- Handle fetching quiz questions from an external API
- Includes functions such as `get_questions()` which return the questions as a list of dictionaries for easy consumption.

### `quiz_app.py`

- Contains the main quiz logic
- Import `fetch_questions.py` to retrieve quiz data
- Manages questions shuffling, user interaction, timing, and scoring.

### Installation

1. Install dependencies: `pip3 install requests
`
