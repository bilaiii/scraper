# WebScraper for Edus
A simle WebScraper to fetch homework tasks (and maybe more in the future) from Edus - my school journal platform
## Installation

deps:
- [uv](https://github.com/astral-sh/uv)
- [geckodriver](https://github.com/mozilla/geckodriver) in your PATH

1. Clone this repo
```bash
git clone https://github.com/bilaiii/scraper.git
cd scraper
```
2. Sync the project dependencies
```bash
uv sync
```
3. Make a `.env` file and set your login and password
```bash
echo 'LOGIN="<your-login>"
PASSWD="<your-password>"' > .env
```
4. Run the scraper
```bash
uv run main.py
```

## Usage
- Simply run the scraper
- Forward the stdout to a markdown file
```bash
uv run main.py > homework.md | uv run main.py >> homework.md
```
