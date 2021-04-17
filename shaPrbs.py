# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 09:58:41 2021

@author: Pedro
"""

from hashlib import blake2b
h = blake2b(digest_size=25)
v = '0747'
h.update(v.encode())

print(h.hexdigest())