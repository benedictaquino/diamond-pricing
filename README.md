# Diamond Pricing Model

For my Linear Models course at Holy Cross my final project was a diamond pricing
model created using multivariate linear regression techniques on a data set of 
308 diamonds. The analysis was done using R. 

After completing Galvanize's Data Science Immersive program I wanted to revisit
this project using Python. Also, R's tidyverse package has a built in dataset
of diamonds with some similar features. I wanted to train the model on this 
larger dataset of ~54,000 diamonds and see how it performs on the 308 diamonds,
as well as see how the model trained on the 308 diamonds I created for my course
project performs on the larger set. The features are slightly different, but my 
models only used the common features. 

###### The details of my old project can be seen [in this repository](https://github.com/benedictaquino/r-diamond-project)

## Technical Report
###### Python code, outputs, additional plots, and other specifics can be found in my [notebook](notebooks/linearmodels.ipynb).

### Summary

This study is designed to create a sensible pricing model for diamonds. The objective of this analysis is to use regression methods to test for associations between `price` and the other characteristics of diamonds. With a significance level of *α* = 0.05, I found that there was a significant quadratic relationship between `price` and `carat`, and significant association with `color` as well. My final model was a second-order regression model which included `carat`, `clarity`, and `color` as my covariates.

### Data Source and Management

My dataset consisted of information on 53,940 diamonds. The features are described within Table 1.

##### Table 1. Variable Descriptions

| Variable  |    Description       |Values|
|:----------|----------------------|------------------------|
|**price**|price in US dollars|$326 to $18,823|
|**carat**|weight of the diamond|0.2 to 5.01|
|**cut**|quality of the cut|Fair, Good, Very Good, Premium, Ideal|
|**color**|diamond colour|J (worst) to D (best)|
|**clarity**|a measurement of how clear the diamond|I1 (worst), SI2, SI1, VS2, VS1, VVS2, VVS1, IF (best)|
|**x**|length in mm|0 to 10.74|
|**y**|width in mm |0 to 58.9|
|**z**|depth in mm |0 to31.8|
|**depth**|total depth percentage = z / mean(x, y) = 2 * z / (x + y)|43 to 79|
|**table**|width of top of diamond relative to widest point|43 to 95|
|**lnprice***|A log transformation was used to adjust for homoscedasticity|ln(326) to ln(18,823)|
|**recolor***|Regrouping of the color variable|DE, FG, H, I, J|
###### * engineered features