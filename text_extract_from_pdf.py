import pytesseract
from pdf2image import convert_from_path

# Path to the PDF file
pdf_path = 'SG Fintech 2023_R3.pdf'

# Convert PDF to images
pages = convert_from_path(pdf_path)

# Initialize an empty list to store company names
company_names = []

# Iterate through each page and extract text from images
for page in pages:
    text = pytesseract.image_to_string(page)
    company_names.append(text)

# Write the extracted company names to a text file
with open('company_names.txt', 'w') as f:
    for name in company_names:
        f.write(name + '\n')

print("Company names have been extracted and saved to company_names.txt")