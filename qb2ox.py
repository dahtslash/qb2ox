import re

# Read the entire input file
with open('input.txt', 'r') as file:
    content = file.read()

# Updated regex pattern to match items with flexible spacing
# Added '-' to the character class so that hyphens in item names are included.
item_pattern = re.compile(
    r'\s*([\w\-\[\]\'"]+)\s*=\s*\{(.*?)\},?', re.DOTALL
)

# Corrected regex for key-value pairs (handles optional commas, spaces, and line breaks)
attribute_pattern = re.compile(
    r'\s*[\[\]\'"]*([\w_]+)[\[\]\'"]*\s*=\s*(?:"([^"]*)"|\'([^\']*)\'|([^,\n\}]+))\s*(?:,|$)'
)

# Process items
output = []

for item_match in item_pattern.finditer(content):
    # Remove the enclosing brackets/quotes to get the clean item name.
    item_name = item_match.group(1).strip("[]'\"")
    attributes = item_match.group(2)

    # Extract key-value pairs.
    attribute_pairs = attribute_pattern.findall(attributes)
    attr_dict = {
        key: (val1 or val2 or val3).strip()
        for key, val1, val2, val3 in attribute_pairs
    }

    # Check required fields: label and weight are required.
    label = attr_dict.get('label')
    weight = attr_dict.get('weight')
    # If shouldClose is missing, default it to 'false'
    shouldClose = attr_dict.get('shouldClose', 'false')

    if label and weight:
        output.append(f"['{item_name}'] = {{\n"
                      f"    label = '{label}',\n"
                      f"    weight = {weight},\n"
                      f"    stack = false,\n"
                      f"    close = {shouldClose}\n"
                      f"}},\n")

# Write output to output.lua
with open('output.lua', 'w') as file:
    file.writelines(output)

