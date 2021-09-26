**Phase 1: Politician Index Fund**

- Goal was to provide investment recommendations after we trained our model using public data on politician investments and transactions
- Our original expectation was that the model would be able to predict how much a stock price would change given historical stock data

- Assumptions
	- Politicians are able to make better investment decisions
		- Maybe only certain politicians are making better investment decisions. The difficulty is knowing which politicians.
	- We can predict future stock prices by looking at the past stock prices
	- Interpolating where there is missing data shouldn't significantly affect the accuracy of our model
	- 14 days should have been enough for our look-back days
	- We would only invest in discrete steps

- Data collection
	- House stock watcher website (https://housestockwatcher.com/)
		- Pulled politician transaction data from this site, including ticker, transaction date, transaction type, disclosure date, amount, and owner name
		- Saved the data as json file
		- Converted to parquet file
		- Use pandas to convert parquet to DataFrame
	- Pulled SNP 500 stock data from stock_info module from yahoo_fin package
	
- Models we tried using
	- Keras model
		- A kind of neural net model?
		- Used one-hot encoding for our feature vectors

	- Time series model
		- Goal was to predict the closing price of the ticker on each day given the previous 14 days
		- Represented all of the stocks as a time series
		- Each element in the time series represented one day of data
		- Built a numpy array of size (# stock info parameters (open, close, etc.) x # stocks x # unique dates) to store the data
		- Used multi-hot encoding to build feature matrix
		- Used linear regression to test performance of the model
			- Tried to fit our time series predictions to a linear regression model

	- Both models
		- Trained the models based on transaction dates and then also disclosure dates
			
- Result
	- Both models failed since they were unable to make better predictions about change in stock price compared to their predictions about the mean of the test data set?

- Analysis
	- One possible reason was that there was not enough data to train the models successfully. It was possible the models needed more politician investment data in order to make accurate predictions.
	- Also possible that one or more of our assumptions was flawed

**Phase 2: Math-based investment strategy**

- https://maslov.bioengineering.illinois.edu/optimal_investment_ijtaf.pdf
- Two researchers, Sergei Maslov and Yi-Cheng Zhang, designed an optimal investment strategy in a portfolio of assets subject to a multiplicative Brownian motion. The strategy provided the maximal typical long-term growth rate of investor’s capital.
- They determined the optimal fraction of capital that an investor should keep in risky assets as well as weights of different assets in an optimal portfolio.

- Our goal was to implement this strategy in our code using a list of around 500 stocks from S&P 500
- Did not involve any machine learning, just a mathematical model	

- Assumptions
	- The price of an asset experiences a multiplicative random walk with some known probability distribution of steps	
		- The asset’s price changes by a random factor, drawn from some probability distribution, and is uncorrelated from price dynamics at earlier intervals
		- This assumption is known to hold in real financial markets beyond a certain time scale. In other words, it would work better with long-term investments.
	- Additional assumptions?

- Data collection
	- Pulled SNP 500 stock data from stock_info module from yahoo_fin package

- Parameters
	- Max number of stocks (desired max number of stocks to be recommended to invest in)
	- Investment window days (length of time user plans to hold these stocks before selling)
	- Start date (how far back to look at historical stock data to provide better recommendations)
	
- Outputs
	- Ticker names with corresponding recommended investment proportions
	- Expected total return (mean)
	- Variance and standard deviation
	- Confidence intervals (probability that expected investment return will fall within a range)

- Result
	- This method appeared to be successful since the recommended stocks seemed to have overall positive trends

- Sample Parameters
	- MAX_NUM_STOCKS = 10
	- INVESTMENT_WINDOW_DAYS = 120
	- END_DATE = datetime.datetime.now().date()
	- START_DATE = END_DATE - datetime.timedelta(days=365 * 2)

- Sample Output

	- Suggested investment proportions

		- [[0.44327548277981454, 'MRNA'],
		    [0.39095639662353404, 'TSLA'],
		    [0.08711342409231772, 'ENPH'],
		    [0.0786546965043337, 'GE'],

	- Mean/expected total return: 0.6903304024426118 (99.44%)
       Variance:  0.0011316143236405134
       Standard dev:  0.03363947567428056 

	- 99.0% confidence interval: 0.6903304024426118 ± 0.08664954719783226
      Expected investment return: 82.88% - 117.49%

	- 95.0% confidence interval: 0.6903304024426118 ± 0.06593216078040114
      Expected investment return: 86.71% - 113.03%

	- 85.0% confidence interval: 0.6903304024426118 ± 0.04842508389899549
      Expected investment return: 90.01% - 109.33%

