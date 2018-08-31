Speedtest Logger
================

A simple library to log the results of broadband speed tests to a csv file.

Installation
------------

The library requires Python 3.6 or greater.

To install:

    $ pip install speedtest_logger

Usage
-----

    $ speedtest-logger <path to directory to hold log files>

The logger will conduct a speed test and log the result, using csv format, to `speedtest.log` in
the directory specified.

The log file is set to rotate each day and the intention is that you would create a cron job to schedule
the logger at whatever frequency is desired.
