import six


class RestCountryException(Exception):
    """RestCountry exception"""

    def __init__(self, message, **kwargs):
        self.message = six.text_type(message) if message else "Unknown error"
        super(RestCountryException, self).__init__(message, **kwargs)

    def __str__(self):
        return self.message


class NotFound(RestCountryException):
    message = six.text_type("Not Found")
