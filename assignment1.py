import csv
import json
with open('rainfall_india_1901-2015.csv','r') as csv_file, open('rainfall_india_1901-2015.jl','w') as output_file:
     for row in csv.DictReader(csv_file,delimiter=','):
             json.dump(row,output_file)
             output_file.write('\n')