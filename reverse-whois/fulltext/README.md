# Fulltext RIPE scraper

This tool emulates the use of the website https://apps.db.ripe.net/db-web-ui/#/fulltextsearch.

It uses Selenium and it will open a browser window. Please do not close it.

It can get IPv4 and IPv6 addresses. Also emails and mnt-by, but they are not really useful.

By default only IPv4 is extracted, uncomment to add more.

## Installation

### Install the firefox webdriver

Go to https://pypi.org/project/selenium/

In the drivers section

Download for firefox

Move the geckodriver file to the path, e.g., /usr/bin

### Install the tool

```
pip3 install -r requeriments.txt
```

## Usage

```
python3 fulltext.py
```

## FAQ

If the tool gives problems when running, it might be because of the screen size.

Modify the line 65 'browser.execute\_script("window.scrollTo(0, 300)")'.

Change parameters or make full screen.

