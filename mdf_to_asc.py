import asammdf

# Open the MDF4 file
mdf_file = asammdf.MDF("input_file.mdf")

# Create a new ASC file for writing
asc_file = open("output_file.asc", "w")

# Loop through the channels in the MDF file
for channel in mdf_file.iter_channels():
    asc_file.write(f"{channel.name} ({channel.unit})\n")
    timestamps = channel.timestamps
    values = channel.samples
    for i in range(len(timestamps)):
        timestamp = timestamps[i]
        value = values[i]
        asc_file.write(f"{timestamp:.6f} {value:.6f}\n")
    asc_file.write("\n")

# Close the ASC file
asc_file.close()
