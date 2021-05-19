## Streaming yfinance data for 10 stocks on May 11th, 2021 with an interval of 5 minutes to AWS Kinesis using AWS Lambda to for interactive query on AWS Athena 

Project objective: Learning about near real-time data streaming pipeline from loading data to querying data using AWS technologies

The 10 stocks are:
- Facebook (FB)
- Shopify (SHOP)
- Beyond Meat (BYND)
- Netflix (NFLX)
- Pinterest (PINS)
- Square (SQ)
- The Trade Desk (TTD)
- Okta (OKTA)
- Snap (SNAP)
- Datadog (DDOG)


I. Set up AWS Kinesis data stream and data firehose delivery stream

First, we need to go to AWS Kinesis and create a data stream with 1 open shard 

Second, we proceed to set up a data firehose delivery stream for the data stream that we just created

Third, create a S3 bucket to use it as a destination for the data firehose delivery stream 

Fourth, specify the buffer conditions fo the data firehose delivery stream: 1MiB or 60 seconds

(See Appendix A for a screenshot of my Kinesis Data Firehose Delivery Stream Monitoring)

II. Provision AWS Lambda to transform and stream yfinance data to AWS Kinesis data stream and store it in AWS S3 bucket

Go to AWS Lambda and create a function in python like data_transformer.py, which uses the yfinance module to get stock data and transform each record into a json object like below to push them to AWS Kinesis:

{
  "high": 67.5, 
  "low": 64.61, 
  "ts": "2020-05-13 09:30:00-04:00", 
  "name": "DDOG"
}

Note: In order to import yfinance and other third party libraries, we need to create a lambda layer that includes the python dependencies and add that layer to the lambda function

III. Configure AWS Glue and Athena to query directly from S3 bucket

Go to AWS Glue and create tables using a crawler. Then, set up a crawler that points to the s3 bucket that contains the data that we just streamed. 

Once done setting up the crawler, run the crawler then double check by clicking on the table and see how many records were loaded as well as its schema

Then, go to Athena and choose the database that contains the table and start querying the data directly from s3 bucket. 

For example, I did a query to get the highest "high" every hour of each stock and another query to get the lowest "low" of each stock. (check query.sql) Then download the results in csv file, under "result.csv" and "result2.csv", accordingly. Then, I read those files in a jupyter notebook to do a couple of visualizations using matplotlib and seaborn. (Check Analysis.pdf and Analysis.ipynb)

Note: finance_data.zip is the data that I retrieved from s3 bucket

### Appendix A
![image](https://user-images.githubusercontent.com/55850536/118857564-2e8ce680-b8a6-11eb-93e6-16880b30399c.png)

