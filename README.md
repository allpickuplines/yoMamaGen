YoMamaGen
=========
Generates random YoMama jokes.

Getting Started
---------------

```
    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt
```

Scraping Data
-------------

This project uses Scrapy to scrape the data, all Scrapy commands are available e.g.

```
    scrapy list
    scrapy crawl [spider_name]
```

Providing an API
----------------

This project uses Flask, Peewee ORM and Flask-Peewee to provide a REST API.

```
    python app.py
```

Then follow on-screen instructions

Consuming the API
-----------------

This app uses Phonegap and simple JQuery AJAX to consume the API and provide mobile apps.


