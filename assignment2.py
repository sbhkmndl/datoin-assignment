import json

with open('rainfall_india_1901-2015.jl','r') as file_json_lines:
    total_rainfall = 0.0
    total_no_div = 0
    for line in file_json_lines:
        state_dict = json.loads(line)  
        #load each line from rainfall_india_1901-2015.jl as python dictionary
        if state_dict['SUBDIVISION'] == 'COASTAL KARNATAKA':
        #if state is 'COASTAL KARNATAKA' then do something
            if state_dict['ANNUAL'] != 'NA':
            #some field has 'NA' value
                total_rainfall += float(state_dict['ANNUAL'])
            total_no_div += 1
    print(total_rainfall/total_no_div)
        