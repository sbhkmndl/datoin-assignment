'''
Convert the given CSV file into JSON-Lines file and save to a new json-lines file 
with the name 'rainfall_india_1901-2015.jl'. For more details on json-lines format visit here: http://jsonlines.org/
'''

import csv
import json
with open('rainfall_india_1901-2015.csv','r') as csv_file, open('rainfall_india_1901-2015.jl','w') as output_file:
     for row in csv.DictReader(csv_file,delimiter=','):
             json.dump(row,output_file)
             output_file.write('\n')