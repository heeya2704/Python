# Use re.sub() to replace all email addresses in a string with '[hidden email]' 
# and print the modified string.
# Constraint: Do not use any external libraries except re.

import re

text = "Please reach out to support@swiggy.com or contact manager.alex@company.org for assistance."

email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

masked_text = re.sub(email_pattern, '[hidden email]', text)

print("Original Text:")
print(text)
print("\nMasked Text:")
print(masked_text)
