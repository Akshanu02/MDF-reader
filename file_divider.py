import os

# Define the path to your big file and the directory where you want to save the smaller files.
input_file_path = "/home/ttl_admin/mdf_reader/Test_9_normal.mdf"
output_directory = "/home/ttl_admin/mdf_reader"

# Ensure the output directory exists, create it if it doesn't.
os.makedirs(output_directory, exist_ok=True)

# Open the input file in binary mode.
with open(input_file_path, 'rb') as input_file:
    # Read the binary contents of the input file.
    file_contents = input_file.read()

# Calculate the size of each smaller file.
chunk_size = len(file_contents) // 20

# Split the file contents into 20 smaller pieces.
smaller_files = [file_contents[i:i + chunk_size] for i in range(0, len(file_contents), chunk_size)]

# Save each smaller piece as a separate file.
for i, smaller_file_contents in enumerate(smaller_files, start=1):
    smaller_file_path = os.path.join(output_directory, f'smaller_file_{i}.mdf')
    with open(smaller_file_path, 'wb') as smaller_file:
        smaller_file.write(smaller_file_contents)
    print(f'Saved {smaller_file_path}')

print("Done")
