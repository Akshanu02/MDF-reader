import mdfreader
import canmatrix

# Define the paths to your MDF and ASC files
mdf_file_path = 'smaller_file_1.mdf'
asc_file_path = 'output1.asc'

# Function to convert MDF to ASC
def convert_mdf_to_asc(mdf_file, asc_file):
    # Read MDF file
    mdf = mdfreader.Mdf(mdf_file)

    # Create an empty CAN matrix
    can_matrix = canmatrix.CanMatrix()

    # Loop through all signals and add them to the CAN matrix
    for signal in mdf.signals():
        message = can_matrix.add_signal(
            name=signal.name,
            size=signal.signalsize,
            is_little_endian=signal.is_little_endian,
            byte_order=1 if signal.is_little_endian else 0,
        )

        # Define the start and end bit positions
        start_bit = signal.startbit
        end_bit = signal.startbit + signal.signalsize - 1

        message.add_signal(
            name=signal.name,
            start_bit=start_bit,
            size=signal.signalsize,
            is_little_endian=signal.is_little_endian,
        )

    # Export the CAN matrix to ASC format
    canmatrix.formats.dump(
        can_matrix, asc_file, 'asc', bit_fmt="big_endian", extended=True
    )

if __name__ == "__main__":
    convert_mdf_to_asc(mdf_file_path, asc_file_path)
    print(f"Conversion complete. Output written to {asc_file_path}")
