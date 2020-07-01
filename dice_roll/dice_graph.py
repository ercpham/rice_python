#!/usr/bin/env python3
import random
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

size_string = input("Enter dice sizes: ")
size_list = size_string.split(" ")
size_list = list(map(int, size_list))
length = len(size_list)

num_rolls = int(input("Enter number of times to roll: "))
roll_list = []

for i in range(num_rolls):
    roll_sum = 0
    for j in range(length):
        roll_sum += random.randint(1,size_list[j])
    roll_list.append(roll_sum)

df = pd.DataFrame(data = {'Roll Sums': roll_list})

print(df.head())

ax = sns.countplot(x = 'Roll Sums', data=df)

plt.show()