YoMamaGen
=========
Generates random YoMama jokes.

See: http://yomamagen.com

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

Cleaning Up The Data
-------------------

To sort categories properly and add manually added jokes, run:

```
    python app/models.py
```


Providing an API
----------------

This project uses Flask, Peewee ORM and Flask-Peewee to provide a REST API.

```
    python manage.py runserver
```

Then follow on-screen instructions

Consuming the API
-----------------

This app uses Phonegap and simple JQuery AJAX to consume the API and provide mobile apps.


