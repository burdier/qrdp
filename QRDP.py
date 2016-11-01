#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os 
import json 

#server configure
with open("config.json") as json_file:
    json_data = json.load(json_file)

    server = json_data["server"]["host"]


def desc():
    while True:
        username=str(input("username:>"))
        print("")
        os.system("C:\\Windows\\System32\\query.exe session "+username+" /server:"+server)
       	print("")
        session = input("session name or id to logoff:> ") 
        os.system("C:\\Windows\\System32\\logoff.exe "+ session+ " /server:"+server)
        os.system("cls")
        print(username+ " logoff")
print(""" 

	Qrdp disconnect session by:Bursoft (Luis Miguel Burdier)

			""" )
desc()
