# 📊 CSV Column Viewer

A lightweight Python CLI tool for quickly inspecting CSV files.

## Features

- Count rows
- Count columns
- Display column names
- Preview the first 3 rows
- No external dependencies

## Run

```bash
python main.py
```

## Example

```text
📊 CSV Column Viewer
===================================

Enter CSV file path: students.csv

📋 CSV Summary
===================================

Rows    : 50
Columns : 4

Column Names:
  • name
  • age
  • department
  • mark

First 3 Rows:
{'name': 'Arun', 'age': '20', 'department': 'CSE', 'mark': '87'}
{'name': 'Meena', 'age': '19', 'department': 'ECE', 'mark': '91'}
{'name': 'Rahul', 'age': '20', 'department': 'CSE', 'mark': '78'}
```

## Built With

- Python
- CSV module
- File handling
