import pandas as pd
from datetime import datetime

# Read the CSV file into a DataFrame with UTF-8 encoding
df = pd.read_csv('book_data.csv', encoding='utf-8')

# Handle missing values (replace with 0 in this example)
df['distribution_expense'].fillna(0, inplace=True)

# Function to parse and reformat dates
def parse_and_reformat_date(date_str):
    date_formats = ['%d-%m-%Y', '%m-%d-%Y', '%Y-%m-%d', '%m/%d/%Y', '%d/%m/%Y', '%m/%d/%Y']
    for date_format in date_formats:
        try:
            return datetime.strptime(date_str, date_format).strftime('%Y-%m-%d')
        except ValueError:
            pass
    # Return the current date if none of the formats match
    return datetime.now().strftime('%Y-%m-%d')

# Apply the date parsing function to the date column
df['published_date'] = df['published_date'].apply(parse_and_reformat_date)

# Save the cleaned data to a new CSV file
df.to_csv('cleaned_book_data.csv', index=False)

print("Data cleaned and saved to 'cleaned_book_data.csv'.")
