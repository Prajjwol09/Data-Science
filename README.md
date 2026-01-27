# Day 1: Python Fundamentals

## Topics Covered

### **Data Types**
- Checking data types with `type()`
- Integer, String, Complex numbers
- Lists, Range, Boolean

### **Type Conversion & Casting**
- Converting between data types
- Using `int()`, `float()`, `str()`, `complex()`, `bool()`

### **Random Numbers**
- Generating random numbers with `random.randrange()`

### **Python Functions**
- Basic function definition and calling
- Return values and `return` statement
- The `pass` statement

### **Function Arguments**
- Parameters vs Arguments
- Multiple arguments
- Default parameter values
- Keyword arguments

---

# Day 2: Python Intermediate Concepts

## Topics Covered

### **Function Arguments (Advanced)**
- Positional arguments
- Mixing positional and keyword arguments
- Positional-only arguments (`/`)
- Keyword-only arguments (`*`)
- Combining positional-only and keyword-only

### **Arbitrary Arguments**
- `*args` for variable positional arguments
- `**kwargs` for variable keyword arguments
- Combining `*args` and `**kwargs`
- Unpacking lists with `*`

### **Variable Scope**
- Local scope
- Global scope
- `global` keyword
- `nonlocal` keyword
- Nested functions

### **Loops**
- `while` loops
- `for` loops with sequences
- Loop control statements:
  - `break`
  - `continue`
- Nested loops
- `range()` function

### **Lists**
- List operations
- Indexing and slicing
- List methods:
  - `insert()`, `append()`, `extend()`
  - `remove()`, `pop()`
- List comprehension
- Checking if item exists
- Clearing lists

### **Dictionaries**
- Creating dictionaries
- Accessing values
- Dictionary properties (duplicate keys overwrite)

---

# Day 3: Error and file handling, Numpy

## Topics Covered

### 1. **Error Handling**
- `try` and `except` blocks
- Multiple exception types
- `else` clause (executes when no errors)
- `finally` clause (always executes)
- Raising custom exceptions with `raise`

### 2. **File Handling**
- Opening files with `open()`
- Reading files (`read()`, `readline()`)
- Writing to files (`write()`, `append()`)
- Using `with` statement (auto-closes files)
- Creating new files
- Deleting files with `os.remove()`
- Checking file existence with `os.path.exists()`

### 3. **NumPy Introduction**
- Creating arrays with `np.array()`
- 1D, 2D, and 3D arrays
- Checking array dimensions with `.ndim`
- Creating higher-dimensional arrays
  
---

## Day 4: Pandas Basics & NumPy Essentials

### Topics Covered

#### Pandas DataFrames
* Creating DataFrames with `pd.DataFrame()`
* Row and Column counts using `df.shape[0]` and `df.shape[1]`

#### NumPy Data Types
* Checking data types with `.dtype`
* Defining `dtype` during array creation (e.g., `dtype='S'`)
* Type conversion using `.astype()`
* Data type errors and limitations

#### Array Ownership: Copy vs. View
* Creating copies with `.copy()`
* Creating views with `.view()`
* Checking data ownership with the `.base` attribute

#### Array Shape & Reshaping
* Defining dimensions with `ndmin`
* Reshaping arrays (1D to 2D and 3D)
* Using unknown dimensions with `-1`
* Flattening multi-dimensional arrays to 1D

---

## Day 5: NumPy Universal Functions (ufuncs)

### Topics Covered

#### Vectorization & Custom ufuncs
* Vectorized operations using `np.add()`
* Creating custom universal functions with `np.frompyfunc()`
* Validating function types using `type()`

#### Simple Arithmetic
* Basic operations: `np.add()`, `np.subtract()`, `np.multiply()`, `np.divide()`
* Power and Remainder: `np.power()`, `np.mod()`
* Absolute values: `np.absolute()`

#### Summations & Products
* Total sum of arrays with `np.sum()`
* Summation over specific axes (`axis=1`)
* Cumulative sums using `np.cumsum()`
* Array products using `np.prod()`
* Cumulative products using `np.cumprod()`

#### Trigonometric & Hyperbolic Functions
* Standard trig functions: `np.sin()` and `np.arcsin()`
* Angle conversion: `np.deg2rad()` and `np.rad2deg()`
* Pythagoras Theorem: Calculating hypotenuse with `np.hypot()`
* Hyperbolic functions: `np.sinh()` and `np.arcsinh()`

#### Rounding Decimals
* `np.trunc()` and `np.fix()`: Removing decimals toward zero
* `np.around()`: Rounding to a specific number of decimal places
* `np.floor()`: Rounding down to the nearest integer
* `np.ceil()`: Rounding up to the nearest integer

---

## Day 6: Pandas Data Manipulation & Visualization

### Topics Covered

#### Data Structures: DataFrames & Series
* Creating DataFrames from dictionaries with custom indices
* Creating Series with labeled indices and names
* Filtering Series using specific index lists

#### Data Loading & Inspection
* Reading CSV files with `pd.read_csv()` and `index_col`
* Inspecting datasets with `.shape`, `.head()`, and `.tail()`
* Using `.to_string()` to print entire DataFrames
* Converting JSON-structured dictionaries into DataFrames
* Getting structural summaries with `.info()`

#### Data Selection & Indexing
* Accessing specific rows by label using `.loc[]`
* Selecting multiple rows using list-based indexing
* Accessing and iterating through the `df.index`

#### Data Cleaning: Handling Missing Values
* Removing null values with `.dropna()` (New vs. Inplace)
* Global replacement of nulls with `.fillna()`
* Column-specific imputation using dictionaries
* Statistical imputation: Filling nulls with `.mean()`, `.median()`, or `.mode()[0]`

#### Data Cleaning: Fixing Values & Duplicates
* Replacing specific cell values using `.loc[index, column]`
* Conditional removal of rows based on value thresholds
* Identifying duplicates with `.duplicated()`
* Removing redundant data with `.drop_duplicates(inplace=True)`

#### Data Analysis & Visualization
* Calculating relationships with `.corr()` (Correlation Matrix)
* Creating Scatter Plots with `.plot(kind='scatter')`
* Understanding data frequency with Histograms using `.plot(kind='hist')`
* Visualizing plots using `matplotlib.pyplot.show()`

#### Date & Time Manipulation
* Converting strings to datetime using `pd.to_datetime()`
* Handling varied date formats with `format='mixed'`

---

# Movie Dataset Data Cleaning & Preprocessing (Python)

## Overview
This project focuses on **systematic data cleaning and preprocessing** of a movie dataset using **Python, Pandas, and NumPy**.  
The objective is to transform messy, inconsistent, and partially missing raw data into **clean, analysis-ready features**, while preserving the original columns for reference.

The notebook demonstrates **real-world data cleaning workflows**, including string normalization, missing value handling, datatype conversion, and feature engineering.

---

## Tech Stack
- Python  
- Pandas  
- NumPy  
- Matplotlib & Seaborn (imported for future visualization and analysis)

---

## Dataset
- File: `movies.csv`
- Format: CSV
- Contains attributes such as:
  - Year
  - Genre
  - Rating
  - Votes
  - Runtime
  - Gross Revenue
  - One-line Description
  - Director & Stars

---

## Initial Data Exploration
The dataset is explored using:
- `head()` and `tail()` to inspect records
- `info()` to understand data types and missing values
- `shape` and `len()` to evaluate dataset size

This ensures all cleaning steps are **data-driven and justified**.

---

## Data Cleaning Process

### Year Column
- Removed:
  - Parentheses `()`
  - En dashes `–`
  - Extra spaces and standalone symbols
- Handled blank and missing values
- Created a new column: **`Year_Cleaned`**
- Missing values filled with `"Unknown"`
- Original column preserved for traceability

---

### Genre Column
- Removed newline characters and extra spaces
- Standardized empty values
- Created **`Genre_Cleaned`**
- Missing values replaced with `"Unknown"`

---

### Rating Column
- Analyzed distribution and range
- Created **`Rating_Cleaned`**
- Converted invalid or empty entries to `NaN` for numerical consistency

---

### Votes Column
- Removed thousands separators (commas)
- Converted data from string to numeric
- Invalid values coerced to `NaN`
- Output stored in **`Votes_Cleaned`**

---

### Runtime Column
- Performed statistical inspection
- Identified potential inconsistencies for downstream analysis

---

### Gross Revenue Column
- Removed currency symbols (`$`) and magnitude indicators (`M`)
- Converted values to numeric format
- Scaled values to **actual dollar amounts**
- Stored in **`Gross_Cleaned`**

---

### One-Line Description Column
- Removed newline characters
- Trimmed unnecessary whitespace
- Replaced empty strings with `NaN`
- Stored in **`OneLine_Cleaned`**

---

### Director & Stars Column
- Removed labels:
  - `Director:`
  - `Stars:`
  - `Star:`
- Removed pipe (`|`) separators and newline characters
- Normalized spacing
- Replaced empty values with `NaN`
- Stored in **`Stars_Cleaned`**

---

## Key Concepts Demonstrated
- String cleaning using regex
- Handling missing and malformed data
- Safe datatype conversion
- Feature engineering with cleaned columns
- Preserving raw data alongside processed data

---

