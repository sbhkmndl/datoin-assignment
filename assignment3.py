import json
from itertools import groupby

with open('rainfall_india_1901-2015.jl','r') as file_json_lines:
    karnataka_dict = [json.loads(line) for line in file_json_lines if 'KARNATAKA' in line]
    group_divs = [list(gr) for key, gr in groupby(karnataka_dict,lambda x:x['SUBDIVISION'])]
    all_group_divs = list()
    for state in group_divs:
        total_rain = sum(0 if item['ANNUAL']=='NA' else float(item['ANNUAL']) for item in state)
        total_sub = len(state)
        state_name = state[0]['SUBDIVISION']
        all_group_divs.append([state_name,total_rain/total_sub])
    print(sorted(all_group_divs,key=lambda k:k[1],reverse=True))
