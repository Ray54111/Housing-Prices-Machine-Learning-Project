# Housing-Prices-Machine-Learning-Project
![alt text](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbdIFh1zgSpV6enhk8P5TAKOG3DSaDIw3uiw&usqp=CAU)

Geraldine Longo,
Ekta Jindal,
Robert Hascall,
Chika Okam,
Raymundo Zapien,
Daniel Corral

## Resources
[Zillow Housing Data: Home Values "https://www.zillow.com/research/data/"]

## Objective & Data
The aim of our project is to predict future housing prices in California. We’ll examine Zillow data from February 2019 through February 2023 by combining Zillow data sets by county, city, neighborhood (region name), number of bedrooms and home value by month for the stated time-period

## Training and Testing 
To preprocess the data we will split the data into test and trained based on a certain time period. We'll create a regression model to predict the housing prices for the coming 12 months. Can check the accuracy of the model by checking the R-squared score the model provides. From there we can optimize the model by widening the scope of years being trained. Once the model is optimized we can look at the neighborhoods/city within California to make a price prediction model on those high-interest neighborhoods.


Load Zillow data using california homes only. Cleanup csv by adding new features/data using zillows data on  number of bedrooms within a home (1-5+). Look for null values and only train model on data set with non-null values. Create a histogram to see the distribution of the various features. Check correlation. Create a heatmap using sns(seaborn) to check predicters for the house values. Discovering and visualize data to gain insights by visualizing positive correlations or negative ones by experimenting with features and training data based on skewed correlations. Data preprocessing. Data cleaning and handling texts/categorical features. Feature Engineering. Linear Regression Model to better evaluate and predict the housing prices in the future. We will be using pandas, numby, matplotlib.pyplot and seaborn for coding and for visuals.
Features for the housing: county, city, neighborhood (region name), number of bedrooms and home value by month for the stated time-period

