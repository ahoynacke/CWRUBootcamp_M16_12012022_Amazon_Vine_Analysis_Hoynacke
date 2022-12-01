# CWRUBootcamp_M16_12012022_Amazon_Vine_Analysis_Hoynacke
# Project Overview 

Since your work with Jennifer on the SellBy project was so successful, you’ve been tasked with another, larger project: analyzing Amazon reviews written by members of the paid Amazon Vine program. The Amazon Vine program is a service that allows manufacturers and publishers to receive reviews for their products. Companies like SellBy pay a small fee to Amazon and provide products to Amazon Vine members, who are then required to publish a review.

In this project, you’ll have access to approximately 50 datasets. Each one contains reviews of a specific product, from clothing apparel to wireless products. You’ll need to pick one of these datasets and use PySpark to perform the ETL process to extract the dataset, transform the data, connect to an AWS RDS instance, and load the transformed data into pgAdmin. Next, you’ll use PySpark, Pandas, or SQL to determine if there is any bias toward favorable reviews from Vine members in your dataset. Then, you’ll write a summary of the analysis for Jennifer to submit to the SellBy stakeholders.

# Project Requirements 

Deliverable 1: Perform ETL on Amazon Product Reviews
Deliverable 2: Determine Bias of Vine Reviews

#Deliverable 1
The Amazon_Reviews_ETL.ipynb file does the following:
  1. An Amazon Review dataset is extracted as a DataFrame
  
  <img width="1311" alt="Screen Shot 2022-12-01 at 6 16 19 PM" src="https://user-images.githubusercontent.com/111096384/205179304-a3ef4fb7-7703-4011-8f7e-fa7c3c55b7c0.png">
  
  2. The extracted dataset is transformed into four DataFrames with the correct columns 
  
  <img width="977" alt="Screen Shot 2022-12-01 at 6 15 28 PM" src="https://user-images.githubusercontent.com/111096384/205179325-c37ba1ef-94d8-4f24-baf7-7573c5478a31.png">

<img width="1110" alt="Screen Shot 2022-12-01 at 6 18 13 PM" src="https://user-images.githubusercontent.com/111096384/205179576-d901eec2-5482-498e-aa3b-05fb7bc849d9.png">

<img width="660" alt="Screen Shot 2022-12-01 at 6 18 38 PM" src="https://user-images.githubusercontent.com/111096384/205179583-8f262f9b-3089-45b6-8ec9-e1c8677b21f9.png">

<img width="1281" alt="Screen Shot 2022-12-01 at 6 18 55 PM" src="https://user-images.githubusercontent.com/111096384/205179593-d5fbbb0b-c683-4a6b-a5f6-e572d539b588.png">

  3. All four DataFrames are loaded into their respective tables in pgAdmin 
