# CORD-19 COVID-19 Metadata Analysis

## Overview
This project analyzes the CORD-19 metadata.csv dataset to explore patterns in COVID-19 research publications. It includes data cleaning, exploration, visualization, and an interactive Streamlit app.

## Project Structure
- **cord19_analysis.ipynb**: Jupyter notebook for all analysis and visualizations.
- **streamlit_app.py**: Streamlit app for interactive data exploration.
- **data/metadata.csv**: Dataset used in the project.
- **requirements.txt**: Package dependencies.
- **README.md**: Documentation and reflection.

## Key Steps
1. **Data Loading**: Loaded metadata.csv using pandas and explored structure and missing values.
2. **Data Cleaning**: Removed columns with excessive missing values, converted dates, added abstract word count.
3. **Analysis**: Counted papers by year, identified top journals, most frequent words in titles, and visualized distributions.
4. **Visualization**: Created bar charts, word cloud, and time trends.
5. **Streamlit App**: Built a simple interactive dashboard for exploring the dataset.

## Findings
- Most publications occurred in 2020 and 2021.
- Top journals include [List top journals found].
- Common words in titles: COVID, coronavirus, pandemic, etc.
- Most data comes from a few main sources.

## Reflection
- **Challenges**: Large dataset size, handling missing values, and date parsing.
- **Learning**: Improved skills with pandas, matplotlib, seaborn, and Streamlit. Learned how to debug and incrementally build up analysis.
- **Tips**: Start with small samples, use pandas documentation, and visualize early.

## How To Run
1. Install requirements:
    ```bash
    pip install pandas matplotlib seaborn streamlit wordcloud
    ```
2. Run Jupyter notebook for analysis.
3. Start the Streamlit app:
    ```bash
    streamlit run streamlit_app.py
    ```

---

## License
Open for educational and research use.
