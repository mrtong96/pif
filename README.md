# Politician Index Fund (PIF) project

### Overview

The goal of this project was to build a simple investment AI that would try to use the publicly available information on politicians' stock activity to make investment decisions. In order to train our model, we scraped the stock prices of all of the SNP500 companies and looked at the past year of stock activity from active house of representative members and attempted to train various machine learning models. The models we trained were various regression models ranging from simple linear regression to neural networks and ARIMA models.

### Data sources

* Our main source of SNP500 stock data was from the yahoo-fin package [link](https://pypi.org/project/yahoo-fin/).
* For the stock transaction information we pulled it from the sec.gov website.
* Google doc we used for planning things [here](https://docs.google.com/document/d/1wQMsRnNDKjZF4n9tTS-SjrIXSISYOlHtGk3iBDKqzms/edit)

### High-level modeling approach

* For this project, we wanted to validate the following hypotheses
	* Given the historical price of stocks and the transactions of politicians, could we predict the movement of the stock market more accurately than using only the historical stock prices.
	* If we can validate the first hypothesis, how much additional money do we estimate that we can make using our method.
* In order to model this, we looked at:
	* For the transactions, we attempted to train models using both the actual transaction date and the dates the transactions were reported to have happened.
	* Our strategy for testing the dates in this manner was to first see whether or not ideal information (i.e., we know the transactions as soon as they happen) was substantially better than non-ideal information.
* In order to simplify our model for the prototyping phase we:
	* Assume that the stock market was open every day. For days in which it was closed, interpolated logarithmically. For example, if the stock price on day 1 was p_1 and the stock price on day 3 was p_3, our estimated price for day 2 is sqrt(p_1 * p_3)
	* Assume that we can sell our stocks on any day (including days where the market is closed)
	* Instead of training a model to make intelligent investing decisions, we instead trained a model to predict the stock prices.
	* That we can treat each stock independently from each other.
* For feature generation
	* We used one-hot encoding for each of the politician's transaction types (buy/sell, partial sell)
	* For each stock we used a lookback window of 14 days (i.e., to predict the stock on any given day we would only look at the past 14 days of data.
* For model training
	* We took these features and tried training a linear regression model (the model tried to predict the log change in stock prices) as well as a neural net

### Results of PIF
* We could not show significant improvement for the model with politicians' transactions over the model with only the stock information.
* To validate this, we looked at the RMSE error of our price predictions as well as plotted a histogram. From this both the RMSE and the histograms showed no significant signs of improvment.

#### Follow up: Building a small investment bot
* Because the main idea behind PIF was unsuccessful, we instead decided to pivot the project to build a small investment bot.
* The bot assumes that:
	* The stocks have a constant performance characteristics throughout the entire lookback window
	* The performance of the stock prices can be modeled as a random walk with some normal distribution in the logarithmic space.
	* That the performance of stocks are not mutually independent from each other. To represent this correlation we build a covariance matrix to try to model this behavior.
* The bot tries to
	* Follow the implementation from [this](https://maslov.bioengineering.illinois.edu/optimal_investment_ijtaf.pdf) research paper. `Optimal investment strategy for risky investments`
	* Maximize the typical expected return for some investment over some adjustable period of time.
	* Suggest up to a configurable maximum number of stocks to invest in
* The bot will recommend the relative ratios of stocks you should invest in as well as the expected returns of the investments.

### Closing thoughts
* Overall this was a fun project. Michael likes building investment bots as a hobby and while they never usually make him money, they're typically fun learning projects.
* In the end, we have still built an investment bot that tries to make good investments based off of some very simplified assumptions on how the stock market works.

### Authors
* Michael Tong
* Amber Yeh
* Katrina Chen

