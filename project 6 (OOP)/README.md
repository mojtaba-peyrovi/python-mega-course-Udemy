### Object Oriented Programming:
---
##### SQLITE: 

Here I will practice a bit more about OOP with Python and for the first try we use the small app made in the previous lectures. The code hs saved in this directory.

- A good approach, is to make the app without classes first, and just use functions, then later after we understood how it should work, we make the app again with OOP approach.

- We don't call functions anymore when we use classes because it is already included in the class initialization.

We added a class called Database to the backend, so it will have to have an initialization as we can see inside the class. And also an object which is called database = Database()

Then we have to change "Import backend" on the top of frontend.py to this:
```
from backend import database
```
and since backend doesn't exist anymore, we need to replace any reference to backend, into database.

- Another step we can do, is to pass a parameter called db to backend init method and then pass the "books.db" parameter into the database object when we want to call it, which is in frontend here:
```
database  = Database("books.db")
```
- when we write the class, we need to pass self to all methods inside it.

In order  to improve this code, we can have the database opened but not closed at the init, and keep it open, so that we won't have to have the connection opened and closed for each method.

Another thing is, the variable cur can't be found because it is defined as a variable inside init method and can't be used outside of it. In order to make cur to be found we can call it like this:
```
self.cur.execute("SQL_QUERY")
```
we will have to add it into all methods' variables including the init.

Also we removed conn.close() from all methods. For having one method to take care of all closing after each time the script is exited, we can use del function:
```
def __del__(self):
    self.conn.close()
```

#### The accounting example:

Out object is our bank account. The initial value in the account is 1000 and it's written in balance.txt file. 
As init function, we make a temporary variable to open the txt file and read it, then save the value as an integer inside a variable called "balance"

- Then we need to create an object instance out of the class, and we can call it "account".

Now, we will pas the name of "balance.txt" file to the instance, like this:
```
account = Account("balance.txt")
```

__Naming Convention:__ We call the whole app folder, package, then every py file inside it will be called Module, and inside each module, there could be several classes.

If we say print(account), it only returns the object, but if we want to see the actual value of the balance, we need to call the balance variable inside the object, like this:
```
print(account.balance)
```
- when we have a parameter inside the init function that we need to use inside other methods (in this example filepath variable) we can say in init:
```
self.filepath = filepath
```
then we can pass self.filepath anywhere else.

##### Inheritance:
Inheritance is the process of building a second class based on a base class. The second class will inherit all properties and methods of the parent class.

For example in the accounting app we can make a new class for checking accounts. It doesn't make sense to start writing all methods from Account class into the checking class. Instead, we make the checking class inherit from Account class and it is simple, we just need to call parent class'es init function inside the init function of the child class and pass self and all variables that were passed into the parent class also we need to pass them into the child class too and we will pass the parent name inside child name when we want to declare it. like this:
```
class child(parent):
    def __init__(self, param1, param2, ...):
        parent. __init__(self, para1, param2, ...)
```

__Review of oop terminology:__

- __class__ or blueprint (Account class)

- __Object instance or object__ which is when we say account = Account() this account is the object.

- __Instance variables:__ The variables that are made inside the methods of the class, like filepath.

- __Class variables:__ variables that are defined inside the class but outside any method and it will be shared with all methods.

- __Doc strings;__ we wrap some text right after the class declaration by """ and explain about the class. We can call an instance variable and it shows the text like this:
```
print(variable.__doc__)
```  
- __Constructor:__ other name of the init method.
- __Instantiation:__ the process of making the object from the class. like: account = Account()

- __Attributes:__ When we call the object's variables with a dot (can be instance variables or class variable) we call them attributes like checking.balance, here balance is the attribute. 