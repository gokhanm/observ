# Copyright 2016 Gokhan MANKARA <gokhan@mankara.org>

import os
from observ.exceptions import ObservConfigException
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser


class Config():
    def __init__(self):
        """
            Parsing configuration file.
            /etc/observ.conf
        """
        self.config_path = os.path.join('/etc', 'observ.conf')
        self.config = ConfigParser()
        self.config.read(self.config_path)

    def all_sections(self):
        """
            :return: Return all sections in conf file
        """
        sections = self.config.sections()
        
        return sections

    def section_keys(self, section):
        """
            :return: Return keys in specified section
        """

        sections = self.all_sections()
        keys = [key for key in sections]

        return keys

    def section_key_value(self, section, key):
        """
            :return: Return key value in specified section
        """

        value = self.config.get(section, key)

        if len(value) == 0:
            raise ObservConfigException('Please edit %s key in /etc/observ.conf' %
                                        key)

        return value
        
