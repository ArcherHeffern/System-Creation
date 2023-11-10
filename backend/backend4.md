# Review
* Client server architecture
* HTTP

# Storing Data
* Our data structures in programs do not persist between program executions
* We would like to save data to disk (permanently)

Note: Data runs the world. Most large companies tech products (Netflix, Google Search, Amazon) 

### Approach 1
* Save data to a file

Issues: 
* What happens if our computer crashes in the middle of a transaction?
* What happens if we want to work in a multithreaded environment?
* How can we maintain consistent logical state of our data?
    * (Decrementing one persons balance during financial transaction would cause invalid state)

Niceties: 
* How can we reason about the relationships between our data? 

TLDR: Very unreliable and not a nice interface

### Approach 2
Use a database  

A database is a *program* that writes and reads files RELIABLY  
Similar to servers, if we have a dedicated computer for running the database, we can call the computer a database  
A lot of databases have built in servers to make remote access possible

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
