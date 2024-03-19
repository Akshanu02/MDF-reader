import mdfreader

def extract_can_ids_from_mdf(mdf_file):
    can_ids = set()

    with mdfreader.MdfFile(mdf_file) as mdf:
        for signal in mdf.signals:
            if signal.bus_type == 'CAN':
                can_ids.add(signal.sig_type)

    return can_ids

def save_can_ids_to_file(can_ids, output_file):
    with open(output_file, 'w') as file:
        for can_id in can_ids:
            file.write(can_id + '\n')

if __name__ == "__main__":
    input_file = "Test_9_normal.mdf"  # Replace with your .mdf file path
    output_file = "unique_can_ids.txt"  # Specify the output file path

    can_ids = extract_can_ids_from_mdf(input_file)

    if can_ids:
        print("Unique CAN IDs found in the logged data:")
        for can_id in can_ids:
            print(can_id)

        save_can_ids_to_file(can_ids, output_file)
        print(f"Unique CAN IDs saved to {output_file}")
    else:
        print("No CAN IDs found in the logged data.")
