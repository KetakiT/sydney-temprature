Following instructions are specific to Windows10. 
However, the program can be run on MacOS and Linux provided that Python3 and pytest are installed.

1. Install the latest python3 - use default installation
	https://www.python.org/downloads/

	Make sure environment variable PATH contains below paths where .... is the location where python is installed 
	....\Python\Python39\ and ....\Python\Python39\Scripts\

2. Install pytest using below command in command prompt
	pip install -U pytest
	
	Refer to the link below if needed
	https://docs.pytest.org/en/stable/getting-started.html

3. Files needed 
	Program file 
		SydneyTemprature.py
	Input files required to run the tests(in the same folder as program file) 
		sydney-temperature.csv
		sydney-temperature_3.csv
		sydney-temperature_4.csv

4. How to run the program

	* Open command prompt 
	* Change directory to the folder where python script and input files are located
	  Alternatively, provide absolute paths for both, the script and the input file

	* To run the program
		py SydneyTemprature.py sydney-temperature.csv

	* To run the tests
		pytest SydneyTemprature.py

	
	Sample outputs 

		C:\Coates>pytest SydneyTemprature.py
		============================================================= test session starts ==============================================================
		platform win32 -- Python 3.9.0, pytest-6.1.2, py-1.9.0, pluggy-0.13.1
		rootdir: C:\Coates
		collected 4 items

		SydneyTemprature.py ....                                                                                                                  [100%]

		============================================================== 4 passed in 0.04s ===============================================================

		C:\Coates>py SydneyTemprature.py sydney-temperature.csv
		February 7.0
