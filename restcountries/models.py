from restcountries.expections import NotFound


class ResultSet(list):
    """A list like object that holds results from a RestCountries API query."""


class Model(object):
    _not_found_error_class = NotFound

    def __init__(self, **kwargs):
        self._repr_values = {"id": "Id"}

    @classmethod
    def _parse(cls, data, sub_item=False):
        data = data or {}
        if not data and not sub_item:
            raise cls._not_found_error_class()

        instance = cls() if data else None
        for key, value in data.items():
            if type(value) == str:
                value = value.strip()
            setattr(instance, key, value)
        return instance

    @classmethod
    def _parse_list(cls, data, sub_item=False):
        """Parse a list of JSON objects into a result set of model instances."""
        results = ResultSet()
        data = data or []
        for obj in data:
            if obj:
                results.append(cls._parse(obj, sub_item=sub_item))
        return results

    def __repr__(self):
        items = filter(lambda x: x[0] in self._repr_values.keys(), vars(self).items())
        state = ['%s: %s' % (self._repr_values[k], repr(v)) for (k, v) in items]
        return '<%s: %s >' % (self.__class__.__name__, ', '.join(state))


class Country(Model):

    def __init__(self, **kwargs):
        super(Country, self).__init__(**kwargs)
        self._repr_values = {"name": "Name", "alpha2Code": "Code"}

    @classmethod
    def _parse(cls, data, sub_item=False):
        country = super(Country, cls)._parse(data, sub_item=sub_item)

        if hasattr(country, "currencies"):
            country.currencies = Currency._parse_list(country.currencies, sub_item=True)

        if hasattr(country, "languages"):
            country.languages = Language._parse_list(country.languages, sub_item=True)

        if hasattr(country, "regionalBlocs"):
            country.regional_blocs = RegionalBloc._parse_list(country.regionalBlocs, sub_item=True)

        return country


class Currency(Model):

    def __init__(self, **kwargs):
        super(Currency, self).__init__(**kwargs)
        self._repr_values = {"name": "Name", "code": "Code"}


class Language(Model):

    def __init__(self, **kwargs):
        super(Language, self).__init__(**kwargs)
        self._repr_values = {"name": "Name"}


class RegionalBloc(Model):

    def __init__(self, **kwargs):
        super(RegionalBloc, self).__init__(**kwargs)
        self._repr_values = {"name": "Name"}
