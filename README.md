# CWRUBootcamp_M16_12012022_Amazon_Vine_Analysis_Hoynacke
# Project Overview 

Since your work with Jennifer on the SellBy project was so successful, you’ve been tasked with another, larger project: analyzing Amazon reviews written by members of the paid Amazon Vine program. The Amazon Vine program is a service that allows manufacturers and publishers to receive reviews for their products. Companies like SellBy pay a small fee to Amazon and provide products to Amazon Vine members, who are then required to publish a review.

In this project, you’ll have access to approximately 50 datasets. Each one contains reviews of a specific product, from clothing apparel to wireless products. You’ll need to pick one of these datasets and use PySpark to perform the ETL process to extract the dataset, transform the data, connect to an AWS RDS instance, and load the transformed data into pgAdmin. Next, you’ll use PySpark, Pandas, or SQL to determine if there is any bias toward favorable reviews from Vine members in your dataset. Then, you’ll write a summary of the analysis for Jennifer to submit to the SellBy stakeholders.

# Project Requirements 

Deliverable 1: Perform ETL on Amazon Product Reviews
Deliverable 2: Determine Bias of Vine Reviews

# Deliverable 1
The Amazon_Reviews_ETL.ipynb file does the following:
  1. An Amazon Review dataset is extracted as a DataFrame
  
  <img width="1311" alt="Screen Shot 2022-12-01 at 6 16 19 PM" src="https://user-images.githubusercontent.com/111096384/205179304-a3ef4fb7-7703-4011-8f7e-fa7c3c55b7c0.png">
  
  2. The extracted dataset is transformed into four DataFrames with the correct columns 
  
  <img width="977" alt="Screen Shot 2022-12-01 at 6 15 28 PM" src="https://user-images.githubusercontent.com/111096384/205179325-c37ba1ef-94d8-4f24-baf7-7573c5478a31.png">

<img width="1110" alt="Screen Shot 2022-12-01 at 6 18 13 PM" src="https://user-images.githubusercontent.com/111096384/205179576-d901eec2-5482-498e-aa3b-05fb7bc849d9.png">

<img width="660" alt="Screen Shot 2022-12-01 at 6 18 38 PM" src="https://user-images.githubusercontent.com/111096384/205179583-8f262f9b-3089-45b6-8ec9-e1c8677b21f9.png">

<img width="1281" alt="Screen Shot 2022-12-01 at 6 18 55 PM" src="https://user-images.githubusercontent.com/111096384/205179593-d5fbbb0b-c683-4a6b-a5f6-e572d539b588.png">

  3. All four DataFrames are loaded into their respective tables in pgAdmin 

# Deliverable 2

The analysis does the following:
1. There is a DataFrame or table for the vine_table data using one of three methods above (5 pt)

<img width="1381" alt="Screen Shot 2022-12-01 at 6 21 43 PM" src="https://user-images.githubusercontent.com/111096384/205179931-58ab3b42-a217-4c1f-bd21-1a4074eae940.png">

3. The data is filtered to create a DataFrame or table where there are 20 or more total votes (5 pt)

<img width="1396" alt="Screen Shot 2022-12-01 at 6 22 49 PM" src="https://user-images.githubusercontent.com/111096384/205180065-ed756835-ad1f-4739-a7e9-a50394601fb8.png">

5. The data is filtered to create a DataFrame or table where the percentage of helpful_votes is equal to or greater than 50% (5 pt)

<img width="1383" alt="Screen Shot 2022-12-01 at 6 23 45 PM" src="https://user-images.githubusercontent.com/111096384/205180171-9b64c3d3-9ea0-495f-b093-f83d1dadc498.png">

7. The data is filtered to create a DataFrame or table where there is a Vine review (5 pt)

<img width="1401" alt="Screen Shot 2022-12-01 at 6 25 11 PM" src="https://user-images.githubusercontent.com/111096384/205180339-53a37e6a-bc8d-40ac-97d2-2728b92b84b6.png">

9. The data is filtered to create a DataFrame or table where there isn’t a Vine review (5 pt)

<img width="1382" alt="Screen Shot 2022-12-01 at 6 25 54 PM" src="https://user-images.githubusercontent.com/111096384/205180445-a501cadb-3f53-4cb1-8744-69cf357a9c68.png">

11. The total number of reviews, the number of 5-star reviews, and the percentage 5-star reviews are calculated for all Vine and non-Vine reviews (15 pt)

<img width="550" alt="Screen Shot 2022-12-01 at 6 27 10 PM" src="https://user-images.githubusercontent.com/111096384/205180826-dd181e50-26aa-4b0b-a389-748848a9f3e8.png">

<img width="1330" alt="Screen Shot 2022-12-01 at 6 31 12 PM" src="https://user-images.githubusercontent.com/111096384/205181052-b51706d4-d20f-4127-afb0-524a02ad998b.png">

<img width="448" alt="Screen Shot 2022-12-01 at 6 35 17 PM" src="https://user-images.githubusercontent.com/111096384/205181507-f4a38d20-8545-41a2-9258-14112e02c5d3.png">



