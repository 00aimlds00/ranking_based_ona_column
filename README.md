# ranking_based_ona_column
Create ranks based on a column in a MySQL table having numeric data
Suppose we have a CSV file with fields name and marks, of few records that needed to quickly rank based on marks obtained. The possibilities are, 
2 or more records can have the same marks (hence same rank).
We first create the MySQL table scorespb2.sql for uploading the data from the csv file, this is particularly useful when there are many records.
Look at the original file below which is unordered and not ranked.

![image](https://github.com/00aimlds00/ranking_based_ona_column/assets/114329091/1cabac2b-2d5b-4d28-af34-e0ea579fc7fb)

So we proceed to write the MySQL query,

SELECT s.name, s.marks, COUNT(t.marks) AS 'Rank' FROM (SELECT DISTINCT marks FROM scorespb) AS t, scorespb AS s WHERE s.marks <= t.marks GROUP BY s.name, s.marks ORDER BY s.marks DESC;

The following output is generated

![image](https://github.com/00aimlds00/ranking_based_ona_column/assets/114329091/4a7aa0a6-72b4-4cd7-bc1a-8f2308c46422)

It may be noticed here that Ranks 15 and 17 allocated to more than 1 names as their marks are same.
