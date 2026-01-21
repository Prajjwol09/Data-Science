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
* **Creating DataFrames:** Building structured data from dictionaries using `pd.DataFrame()`.
* **Shape Exploration:** Using `.shape` to retrieve dimensions.
    * `df.shape[0]` for the number of **rows**.
    * `df.shape[1]` for the number of **columns**.

#### NumPy Data Types & Casting
* **Checking Types:** Using `.dtype` to inspect array data (e.g., `int64`, `S1`, `<U6`).
* **Manual Definition:** Defining types during creation using the `dtype` argument.
* **Type Conversion:** Using `.astype()` to cast existing arrays into new formats (e.g., converting `float` to `int`).
* **Error Handling:** Understanding why passing a string into an integer-defined array (`dtype='i'`) triggers a `ValueError`.

#### Array Ownership: Copy vs. View
* **Copy:** Creates a completely new array. Changes to the copy **do not** affect the original.
* **View:** Creates a reference to the original. Changes to the view **will** change the original data.
* **The `.base` Attribute:** A tool to check if an array owns its data (returns `None` for copies/originals, returns the original array for views).

#### Array Shape & Reshaping
* **Dimensional Control:** Using `ndmin` to force a minimum number of dimensions.
* **Reshaping:** Transforming data between 1D, 2D, and 3D using `.reshape()`.
* **Unknown Dimension:** Using `-1` in a reshape command to let NumPy automatically calculate the correct size for that dimension.
* **Flattening:** Converting any multi-dimensional array into a simple 1D array using `.reshape(-1)`.

---
