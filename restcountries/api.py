from restcountries.country import Country


class RestCountries(object):
    """RestCountries API"""
    BASE_URL = "http://restcountries.eu/rest"
    VERSION = "v2"

    def __init__(self, **kwargs):
        """
        RestCountries Api Instance Constructor

        :param kwargs:
        """
        self.base_url = "%s/%s" % (self.BASE_URL, self.VERSION)

    @property
    def _country(self):
        return Country(api=self)

    def all(self, fields=()):
        return self._country.all(fields=fields)

    def name(self, name, full_text=False, fields=()):
        return self._country.name(name, full_text=full_text, fields=fields)

    def code(self, code, fields=()):
        return self._country.code(code, fields=fields)

    def code_list(self, code_list, fields=()):
        return self._country.code_list(code_list, fields=fields)

    def currency(self, currency, fields=()):
        return self._country.currency(currency, fields=fields)

    def language(self, language_code, fields=()):
        return self._country.language(language_code, fields=fields)

    def capital(self, capital, fields=()):
        return self._country.capital(capital, fields=fields)

    def calling_code(self, calling_code, fields=()):
        return self._country.calling_code(calling_code, fields=fields)

    def region(self, region, fields=()):
        return self._country.region(region, fields=fields)

    def regional_bloc(self, regional_bloc, fields=()):
        return self._country.regional_bloc(regional_bloc, fields=fields)
