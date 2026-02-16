# Web Scraping with BeautifulSoup

A small Python project that scrapes Khabib Nurmagomedov's Wikipedia page and extracts his opponent list from the fight-record table.

## What This Project Does

- Sends an HTTP request to the Wikipedia page
- Parses HTML with BeautifulSoup
- Locates the table containing the `Opponent` column
- Extracts opponent names
- Saves them into `opponents_list.json`

## Tech Stack

- Python 3
- `requests`
- `beautifulsoup4` (installed via `bs4`)

## Project Structure

- `test.py`: scraper script
- `requirements.txt`: dependencies
- `opponents_list.json`: generated output file

## Setup

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
```

## Run

```bash
python test.py
```

After running, the script writes opponent names to `opponents_list.json`.

## Notes

- This project is for learning web scraping basics.
- Website structures can change over time, which may require selector updates.
