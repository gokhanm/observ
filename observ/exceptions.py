#Copyright 2016 Gokhan MANKARA <gokhan@mankara.org>
"""
observ.exceptions
~~~~~~~~~~~~~~~~~~~
This module contains the set of Observ's exceptions.
"""


class ObservException(Exception):
    """Observ main exception class"""
    pass


class ObservPeriodException(ObservException):
    """A period error occurred."""
    pass


class ObservNotifyException(ObservException):
    """A notify error occurred."""
    pass


class ObservEmailUnableRelay(ObservException):
    """An email error occurred."""
    pass


class ObservConfigException(ObservException):
    """A config error occurred."""
    pass


class ObservPipCommandException(ObservException):
    """A pip command error occurred."""
    pass


class ObservPeriodNotSupported(ObservException):
    """A period not supported error occurred."""
    pass

