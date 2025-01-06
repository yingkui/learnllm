import json

# Define the input and output file paths
input_file = '/Users/hang/Documents/learnllm/src/xingxings/data/temp.md'
output_file = '/Users/hang/Documents/learnllm/src/xingxings/data/output.json'

# Initialize a list to store the JSON data
data = []

# Read the input file
with open(input_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Process the lines to extract instruction and output data
for i in range(len(lines)):
    if lines[i].startswith('###'):
        instruction = lines[i].strip().replace('### ', '')
        output = lines[i + 2].strip()
        data.append({
            'instruction': instruction,
            'output': output
        })

# Write the data to the JSON file
with open(output_file, 'w', encoding='utf-8') as jsonfile:
    json.dump(data, jsonfile, ensure_ascii=False, indent=4)

print("Data has been successfully written to output.json")