# Import required packages
import pandas as pd
import re

# Define the regular expressions to be used to parse Sample ID column
regex = r"(\d{5}) ([Vv]\d{1})\s+(\d+)"
stand = r"([a-zA-Z]+) (\d+)"
stand_2 = r"([a-zA-Z]+)(\d+)"
stand_3 = r"([a-zA-Z]+) (\s+) (\d+)"
vander = r"(\d+\s[A-Z]+\s[a-zA-Z]+) ([V]\d{1}) (\d+)"
two_numbers = r"(\d{5})\s+(\d+)"
healthy = r"([a-zA-Z]+\s[a-zA-Z]+) (\d+)"


# Temporary code used to read in excel file as a pandas data frame
sheet = '/Users/maxhaase/Desktop/Grad_School/Fall_2017/Intro_to_programming/Files/Assignment_4/Assignment4/06222016 Staph Array Data.xlsx'
excel = pd.read_excel(sheet, sheetname=None, header=1)
excel_plate1 = excel['Plate 1']
print(type(excel))


# Functions

# Get the name of the plates and add to a list
def read_in_excel(excel_file):
    plates = []
    excel = pd.read_excel(excel_file, sheetname=None, header=1)
    for key in excel.keys():
        plates.append(key)
    return plates


# function to parse first column and add three columns PatientID, Replicate, and Dilution to the original data frame
# 1. take in the plate name and the excel sheet file path as arguments.
# 2. Create a data frame consisting of the plate values
# 3. Create a variable for the values in the column "Sample ID"
# 4. Set a temp dictionary to with keys of the values we want to get from "Sample ID"
# 5. Loop over each row in "Sample ID"
# 6. Search each row with all defined regular expressions, since match 1 and match 6 are similar if
# both are true, set match 1 = None
# 7. If match is True update the values of the temp dict with the values of the groups
# 8. join the temp dict to the data frame and return.
def parse_excel(plate, dataframe):
    data_frame = pd.read_excel(dataframe, sheetname=plate, header=1)
    sample = data_frame['Sample ID']
    temp_dict = {'PatientID': [], 'Replicate': [], 'Dilution': []}
    for items in sample:
        match0 = re.search(regex, items)
        match1 = re.search(stand, items)
        match2 = re.search(vander, items)
        match3 = re.search(two_numbers, items)
        match4 = re.search(stand_2, items)
        match5 = re.search(stand_3, items)
        match6 = re.search(healthy, items)
        if match1 and match6:
            match1 = None
        if match0:
            temp_dict['PatientID'].append(match0.group(1))
            temp_dict['Replicate'].append(match0.group(2))
            temp_dict['Dilution'].append(match0.group(3))
            continue
            # print(items)
            # print(match0)
            # print(match0.group(0))
            # print(match0.group(1))
            # print(match0.group(2))
            # print(match0.group(3))
        if match1:
            temp_dict['PatientID'].append(match1.group(1))
            temp_dict['Replicate'].append('NaN')
            temp_dict['Dilution'].append(match1.group(2))
            continue
            # print(items)
            # print(match1)
            # print(match1.group(0))
            # print(match1.group(1))
            # print(match1.group(2))
        if match2:
            temp_dict['PatientID'].append(match2.group(1))
            temp_dict['Replicate'].append(match2.group(2))
            temp_dict['Dilution'].append(match2.group(3))
            continue
            # print(items)
            # print(match2)
            # print(match2.group(0))
            # print(match2.group(1))
            # print(match2.group(2))
            # print(match2.group(3))
        if match3:
            temp_dict['PatientID'].append(match3.group(1))
            temp_dict['Replicate'].append('NaN')
            temp_dict['Dilution'].append(match3.group(2))
            continue
        if match4:
            temp_dict['PatientID'].append(match4.group(1))
            temp_dict['Replicate'].append('NaN')
            temp_dict['Dilution'].append(match4.group(2))
            continue
        if match5:
            temp_dict['PatientID'].append(match5.group(1))
            temp_dict['Replicate'].append('NaN')
            temp_dict['Dilution'].append(match5.group(3))
            continue
        if match6:
            temp_dict['PatientID'].append(match6.group(1))
            temp_dict['Replicate'].append('NaN')
            temp_dict['Dilution'].append(match6.group(2))

    data_frame = data_frame.join(pd.DataFrame(temp_dict, index=data_frame.index))
    return data_frame


# Call function to get list of plate names from excel file.
plates = read_in_excel(sheet)
print(plates)

# loop over each plate name, calling parse_excel and updating the plate data frames
for plate in plates:
    print(plate)
    excel[plate] = parse_excel(plate, sheet)
print(excel)


# dict = {}
# for plate in plates:
#     dataframe_temp = parse_excel(plate, sheet)
#     dict[plate] = pd.DataFrame(dataframe_temp)
# print(dict)


