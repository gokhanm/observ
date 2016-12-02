# Copyright 2016 Gokhan MANKARA <gokhan@mankara.org>

from observ.crontab import CronTab


class Cron:
    def __init__(self, user):
        self.tab = CronTab(user=user)

    def write(self):
        """
            Write crontab settings
        """
    
        self.tab.write()

    def run(self, cmd, run_time):
        """
            :param cmd: which command to write crontab
            :param run_time: in which period the cron works
                             Available Periods:
                                hourly, daily, monthly, weekly
        """

        cron_job = self.tab.new(cmd, comment='Observ crontab job')

        if 'hourly' == run_time:
            cron_job.every().hours()
        elif 'daily' == run_time:
            cron_job.every().dow()
        elif 'monthly' == run_time:
            cron_job.every().month()
        elif 'weekly' == run_time:
            cron_job.setall('0 0 * * 0')

        self.write()

