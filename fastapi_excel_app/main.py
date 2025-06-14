from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
import pandas as pd
import os

# Initialize app
app = FastAPI()

# Redirect root to docs
@app.get("/")
def root():
    return RedirectResponse(url="/docs")

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# File path of data
EXCEL_FILE_PATH = "Data/capbudg.xlsx"

# here  List all tables (sheet names)
def get_all_tables():
    if not os.path.exists(EXCEL_FILE_PATH):
        raise HTTPException(status_code=404, detail="Excel file not found.")
    xlsx = pd.ExcelFile(EXCEL_FILE_PATH)
    return xlsx.sheet_names

# Endpoint: List Tables
@app.get("/list_tables")
def list_tables():
    tables = get_all_tables()
    return {"tables": tables}

# Endpoint: Get Table Details (row names)
@app.get("/get_table_details")
def get_table_details(table_name: str = Query(...)):
    try:
        xlsx = pd.ExcelFile(EXCEL_FILE_PATH)
        if table_name not in xlsx.sheet_names:
            raise HTTPException(status_code=404, detail="Table not found.")
        df = pd.read_excel(EXCEL_FILE_PATH, sheet_name=table_name, header=None)
        row_names = df.iloc[:, 0].dropna().tolist()
        return {"table_name": table_name, "row_names": row_names}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint: Sum numeric values of a row
@app.get("/row_sum")
def row_sum(table_name: str = Query(...), row_name: str = Query(...)):
    try:
        xlsx = pd.ExcelFile(EXCEL_FILE_PATH)
        if table_name not in xlsx.sheet_names:
            raise HTTPException(status_code=404, detail="Table not found.")

        df = pd.read_excel(EXCEL_FILE_PATH, sheet_name=table_name, header=None)
        if row_name not in df.iloc[:, 0].values:
            raise HTTPException(status_code=404, detail="Row name not found.")

        row_index = df.index[df.iloc[:, 0] == row_name].tolist()[0]
        numeric_values = pd.to_numeric(df.iloc[row_index, 1:], errors='coerce')
        total_sum = numeric_values.sum()

        return {
            "table_name": table_name,
            "row_name": row_name,
            "sum": total_sum
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
