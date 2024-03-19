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

def list_arbitration_ids(mdf_file_path, output_file_path):
    # Open the MDF file
    mdf = asammdf.MDF(mdf_file_path)

    # Extract arbitration IDs and their respective channels
    arbitration_ids = {}
    for message in mdf:
        for signal in message.signals:
            arbitration_ids[signal.arbitration_id] = signal.name

    # Write the arbitration IDs and channels to an output file
    with open(output_file_path, "w") as output_file:
        for arbitration_id, channel_name in arbitration_ids.items():
            output_file.write(f"Arbitration ID: {arbitration_id}, Signal: {channel_name}\n")

if __name__ == "__main__":
    mdf_file_path = "smaller_file_1.dat"  # Replace with the path to your .mdf file
    signal_names_output_path = "output_signal_names.txt"  # Replace with the desired output file path for signal names
    arbitration_ids_output_path = "output_arbitration_ids.txt"  # Replace with the desired output file path for arbitration IDs

    extract_signal_names(mdf_file_path, signal_names_output_path)
    list_arbitration_ids(mdf_file_path, arbitration_ids_output_path)
