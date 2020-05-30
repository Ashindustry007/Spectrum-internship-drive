# Spectrum-internship-drive
My first project of Data science

The goal of the project was to predict the final grade of a student using the features provide. 
There were both nominal and ordinal categorical data. Some numerical and binary features.
First I converted all the datas into numerical data using labelencoder or get_dummies func. And checked for null values and prepared it for processing.

For selection of features I used Univariate selection method called SelectKBest with score_func as chi squared. That did yield me score and I made another DF out of it.
I iterated the no. of features to be drop from the sorted nlargest to check the best fit. So I dropped 34 features from down.

The best features to be considered are ['failures', 'schoolsup', 'absences', 'G1', 'G2']

RMSE =  1.5207162780902819

r2.score =  97.9933469627282 (with a random state of 101)

