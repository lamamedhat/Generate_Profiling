import pandas as pd 
import os
import sys
from ydata_profiling import ProfileReport

def read_csv_to_dataframe(csv_path):
    """
    Read data from CSV file into a pandas DataFrame.

    Parameters:
    - csv_path (str): Path to CSV file.

    Returns:
    - pd.DataFrame: The DataFrame containing the data.
    """
    try:
        df = pd.read_csv(csv_path)
        return df
    except Exception as e:
        print(f"Error reading CSV file:{e}")
        sys.exit(1)

def generate_pandas_profile(dataframe):
    """
    Generate Pandas Profile Report for the given DataFrame.

    Parameters:
    - dataframe (pd.DataFrame): The DataFrame For which to generate profile.

    Returns:
    - Pd.DataFrame: The profile Report as a DataFrame.
    
    """
    try:
        profile=ProfileReport(dataframe,title="Data Report")
        return profile
    except Exception as e:
        print(f"Error generating pandas profile{e}")
        sys.exit(1)

def Write_profile_to_directore(profile,output_dir):
    """
    Write the Pandas Profile Report to the specified output directory.

    Parameters:
    - profile (pd.DataFrame): The Pandas Profile Report DataFrame. 
    - output_dir (str): Path to the output directory.

    """      
    try:
        output_path=os.path.join(output_dir,"pandas_profile_report.html")
        profile.to_file(output_path)
        print(f"Pandas PRofile Report written to {output_path}")
    except Exception as e:
        print(f"Error writting Pandas Profile Report{e} ")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv)!=3:
        print(f" Usage: python script.py <csv_file_path> <output_directory>")
        sys.exit(1)
    csv_path=sys.argv[1]
    output_dir=sys.argv[2]

    # Read data into DataFrame
    data_df = read_csv_to_dataframe(csv_path)

    # Generate Pandas Profile 
    profile_df=generate_pandas_profile(data_df)

    # Write profile to the output directory
    Write_profile_to_directore(profile_df,output_dir)                
