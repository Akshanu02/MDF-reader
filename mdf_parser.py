import mdfreader

# Define the path to your MDF file
mdf_file_path = 'smaller_file_1.mdf'

# Function to read and parse MDF file into CAN messages
def read_and_parse_mdf(mdf_file):
    try:
        mdf = mdfreader.Mdf(mdf_file)

        # Initialize a dictionary to store the parsed CAN messages
        can_messages = {}

        # Loop through all signals and create CAN messages
        for signal in mdf.signals():
            message_id = signal.msgid
            if message_id not in can_messages:
                can_messages[message_id] = []

            can_messages[message_id].append({
                "name": signal.name,
                "value": signal.values,
                "timestamp": signal.timestamps,
            })

        # Print the parsed CAN messages
        for message_id, signals in can_messages.items():
            print(f"CAN Message ID: {message_id}")
            for signal in signals:
                print(f"Signal Name: {signal['name']}")
                print(f"Values: {signal['value']}")
                print(f"Timestamps: {signal['timestamp']}")
                print()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    read_and_parse_mdf(mdf_file_path)
