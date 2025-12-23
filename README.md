# ADVANCED PYTHON PROGRAMMING FOR DATA SCIENCE

**Course Code:** ENCT 325
**Year:** III | **Part:** I
**Lecture:** 3 hours | **Tutorial:** 2 hours | **Practical:** 1 hour

---

## Course Objectives

The objective of this course is to develop advanced proficiency in Python programming for data science applications. It focuses on:

- Efficient coding practices
- Sophisticated data manipulation
- Statistical analysis and data visualization using modern Python libraries
- Fundamental data engineering and pipeline design concepts
- Automation and scaling of real-world data workflows

---

## Course Outline

### 1. Advanced Python Concepts and Best Practices (7 hours)

1.1 Review of Python essentials and coding conventions<br>
1.2 Advanced data structures: Collections, iterators, generators, and decorators<br>
1.3 Functions and lambda expressions<br>
1.4 Object-Oriented Programming for data science applications<br>
1.5 Exception handling, debugging, and logging<br>
1.6 Working with modules and packages

📁 **Resources:** [resources/chapter-01-python-concepts/](resources/chapter-01-python-concepts/)

### 2. Data Sources and APIs (7 hours)

2.1 Reading and writing structured/unstructured data (CSV, JSON, Excel, text)<br>
2.2 Database access with relational database and non-relational database<br>
2.3 Accessing and processing data from APIs (REST, SOAP)<br>
2.4 Web scraping using requests and BeautifulSoup<br>
2.5 Handling large datasets with chunking and lazy evaluation

📁 **Resources:** [resources/chapter-02-data-sources/](resources/chapter-02-data-sources/)

### 3. Advanced Data Wrangling and Transformation (9 hours)

3.1 Advanced Pandas operations: Merging, joining, reshaping, pivoting<br>
3.2 Handling missing, categorical, and time-series data<br>
3.3 Feature transformation, scaling, and encoding<br>
3.4 Memory optimization and efficient data processing<br>
3.5 Building a reusable data-cleaning pipeline<br>
3.6 Introduction to data pipeline components (Ingestion, transformation, storage)

📁 **Resources:** [resources/chapter-03-data-wrangling/](resources/chapter-03-data-wrangling/)

### 4. Applied Statistics and Exploratory Analysis (7 hours)

4.1 Statistical measures: Correlation, covariance, skewness, kurtosis
4.2 Probability review, sampling, and hypothesis testing
4.3 Regression and trend analysis using stats models
4.4 Exploratory data analysis (EDA) using descriptive and inferential methods
4.5 Automation of EDA workflows using Python

📁 **Resources:** [resources/chapter-04-statistics-eda/](resources/chapter-04-statistics-eda/)

### 5. Data Visualization and Storytelling (7 hours)

 5.1 Principles of effective visualization and dashboard design<br>
 5.2 Visualization with Matplotlib: Line, bar, histogram, scatter, subplots<br>
 5.3 Seaborn for statistical visualization: Box plot, pair plot, heat map<br>
 5.4 Interactive visualization using Plotly<br>
 5.5 Visualization driven insight generation<br>
 5.6 Case study: End-to-end visualization and reporting project

📁 **Resources:** [resources/chapter-05-visualization/](resources/chapter-05-visualization/)

### 6. Data Engineering and Automation (8 hours)

 6.1 Overview of data engineering in applied data science<br>
 6.2 Designing and implementing ETL pipelines<br>
 6.3 Automating workflows with schedulers (CRON, schedule)<br>
 6.4 Logging, monitoring, and error handling in pipelines<br>
 6.5 Data storage and retrieval strategies for pipelines<br>
 6.6 Automated report generation (Excel, HTML, PDF)<br>
 6.7 Case study: End-to-end automated analytics pipeline

📁 **Resources:** [resources/chapter-06-data-engineering/](resources/chapter-06-data-engineering/)

---

## Tutorial Sessions (30 hours)

1. **Python refresher and best practices:** Review of Python syntax, indentation, and PEP8 coding conventions through short exercises
2. **Iterators, generators, and decorators:** Writing small programs using generators for data streaming and decorators for function modification
3. **Object-oriented programming (OOP):** Designing simple class-based programs and demonstrating inheritance and encapsulation in python
4. **Data access and integration:** Reading data from CSV, Excel, JSON, and APIs; Discussion on best practices for data ingestion
5. **Database and SQL interaction:** Practice using SQLite and SQLAlchemy to query and manipulate structured datasets
6. **Web scraping practice:** Extracting tabular data using requests and BeautifulSoup; Handling exceptions and encoding issues
7. **Advanced Pandas operations:** Hands-on merging, reshaping, pivoting, and group-by operations for complex data manipulation
8. **Data cleaning and transformation:** Exercises on handling missing values, encoding categorical data, and normalization techniques
9. **Statistical computation and EDA:** Performing descriptive analysis, correlation, and hypothesis testing using Python libraries
10. **Data visualization practice:** Creating comparative plots using matplotlib, Seaborn, and Plotly; Customizing themes and layouts
11. **Pipeline and automation concepts:** Designing pseudocode and flow diagrams for ETL data pipelines and discussing error handling strategies
12. **Mini case study discussion:** Guided review of a small end-to-end applied data pipeline from ingestion to visualization and reporting

---

## Practical Sessions (15 hours)

1. Setting up Python environment for applied data workflows and writing modular programs using OOP and functions
2. Collecting data via APIs and web scraping
3. Building advanced data cleaning and transformation pipelines using Pandas
4. Conducting exploratory data analysis and statistical summaries
5. Developing interactive visualizations using Plotly, matplotlib and Seaborn
6. Automating ETL tasks and data refresh using Python schedulers
7. Generating summary dashboards and automated analytical reports
8. **Mini Project:** Build a complete applied data pipeline from ingestion to visualization and reporting on a real-world dataset

---

## Evaluation Scheme

### Final Exam

The questions will cover all the chapters in the syllabus. The evaluation scheme is as follows:

| Chapter         | Hours        | Marks Distribution* |
| --------------- | ------------ | ------------------- |
| 1               | 7            | 9                   |
| 2               | 7            | 9                   |
| 3               | 9            | 12                  |
| 4               | 7            | 10                  |
| 5               | 7            | 9                   |
| 6               | 8            | 11                  |
| **Total** | **45** | **60**        |

*There may be minor deviation in marks distribution.

---

## References

1. McKinney, W. (2022). *Python for data analysis.* O'Reilly Media.
2. VanderPlas, J. (2016). *Python data science handbook.* O'Reilly Media.
3. Beazley, D. (2021). *Python cookbook.* O'Reilly Media.
4. Grus, J. (2022). *Data science from scratch.* O'Reilly Media.

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Basic understanding of Python programming
- Familiarity with data structures and algorithms

### Recommended Setup

1. Install Python from [python.org](https://www.python.org/)
2. Set up a virtual environment
3. Install required packages:
   ```bash
   pip install pandas numpy matplotlib seaborn plotly scipy scikit-learn requests beautifulsoup4 sqlalchemy
   ```

---

## Course Structure

This repository contains materials organized by:

```
advanced-python/
├── resources/              # Chapter-wise learning resources
│   ├── chapter-01-python-concepts/
│   ├── chapter-02-data-sources/
│   ├── chapter-03-data-wrangling/
│   ├── chapter-04-statistics-eda/
│   ├── chapter-05-visualization/
│   └── chapter-06-data-engineering/
├── tutorials/              # Tutorial session materials
├── practicals/             # Practical lab exercises
├── assignments/            # Student assignments and submissions
├── projects/               # Course projects and mini-projects
└── datasets/               # Sample datasets for practice
```

### Resource Folders

Each `chapter-XX-topic/` folder should contain:
- 📚 **lecture-notes/** - Lecture slides and notes
- 💻 **code-examples/** - Demonstration code and scripts
- 📓 **notebooks/** - Jupyter notebooks for hands-on practice
- 📝 **exercises/** - Practice problems and challenges
- ✅ **solutions/** - Solutions to exercises
- 📖 **reading-materials/** - Additional articles and references

---

*Last Updated: December 2025*
