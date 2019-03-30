#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 23:25:02 2019

@author: mevrick
"""


import requests
 
proxies = {"http":"http://103.23.207.106:53281",
           "https":"http://188.73.8.12:48353",
           
           "https":"96.9.86.170:23500",
           "http":"96.9.86.170:23500"}
r = requests.get('http://jsonip.com',proxies=proxies)
ip= r.json()['ip']
print('Your IP is', ip)
