# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 15:22:56 2023

@author: kalypatn
"""

#Nesting
Capitals = {"France":"Paris",
            "Germany": "Berlin",
            }

#Nesting a list in a Dictionary
travel_log = {
            "France" : ["Paris", "Lille", "Dijon"],
            "Germany" : ["Berlin", "Hamburg"],
            }

#Dictionary which is nested itself in another dictionary
travel_log = {
            "France" : {"cities_visited" : ["Paris", "Lille", "Dijon"], "total_visits":12},
            "Germany" : {"cities_visited" :["Berlin", "Hamburg"], "total_visits":5},
            }


#Nesting a dictionary inside a list
travel_log = [
                {"country" :"France", 
                 "cities_visited" : ["Paris", "Lille", "Dijon"],
                 "total_visits":12
                 },
                {
                "country": "Germany",
                "cities_visited" :["Berlin", "Hamburg"],
                "total_visits":5
                },
            ]