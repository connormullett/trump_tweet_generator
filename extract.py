#!/bin/env python

import csv, string

out_file = 'data/data.csv'
data_files = ['realdonaldtrump', 'trumptweets']

file_handle = open(out_file, 'w+')

translator = str.maketrans('', '', string.punctuation)

for data_file in data_files:
  with open(f'data/{data_file}.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar="'")
    for row in reader:
      field = row[2]
      data = field.translate(translator)
      file_handle.write(data + '\n')


file_handle.close()
print('Done')

