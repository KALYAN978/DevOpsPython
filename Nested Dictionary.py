# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 13:09:07 2023

@author: kalypatn
"""

bike = {"brand":"Bajaj",
        "Model":"Avenger",
        "year":2019,
        "engine":"220cc"}

mobile = {"brand":"iphone",
          "Os":"IOS"}

Apple = {"bike":bike,
         "mobile":mobile
         }


print("\n Apple Products")
for x in Apple.items():
    print(x)