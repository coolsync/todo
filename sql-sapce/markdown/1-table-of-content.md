# SQLite



## 创建数据库

语法

实例



## 附加数据库



基本语法如下：

```sql
ATTACH DATABASE file_name AS database_name;
```

## 分离数据库

基本语法如下：

```sql
DETACH DATABASE 'Alias-Name';
```



## 创建表

**CREATE TABLE** 语句用于创建一个新表

**.tables** 命令来验证表是否已成功创建

使用 SQLite **.schema** 命令得到表的完整信息





## 删除表

**DROP TABLE** 语句用来删除表定义及其所有相关数据、索引、触发器、约束和该表的权限





## Insert 



## Select



## SQLite 运算符



### SQLite 算术运算符

假设变量 a=10，变量 b=20，则：

| 运算符 | 描述                                    | 实例              |
| :----- | :-------------------------------------- | :---------------- |
| +      | 加法 - 把运算符两边的值相加             | a + b 将得到 30   |
| -      | 减法 - 左操作数减去右操作数             | a - b 将得到 -10  |
| *      | 乘法 - 把运算符两边的值相乘             | a * b 将得到 200  |
| /      | 除法 - 左操作数除以右操作数             | b / a 将得到 2    |
| %      | 取模 - 左操作数除以右操作数后得到的余数 | b % a will give 0 |





### SQLite 比较运算符



### SQLite 逻辑运算符

逻辑运算符列表:

| 运算符  | 描述                                                         |
| :------ | :----------------------------------------------------------- |
| AND     | AND 运算符允许在一个 SQL 语句的 WHERE 子句中的多个条件的存在。 |
| BETWEEN | BETWEEN 运算符用于在给定最小值和最大值范围内的一系列值中搜索值。 |
| EXISTS  | EXISTS 运算符用于在满足一定条件的指定表中搜索行的存在。      |
| IN      | IN 运算符用于把某个值与一系列指定列表的值进行比较。          |
| NOT IN  | IN 运算符的对立面，用于把某个值与不在一系列指定列表的值进行比较。 |
| LIKE    | LIKE 运算符用于把某个值与使用通配符运算符的相似值进行比较。  |
| GLOB    | GLOB 运算符用于把某个值与使用通配符运算符的相似值进行比较。GLOB 与 LIKE 不同之处在于，它是大小写敏感的。 |
| NOT     | NOT 运算符是所用的逻辑运算符的对立面。比如 NOT EXISTS、NOT BETWEEN、NOT IN，等等。**它是否定运算符。** |
| OR      | OR 运算符用于结合一个 SQL 语句的 WHERE 子句中的多个条件。    |
| IS NULL | NULL 运算符用于把某个值与 NULL 值进行比较。                  |
| IS      | IS 运算符与 = 相似。                                         |
| IS NOT  | IS NOT 运算符与 != 相似。                                    |
| \|\|    | 连接两个不同的字符串，得到一个新的字符串。                   |
| UNIQUE  | UNIQUE 运算符搜索指定表中的每一行，确保唯一性（无重复）。    |









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





## WHERE Clause (子句)



## AND & OR Operators
