#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np


df = pd.DataFrame(pd.DataFrame(np.random.randint(low=0, high=10, size=(5, 5)),
                       columns=['a', 'b', 'c', 'd', 'e']))
print(df.head())

df.to_csv('numppy.csv')

