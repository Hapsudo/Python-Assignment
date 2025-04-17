# File Read and Write Challenge
def process_file():
    try:
        # Opening the file and reading the content
        source = open("week4.txt", "r")
        lines = source.readline()
        source.close()

        # Modifying the content
        updated_file = [line.upper() for line in lines]

        # Write modified count to a new file
        result = open("process.txt", "w")
        result.write("UPDATED TEXT:\n")
        result.writelines(updated_file)
        result.close()

        print("File processed successfully. Check the 'updated.text' for reference.")

    except FileNotFoundError:
        print("File does not exist please recheck the name")

# Error Handling Lab for filename
def read_file():
    # Ask the user to enter a filename
    filename = input("Enter the filename you want to read (e.g., name.txt): ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("\n File Content:\n")
            print(content)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the function
read_file()
