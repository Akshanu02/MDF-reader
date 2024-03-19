import can

def asc_to_blf(asc_file, blf_file):
    with open(asc_file, 'r') as asc_file:
        # Create a BLF log file
        log = can.BLFWriter(blf_file)

        # Skip the header row
        next(asc_file, None)

        # Read the ASC data and convert it to BLF
        for line in asc_file:
            parts = line.strip().split()
            if len(parts) >= 8:
                timestamp = float(parts[0])
                channel = int(parts[2])
                message_id = int(parts[3])
                dlc = int(parts[4])
                data = bytearray([int(float(x)) for x in parts[5:]])  # Parse data as integers

                msg = can.Message(
                    arbitration_id=message_id,
                    data=data,
                    is_extended_id=False,
                    dlc=dlc,
                    timestamp=timestamp,
                )
                log.on_message_received(msg)

    print(f"Conversion completed. Converted data saved to {blf_file}")

if __name__ == "__main__":
    asc_file = "output_11.asc"  # Change to your ASC file name
    blf_file = "output.blf"  # Change to your desired BLF file name
    asc_to_blf(asc_file, blf_file)
