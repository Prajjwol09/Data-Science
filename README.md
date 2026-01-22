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
