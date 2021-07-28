# Lagos-Temperature-Data

## Overview
This is an EDA that explores the temperature rates in Lagos state, Nigeria over 150 years compared to the world data.

## Packages Used
1. SQL
2. Python Version: 3.7
3. Pandas
4. Seaborn
5. Matplotlib

## Data
The data was extracted from the SQL Server on the Udacity website and stored as a comma seperated variable file.

Two datasets were imported. 
1. Lagos temperature data
2. Global temperature data

The scrapped data contained;
<ul>
<li> year </li>
<li> city </li>
<li> country </li>
  <li> temperature </li>
</ul>
  
## Data Cleaning
<ul>
<li>I removed the city and country columns as I was solely focusing on Lagos city temperature data in comparison with that of the world temperature.</li>
<li> Global temperature was being measured from the year 1750 and Lagos temperature began at 1849. Hence, to conform with data consistency, the missing years were dropped </li>
<li> Global temperature data ended at 2015, and Lagos at 2013. The two missing years were also dropped. </li>
<li> Lagos city temperature data had some null values and these rows were filled using the modal temperature for Lagos data </li> <\ul>

## Feature Engineering
1. Calculating Exponential Moving Averages
  
  The exponential moving average (EMA) is a technical chart indicator that tracks the continuous data over time.
  Unlike SMA and CMA, exponential moving average gives more weight to the recent temperatures and as a result of which, it can be a better model or better capture the movement of the trend in a faster way. EMA's reaction is directly proportional to the pattern of the data.
  
2. Merging Lagos and Global temperature datasets into One 
  
## EDA  
 1. Line chart showing Global Temperature <br>
  
 ![image](https://user-images.githubusercontent.com/70073139/127247688-4fabbe79-295d-4c0d-bfe5-ca6c9681b97b.png)
  Figure1: Global Temperature Chart for over 150 years
<br>
  
  2. Line chart showing Lagos temperature <br>
  
![image](https://user-images.githubusercontent.com/70073139/127247732-1df4a471-c471-4b13-9cdb-3f9aaca22038.png)
  Figure2: Lagos Temperature Chart for over 150 years
  <br>
  
  3. Comparing Lagos Temperature and world temperature <br>
  
  ![image](https://user-images.githubusercontent.com/70073139/127248233-c4d23a35-9e57-4954-a4a4-ee0e4e22dcd1.png)
  Figure3: Comparing Temperatures between Lagos and the Globe

## Conclusion
  <ul>
<li>  Lagos temperature is alot higher than the world temperature. About 3 times higher than the world mean temperature. </li>
  <li>  The differences between Lagos and the world temperature have not changed over 150 years. </li>
<li> The relationship between Lagos and world temperature is linear. Both increase together and they also reduce together. </li>
<li> The overall trend shows that the world temperature is getting higher and this has been increasing over the years albeit slowly. </li>
  </ul>
