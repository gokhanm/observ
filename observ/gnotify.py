# Copyright 2016 Gokhan MANKARA <gokhan@mankara.org>

import gi
gi.require_version('Notify', '0.7')

from gi.repository import GObject
from gi.repository import Notify

from observ.config import Config


class Gnotify(GObject.Object):
    def __init__(self):
        """
            Sending notification to Gnome Notify module
        """
        super(Gnotify, self).__init__()
        # lets initialise with the application name
        Notify.init("Observ")
        self.config = Config()

    def send_notification(self, text):
        """
            :param text: text message
        """
        title = self.config.section_key_value('Gnome', 'title')
        icon = self.config.section_key_value('Gnome', 'icon')

        n = Notify.Notification.new(title, text, icon)
        n.show()

