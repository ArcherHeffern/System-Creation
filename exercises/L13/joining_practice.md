# Joining Practice
Joining allows us to make use of primary/foreign keys to combine rows from multiple tables

__Inner Join__
Combine these tables where a foreign key and primary key match. If there is no match for a field, ignore it. 

__Left Join, Right Join, Outer Join__
All different ways of handling missing matches by filling with NULLS. We will skip these. 

## Example 1
User Table
| user_id | name | 
| --- | --- | 
| 0 | "Timmy" | 
| 1 | "Sarah" | 
| 2 | "Mancy" | 

Account Table
| account_id | user_id -> User.id | balance | 
| --- | --- | --- | 
| 0 | 0 | 500 |
| 1 | 0 | -100 | 
| 2 | 1 | 300 | 

Create a new table with the fields "name", and "balance"

Execute `./create_db.sh` to create the tables

## Example 2

# Joining Practice Solutions
## Example 1
SELECT name, Account.balance FROM User INNER JOIN Account ON User.id = Account.user_id;

| name | balance | 
| --- | --- | 
| Timmy | -100 | 
| Timmy | 500 | 
| Sarah | 300 |

## Example 2