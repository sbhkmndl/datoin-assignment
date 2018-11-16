import json
from itertools import groupby
        
with open('rainfall_india_1901-2015.jl','r') as file_json_lines:
    months = ('JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC')
    rain_months = {'JAN':0,'FEB':0,'MAR':0,'APR':0,'MAY':0,'JUN':0,'JUL':0,'AUG':0,'SEP':0,'OCT':0,'NOV':0,'DEC':0}
    subdivs_dict = [json.loads(line) for line in file_json_lines]
    # get all subdivision as python dictionary file
    group_state = [list(gr) for key, gr in groupby(subdivs_dict,lambda x:x['SUBDIVISION'])]
    # group by subdivision
    state_dict = dict()
    # create a dictionary that contain sibdivision name and total rain in each month 
    for state in group_state:
        state_dict[state[0]['SUBDIVISION']]=dict()
        # initiate dictionary for each subdivision 
        for month in months:
        # iterate through each month
            state_dict[state[0]['SUBDIVISION']][month] = sum(0 if item[month]=='NA' else float(item[month]) for item in state)
            # calculate total number of rain for each month for each subdivision
    for state in state_dict:
        sorted_rain = sorted(state_dict[state],key=state_dict[state].get)[:4]
        # get month by lower rain for each subdivision
        for r in sorted_rain:
            rain_months[r] += 1
            # calculate month have lower rain 
    lower_rain_month = sorted(rain_months,key=rain_months.get,reverse=True)[:4]
    # get overall lower rain
    print(lower_rain_month)