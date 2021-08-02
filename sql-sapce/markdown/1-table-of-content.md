# SQLite

REFENCE:

```bash

- [SQLite - Home](https://www.tutorialspoint.com/sqlite/index.htm)
- [SQLite - Overview](https://www.tutorialspoint.com/sqlite/sqlite_overview.htm)
- [SQLite - Installation](https://www.tutorialspoint.com/sqlite/sqlite_installation.htm)
- [SQLite - Commands](https://www.tutorialspoint.com/sqlite/sqlite_commands.htm)
- [SQLite - Syntax](https://www.tutorialspoint.com/sqlite/sqlite_syntax.htm)
- [SQLite - Data Type](https://www.tutorialspoint.com/sqlite/sqlite_data_types.htm)
- [SQLite - CREATE Database](https://www.tutorialspoint.com/sqlite/sqlite_create_database.htm)
- [SQLite - ATTACH Database](https://www.tutorialspoint.com/sqlite/sqlite_attach_database.htm)
- [SQLite - DETACH Database](https://www.tutorialspoint.com/sqlite/sqlite_detach_database.htm)
- [SQLite - CREATE Table](https://www.tutorialspoint.com/sqlite/sqlite_create_table.htm)
- [SQLite - DROP Table](https://www.tutorialspoint.com/sqlite/sqlite_drop_table.htm)
- [SQLite - INSERT Query](https://www.tutorialspoint.com/sqlite/sqlite_insert_query.htm)
- [SQLite - SELECT Query](https://www.tutorialspoint.com/sqlite/sqlite_select_query.htm)
- [SQLite - Operators](https://www.tutorialspoint.com/sqlite/sqlite_operators.htm)
- [SQLite - Expressions](https://www.tutorialspoint.com/sqlite/sqlite_expressions.htm)
- [SQLite - WHERE Clause](https://www.tutorialspoint.com/sqlite/sqlite_where_clause.htm)
- [SQLite - AND & OR Clauses](https://www.tutorialspoint.com/sqlite/sqlite_and_or_clauses.htm)
- [SQLite - UPDATE Query](https://www.tutorialspoint.com/sqlite/sqlite_update_query.htm)
- [SQLite - DELETE Query](https://www.tutorialspoint.com/sqlite/sqlite_delete_query.htm)
- [SQLite - LIKE Clause](https://www.tutorialspoint.com/sqlite/sqlite_like_clause.htm)
- [SQLite - GLOB Clause](https://www.tutorialspoint.com/sqlite/sqlite_glob_clause.htm)
- [SQLite - LIMIT Clause](https://www.tutorialspoint.com/sqlite/sqlite_limit_clause.htm)
- [SQLite - ORDER By Clause](https://www.tutorialspoint.com/sqlite/sqlite_order_by.htm)
- [SQLite - GROUP By Clause](https://www.tutorialspoint.com/sqlite/sqlite_group_by.htm)
- [SQLite - HAVING Clause](https://www.tutorialspoint.com/sqlite/sqlite_having_clause.htm)
- [SQLite - DISTINCT Keyword](https://www.tutorialspoint.com/sqlite/sqlite_distinct_keyword.htm)
```



## CREATE Database

语法

实例



## ATTACH Database





```sql
ATTACH DATABASE file_name AS database_name;
```



## DETACH Database



```sql
DETACH DATABASE 'Alias-Name';
```



## CREATE Table

**CREATE TABLE** 语句用于创建一个新表

**.tables** 命令来验证表是否已成功创建

使用 SQLite **.schema** 命令得到表的完整信息





## DROP Table

**DROP TABLE** 语句用来删除表定义及其所有相关数据、索引、触发器、约束和该表的权限





## INSERT Query





## SELECT Query





## SQLite - Operators



### SQLite Arithmetic Operators

假设变量 a=10，变量 b=20，则：

| 运算符 | 描述                                    | 实例              |
| :----- | :-------------------------------------- | :---------------- |
| +      | 加法 - 把运算符两边的值相加             | a + b 将得到 30   |
| -      | 减法 - 左操作数减去右操作数             | a - b 将得到 -10  |
| *      | 乘法 - 把运算符两边的值相乘             | a * b 将得到 200  |
| /      | 除法 - 左操作数除以右操作数             | b / a 将得到 2    |
| %      | 取模 - 左操作数除以右操作数后得到的余数 | b % a will give 0 |





### SQLite Comparison Operators



| <>   | Checks if the values of two operands are equal or not, if the values are not equal, then the condition becomes true. | (a <> b) is true. |
| ---- | ------------------------------------------------------------ | :---------------: |



### SQLite Logical Operators

[Show Examples](https://www.tutorialspoint.com/sqlite/sqlite_logical_operators.htm)

| Sr.No. |                    Operator & Description                    |
| ------ | :----------------------------------------------------------: |
|        |                                                              |
| 1      | **AND** The AND operator allows the existence of multiple conditions in an SQL statement's WHERE clause. |
|        |                                                              |
| 2      | **BETWEEN** The BETWEEN operator is used to search for values that are within a  set of values, given the minimum value and the maximum value. |
|        |                                                              |
| 3      | **EXISTS** The EXISTS operator is used to search for the presence of a row in a specified table that meets certain criteria. |
|        |                                                              |
| 4      | **IN** The IN operator is used to compare a value to a list of literal values that have been specified. |
|        |                                                              |
| 5      | **NOT IN** The negation of IN operator which is used to compare a value to a list of literal values that have been specified. |
|        |                                                              |
| 6      | **LIKE** The LIKE operator is used to compare a value to similar values using wildcard operators. |
|        |                                                              |
| 7      | **GLOB** The GLOB operator is used to compare a value to similar values using  wildcard operators. Also, GLOB is case sensitive, unlike LIKE. |
|        |                                                              |
| 8      | **NOT** The NOT operator reverses the meaning of the logical operator with which it is used. Eg. NOT EXISTS, NOT BETWEEN, NOT IN, etc. **This is negate operator.** |
|        |                                                              |
| 9      | **OR** The OR operator is used to combine multiple conditions in an SQL statement's WHERE clause. |
|        |                                                              |
| 10     | **IS NULL** The NULL operator is used to compare a value with a NULL value. |
|        |                                                              |
| 11     |              **IS** The IS operator work like =              |
|        |                                                              |
| 12     |           **IS NOT** The IS operator work like !=            |
|        |                                                              |
| 13     |    **\|\|** Adds two different strings and make new one.     |
|        |                                                              |
| 14     | **UNIQUE** The UNIQUE operator searches every row of a specified table for uniqueness (no duplicates). |







### SQLite Bitwise Operators

Following is the truth table for **&** and **|**.

|  p   |  q   | p & q | p \| q |
| :--: | :--: | :---: | :----: |
|  0   |  0   |   0   |   0    |
|  0   |  1   |   0   |   1    |
|  1   |  1   |   1   |   1    |
|  1   |  0   |   0   |   1    |







## SQLite - Expressions

#### Syntax

```sqlite
SELECT column1, column2, columnN 
FROM table_name 
WHERE [CONDITION | EXPRESSION];
```



### Boolean Expressions

```sqlite
SELECT column1, column2, columnN 
FROM table_name 
WHERE SINGLE VALUE MATCHING EXPRESSION;
```

```sqlite
sqlite> SELECT * FROM COMPANY WHERE SALARY = 10000;
ID          NAME        AGE         ADDRESS     SALARY
----------  ----------  ----------  ----------  ----------
4           James        24          Houston   10000.0
```



### Numeric Expression

```sqlite
SELECT numerical_expression as  OPERATION_NAME
[FROM table_name WHERE CONDITION] ;
```

```sqlite
sqlite> SELECT (15 + 6) AS ADDITION
ADDITION = 21
```

```sqlite
sqlite> SELECT COUNT(*) AS "RECORDS" FROM COMPANY; 
RECORDS = 7
```



### Date Expressions

```sqlite
sqlite>  SELECT CURRENT_TIMESTAMP;
CURRENT_TIMESTAMP  
-------------------
2021-07-29 06:54:10
```





## WHERE Clause



## AND & OR Operators





## UPDATE Query



## DELETE Query





## SQLite - LIKE Clause





## SQLite - GLOB Clause





## LIMIT Clause







## ORDER By Clause





## GROUP By Clause





## HAVING Clause





## DISTINCT Keyword
