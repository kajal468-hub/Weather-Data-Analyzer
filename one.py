import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


def main():

    # Enter CSV file name
    filename = input("Enter CSV file name: ").strip()

    # Check whether file exists
    if not os.path.isfile(filename):
        print(f"Error: File '{filename}' not found. Please enter a valid file name.")
        return

    try:
        # Read CSV file
        df = pd.read_csv(filename, header=None, skip_blank_lines=True)

        # Check for empty file
        if df.empty:
            print("Error: CSV file is empty.")
            return

        # Remove header row if present
        first_row = [str(x).strip().lower() for x in df.iloc[0]]

        if "date" in first_row and "temp" in first_row:
            df = df.iloc[1:].reset_index(drop=True)

        # Assign column names
        if len(df.columns) < 4:
            print("Error: CSV must contain Date, Temp, Humidity and Rainfall.")
            return

        df = df.iloc[:, :4]
        df.columns = ["Date", "Temp", "Humidity", "Rainfall"]

        # Convert columns into correct data types
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

        for col in ["Temp", "Humidity", "Rainfall"]:
            df[col] = pd.to_numeric(df[col], errors="coerce")

        # Remove invalid date rows
        df = df.dropna(subset=["Date"])

        # Remove duplicate rows
        original_rows = len(df)
        df = df.drop_duplicates()
        duplicates_removed = original_rows - len(df)

        # Fill missing temperature with mean
        temp_mean = df["Temp"].mean()

        if pd.notna(temp_mean):
            df["Temp"] = df["Temp"].fillna(temp_mean)

        # Fill other missing numerical values with their means
        for col in ["Humidity", "Rainfall"]:
            mean_value = df[col].mean()

            if pd.notna(mean_value):
                df[col] = df[col].fillna(mean_value)

        # Check if data is available
        if df.empty or df["Temp"].isna().all():
            print("Error: No valid temperature data found.")
            return

        # Select menu option
        print("\n----- WEATHER DATA ANALYZER -----")
        print("1. Weather Summary")
        print("2. Clean Data and Plot Charts")

        choice = input("Enter your choice: ").strip()

        # Calculate statistics using NumPy
        temperatures = df["Temp"].to_numpy()

        average_temp = np.mean(temperatures)
        maximum_temp = np.max(temperatures)
        minimum_temp = np.min(temperatures)
        std_dev = np.std(temperatures)

        # Find hottest and coldest dates
        max_date = df.loc[df["Temp"].idxmax(), "Date"]
        min_date = df.loc[df["Temp"].idxmin(), "Date"]

        total_rainfall = df["Rainfall"].sum()

        # Test Case 1 and Test Case 2
        if choice == "1":

            print("\n----- WEATHER SUMMARY -----")

            print(f"Average Temp: {average_temp:.2f} C")
            print(f"Max: {maximum_temp:g} ({max_date.strftime('%Y-%m-%d')})")
            print(f"Min: {minimum_temp:g} ({min_date.strftime('%Y-%m-%d')})")
            print(f"Total Rainfall: {total_rainfall:g} mm")
            print(f"Std Dev: {std_dev:.2f}")

        # Test Case 4
        elif choice == "2":

            print("\n----- DATA CLEANING REPORT -----")

            print(f"Duplicates removed: {duplicates_removed}")

            if pd.notna(temp_mean):
                print(f"Missing Temp filled with mean: {temp_mean:.2f}")

            print(f"Cleaned rows: {len(df)}")

            # Line Chart
            plt.figure(figsize=(9, 5))

            plt.plot(
                df["Date"],
                df["Temp"],
                marker="o",
                label="Temperature"
            )

            plt.title("Temperature Trend")
            plt.xlabel("Date")
            plt.ylabel("Temperature (C)")
            plt.legend()
            plt.grid(True)
            plt.xticks(rotation=45)
            plt.tight_layout()

            print("Line chart 'Temperature Trend' displayed")
            plt.show()

            # Bar Chart
            plt.figure(figsize=(9, 5))

            plt.bar(
                df["Date"].dt.strftime("%Y-%m-%d"),
                df["Temp"]
            )

            plt.title("Daily Temperature")
            plt.xlabel("Date")
            plt.ylabel("Temperature (C)")
            plt.xticks(rotation=45)
            plt.tight_layout()

            plt.show()

        else:
            print("Invalid menu option. Please select 1 or 2.")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
    