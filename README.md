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

