# Interview prediction case study
Predict whether interview applicants will actually show up for an interview.

Data is in the data folder.  This data is the subject of a Kaggle competition you can read about [here](https://www.kaggle.com/vishnusraghavan/the-interview-attendance-problem).  The data are more thoroughly described on the Kaggle website.

# Exploratory Data Analysis 
The dataset is comprised of 1234 rows of data with 22 categorical columns and one timestamp column that describe an instance of a scheduled interview or an unscheduled interview that occured. Columns included information about the company, role, location, basic application information, and a large number of free entry columns regarding scheduling and communication with the applicant.

Each column allowed for free-entry of values, which resulted in a large amount of data entry errors, and a large number of categories of answers for each feature. Additionally, the data also contains a number of missing values in specific columns, and a single row with missing value. Many of the entries in columns corresponding to applicant scheduling and communication had unusual entries that were not easily classifed.  Correcting these missing values proved to be challenging as each column required specific logic associated with how the missing or atypical-category values should be filled. After replacing these missing values, all data except the date of the interview were converted to dummy values for modeling.

# Modeling Approaches

We decided to split our efforts on different modeling approaches, including: Random Forest Classifiers, XGBoost Classifier, Logistic Regression, and Neural Networks.

Information about models...


# Model Performance

Performance of Random Forest (Andrew):


Performance of XGBoost Classifier (Kyle):


Performance of Logistic Regression (Alyse):



Performance of Neural Network (Jarred):


# Results and Conclusions


