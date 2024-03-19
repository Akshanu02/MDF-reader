import asammdf

# Define the path to the MDF file
mdf_file_path = "Test_9_normal.mdf"

# Open the MDF file
mdf = asammdf.MDF(mdf_file_path)

# List all available signals
signals = mdf.channels_db.keys()

# Loop through signals and extract data
for signal in signals:
    data = mdf[signal].samples
    print(f"Signal: {signal}")
    print(f"Data: {data}")
    print("\n")
