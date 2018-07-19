#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

# this is a function that just returns the 'values' list so it can be sorted below
def getValue(item) :
    return item.value

def knapsack_solver(items, capacity):
  # sorting the item's values from largest to smallest with the key and size divided by value..
  # this is so we can just grab the first couple of items with the highest values until our knapsack is full
  # items = sorted(items, key=getValue, reverse=True)
  items = sorted(items, key=lambda i: i.size / i.value)
  # just wanted to look at the items after the value got sorted
  print(items)
  # creating an empty list called 'choices' to put our highest valued items into
  choices = []
  # creating a variable to keep track of our total values as we add them
  totalValue = 0

  # looping over all the items 
  for i in items:
  # deciding if the current item's size is less than or equal to the capacity of our knapsack
    if i.size <= capacity:
  # if it does fit, we subtract the size from the knapsacks capacity
      capacity -= i.size
  # adding the index of that item to our choices array/list
      choices.append(i.index)
  # adding the chosen item's value to our total value tracker
      totalValue += i.value
  # returning the totalvalue of our knapsack's choices and the index of all the choices we selected
  return [totalValue, choices]


if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')
