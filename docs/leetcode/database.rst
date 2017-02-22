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

复杂度应该为线性。或者使用 MAX 函数也可以。

177. Nth Highest Salary
-----------------------

Write a SQL query to get the nth highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
+----+--------+
| 2  | 200    |
+----+--------+
| 3  | 300    |
+----+--------+

For example, given the above Employee table, the nth highest salary where n = 2 is 200. If there is
no nth highest salary, then the query should return null.

Answer:

.. code-block:: sql

    CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
    BEGIN
      DECLARE offset INT;
      SELECT N - 1 INTO offset;
      RETURN (
          SELECT (
            SELECT Salary FROM Employee GROUP BY Salary ORDER BY Salary DESC LIMIT 1 OFFSET offset
          ) AS NthHighestSalary
      );
    END

OFFSET 后面必须跟一个已经计算出来的变量，而不能是表达式。


178. Rank Scores
----------------

Write a SQL query to rank scores. If there is a tie between two scores, both should have the same
ranking. Note that after a tie, the next ranking number should be the next consecutive integer value.
In other words, there should be no "holes" between ranks.

+----+-------+
| Id | Score |
+----+-------+
| 1  | 3.50  |
+----+-------+
| 2  | 3.65  |
+----+-------+
| 3  | 4.00  |
+----+-------+
| 4  | 3.85  |
+----+-------+
| 5  | 4.00  |
+----+-------+
| 6  | 3.65  |
+----+-------+

For example, given the above Scores table, your query should generate the following report (order
by highest score):

+-------+------+
| Score | Rank |
+-------+------+
| 4.00  | 1    |
+----+-------+
| 4.00  | 1    |
+----+-------+
| 3.85  | 2    |
+----+-------+
| 3.65  | 3    |
+----+-------+
| 3.65  | 3    |
+----+-------+
| 3.50  | 4    |
+-------+------+

Answer:

.. code-block:: sql

    SELECT
      Score, Rank
    FROM
        (
        SELECT
            Score,
            @rowNum:=IF(Score < @prevVal,
                @rowNum + 1,
                @rowNum) AS Rank,
            @prevVal:=Score
        FROM
            Scores,
            (SELECT @rowNum:=1) x,
            (SELECT @prevVal:=0) y
        ORDER BY Score DESC
        ) tmp

以上语句用两个变量实现了 dense_rank() 函数的功能。


180. Consecutive Numbers
------------------------

Write a SQL query to find all numbers that appear at least three times consecutively.

+----+-----+
| Id | Num |
+----+-----+
| 1  |  1  |
+----+-----+
| 2  |  1  |
+----+-----+
| 3  |  1  |
+----+-----+
| 4  |  2  |
+----+-----+
| 5  |  1  |
+----+-----+
| 6  |  2  |
+----+-----+
| 7  |  2  |
+----+-----+

For example, given the above Logs table, 1 is the only number that appears consecutively
for at least three times.

Answer:

.. code-block:: sql

    FROM (
        SELECT
            Num,
            @times:=IF(Num = @preVal,
                @times + 1,
                1) AS TIMES,
            @preVal:=Num
        FROM
            Logs,
            (SELECT @times:=0) x,
            (SELECT @preVal:=0) y
        ORDER BY Id
      ) tmp
    WHERE TIMES > 2

该题与上一题类似，需要用到变量。


181. Employees Earning More Than Their Managers
-----------------------------------------------

The Employee table holds all employees including their managers. Every employee has an Id, and
there is also a column for the manager Id.

+----+-------+--------+-----------+
| Id | Name  | Salary | ManagerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
+----+-------+--------+-----------+
| 2  | Henry | 80000  | 4         |
+----+-------+--------+-----------+
| 3  | Sam   | 60000  | NULL      |
+----+-------+--------+-----------+
| 4  | Max   | 90000  | NULL      |
+----+-------+--------+-----------+

Given the Employee table, write a SQL query that finds out employees who earn more than their
managers. For the above table, Joe is the only employee who earns more than his manager.

+----------+
| Employee |
+----------+
| Joe      |
+----------+

Answer:

.. code-block:: sql

    SELECT X.Name as Employee
    FROM Employee AS X JOIN Employee AS Y ON X.ManagerId =Y.Id
    WHERE X.Salary > Y.Salary

Only beats 40%, 希望能知道更快的查询方法。


182. Duplicate Emails
---------------------

Write a SQL query to find all duplicate emails in a table named Person.

+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
+----+---------+
| 2  | c@d.com |
+----+---------+
| 3  | a@b.com |
+----+---------+

For example, your query should return the following for the above table:

+---------+
| Email   |
+---------+
| a@b.com |
+---------+

Note: All emails are in lowercase.

Answer:

.. code-block:: sql

    SELECT Email FROM Person GROUP BY Email HAVING COUNT(*) > 1

只是简单考察了 GROUP BY 及 HAVING 的用法。只超过了20%的人，有理由怀疑分布的测试用例和环境变化很大。


183. Customers Who Never Order
------------------------------

Suppose that a website contains two tables, the Customers table and the Orders table. Write a SQL
query to find all customers who never order anything.

Table: Customers.

+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
+----+-------+
| 2  | Henry |
+----+-------+
| 3  | Sam   |
+----+-------+
| 4  | Max   |
+----+-------+

Table: Orders.

+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
+----+------------+
| 2  | 1          |
+----+------------+

Using the above tables as example, return the following:

+-----------+
| Customers |
+-----------+
| Henry     |
+-----------+
| Max       |
+-----------+

Answer:

.. code-block:: sql

    SELECT Customers.Name AS Customers FROM
    Customers LEFT JOIN (
    SELECT DISTINCT CustomerId FROM Orders
    ) Buy ON Customers.Id = Buy.CustomerId
    WHERE Buy.CustomerId IS NULL

使用 LEFT JOIN 实现了集合减法。

