import asammdf

def extract_signal_names(mdf_file_path, output_file_path):
    # Open the MDF file
    mdf = asammdf.MDF(mdf_file_path)

    # Extract the signal names
    signal_names = [channel.name for channel in mdf.iter_channels()]

    # Write the signal names to an output file
    with open(output_file_path, "w") as output_file:
        for name in signal_names:
            output_file.write(name + "\n")

if __name__ == "__main__":
    mdf_file_path = "Test_9_normal.mdf"  # Replace with the path to your .mdf file
    output_file_path = "output_signal_names.txt"  # Replace with the desired output file path

    extract_signal_names(mdf_file_path, output_file_path)
