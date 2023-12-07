# Review
* Client server architecture
* HTTP

# Data
**Data runs the world**

We should probably save our data somewhere

Current issue: Our program data does not persist between program executions

## Approach 1: Save to file
* Save data to a file

Issues:
* Unreliable
    * What happens if our computer crashes in the middle of a transaction?
    * What happens if we want to work in a multithreaded environment?
    * How can we maintain consistent logical state of our data?
        * (Decrementing one persons balance during financial transaction would cause invalid state)
* Reasoning about our data format

## Approach 2: Advanced saving of files (Database)

### Basic Database Concepts

A database is a *program* that writes and reads files RELIABLY  
Similar to servers, if we have a dedicated computer for running the database, we can call the computer a database  
Most databases have built in servers to make remote access possible

A database will handle all the issues above  
Databases usually follow some paradigm to make working with data easier to reason about  

How databases accomplish this is beyond the scope of this track  

_ACID Compliance_
* Databases should protect against the various issues I had previously mentioned
ACID are the standards for good databases. You may find you don't need these, and as such, may be better off writing to disk.

1. (All or nothing) Atomicity: Transactions happen entirely, or not at all
2. Consistency: Ignore this, its really up to the developer to enforce the consistency of data. The concept of transactions makes this easier however
3. Isolation: All transactions are executed as if they have the whole database to theirselves (Concurrency stuffs)
4. Durability: Once a transaction happens, nothing can undo it - not even a full system crash

_4 Basic Operations_
Create, Read, Update, Delete

_Transactions_
We can perform multiple operations and treat them as one. 
Either all steps will execute, or none of them will

_Database Paradigms_
How should we reason about our data? 

1. Relational (use Structured Query Language)
2. Document (JSON)
3. Graph
4. Vector
5. And way more!

Each paradigm has many different implementations  
eg. PostgreSQL, MySQL, SQLite, and Microsoft SQL Server are all Relational Databases, with slightly different features and promises

[7 Database Paradigms](https://www.youtube.com/watch?v=W2Z7fbCLSTw)

### Relational Databases
We will focus on relational databases because they are pretty standard. In addition, we can learn a lot about proper data modeling, not only in databases, but in your own programs. 
*Do examples in Excel*

_Tabular Data_

1+ Tables
Each table has columns - each with a header / datatype


Interating with database uses SQL (Structured Query Language)
* Declarative language
    * Says JUST DO something instead of HOW to do it (database figures out how to execute querys under the hood)
    * Examples are: All markup languages (HTML, CSS), React (declarative framework), SQL
* Eg. SELECT NAME *(column)* FROM PEOPLE *(table)*


## Homework
1. Design database schema for mail web server. You should probably have tables for Users and Mail. Maybe some other things as well
2. Add reliability to your mail server using the SQLite3 module in python

## Data Modeling
Watch this video on data modeling, don't be dissuaded by rust in the title, the ideas are similar for every language. 
[Rust Data Modeling without Classes](https://youtu.be/z-0-bbc80JM?si=6MXzRy8gW2TNfKKm&t=185) Start at part 1 (@3:05), stop at part 3 (@7:30)

Takeaway: Use tabular data and 3rd normal form

