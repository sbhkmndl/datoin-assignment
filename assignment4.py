'''
Display the top 3 months on which KERALA state usually gets higher rainfall than other months.
'''

import json

with open('rainfall_india_1901-2015.jl','r') as fr:
    rain_months = {'JAN':0.0,'FEB':0.0,'MAR':0.0,'APR':0.0,'MAY':0.0,'JUN':0.0,'JUL':0.0,'AUG':0.0,'SEP':0.0,'OCT':0.0,'NOV':0.0,'DEC':0.0}
    # initiate rain for each month
    karnataka_dict = [json.loads(line) for line in fr if 'KARNATAKA' in line]
    # get sibdivision of Karnataka 
    for subdiv in karnataka_dict:
        for season in rain_months:
        #  iterate through every sason
            rain_months[season] += 0 if subdiv[season]=='NA' else float(subdiv[season])
            # calculate total rane for every month
    higher_rain = sorted(rain_months,key=rain_months.get,reverse=True) 
    # sort by higher rain
    print(higher_rain[:3])