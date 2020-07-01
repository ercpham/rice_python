import random
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

size_string = input("Enter dice sizes: ")
size_list = size_string.split(" ")
size_list = list(map(int, size_list))
length = len(size_list)

target_number = int(input("Target number: "))
consec = int(input("How many repeats? "))

trials = int(input("How many trials? "))

max_rolls = int(input("Max rolls per trial? "))

roll_list = []

for k in range(trials):
    repeats = 0
    total_rolls = 0
    while repeats < target_number:
        roll_sum = 0
        for j in range(length):
            roll_sum += random.randint(1,size_list[j])
        if roll_sum == target_number:
            repeats += 1
        else:
            repeats = 0
        total_rolls += 1
    if total_rolls < max_rolls:
        roll_list.append(total_rolls)

df = pd.DataFrame(data = {'Total Rolls': roll_list})
ax = sns.distplot(df, bins = 20)

plt.show()

# print("It took {} rolls to roll the number {}, {} consecutive times".format(total_rolls, target_number, consec))