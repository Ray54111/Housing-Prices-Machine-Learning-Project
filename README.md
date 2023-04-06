# Housing-Prices-Machine-Learning-Project
![alt text](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbdIFh1zgSpV6enhk8P5TAKOG3DSaDIw3uiw&usqp=CAU)
* Geraldine Longo,
* Ekta Jindal,
* Robert Hascall,
* Chika Okam,
* Raymundo Zapien,
* Daniel Corral
## Resources
[Zillow Housing Data: Home Values "https://www.zillow.com/research/data/"]
## Overview
Housing prices in California continue to increase as incomes rise, unemployment drops, and industries grow. Like many, our team wants to predict how housing prices will change over the years as we decide where we want to relocate long-term.
## Objective & Data
By analyzing housing market data and trends between 2019-2023, the Housing Price Prediction  will predict whether the housing market will rise or drop in the state of California. For example, clients who are looking for new home to buy or rental/investment property will be able to decide where to buy homes based on the number of bedrooms and neighborhoods comparing the housing price.
## Technologies
1. Tableau
2. PostgreSQL
3. Python
4. Jupyter
5. Github
6. Prophet
7. scikit-learn
8. Pandas
9. Matplotlib
10. Seaborn
## Sourcing the Data
Our team sourced data from verified site to answer our confirmed analysis questions. We pulled multiple sets with information on housing prices with neighborhood and bedrooms count etc. that will support our overall analysis.
## We will answer the following questions with our data:
1. Given the data available, can we expect housing prices to increase or decrease in the coming months?
2. What are the differences in price based on different client needs (example bedroom count, neighborhood etc.)
3. Given a location, what pertinent information should be understood by someone looking to move to the area?
## Preliminary Data Processing:
* The first steps were to check the kind of data types were inside of the CSV file housing our data for each city. We found that our dataset had city name, state, county and average sales price for all home types inside of that city with time steps of months from 2019 to 2023.
* The next was to check for duplicates and null values in the data frames/tables we created.
## ETL:
1. Extract - Extract clean data from confirmed sources, ensuring it has all necessary information and limited null values
2. Transform - Transform data, removing null values and unnecessary columns, joining datasets, creating separate data frames
3. Load - Load the data by writing it into Postgres using the confirmed look-up tables to allow multiple users to access
## Database Process:
* Used postgres by way of pgAdmin as our database to house the tables of data
* Used SqlAlchemy to create the database and schemas through Python and extract from the database into our prediction models.
## Visualizations using Tableau to analyze California Home Value trends:
https://public.tableau.com/app/profile/roberth7189/viz/CAHomePrices_16800593056980/HomeValuesinCA-TheStory?publish=yes
## Machine Learning Models Deployed:
1. The selected dataset comprises fifty months housing prices data from Zillow.com (2019-01-31 to 2023-02-28).
2. These historical prices were used as features for predicting our numerical
target/dependent variable (future price).
3. Supervised learning models, specifically, Linear Regression using scikit-learn, and a newly-researched model known as Prophet Model were both employed to predict home prices.
## Regression Model
1. Initially created a Data Frame of home prices in California from February 2019 to February, 2023
2. Preprocessing: The data was cleaned (e.g., removing irrelevant rows and columns, and then splitting the data into subsets for training and testing the model (using 75% to 25% split respectively))
3. Training: Since the aim was to develop a model to predict future home prices, we
began by training the model to predict February 2023
4. In preparing the Linear Regression Model, we dropped the previous twelve months data prior to February, 2023, since we wanted to train the model to recognize patterns for prediction.
Validating: We used a small subset of labeled data (y_test) to compare with the model’s predictions (predicted2023_02_28).
5. Predicting: If the linear regression model satisfies the relevant metrics such as; the model score, R2, MSE, RMSE, and standard deviation, then it can be used in predicting future home prices.
## Prophet Prediction Model
Two models were created:
1. One showed the aggregated city-wide data to predict the estimated home value in the coming 5 years for homeowners/investors knowledge
2. The other shows what the estimated values are for a 6-month window to show how the market may change within the coming months
## Challenges & Recommendations:
1. We would explore more machine learning models and fine tune them to try and get a better fitting model.
2. One major area where we feel we could have improved our project is by taking more time to discover more data sets and factors that may influence housing prices (Example: Population, Square feet area, Average rent, Crime rate, Price of gas, Health care).
3. There are likely many variables we could not find data on handily, and that would probably be the best place to improve our project.