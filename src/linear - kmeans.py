import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import pandas as pd
import sklearn.linear_model
import sklearn.neighbors


def preparing_country_stats(gdp_csv, life_expectancy_csv):
    gdp_data_frame = pd.DataFrame(gdp_csv, columns=['Country', 'GDP Per Capita'])
    life_expectancy_frame = pd.DataFrame(life_expectancy_csv, columns=['Country', 'Life Expectancy'])

    gdp_to_life_expectancy = pd.merge(gdp_data_frame, life_expectancy_frame, on="Country", how="inner").dropna()
    return gdp_to_life_expectancy


# Stats of 2017
def linear_regression_gdp_to_life(new_gdp, knn_range):
    gdp_per_capita = pd.read_csv("gdp-per-capita.csv", thousands=",")

    life_expectancy = pd.read_csv("2017-country-life-expectancy .csv", thousands=",")
    life_expectancy = life_expectancy.rename(columns={"Country Name": 'Country', "2017": 'Life Expectancy'})

    country_stats = preparing_country_stats(gdp_per_capita, life_expectancy)
    X = np.c_[country_stats["GDP Per Capita"]]
    y = np.c_[country_stats["Life Expectancy"]]

    # creating linear regression model
    model = sklearn.linear_model.LinearRegression()
    model.fit(X, y)

    # Testing Linear Regression model
    X_new = [[new_gdp]]
    print("Prediction - Linear Regression | GDP Per Capita: " + str(new_gdp) + " | Life Expectancy: " + str(model.predict(X_new)))

    # creating k-nearest-neighbors model
    k = len(country_stats[(country_stats['GDP Per Capita'] > knn_range[0]) & (country_stats['GDP Per Capita'] < knn_range[1])])
    knn_model = sklearn.neighbors.KNeighborsRegressor(n_neighbors=k)
    knn_model.fit(X, y)

    # Testing Nearest Neighbors model
    print("Prediction - Nearest Neighbors | GDP Per Capita: " + str(new_gdp) + " | Life Expectancy: " + str(knn_model.predict(X_new)))


    # Displaying scatter plot with data
    country_stats.plot(kind="scatter", x="GDP Per Capita", y='Life Expectancy')
    plt.grid(True)
    plt.show()


print("--- Andora ----")
andora_gdp = 39134.39337
knn_range = (37500, 40000)
linear_regression_gdp_to_life(andora_gdp, knn_range)
