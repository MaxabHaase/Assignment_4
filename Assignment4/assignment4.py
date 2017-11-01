import pandas as pd
import re
import pprint


sheet = '/Users/maxhaase/Desktop/Grad_School/Fall_2017/Intro_to_programming/Files/Assignment_4/Assignment4/06222016 Staph Array Data.xlsx'
excel = pd.read_excel(sheet, sheetname=None, header=1)

print(excel.keys())

excel_plate1 = excel['Plate 1']

# df = excel_plate1['Sample ID'].str.extract('(?P<PatientID>\d{5})')
# excel_plate1['PatientID'] = df
# df = excel_plate1['Sample ID'].str.extract('(?P<Replicate>[V]\d{1})')
# excel_plate1['Replicate'] = df
# df = excel_plate1['Sample ID'].str.extract('(?P<Dilution>\d{0})')
# excel_plate1['Dilution'] = df
# print(excel_plate1)


regex = r"(\d{5}) ([V]\d{1}) (\d+)"
stand = r"([a-zA-Z]+) (\d+)"
vander = r"(\d+\s[A-Z]+\s[a-zA-Z]+) ([V]\d{1}) (\d+)"






def parse_excel(data_frame):
    sample = excel_plate1['Sample ID']
    temp_dict = {'PatientID': [], 'Replicate': [], 'Dilution': []}
    for items in sample:
        match0 = re.search(regex, items)
        match1 = re.search(stand, items)
        match2 = re.search(vander, items)
        if match0:
            temp_dict['PatientID'].append(match0.group(1))
            temp_dict['Replicate'].append(match0.group(2))
            temp_dict['Dilution'].append(match0.group(3))
            print(items)
            print(match0)
            print(match0.group(0))
            print(match0.group(1))
            print(match0.group(2))
            print(match0.group(3))
        if match1:
            temp_dict['PatientID'].append(match1.group(1))
            temp_dict['Replicate'].append('NaN')
            temp_dict['Dilution'].append(match1.group(2))
            print(items)
            print(match1)
            print(match1.group(0))
            print(match1.group(1))
            print(match1.group(2))
        if match2:
            temp_dict['PatientID'].append(match2.group(1))
            temp_dict['Replicate'].append(match2.group(2))
            temp_dict['Dilution'].append(match2.group(3))
            print(items)
            print(match2)
            print(match2.group(0))
            print(match2.group(1))
            print(match2.group(2))
            print(match2.group(3))
    pprint.pprint(temp_dict)
#
# def split_(item):
#     d = {'PatientID ': [], 'Replicate': [], 'Dilution': []}
#     for chr in item:
#         if chr == '\s':
#
#
#         list += chr



parse_excel(excel_plate1)


