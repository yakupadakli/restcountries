# restcountries

A library that provides a Python wrapper to [RestCountries API](https://restcountries.eu/).

## Installation

The easiest way to install the latest version
is by using pip/easy_install to pull it from PyPI:

    pip install restcountries

You may also use Git to clone the repository from
Github and install it manually:

    git clone https://github.com/yakupadakli/restcountries.git
    cd restcountries
    python setup.py install

Python 2.7, 3.4, 3.5 and 3.6, is supported for now.


## Usage

    from restcountries.api import RestCountries
    
    restcountries = RestCountries()


#### ALL

Get all list of countries.

    restcountries.all()

##### NAME

Search by country name. It can be the native name or partial name.

    restcountries.name("Turk")

##### FULL NAME

Search by country full name.

    restcountries.name("Turkey", full_text=True)

##### CODE

Search by ISO 3166-1 2-letter or 3-letter country code.

    restcountries.code("tr")

##### LIST OF CODES

Search by list of ISO 3166-1 2-letter or 3-letter country codes.

    restcountries.code_list(["tr", "ee"])

##### CURRENCY

Search by ISO 4217 currency code.

    restcountries.name("Turk")

##### LANGUAGE

Search by ISO 639-1 language code.

    restcountries.name("Turk")

##### CAPITAL CITY

Search by capital city.

    restcountries.name("Turk")

##### CALLING CODE

Search by calling code.

    restcountries.name("Turk")

##### REGION

Search by region: Africa, Americas, Asia, Europe, Oceania.

    restcountries.name("Turk")

##### REGIONAL BLOC

Search by regional bloc:

~~~
* EU (European Union)
* EFTA (European Free Trade Association)
* CARICOM (Caribbean Community)
* PA (Pacific Alliance)
* AU (African Union)
* USAN (Union of South American Nations)
* EEU (Eurasian Economic Union)
* AL (Arab League)
* ASEAN (Association of Southeast Asian Nations)
* CAIS (Central American Integration System)
* CEFTA (Central European Free Trade Agreement)
* NAFTA (North American Free Trade Agreement)
* SAARC (South Asian Association for Regional Cooperation)
~~~
    restcountries.name("Turk")
