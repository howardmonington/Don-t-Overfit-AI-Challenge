# Don't Overfit AI Challenge

#### -- Project Status: [Completed]

## Project Intro/Objective
This is a coding challenge. The challenge is to not overfit to a dataset with only 300 features and 250 observations of training data, while predicting 19,750 rows of test data.


### Methods Used
* Data Visualization - bar charts, histograms, boxplots
* Machine Learning
* Scaling - StandardScaler
* Synthetic Minority Oversampling (SMOTE)
* Predictive Modeling
* Univariate Feature Selection - SelectKBest
* Receiver Operating Characteristic (ROC) Score

### Technologies
* Python
* pandas, numpy
* jupyter
* StandardScaler
* SMOTE
* SelectKBest
* ROC Score

## Project Description
In this project, the dataset was unbalanced with almost twice as many positive examples as negative examples, so I applied Synthetic Minority Over-sampling (SMOTE) in order to make the dataset more balanced. Then, in order to train my model, I used used functions to test different classifiers in order to find the most accurate model. I tested the RandomForestClassifier, SVC, and KNeighborsClassifier. The most accurate classifier was SVC.

### Dataset Location
The Raw Data can be found [here](https://www.kaggle.com/c/dont-overfit-ii)

## Featured Notebooks/Analysis/Deliverables
* [Notebook](https://github.com/lukemonington/Don-t-Overfit-AI-Challenge/blob/master/don-t-overfit-ii.ipynb)


## Contributing Members

**[Luke Monington](https://github.com/lukemonington)**

## Contact
* I can be reached at lukemonington@aol.com.
