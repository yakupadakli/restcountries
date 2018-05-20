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

    def all(self):
        return self._country.all()

    def name(self, name, full_text=False):
        return self._country.name(name, full_text=full_text)

    def code(self, code):
        return self._country.code(code)

    def code_list(self, code_list):
        return self._country.code_list(code_list)

    def currency(self, currency):
        return self._country.currency(currency)

    def language(self, language_code):
        return self._country.language(language_code)

    def capital(self, capital):
        return self._country.capital(capital)

    def calling_code(self, calling_code):
        return self._country.calling_code(calling_code)

    def region(self, region):
        return self._country.region(region)

    def regional_bloc(self, regional_bloc):
        return self._country.regional_bloc(regional_bloc)
