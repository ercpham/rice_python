#!/usr/bin/env python3
import random

size_string = input("Enter dice sizes: ")
size_list = size_string.split(" ")
size_list = list(map(int, size_list))

roll_sum = 0

length = len(size_list)

for index in range(length):
    roll = random.randint(1, size_list[index])
    print("Dice {}: {}".format(index+1, roll))
    roll_sum += roll

print("Sum of dice rolls: {}".format(roll_sum))