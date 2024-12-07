
import sys

def textToLists(filename, sort=False):

    list1 = []
    list2 = []
    try:
        with open(filename) as input:
            for line in input:
                line = line.split() # remove whitespace and split line into 2 numbers
                list1.append(int(line[0]))
                list2.append(int(line[1]))
        if sort:
            list1.sort()
            list2.sort()
        return (list1, list2)
    
    # error handling below from Microsoft Copilot
    except FileNotFoundError:
        print("Error: The file was not found. Please check the file path and try again.")
        sys.exit(1)
    except PermissionError:
        print("Error: You do not have permission to access this file. Please check your permissions.")
        sys.exit(1)
    except IsADirectoryError:
        print("Error: The specified path is a directory, not a file. Please provide a file path.")
        sys.exit(1)
    except IOError as e:
        print(f"Error: An unexpected I/O error occurred. Details: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: An unexpected error occurred. Details: {e}")
        sys.exit(1)
