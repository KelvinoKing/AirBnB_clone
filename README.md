# AirBnB_Clone

**This project is an AirBnB clone. You can check out AirBnB website
by following this link https://www.airbnb.com/**

## Project Objectives

**After 4 months, it will have a complete web application composed by:**

	- A command interpreter to manipulate data without a visual interface,
	  like in a Shell (perfect for development and debugging)

	- A website (the front-end) that shows the final product
	  to everybody: static and dynamic

	- A database or files that store data (data = objects).

	- An API that provides a communication interface between
	  the front-end and your data (retrieve, create, delete, update them)

## Concepts Learned
- models
- Unittest
- Python packages concept page
- Serialization/Deserialization
- *args, **kwargs
- datetime
- More coming soon!

## Steps
**The project is built step by step. Each step will link to a concept:**

### 	The console

	- create your data model
	- manage (create, update, destroy, etc) objects via a console /
	  command interpreter
	- store and persist objects to a file (JSON file)
	- The first piece is to manipulate a powerful storage system. 
	  This storage engine will give us an abstraction between 
	  “My object” and “How they are stored and persisted”. 
	  This means: from your console code (the command interpreter 
	  itself) and from the front-end and RestAPI you will build later,
	  you won’t have to pay attention (take care) of how your objects
	  are stored.
	- This abstraction will also allow you to change the type of 
	  storage easily without updating all of your codebase.
	- The console will be a tool to validate this storage engine

####     The Console Commands

          - create <class name> = Creates a new object

	  - show <class name> <obj id> = Prints str rep of an instance class

	  - destroy <class name> <obj id> = Deletes a class instance

	  - all = Prints all string rep of all class instances in a list

	  - update <class name> <obj id> <attribute name> <value> = Updates an instace


##### For more information about the project checkout the wiki page https://github.com/KelvinoKing/AirBnB_clone/wiki
