from restcountries.client import Client
from restcountries.models import Country as CountryModel


class Country(Client):
    """Country operations."""

    def __init__(self, **kwargs):
        super(Country, self).__init__(**kwargs)
        self.fields_tag = "fields"

    def _country_list(self, url, params=None, fields=()):
        params = params or {}
        params.update(self._get_filter_params(fields))
        result = self._get(url, params=params)
        return CountryModel._parse_list(result)

    def _country_get(self, url, params=None, fields=()):
        params = params or {}
        params.update(self._get_filter_params(fields))
        result = self._get(url, params=params)
        return CountryModel._parse(result)

    def _get_filter_params(self, fields):
        return {self.fields_tag: ";".join(fields)}

    def all(self, fields=()):
        """
        Get all list of countries.

        :param fields: Filter the output of your request to include only the specified fields.
        :return [List]: Country list.
        """
        url = "/all"
        return self._country_list(url, fields=fields)

    def name(self, name, full_text=False, fields=()):
        """
        Search by country name. It can be the native name or partial name.

        :param name: Country name.
        :param full_text: Search by country full name.
        :param fields: Filter the output of your request to include only the specified fields.
        :return [List]: Country list.
        """
        url = "/name/%s" % name
        params = {"fullText": full_text}
        return self._country_list(url, params=params, fields=fields)

    def code(self, code, fields=()):
        """
        Search by ISO 3166-1 2-letter or 3-letter country code.

        :param code: Country code.
        :param fields: Filter the output of your request to include only the specified fields.
        :return [List]: Country list.
        """
        url = "/alpha/%s" % code
        return self._country_get(url, fields=fields)

    def code_list(self, code_list, fields=()):
        """
        Search by list of ISO 3166-1 2-letter or 3-letter country codes.

        :param code_list: Country code list.
        :param fields: Filter the output of your request to include only the specified fields.
        :return [List]: Country list.
        """
        url = "/alpha"
        codes = ";".join(code_list)
        params = {"codes": codes}
        return self._country_list(url, params=params, fields=fields)

    def currency(self, currency_code, fields=()):
        """
        Search by ISO 4217 currency code.

        :param currency_code: Currency code.
        :param fields: Filter the output of your request to include only the specified fields.
        :return [List]: Country list.
        """
        url = "/currency/%s" % currency_code
        return self._country_list(url, fields=fields)

    def language(self, language_code, fields=()):
        """
        Search by ISO 4217 currency code.

        :param language_code: Language code.
        :param fields: Filter the output of your request to include only the specified fields.
        :return [List]: Country list.
        """
        url = "/lang/%s" % language_code
        return self._country_list(url, fields=fields)

    def capital(self, capital, fields=()):
        """
        Search by capital city.

        :param capital: Capital city.
        :param fields: Filter the output of your request to include only the specified fields.
        :return [List]: Country list.
        """
        url = "/capital/%s" % capital
        return self._country_list(url, fields=fields)

    def calling_code(self, calling_code, fields=()):
        """
        Search by calling code.

        :param calling_code: Calling code.
        :param fields: Filter the output of your request to include only the specified fields.
        :return [List]: Country list.
        """
        url = "/callingcode/%s" % calling_code
        return self._country_list(url, fields=fields)

    def region(self, region, fields=()):
        """
        Search by region: Africa, Americas, Asia, Europe, Oceania.

        :param region: Region.
        :param fields: Filter the output of your request to include only the specified fields.
        :return [List]: Country list.
        """
        url = "/region/%s" % region
        return self._country_list(url, fields=fields)

    def regional_bloc(self, regional_bloc, fields=()):
        """
        Search by regional bloc:
            EU (European Union)
            EFTA (European Free Trade Association)
            CARICOM (Caribbean Community)
            PA (Pacific Alliance)
            AU (African Union)
            USAN (Union of South American Nations)
            EEU (Eurasian Economic Union)
            AL (Arab League)
            ASEAN (Association of Southeast Asian Nations)
            CAIS (Central American Integration System)
            CEFTA (Central European Free Trade Agreement)
            NAFTA (North American Free Trade Agreement)
            SAARC (South Asian Association for Regional Cooperation)

        :param regional_bloc: Regional bloc.
        :param fields: Filter the output of your request to include only the specified fields.
        :return [List]: Country list.
        """
        url = "/regionalbloc/%s" % regional_bloc
        return self._country_list(url, fields=fields)
