1. Introduction

Pandas is an open-source Python library used for data manipulation and data analysis. It provides fast, flexible, and expressive data structures designed to make working with structured data easy and intuitive. Pandas is widely used in data science, machine learning, data analytics, and scientific computing.

2. Why Pandas?

Pandas is used because it:
    - Handles large datasets efficiently
    - Provides powerful tools for data cleaning and preprocessing
    - Supports time series analysis
    - Integrates easily with other libraries like NumPy, Matplotlib, Seaborn, and Scikit-learn

3. Key Features of Pandas:

    - Fast and efficient DataFrame and Series objects
    - Easy handling of missing data
    - Data alignment and integrated handling of indexed data
    - Flexible reshaping and pivoting of datasets
    - Powerful group by and aggregation operations
    - Reading and writing data in multiple formats (CSV, Excel, JSON, SQL, etc.)

4. Core Data Structures:

    1)  Series
    A Series is a one-dimensional labeled array capable of holding data of any type.
    Example:
        import pandas as pd
        s = pd.Series([10, 20, 30, 40])
        print(s)

    output :
    0    10
    1    20
    2    30
    3    40
    dtype: int64

    2) DataFrame
    A DataFrame is a two-dimensional, size-mutable, and labeled data structure similar to a table in a database or an Excel spreadsheet.
    Example:
        data = {
            "Name": ["Ram", "Sita", "Hari"],
            "Age": [20, 21, 22]
        }

        df = pd.DataFrame(data)
        print(df)

    output :
        Name  Age
    0   Ram   20
    1  Sita   21
    2  Hari   22

5. Data Input and Output:

Pandas supports multiple file formats:
-> CSV files → read_csv()
-> Excel files → read_excel()
-> JSON files → read_json()
-> SQL databases → read_sql()

6. Data Operations in Pandas:

    1) Data Selection:
        - Column selection
        - Row selection using loc[] and iloc[]
    Example :
    df["Age"]
    df.loc[0]

    2) Data Filtering:
    Example:
    df[df["Age"] > 20]

    3) Handling Missing Values:
        - isnull()
        - dropna()
        - fillna()

    4) Sorting Data:
    Example :
    df.sort_values(by="Age")

7.  Data Aggregation and Grouping:

The groupby() function is used to split data into groups and apply aggregate functions like sum, mean, count, etc.
Example :
df.groupby("Age").count()

8. Data Visualization:

Pandas provides basic plotting features using Matplotlib.
Example :
df.plot(kind="bar")

9. Applications of Pandas:

    - Data cleaning and preprocessing
    - Exploratory Data Analysis (EDA)
    - Statistical analysis
    - Financial data analysis
    - Machine learning data preparation

10. Advantages of Pandas:

    - Easy to learn and use
    - High performance for data manipulation
    - Extensive documentation and community support
    - Seamless integration with Python data science ecosystem

11. Limitations of Pandas:

    - Not ideal for very large datasets (big data)
    - High memory consumption
    - Slower compared to low-level languages for heavy computation

12. Conclusion:

Pandas is an essential library in Python for data science and analytics. Its powerful data structures and rich set of functions make it a core tool for anyone working with data. Learning Pandas provides a strong foundation for advanced topics such as machine learning and big data analytics.

13. Reference:

        Official Pandas Documentation
        https://pandas.pydata.org/docs/

    
## Contributed By: 
**Author:** Anshriti Sharma 
**Author:**Shreeti Shrestha 
**Program:** Computer Engineering, Himalaya College of Engineering 
**Email:**shanshriti1121@gmail.com 
**Email:**shreetishrestha94@gmail.com 
**Last Updated:** January 2026







