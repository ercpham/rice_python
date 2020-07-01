#!/usr/bin/env python3
import random
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

num_rolls = int(input("Enter number of times to roll: "))
roll_list = []

for i in range(num_rolls):
    roll_list.append(random.randint(1,6) + random.randint(1,6))

df = pd.DataFrame(data = {'Roll Sums': roll_list})

print(df.head())

ax = sns.countplot(x = 'Roll Sums', data=df)

plt.show()