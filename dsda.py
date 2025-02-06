# Python script to create 300 text files with the naming pattern 17013490001.txt to 17013490300.txt

# Directory where the files will be created (optional, you can specify your path)
directory = "./"  # Use current directory for this example

# Loop through the range 1 to 300 to create files
for i in range(1, 301):
    # Creating the filename based on the pattern
    filename = f"1701349{i:03d}.txt"  # Format i as a 3-digit number (e.g., 001, 002, ...)
    
    # Construct the full path
    filepath = directory + filename
    
    # Open the file in write mode and create it
    with open(filepath, 'w') as file:
        file.write(f"This is file {filename}")  # You can customize the content here

    print(f"Created file: {filename}")

print("All files created successfully.")
