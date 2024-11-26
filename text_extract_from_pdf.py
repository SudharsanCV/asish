import pytesseract
from pdf2image import convert_from_path
import re

# Path to the PDF file
pdf_path = 'SG Fintech 2023_R3.pdf'

# Convert PDF to images
pages = convert_from_path(pdf_path)

# Initialize an empty list to store company names
company_names = []

# Define a function to clean and extract company names
def extract_company_names(text):
    # Split text into lines and remove unnecessary whitespaces
    lines = text.split('\n')
    # Filter lines with plausible company name characteristics
    names = [line.strip() for line in lines if len(line.strip()) > 1 and not line.isnumeric()]
    return names

# Iterate through each page and extract text from images
for page in pages:
    text = pytesseract.image_to_string(page)
    company_names.extend(extract_company_names(text))

# Remove duplicates and sort the names
unique_company_names = sorted(set(company_names))

# Write the extracted company names to a text file
with open('company_names.txt', 'w') as f:
    for name in unique_company_names:
        f.write(name + '\n')

print("Company names have been extracted and saved to company_names.txt")
