# GDP_life_expectancy_linear_knn_models

## What is the purpose of this project? What was my goal?
  - Compare linear regression, and k nearest neighbor algorithms.
  - Load, and prepare data using pandas. 
  
  - Wanted to learn if there is a strong correlation between money and life expectancy.

## Data used
  - 2017-country-life-expectancy.csv 
  - gdp-per-capita.csv
  - Both datasets are from 2017, and were pulled from data.worldbank.org. 
  - Dataset of size > 200

## Model, and Preparation of Data, Plotting data
  - Pandas was used to load the csv files, and also merge them based off Country name. 
  - Numpy was used to extract the information, and set X, and y values. 
  - Scikit-learn has both linear regression, and knn models built in.I originally created a linear model based off GDP (X), 
    and life expectancy (y) and then used both built in regressors to create predictions. 
  - In order to choose the "k" parameter for knn regressor, I found all countries within a specific range based off GDP of the country I wanted to predict. (Example below)
  - After both models were set, and predictions were made. I plotted the data with matplotlib


## Results, and Tests
  - There were couple of cases where high GDP resulted in lower life expectancy compared to other countries in the same cohort. There were also countries who had higher life expectancy than expected (based off similar GDP's). 
  - Overall there is a strong correlation with a countries wealth, and average life expectancy. For the most part of the graph, as the GDP increased the life expectancy increased. 
  
  - For my test I used Andora
    andora_gdp = 39134.39337
    knn_range = (37500, 40000) <-- I set the range based off Andora's 2017 GDP
    linear_regression_gdp_to_life(andora_gdp, knn_range)
    
    The linear regression model outputed near 81 years, while the knn model outputted near 78 years. 


## What I learned?
  - More data more precision 
  - How important it is to extract unnecessary data, or outliers such as null values. 
  - I only played around with knn, and linear regression but there are more effective models such as logistic regression. 

## What I would like to add in the future?
  - Logistic Regression
  - Add "year" as a feature and see how that plays a factor in the prediciton. 
  


