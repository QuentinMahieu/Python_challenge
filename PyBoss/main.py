#import the modules
import pandas as pd 
from datetime import datetime
import re
from abbrevations import us_state_abb

#import the file
filepath = "employee_data.csv"
data = pd.read_csv(filepath, delimiter =",")

#First we split the column "Name"
splittedName = data["Name"].str.split(" ",n =1, expand = True )
data["First Name"] = splittedName[0]
data["Last Name"] = splittedName[1]

#dropping the old name column in the actual data frame(inplace) and reorganise the data
data.drop(columns = ["Name"], inplace = True)
#reorder the data
data = data[["Emp ID","First Name","Last Name","DOB","SSN","State"]]

#formatting dates by conerting the column to datetime and adding the format we want
data["DOB"] = pd.to_datetime(data["DOB"])
data["DOB"] = data["DOB"].dt.strftime("%m/%d/%y")

#hide the 5 first SSN numbr with a pattern (using the re module)
data["SSN"] = data["SSN"].apply(lambda x: re.sub(r'\d', '*', x, count=5))

#replace the last stats column with their abbrevation
state_abb = []
for state in data["State"]:
    abb = us_state_abb[state] 
    state_abb.append(abb)
data["State abb"] = state_abb

#dropping the old State data frame, and rename the Sate abb in state
data.drop(columns = ["State"], inplace = True)
data.rename(columns = {"State abb" : "State"}, inplace = True)

outputpath = "employee_data_formatted.csv"
data.to_csv(outputpath, index = False)
