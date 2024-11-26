import re

# Read the uncleaned text file
with open('company_names.txt', 'r') as file:
    raw_text = file.read()

# Define a function to clean and extract company names
def clean_company_names(text):
    # Split text into lines
    lines = text.split('\n')
    
    # Initialize an empty list for cleaned company names
    cleaned_names = []
    
    for line in lines:
        # Remove special characters and extra spaces
        line = re.sub(r'[^\w\s&.,]', '', line)  # Keep letters, numbers, spaces, and some symbols
        line = line.strip()  # Remove leading/trailing spaces
        
        # Exclude lines that are too short or don't look like company names
        if len(line) > 2 and not line.isnumeric():
            cleaned_names.append(line)
    
    # Remove duplicates and sort the list
    return sorted(set(cleaned_names))

# Clean the company names
cleaned_company_names = clean_company_names(raw_text)

# Write the cleaned company names to a new text file
with open('cleaned_company_names.txt', 'w') as file:
    for name in cleaned_company_names:
        file.write(name + '\n')

print("Cleaned company names have been saved to cleaned_company_names.txt")
