import pandas as pd
import re
from pathlib import Path

def clean_text(text):
    if pd.isna(text):
        return ''
    # Remove extra spaces between words
    text = re.sub(r'\s+', ' ', text)
    # Remove multiple hyphens and keep only one
    text = re.sub(r'-+', '-', text)
    # Remove spaces around hyphens
    text = re.sub(r'\s*-\s*', '-', text)
    # Remove leading and trailing spaces
    text = text.strip()
    # Remove the word "-NULL"
    text = text.replace('-NULL', '')
    return text

def clean_dataframe(df):
    # Apply clean_text function to each cell in the DataFrame
    return df.applymap(lambda x: clean_text(x) if isinstance(x, str) else x)

# Construct the path to the Excel file
current_file_path = Path(__file__)
parent_directory = current_file_path.parent.parent
report_dir = parent_directory / 'Files'
input_file = report_dir / 'HDFC Bank statment 1.xls'

# Load the Excel file
df = pd.read_excel(input_file, engine='xlrd')
# Select the first 100 rows
df = df.head(100)

# Clean the DataFrame
cleaned_df = clean_dataframe(df)

# Specify the output file path in the 'Files' directory
output_file = report_dir / 'clean_data.csv'

# Save the cleaned DataFrame to a CSV file in the 'Files' directory
cleaned_df.to_csv(output_file, index=False)

print(f"Cleaned data saved to {output_file}")
