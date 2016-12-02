# Copyright 2016 Gokhan MANKARA <gokhan@mankara.org>
"""
Usage:
    observ [--notify NOTIFY] [--list]
    observ (--period PERIOD --notify NOTIFY)
    observ -h | --help
    observ -v | --version

Options:
    -h --help                          : Show this screen
    -v --version                       : Show version
    -p <period>, --period <period>     : Outdated package check period with cron
                                         hourly, daily, weekly or monthly
    
    -n <notify>, --notify <notify>     : Sending information with mail or desktop notification
                                         system like GNOME Notify. for now desktop
                                         notification only supporting for GNOME
                                         Param: mail or gnome

    -l --list                          : Listing outdated packages
"""

from __future__ import print_function
from docopt import docopt
from platform import python_version

from observ import __version__
from observ.cron import Cron
from observ.config import Config
from observ.gnotify import Gnotify
from observ.mail import Email
from observ.utils import Util
from observ.exceptions import (
        ObservPeriodException, ObservNotifyException, ObservPeriodNotSupported)


def main():
    config = Config()
    args = docopt(__doc__)

    period = args['--period']
    print_list = args['--list']
    notify = args['--notify']
    version = args['--version']

    if version:
        print('observ : pip outdated notifier', 'Version: %s' % __version__,
                'Python Version: %s' % python_version(), sep='\n')

    if period is not None and notify is not None:
        user = config.section_key_value('cron', 'username')
        cron = Cron(user=user)
        cmd = 'observ -n %s' % notify

        if 'hourly' == period:
            cron.run(cmd=cmd, run_time='hourly')
        elif 'daily' == period:
            cron.run(cmd=cmd, run_time='daily')
        elif 'weekly' == period:
            cron.run(cmd=cmd, run_time='weekly')
        elif 'mountly' == period:
            cron.run(cmd=cmd, run_time='monthly')
        else:
            raise ObservPeriodNotSupported('%s perid not supported' % period)

        print('Observ set %s' % period)
        exit(0)

    if notify is not None:
        result = Util().list(parse=True)
        
        if 'mail' == notify:

            server = config.section_key_value('mail', 'server')
            username = config.section_key_value('mail', 'username')
            password = config.section_key_value('mail', 'password')
            port = config.section_key_value('mail', 'port')
            destination = config.section_key_value('mail', 'destination')
            mail_from = config.section_key_value('mail', 'mail_from')
            subject = config.section_key_value('mail', 'subject')
            tls = config.section_key_value('mail', 'start_tls')
            relay = config.section_key_value('mail', 'relay')
            signature = config.section_key_value('mail', 'signature')

            msj = result + signature

            Email(server, username=username, password=password,
                  port=port, tls=tls, relay=relay).send(
                                                        destination, 
                                                        mail_from, 
                                                        subject, 
                                                        msj
                                                        )
        elif 'gnome' == notify:
            msj = "New Outdated Pip Packages Found. Please run 'observ --list'\
                    command on terminal to see packages"
            Gnotify().send_notification(msj)
        else:
            ObservNotifyException('%s not supported. Available notify types: gnome, mail' % notify)

    if print_list:
        Util().list()


if __name__ == '__main__':
    main()

