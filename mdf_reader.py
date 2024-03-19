import mdfreader

# Path to the MDF file
mdf_file_path = "/home/ttl_admin/mdf_reader/smaller_file_1.mdf"

# Load the MDF file
mdf = mdfreader.Mdf(mdf_file_path)

# List all the available channels in the MDF file
channels = mdf.list_channels()

# Print the names of the channels
print("Available Channels:")
for channel in channels:
    print(channel)

# Read and extract data for a specific channel
# Replace 'Your_Channel_Name' with the name of the channel you want to extract
channel_name = "Your_Channel_Name"

if channel_name in channels:
    data = mdf.get_channel_data(channel_name)
    print(f"Data for channel '{channel_name}':")
    print(data)
else:
    print(f"Channel '{channel_name}' not found in the MDF file.")

# Close the MDF file
mdf.close()
