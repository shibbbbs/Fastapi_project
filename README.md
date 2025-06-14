# Fastapi_project
# 📊 Equity Analysis Project API

This project is a simple FastAPI-based application designed to read financial data from an Excel file and provide API endpoints for interacting with the data. The Excel file performs an equity analysis of a project and contains various financial tables such as investment details, working capital, growth rates, cashflows, and investment measures.

---

## 📁 Project Structure


## 📖 Excel File Details

The primary data source is the `capbudg.xlsx` file, which contains the following sheets (tables):
Since i have save the data to latest xlsx format
- **Sheet Names (Tables)**:
  1. **Input** — Contains initial investment, cashflow details, working capital, growth rates, and discount rate assumptions.
  2. **Operating Cashflows** — Shows year-wise calculations for revenues, expenses, depreciation, taxes, and net cash flows.
  3. **Investment Measures** — Contains the summary of NPV, IRR, and ROC for the project.

---

## 🚀 How to Run the API

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt


2. Ensure `capbudg.xlsx` is in the project directory.

3. Run the FastAPI server:


4. Open your browser and go to:


## 📌 API Endpoints

| Method | Endpoint                  | Description                       |
|:--------|:----------------------------|:------------------------------------|
| `GET` | `/`                        | API running message                |
| `GET` | `/list-tables`              | List available tables              |
| `GET` | `/table-data/{table_name}`  | Get data from specified table      |
| `GET` | `/summary`                  | Get Investment Measures summary    |

## 📦 Requirements

- fastapi
- uvicorn
- pandas
- openpyxl

Install them via:

pip install -r requirements.txt

