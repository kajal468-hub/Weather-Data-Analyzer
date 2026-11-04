🌦️ Weather Data Analyzer

1. Project Introduction

Weather Data Analyzer is a Python-based project that analyzes daily weather information stored in a CSV file.

It processes weather data such as date, temperature, humidity, and rainfall. It cleans the data, performs mathematical calculations, and displays graphical representations of weather trends.

2. Project Objective

The main objective of this project is to analyze weather information using Python libraries.

It helps users to:

- Calculate average temperature.
- Find maximum and minimum temperatures.
- Calculate standard deviation.
- Calculate total rainfall.
- Identify and remove duplicate records.
- Handle missing values.
- Visualize weather trends using graphs.

3. Technologies Used

The following technologies and libraries are used:

Technology| Purpose
Python 3| Main programming language
Pandas| Data loading and cleaning
NumPy| Mathematical calculations
Matplotlib| Data visualization
CSV| Data storage format

4. Project Features

1. CSV File Loading: Reads weather information from a CSV file.

2. Data Cleaning: Removes duplicate records and handles missing values.

3. Statistical Analysis: Calculates average, maximum, minimum, and standard deviation of temperature.

4. Rainfall Analysis: Calculates total rainfall.

5. Data Visualization: Generates temperature trend and rainfall charts.

6. Error Handling: Displays an error message when the CSV file is not found.

5. Project Folder Structure

Weather_Data_Analyzer/

- weather_analyzer.py
- weather.csv
- README.md

6. Installation Requirements

Install Python 3 on your computer.

Install the required libraries using the following command:

pip install pandas numpy matplotlib

7. How to Run the Project

Follow these steps:

1. Download or clone the project.
2. Open the project folder in VS Code.
3. Make sure weather.csv and weather_analyzer.py are in the same folder.
4. Open the terminal.
5. Run the following command:

python weather_analyzer.py

6. Enter the CSV file name:

weather.csv

7. Select an option from the main menu.

8. Sample Input

Date,Temp,Humidity,Rainfall
2026-08-01,32,70,0
2026-08-02,34,65,0
2026-08-03,30,80,12

9. Expected Output

WEATHER DATA ANALYZER

Average Temperature: 32.0 C

Maximum Temperature: 34 C

Minimum Temperature: 30 C

Standard Deviation: 1.63

Total Rainfall: 12 mm

The project also generates two graphs:

- Temperature Trend (Line Chart)
- Daily Rainfall (Bar Chart)

10. Test Cases

The project is tested using four test cases:

1. Normal Input: Checks weather data with valid values.
2. Boundary Input: Checks the program with only one weather record.
3. Invalid Input: Checks the error message when the CSV file does not exist.
4. Different Valid Scenario: Checks duplicate removal and missing value handling.

11. Advantages

- Easy to understand and use.
- Saves time in weather data analysis.
- Handles missing and duplicate data.
- Provides graphical weather visualization.
- Uses popular Python libraries.

12. Conclusion

The Weather Data Analyzer project demonstrates how Python can be used for data analysis and visualization.

By using Pandas, NumPy, and Matplotlib, the project makes it easier to organize weather information, calculate important statistics, and understand weather patterns through graphs.

13. Author

Name: Kajal Sahu

Course: Bachelor of Computer Applications (BCA)

University: Rungta International Skills University

Department: School of Information Technology