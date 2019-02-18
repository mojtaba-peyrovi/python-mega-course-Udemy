### Dealing with different databases:
---
##### SQLITE: 
This database engine is based on files instead of a table. It means whatever the application wants to save, will be saved as a file with .db suffix and anyone can use it even if they don't have sqlite in their machine.

We can also think about it as a small portable database attached to the application.

- The library that connects Python to Sqlite is called "Sqlite3"
- The library that connects Python to PostgreSql is called "Psycopg2"

 
###### Connection to sqlite: 
It has 5 steps:
        
           1- Connect to the database
           2- Create a cursor object
           3- Write an sql query
           4- Commit changes
           5- Close database connection

__Godd Tip:__ For writing the sql to create the table, we can add "IF NOT EXISTS, like this:
```
cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
```
Then it passes if the table exists, and doesn't return any error.

 