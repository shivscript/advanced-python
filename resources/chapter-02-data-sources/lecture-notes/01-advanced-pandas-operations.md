# Complete Pandas Guide:


## Introduction

Pandas is a powerful Python library for data manipulation, analysis, and cleaning. It provides data structures and functions needed to work with structured data seamlessly. Whether you're cleaning datasets, performing exploratory data analysis, or preparing data for machine learning, pandas is an essential tool.

### Why Pandas?
- **Easy to use**: Intuitive syntax for data manipulation
- **Flexible**: Handle various data formats and types
- **Powerful**: Perform complex operations with minimal code
- **Integration**: Works seamlessly with NumPy, Matplotlib, and scikit-learn
- **Performance**: Optimized for handling large datasets



## Installation & Setup

### Installing Pandas

```python
# Using pip
pip install pandas

# Using conda
conda install pandas

# Check installation
import pandas as pd

```

### Basic Imports

```python
import pandas as pd
```



## Core Data Structures

### 1. Series

A Series is a one-dimensional labeled array that can hold any data type.

```python
# Create Series from list
s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(s)

# Create Series from dictionary
s = pd.Series({'a': 10, 'b': 20, 'c': 30})

# Access elements
print(s['a'])        # By label
print(s.iloc[0])     # By position
```

### 2. DataFrame

A DataFrame is a two-dimensional labeled data structure with columns of potentially different types.

```python
# Create DataFrame from dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Salary': [50000, 60000, 75000]}
df = pd.DataFrame(data)

# Create DataFrame from list of lists
df = pd.DataFrame([[1, 2], [3, 4]], columns=['A', 'B'])

# Display first few rows
df.head()

# Get basic information
df.info()
df.describe()
```

### 1. Reading and Writing Data

```python
# Read CSV
df = pd.read_csv('data.csv')

# Read Excel
df = pd.read_excel('data.xlsx')

# Read JSON
df = pd.read_json('data.json')

# Write to CSV
df.to_csv('output.csv', index=False)

# Write to Excel
df.to_excel('output.xlsx', index=False)
```

### 2. Inspecting Data

```python
df.head()           # First 5 rows
df.tail()           # Last 5 rows
df.shape            # Dimensions (rows, columns)
df.columns          # Column names
df.index            # Row indices
df.dtypes           # Data types of columns
df.info()           # Detailed information
df.describe()       # Statistical summary
```

### 3. Selecting Data

```python
# Select single column
df['Name']
df.Name

# Select multiple columns
df[['Name', 'Age']]

# Select rows by position
df.iloc[0]          # First row
df.iloc[0:3]        # First 3 rows

# Select rows by label
df.loc['row_name']

# Conditional selection
df[df['Age'] > 25]
df[(df['Age'] > 25) & (df['Salary'] > 55000)]
```

### 4. Basic Operations

```python
# Column arithmetic
df['Bonus'] = df['Salary'] * 0.1

# Rename columns
df.rename(columns={'Name': 'Employee_Name'})

# Drop columns
df.drop('Bonus', axis=1)

# Sort values
df.sort_values('Salary', ascending=False)

# Get unique values
df['Name'].unique()

# Value counts
df['Department'].value_counts()
```

### 5. Handling Missing Data

```python
# Check for missing values
df.isnull()
df.isnull().sum()

# Drop rows with missing values
df.dropna()

# Fill missing values
df.fillna(0)
df.fillna(df.mean())

# Forward fill (propagate values)
df.fillna(method='ffill')

# Backward fill
df.fillna(method='bfill')
```


### 1. GroupBy Operations

```python
# Group by single column
grouped = df.groupby('Department')['Salary'].mean()

# Group by multiple columns
grouped = df.groupby(['Department', 'Gender'])['Salary'].agg(['mean', 'count'])

# Custom aggregation
df.groupby('Department').agg({
    'Salary': ['mean', 'min', 'max'],
    'Age': 'mean'
})

# Apply function to groups
df.groupby('Department').apply(lambda x: x[x['Salary'] > x['Salary'].mean()])
```

### 2. Merging and Joining

```python
# Inner join
merged = pd.merge(df1, df2, on='ID', how='inner')

# Left join
merged = pd.merge(df1, df2, on='ID', how='left')

# Outer join
merged = pd.merge(df1, df2, on='ID', how='outer')

# Concatenate DataFrames
result = pd.concat([df1, df2], axis=0)  # Stack rows
result = pd.concat([df1, df2], axis=1)  # Stack columns

# Join on index
result = df1.join(df2)
```

### 3. Pivot Tables

```python
# Create pivot table
pivot = df.pivot_table(
    values='Salary',
    index='Department',
    columns='Gender',
    aggfunc='mean'
)

# Pivot with multiple aggregations
pivot = df.pivot_table(
    values=['Salary', 'Bonus'],
    index='Department',
    aggfunc=['mean', 'sum']
)
```

### 4. String Operations

```python
# String methods
df['Name'].str.upper()
df['Name'].str.lower()
df['Name'].str.len()

# String contains
df[df['Name'].str.contains('John')]

# Split strings
df['Name'].str.split(' ')

# Replace strings
df['Department'].str.replace('HR', 'Human Resources')
```

### 5. DateTime Operations

```python
# Convert to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Extract components
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day

# Filter by date
df[df['Date'] > '2023-01-01']

# Resample time series
df.set_index('Date').resample('M').sum()  # Monthly sum
```



### 1. MultiIndex (Hierarchical Indexing)

```python
# Create MultiIndex from tuples
arrays = [['A', 'A', 'B', 'B'],
          ['one', 'two', 'one', 'two']]
index = pd.MultiIndex.from_arrays(arrays, names=['first', 'second'])
df = pd.DataFrame(np.random.randn(4, 3), index=index, columns=['X', 'Y', 'Z'])

# Access MultiIndex data
df.loc['A']
df.loc['A', 'one']

# Unstack (pivot)
df.unstack()

# Stack
df.stack()
```

### 2. Window Functions

```python
# Rolling mean
df['Rolling_Mean'] = df['Value'].rolling(window=3).mean()

# Rolling sum
df['Rolling_Sum'] = df['Value'].rolling(window=5).sum()

# Exponential moving average
df['EMA'] = df['Value'].ewm(span=10).mean()

# Rolling standard deviation
df['Rolling_Std'] = df['Value'].rolling(window=5).std()
```
### Why to use lambda ?

- Conciseness: Write one-liner instead of multi-line function
- Performance: Faster execution for simple transformations
- Inline Use: Perfect for apply(), map(), filter() operations
- No Naming: Avoid unnecessary function names for throwaway operations


### 3. Apply and Transform

```python
# Apply function to DataFrame
df.apply(np.sum)
df.apply(lambda x: x.max() - x.min())

# Apply to specific axis
df.apply(lambda x: x['Salary'] * 1.1, axis=1)

# Transform (preserve index)
df[['Salary', 'Bonus']].transform(lambda x: (x - x.mean()) / x.std())

# applymap (element-wise, deprecated in pandas 2.1+)
df.map(lambda x: x * 2)
```

### 4. Categorical Data

```python
# Create categorical
df['Category'] = pd.Categorical(df['Category'], categories=['A', 'B', 'C'], ordered=True)

# Convert to categorical
df['Department'] = df['Department'].astype('category')

# Get categories
df['Category'].cat.categories

# Rename categories
df['Category'].cat.rename_categories({'A': 'Alpha', 'B': 'Beta'})

# Remove unused categories
df['Category'].cat.remove_unused_categories()
```

### 5. Performance Optimization

```python
# Use appropriate data types
df['Age'] = df['Age'].astype('int8')
df['Salary'] = df['Salary'].astype('float32')

# Use inplace operations
df.drop('Unnecessary_Column', axis=1, inplace=True)

# Use query for filtering
df.query('Age > 25 and Salary > 60000')

# Use vectorized operations instead of loops
df['New_Column'] = df['Column1'] + df['Column2']  # Good
# for index, row in df.iterrows(): ...             # Slow

# Use .loc and .iloc instead of direct indexing
df.loc[df['Age'] > 25, 'Salary']

# Memory usage
df.memory_usage(deep=True)
```

### 6. Advanced Groupby

```python
# Named aggregation
result = df.groupby('Department').agg(
    avg_salary=('Salary', 'mean'),
    total_employees=('Name', 'count'),
    max_age=('Age', 'max')
)

# Transform with groupby
df['Salary_Rank'] = df.groupby('Department')['Salary'].rank()

# Filter groups
df.groupby('Department').filter(lambda x: len(x) > 5)

# GroupBy with multiple functions
df.groupby('Department')['Salary'].agg([np.mean, np.sum, np.std])
```

### 7. Custom Functions with Apply

```python
# Apply custom function
def categorize_salary(salary):
    if salary < 50000:
        return 'Low'
    elif salary < 75000:
        return 'Medium'
    else:
        return 'High'

df['Salary_Category'] = df['Salary'].apply(categorize_salary)

# Lambda functions
df['Age_Group'] = df['Age'].apply(lambda x: 'Young' if x < 30 else 'Old')

# Apply with arguments
def multiply(x, factor):
    return x * factor

df['Salary_Adjusted'] = df['Salary'].apply(multiply, args=(1.1,))
```


## Best Practices

### 1. Code Organization

```python
# Use method chaining
result = (df
    .drop('Unnecessary_Column', axis=1)
    .rename(columns={'Name': 'Employee_Name'})
    .assign(Bonus=lambda x: x['Salary'] * 0.1)
    .query('Salary > 50000')
    .sort_values('Salary', ascending=False)
)
```

### 2. Memory Management

```python
# Check memory usage
df.memory_usage(deep=True).sum() / 1024**2  # in MB

# Use appropriate data types from the start
df = pd.read_csv('file.csv', dtype={'Age': 'int8', 'Salary': 'float32'})

# Delete unnecessary objects
del temporary_df
```

### 3. Error Handling

```python
# Handle missing data explicitly
df.dropna(subset=['Column'], inplace=True)

# Validate data types
assert df['Age'].dtype == 'int64', "Age must be integer"

# Check for duplicates
df.drop_duplicates(subset=['ID'], keep='first', inplace=True)
```

### 4. Documentation

```python
# Add comments
df['New_Feature'] = df['Salary'] * 1.1  # 10% bonus calculation

# Use descriptive column names
# Good: df['monthly_salary']
# Bad: df['ms']

# Document data transformations
"""
This script:
1. Loads employee data
2. Removes duplicates
3. Calculates bonuses
4. Exports results
"""
```
## Contributed By:
**Author:** Sushant Gautam

**Program:** Computer Engineering, Himalaya College of Engineering
    
**Email:** sushant98677@gmail.com

**Last Updated:** January 2026
