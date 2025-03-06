import pandas as pd

def load_dataset():
    """Loads the dataset from a CSV file."""
    file_path = input("Enter the path of the dataset (CSV file): ").strip()
    try:
        df = pd.read_csv(file_path)
        if df.empty:
            print("Error: The dataset is empty.")
            return None
        print("\nDataset loaded successfully!\n")
        return df
    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
    except pd.errors.ParserError:
        print("Error: The file is not a valid CSV.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return None

def explore_data(df):
    """Displays basic information about the dataset."""
    while True:
        print("\n== Explore Data ==")
        print("1. Display the first 5 rows")
        print("2. Display the last 5 rows")
        print("3. Display column names")
        print("4. Display data types")
        print("5. Display basic info")
        print("6. Go back")
        choice = input("Enter your choice: ").strip()

        if df.empty:
            print("Error: Dataset is empty.")
            break

        if choice == '1':
            print(df.head())
        elif choice == '2':
            print(df.tail())
        elif choice == '3':
            print(df.columns.tolist())
        elif choice == '4':
            print(df.dtypes)
        elif choice == '5':
            df.info()  
        elif choice == '6':
            break
        else:
            print("Invalid choice! Please try again.")

def handle_missing_data(df):
    """Handles missing data in the dataset."""
    while True:
        print("\n== Handle Missing Data ==")
        print("1. Display rows with missing values")
        print("2. Fill missing values with mean")
        print("3. Drop rows with missing values")
        print("4. Replace missing values with a specific value")
        print("5. Go back")
        choice = input("Enter your choice: ").strip()

        if df.empty:
            print("Error: Dataset is empty.")
            break

        if choice == '1':
            missing_rows = df[df.isnull().any(axis=1)]
            print(missing_rows if not missing_rows.empty else "No missing values found.")
        elif choice == '2':
            try:
                df.fillna(df.mean(numeric_only=True), inplace=True)
                print("Missing values filled with column means.")
            except ValueError:
                print("Error: No numeric columns to fill with mean.")
        elif choice == '3':
            df.dropna(inplace=True)
            print("Rows with missing values dropped.")
        elif choice == '4':
            value = input("Enter the value to replace missing values with: ")
            df.fillna(value, inplace=True)
            print(f"Missing values replaced with {value}.")
        elif choice == '5':
            break
        else:
            print("Invalid choice! Please try again.")

def generate_statistics(df):
    """Generates descriptive statistics of the dataset."""
    if df.empty:
        print("Error: Dataset is empty.")
        return
    print("\n== Generate Descriptive Statistics ==")
    print(df.describe())

def main():
    """Main function to execute the program."""
    df = None
    while True:
        print("\n========= Data Analysis & Cleaning Program =========")
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Handle Missing Data")
        print("4. Generate Descriptive Statistics")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            df = load_dataset()
        elif choice == '2':
            if df is not None:
                explore_data(df)
            else:
                print("Please load a dataset first.")
        elif choice == '3':
            if df is not None:
                handle_missing_data(df)
            else:
                print("Please load a dataset first.")
        elif choice == '4':
            if df is not None:
                generate_statistics(df)
            else:
                print("Please load a dataset first.")
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()  