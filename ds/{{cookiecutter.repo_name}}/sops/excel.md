import os
DATADIR = "../data"

## Spreadsheets and workbooks
for n in os.listdir(DATADIR):
    try:
        print(pd.ExcelFile(DATADIR + "/" + n).sheet_names, n)
    except:
        pass

def load_data(filename: str, workbook: str) -> pd.DataFrame:
    return pd.read_excel(pd.ExcelFile(DATADIR + "/" + filename), workbook)
