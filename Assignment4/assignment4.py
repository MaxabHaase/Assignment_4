# Import required packages
import os
import pandas as pd
import re
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D
script_dir = os.path.dirname(__file__)

# Define the regular expressions to be used to parse Sample ID column
regex = r"(\d{5}) ([Vv]\d{1})\s+(\d+)"
stand = r"([a-zA-Z]+) (\d+)"
stand_2 = r"([a-zA-Z]+)(\d+)"
stand_3 = r"([a-zA-Z]+) (\s+) (\d+)"
vander = r"(\d+\s[A-Z]+\s[a-zA-Z]+) ([V]\d{1}) (\d+)"
two_numbers = r"(\d{5})\s+(\d+)"
healthy = r"([a-zA-Z]+\s[a-zA-Z]+) (\d+)"
no_space = r"(\d{5}) ([Vv]\d{1})(\d+)"


# Temporary code used to read in excel file as a pandas data frame
sheet = '/Users/maxhaase/Desktop/Grad_School/Fall_2017/Intro_to_programming/Files/Assignment_4/Assignment4/06222016 Staph Array Data.xlsx'
excel = pd.read_excel(sheet, sheetname=None, header=1)
excel_plate1 = excel['Plate 1']
print(type(excel))


# Functions

def read_in_excel(excel_file):
    plates = []
    excel = pd.read_excel(excel_file, sheetname=None, header=1)
    for key in excel.keys():
        plates.append(key)
    return plates
# Get the name of the plates and add to a list


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
        match7 = re.search(no_space, items)
        if match1 and match6:
            match1 = None
        if match4 and match7:
            match4 = None
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
            continue
        if match7:
            temp_dict['PatientID'].append(match7.group(1))
            temp_dict['Replicate'].append(match7.group(2))
            temp_dict['Dilution'].append(match7.group(3))
            # print(items)

    data_frame = data_frame.join(pd.DataFrame(temp_dict, index=data_frame.index))
    # print(temp_dict)
    return data_frame
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


def plotter(plate, dataframe):
    results_dir = os.path.join(script_dir, '{}/'.format(plate))
    unique_samples = dataframe[plate]["PatientID"].unique()
    rows = list(dataframe[plate])[4:53]
    # names = list(dataframe[plate])[1:3]
    for x in unique_samples:
        print("Plotting for subject {}".format(x))
        for row in rows:
            index = dataframe[plate].loc[dataframe[plate]['PatientID'] == x].index
            index_min = min(index)
            index_max = max(index)
            # print(row, x, index_min, index_max)
            unique_reps = dataframe[plate]["Replicate"][index_min:index_max].unique()
            plt.close()
            plt.grid(True)
            plt.title('{} {}'.format(x, row))
            plt.ylabel('Intensity')
            plt.xlabel('Dilution')
            for rep in unique_reps:
                index_ = dataframe[plate].loc[
                    (dataframe[plate]['PatientID'] == x) & (dataframe[plate]["Replicate"] == rep)].index
                index_min_ = min(index_)
                index_max_ = max(index_)
                # print(index)
                x_ = (dataframe[plate]["Dilution"][index_min_:index_max_ + 1].values.tolist())
                x_ = [float(i) for i in x_]
                # print(x_)
                y = dataframe[plate][row][index_min_:index_max_ + 1].values.tolist()
                # print(y)
                # plt.plot(x_, y)
                line, = plt.loglog(x_, y, marker='o', basex=10, label=rep)
                plt.legend(handler_map={line: HandlerLine2D(numpoints=4)})
            if not os.path.isdir(results_dir):
                os.makedirs(results_dir)
            fig = plt.gcf()
            fig.savefig(results_dir + '{}-{}.png'.format(x, row))
# function that plots log intensity/log dilution for each subject/row. IT IS VERY SLOW!
# 1. take in arguments for the excel sheet and plate number
# 2. Set a path to put the out put pngs
# 3. Get a list of unique subjects in the plate
# 4. Get the column names for the plots
# 5. loop through each Patient
# 6. loop through each row, for the Patient
# 7. get the index values (rows) of current Patient, get the max/min values
# 8. get the number of visits
# 9. loop through the visits
# 10. Get the indices for the visits, get max/min
# 11. get the x/y values for the indices of the current visit.
# 12. plot the line log/log graph of x/y values
# 13. add folder with plate name and add graphs of that plate to the folder
# 14. save figure.


# Call function to get list of plate names from excel file.
plates = read_in_excel(sheet)
# print(plates)

# loop over each plate name, calling parse_excel and updating the plate data frames
for plate in plates:
    # print(plate)
    excel[plate] = parse_excel(plate, sheet)
    print(plate)
    plotter(plate, excel)
