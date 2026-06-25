import pandas as pd

# Load dataset
df = pd.read_excel("data/customer_call_list.xlsx")

# Remove duplicate rows
df = df.drop_duplicates()

# Drop irrelevant column
df = df.drop(columns='Not_Useful_Column')

# Clean last names — strip trailing punctuation
df['Last_Name'] = df['Last_Name'].str.strip('/._')

# Format phone numbers to XXX-XXX-XXXX
df['Phone_Number'] = df['Phone_Number'].str.replace('[^a-zA-Z0-9]', '', regex=True)
df['Phone_Number'] = df['Phone_Number'].apply(lambda x: str(x))
df['Phone_Number'] = df['Phone_Number'].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10])
df['Phone_Number'] = df['Phone_Number'].str.replace('Na|Nan', '', regex=True)
df['Phone_Number'] = df['Phone_Number'].str.replace('--', '', regex=False)

# Split address into separate columns
df[['Street_Address', 'State', 'Zip_Code']] = df['Address'].str.split(',', expand=True)

# Standardize Yes/No columns to Y/N
df['Paying Customer'] = df['Paying Customer'].str.replace('Yes', 'Y').str.replace('No', 'N')
df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('Yes', 'Y').str.replace('No', 'N')

# Replace null-like values with empty string
df = df.replace({'N/a': '', 'Na': '', 'nan': ''})
df = df.fillna('')

# Default empty Do_Not_Contact to N
df['Do_Not_Contact'] = df['Do_Not_Contact'].replace('', 'N')

# Remove rows where Do_Not_Contact is Y
df = df[df['Do_Not_Contact'] != 'Y']

# Remove rows with no phone number
df = df[df['Phone_Number'] != '']

# Reset index
df = df.reset_index(drop=True)
