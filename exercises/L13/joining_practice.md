# Joining Practice
Joining allows us to make use of primary/foreign keys to combine rows from multiple tables

__Inner Join__
Combine these tables where a foreign key and primary key match. If there is no match for a field, ignore it. 

Syntax: SELECT *fields..* FROM *table* INNER JOIN *other table* ON *foreign_key* = *primary_key*;  
Example: SELECT Table1.field2, Table2.field3 FROM Table1 INNER JOIN Table2 ON Table1.field1 = Table2.field2;  

Can also chain joins:
SELECT ... INNER JOIN _ ON _ INNER JOIN _ ON _...;

__Left Join, Right Join, Outer Join__
All different ways of handling missing matches by filling with NULLS. We will skip these. 

## Example 1
User Table
| user_id | name | 
| --- | --- | 
| 0 | Timmy | 
| 1 | Sarah | 
| 2 | Mancy | 

Account Table
| account_id | user_id -> User.id | balance | 
| --- | --- | --- | 
| 0 | 0 | 500 |
| 1 | 0 | -100 | 
| 2 | 1 | 300 | 

Create a new table with the fields "name", and "balance"

Execute `./create_db.sh` to create the tables

## Example 2
Account Table
| account_id | username | 

Product Table
| product_id | name | 

Transaction Table  
| transaction_id | product_id | account_id | price |   

Create a new table with the fields Account.username, Product.name, and Transaction.price  

Execute `./create_db2.sh` to create the tables  

# Joining Practice Solutions
## Example 1
SELECT name, Account.balance FROM User INNER JOIN Account ON User.id = Account.user_id;

| name | balance | 
| --- | --- | 
| Timmy | -100 | 
| Timmy | 500 | 
| Sarah | 300 |

## Example 2