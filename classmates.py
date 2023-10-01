# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 12:12:15 2023

@author: Dongli
"""

relationships = {}

relationships['Dongli'] = ['Adam', 'Frank', 'George']
relationships['Adam'] = ['Ema', 'Dongli', 'Bob']
relationships['Ema'] = ['Adam', 'Bob', 'Dolly']
relationships['Bob'] = ['Adam', 'Ema', 'Dolly']
relationships['Dolly'] = ['Ema', 'Bob']
relationships['Frank'] = ['Dongli']
relationships['George'] = ['Dongli']