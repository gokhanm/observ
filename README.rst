observ
======

observ is a command line tool to inform you that new versions are available

Installation
============
.. code-block:: bash
    $ python setup.py install

or

.. code-block:: bash
    $ python3 setup.py install

Available Desktop Environment
=============================

Gnome 3.22.2

Usage
=====

.. code-block:: bash
    $ observ --help
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

