# Generate_Profiling
Generate Pandas Profile Report

## Installation
```bash
pip install -r Requirement.txt
```

## Usage
```python
import pandas as pd
from ydata_profiling import ProfileReport
def Generate_profile_report(df):
    Profile=ProfileReport(df)
    Profile.to_file('Pandas_Profile_report.html')
Generate_profile_report(pd.read_csv('Your CSV file'))

```

## Run
Run from the command line
```bash
python3 Generate_profiling.py <csv_file_path> <output_directory>
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
