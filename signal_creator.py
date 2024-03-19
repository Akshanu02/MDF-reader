# Define the number of lines you want to generate
num_lines = 1481

# Define the input file containing signal names
input_signal_file = "signal_names.txt"

# Define the output file name
output_file = "output.txt"

# Read signal names from the input file
with open(input_signal_file, "r") as signal_file:
    signal_names = [line.strip() for line in signal_file.readlines()]

# Open the output file for writing
with open(output_file, "w") as file:
    for i in range(1, num_lines + 1):
        if i <= len(signal_names):
            signals = [f'"{signal_names[i-1]}"']
        else:
            signals = ['']

        line = f'{{"name": "Signal Group #{i}", "signals": [{", ".join(signals)}]}}'

        file.write(line + "\n")

print(f"{num_lines} lines generated and saved to {output_file}")
