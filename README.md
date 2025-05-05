# This portfolio project is part of the AI/ML Engineering career path provided by Codecademy and aims to practically apply end-to-end machine learning (ML) workflow steps . It particularly aims to utilize Naive bayes (using bayes theorem) in classifying sentiment.
-------------------

## Project goals:
    > Applying the famous probability theorem `bayes theorem` through the `Naive Bayes` model in order to calculate the probabilty of a text falling into specific sentiment classes.
    > Showcase a general end-to-end machine learning workflow.
    > Build pipelines for effieciency, reproducability, and generalizabilty of the ML workflow. 

-----------------
## General Workflow (Iterative):

1. **Extract, Transform, Load (ETL):** Import and prepare the dataset (e.g., from CSV or web source).
2. **Basic Preprocessing:** Handle null values, remove duplicates, encode labels.
3. **Train-Test-Validation Split:** Separate the data for training, tuning, and final evaluation.
4. **Exploratory Data Analysis (EDA):** Analyze label distribution, text lengths, frequent tokens, and other insights.
5. **Feature Engineering:** Convert raw text into features using methods like `CountVectorizer`, including potential bigrams or stopword removal.
6. **Model Selection:** Choose a suitable model (e.g., `MultinomialNB`) and pipeline approach.
7. **Model Evaluation:** Evaluate performance using metrics like accuracy, precision, recall, F1-score, and confusion matrix.
8. **Hyperparameter Tuning:** Adjust parameters such as n-gram range, `alpha` (NB smoothing), or vocabulary size.
9. **Model Validation:** Ensure model generalizes well using validation data.
10. **ML Pipeline Building:** Package preprocessing and model steps into a `Pipeline` for consistent inference (and future deployment).

---
## Since we are dealing with **text classification**, NLP preprocessing steps are required (lowercasing, punctuation removal, etc.), and features will be extracted using `CountVectorizer`. The workflow begins by performing cleaning, then Basic EDA (e.g. Checking the most and least repeating words or phrases), and then proceeds to modeling, evaluation, and tuning using a Naive Bayes classifier.


## Note: The dataset intitialy included the following:
**target**: the polarity of the tweet (0 = negative, 4 = positive)

**ids**: The id of the tweet (2087)

**date**: the date of the tweet (Sat May 16 23:58:44 UTC 2009)

**flag**: The query (lyx). If there is no query, then this value is NO_QUERY.

**user**: the user that tweeted (robotickilldozr)

**text**: the text of the tweet (Lyx is cool)

Note: The dataset can viewed here: [Dataset](https://www.kaggle.com/datasets/kazanova/sentiment140)