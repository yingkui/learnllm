import csv

# Define the input and output file paths
input_file = '/Users/hang/Documents/learnllm/src/xingxings/data/temp.md'
output_file = '/Users/hang/Documents/learnllm/src/xingxings/data/ft.csv'

# Initialize lists to store input and output data
inputs = []
outputs = []

# Read the input file
with open(input_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Process the lines to extract input and output data
for i in range(len(lines)):
    if lines[i].startswith('###'):
        input_line = lines[i].strip().replace('### ', '')
        output_line = lines[i + 2].strip()
        inputs.append(input_line)
        outputs.append(output_line)
        print(output_line)

# Write the data to the CSV file
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['input', 'output'])
    for input_text, output_text in zip(inputs, outputs):
        writer.writerow([input_text, output_text])

print("Data has been successfully written to ft.csv")