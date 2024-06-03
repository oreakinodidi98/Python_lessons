# imports 
import pandas as pd
import datetime as dt

# list of all the excell files i will be using
excell_files = ["Unstaffed_Details.xlsx","Linked _Delivery_Details.xlsx", "Accreditations_by_Deliveries.xlsx"]
#combine all exccell files to 1 data file 
combined_excell = pd.DataFrame()

# loop through all the excell files and append them to the combined_excell file

for file in excell_files:
    data = pd.read_excel(file)
    # adjusting the Accreditation Date column to a datetime format, to only show the year, month and day
    data["Accreditation Date"] = data["Accreditation Date"].dt.date
    combined_excell = combined_excell.append(data, ignore_index=True)

# export the combined_excell file to a new excell file
combined_excell.to_excel("combined_excell.xlsx", index=False, sheet_name="combined_excell")