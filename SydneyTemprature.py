import csv
import os.path
import sys

def read_file(filename):
    """
    Inputs:
        filename - name of the file to read
    Outputs:
        Returns three lists for each column in the filename
        Months, Mean maximum temperature, Mean minimum temperature
    Assumptions:
        File type is comma seperated csv
        At least 3 columns are provided
        First column name is 'Month'
    """
    # Initialise three lists for months, mean maximum temprature and mean minimum temprature
    months, mean_max, mean_min = [], [], []

    # Return empty lists if filename does not exist
    if not os.path.isfile(filename):
        return (months, mean_max, mean_min)

    # Open csv file
    with open(filename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')

        # Skip rows before column names
        for skip in readCSV:
            if skip[0] == "Month":
                break
            else:
                next(readCSV)

        # Read columns into 3 lists
        for row in readCSV:
            months.append(row[0])
            mean_max.append(row[1])
            mean_min.append(row[2])

    return (months, mean_max, mean_min)

def find_smallest_temprature_spread(filename):
    """
    Inputs:
        filename - name of the file
    Outputs:
        Month with the smallest temprature spread
        Smallest temprature spread
    Assumptions:
        No empty or invalid values in the input file
    """
    # smallest temprature spread and month
    smallest_temp_spread = 1000
    smallest_temp_spread_month = ""

    # Read input csv file
    months, mean_max, mean_min = read_file(filename)

    # Return "File does not exist" if read_file returns empty lists
    if len(months) == 0:
        return "File does not exist"

    # Calculate temprature spread for each month by subtracting mean minimum temprature from mean maximum temprature
    for month in range(len(months)):

        # Remove '*' from temprature values
        temp_spread = float(mean_max[month].replace("*","")) - float(mean_min[month].replace("*",""))
        
        # Set smallest_temp_spread and month
        if temp_spread < smallest_temp_spread:
            smallest_temp_spread = temp_spread
            smallest_temp_spread_month = months[month]

    # Return string with month with smallest temprature spread and its spread value
    return smallest_temp_spread_month + " " + str(smallest_temp_spread)

# Testcase 1: Given input file as is
def testcase1_find_smallest_temprature_spread():
	assert find_smallest_temprature_spread("sydney-temperature.csv") == "February 7.0"

# Testcase 2: When input file does not exist	
def testcase2_negative():
    assert find_smallest_temprature_spread("invalid.csv") == "File does not exist"

# Testcase 3: Tempratures are in negatives and without *
def testcase3_find_smallest_temprature_spread():
    assert find_smallest_temprature_spread("sydney-temperature_3.csv") == "July 4.699999999999999"

# Testcase 4: File with just column names and actual values, 2 exact smallest spreads
def testcase4_find_smallest_temprature_spread():
    assert find_smallest_temprature_spread("sydney-temperature_4.csv") == "February 7.0"
	
# main function taking filename from the user	
def main():
    script = sys.argv[0]
    filename = sys.argv[1]
    print(find_smallest_temprature_spread(filename))

if __name__ == '__main__':
   main()
   
