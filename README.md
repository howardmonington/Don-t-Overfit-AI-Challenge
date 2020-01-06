# Don-t-Overfit-AI-Challenge-with-GridSearch
This is a coding challenge that I participated in. The challenge is to not overfit to the dataset with 300 features that has only 250 rows of training data and 19,750 rows of test data. This challenge is called "Don't Overfit ii" it can be accessed on Kaggle at this url: https://www.kaggle.com/c/dont-overfit-ii

In this project, the dataset was unbalanced with almost twice as many positive examples as negative examples, so I applied Synthetic Minority Over-sampling (SMOTE). Then, in order to train my model, I used GridSearchCV to test different parameters and classifiers in order to find the most accurate model. I tested the RandomForestClassifier, SVC, and KNeighborsClassifier. The most accurate classifier was SVC.
