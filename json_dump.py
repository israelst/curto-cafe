# -*- coding: utf-8 -*-

import csv
import json


data = {}
data2 = []
with file('output.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    csv_reader.next() #skip header
    for row in csv_reader:
        path, sheet, time, temp, flame = row
        print path, sheet, time, temp, flame
        _id = '{},{}'.format(path,sheet)
        data.setdefault(_id, [])
        data[_id].append({'time': float(time), 'temp': float(temp.replace("'", ""))})

        data2.append({'time': float(time), _id: float(temp.replace("'", ""))})

#with file('data.js', 'w') as js_file:
#    json.dump(data, js_file)

with file('data2.js', 'w') as js_file:
    json.dump(data2, js_file)
