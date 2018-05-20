import unittest

from restcountries.api import RestCountries
from restcountries.models import Country


class CountryTest(unittest.TestCase):
    code = "tr"
    code1 = "ee"
    currency = "try"
    language = "tr"
    field = "capital"
    fields = ("name", "alpha2Code")

    def setUp(self):
        self.restcountries = RestCountries()

    def test_all(self):
        countries = self.restcountries.all()
        self.assertIsInstance(countries, list)
        self.assertIsInstance(countries[0], Country)

        # fields tests
        countries1 = self.restcountries.all(fields=self.fields)
        self._test_fields(countries1)

    def test_name(self):
        countries = self.restcountries.name(name="Turk")
        self.assertIsInstance(countries, list)
        self.assertIsInstance(countries[0], Country)
        self.assertEqual(len(countries), 3)

        # fields tests
        countries1 = self.restcountries.name(name="Turk", fields=self.fields)
        self._test_fields(countries1)

    def test_name_full_text(self):
        countries = self.restcountries.name(name="Turkey", full_text=True)
        self.assertIsInstance(countries, list)
        self.assertIsInstance(countries[0], Country)
        self.assertEqual(len(countries), 1)

        # fields tests
        countries1 = self.restcountries.name(name="Turkey", full_text=True, fields=self.fields)
        self._test_fields(countries1)

    def test_code(self):
        country = self.restcountries.code(self.code)
        self.assertIsInstance(country, Country)
        self.assertEqual(country.alpha2Code.lower(), self.code)

        # fields tests
        country1 = self.restcountries.code(self.code, fields=self.fields)
        self._test_fields([country1])

    def test_code_list(self):
        code_list = [self.code, self.code1]
        countries = self.restcountries.code_list(code_list)
        self.assertIsInstance(countries, list)
        self.assertIsInstance(countries[0], Country)
        self.assertEqual(len(countries), 2)
        self.assertIn(countries[0].alpha2Code.lower(), code_list)
        self.assertIn(countries[1].alpha2Code.lower(), code_list)

        # fields tests
        countries1 = self.restcountries.code_list(code_list, fields=self.fields)
        self._test_fields(countries1)

    def test_currency(self):
        countries = self.restcountries.currency(self.currency)
        self.assertIsInstance(countries, list)
        self.assertIsInstance(countries[0], Country)
        self.assertEqual(len(countries), 1)
        self.assertIn(self.currency, map(lambda x: x.code.lower(), countries[0].currencies))

        # fields tests
        countries1 = self.restcountries.currency(self.currency, fields=self.fields)
        self._test_fields(countries1)

    def test_language(self):
        countries = self.restcountries.language(self.language)
        self.assertIsInstance(countries, list)
        self.assertIsInstance(countries[0], Country)
        self.assertEqual(len(countries), 2)
        self.assertIn(self.language,  map(lambda x: x.iso639_1.lower(), countries[0].languages))
        self.assertIn(self.language,  map(lambda x: x.iso639_1.lower(), countries[1].languages))

        # fields tests
        countries1 = self.restcountries.language(self.language, fields=self.fields)
        self._test_fields(countries1)

    def test_capital(self):
        countries = self.restcountries.capital("ankara")
        self.assertIsInstance(countries, list)
        self.assertIsInstance(countries[0], Country)
        self.assertEqual(len(countries), 1)

        # fields tests
        countries1 = self.restcountries.capital("ankara", fields=self.fields)
        self._test_fields(countries1)

    def test_calling_code(self):
        countries = self.restcountries.calling_code("90")
        self.assertIsInstance(countries, list)
        self.assertIsInstance(countries[0], Country)
        self.assertEqual(len(countries), 1)

        # fields tests
        countries1 = self.restcountries.calling_code("90", fields=self.fields)
        self._test_fields(countries1)

    def test_region(self):
        countries = self.restcountries.region("europe")
        self.assertIsInstance(countries, list)
        self.assertIsInstance(countries[0], Country)

        # fields tests
        countries1 = self.restcountries.region("europe", fields=self.fields)
        self._test_fields(countries1)

    def test_regional_bloc(self):
        countries = self.restcountries.regional_bloc("eu")
        self.assertIsInstance(countries, list)
        self.assertIsInstance(countries[0], Country)

        # fields tests
        countries1 = self.restcountries.regional_bloc("eu", fields=self.fields)
        self._test_fields(countries1)

    def _test_fields(self, countries):
        self.assertIsInstance(countries, list)
        self.assertIsInstance(countries[0], Country)
        self.assertTrue(hasattr(countries[0], self.fields[0]))
        self.assertTrue(hasattr(countries[0], self.fields[1]))
        self.assertFalse(hasattr(countries[0], self.field))


if __name__ == "__main__":
    unittest.main()
