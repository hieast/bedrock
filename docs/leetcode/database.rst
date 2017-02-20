.. _leetcode_database:

Database
========

175. Combine Two Tables
-----------------------

Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| PersonId    | int     |
+-------------+---------+
| FirstName   | varchar |
+-------------+---------+
| LastName    | varchar |
+-------------+---------+

PersonId is the primary key column for this table.

Table: Address

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| AddressId   | int     |
+-------------+---------+
| PersonId    | int     |
+-------------+---------+
| City        | varchar |
+-------------+---------+
| State       | varchar |
+-------------+---------+

AddressId is the primary key column for this table.

Write a SQL query for a report that provides the following information for each person in the
Person table, regardless if there is an address for each of those people:

FirstName, LastName, City, State

----------------------

Answer:

.. code-block:: sql

    SELECT Person.FirstName, Person.LastName, Address.City, Address.State FROM Person LEFT JOIN Address
     ON Person.PersonId = Address.PersonId

考察了 LEFT JOIN 的用法。


176. Second Highest Salary
--------------------------

Write a SQL query to get the second highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
+----+--------+
| 2  | 200    |
+----+--------+
| 3  | 300    |
+----+--------+

For example, given the above Employee table, the second highest salary is 200. If there is no second
highest salary, then the query should return null.

.. code-block:: sql

    SELECT (
    SELECT Salary FROM Employee GROUP BY Salary ORDER BY Salary DESC LIMIT 1 OFFSET 1
    ) AS SecondHighestSalary


