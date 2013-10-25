"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

import os.path
import urllib, urllib2, time
from uuid import getnode as get_mac
mac = get_mac() # mac adress as 48bit intiger
from datetime import datetime

class Setup_Manager:
    def __init__(self, server_url, device):
        self.server_url = server_url
        self.device = device

        self.io_status = False
        self.db_status = False
        self.server_status = False

    def check_io(self):
        if os.path.exists(self.device):
            io_status = True
            print(self.device + " founded")
            return True
        else:
            io_status = False
            print(self.device + " no founded")
            return False

    def check_db (self):
        try:
            import sqlite3 as lite
            connection = lite.connect('checkIn.db')
            cursor = connection.cursor()
            cursor.execute('create table if not exists checkIns(url text(63), time datetime)')
            data = cursor.fetchone()
            self.db_status = True
            print("Database Ready")
        except lite.Error, e:
            self.db_status = False
            print("Database not Ready")

    def check_server(self):

        url = self.server_url + 'checkin/status/'

        values = {'mac' : mac,}

        try:
            print("Checking the server")
            data = urllib.urlencode(values)
            req = urllib2.Request(url, data)
            response = urllib2.urlopen(req)
            answer = response.read()
            if answer == "ok":
                self.server_status = True;
                print(url + " accepted us")
                return True
            else:
                self.server_status = False
                print(url + " did not accept us")
                return True
        except Exception, detail:
            self.server_status = False
            print("Error conectiong to the server")


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

    def test_client_success_auth(self):
        """
        Tests if server authenticates client
        """
        setup_manager = Setup_Manager('http://127.0.0.1:8000/', '/dev/video0')

        self.assertEqual(setup_manager.check_server(), True)
