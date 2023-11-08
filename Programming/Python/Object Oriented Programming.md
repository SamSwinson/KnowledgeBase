- a program is made up of lots of little objects
- an object:
  - is a small bit of self contained code and data
  - it breaks the code up into smaller pieces
- objects can be created and used
- they hide the detail of what goes on within the objects code

Class:
  - this is a template that you can create objects from
  - it's like a cookie cutter

Method or Message:
  - a method is a defined function within a class
  - using the "self" variable within creation of a method means that whatever happens within the method is specific to the variable the object has been assigned to

Field or Attribute:
  - a bit of data within a class

Object or Instance:
  - this is a particular instance of a class that has been created
  - this is like the cookie that the cookie cutter has created

Object Lifecycle:
  - the act of creating and destroying a class
  - creator - __init__
  - destructor - __del__
  - you don't have to create or destroy an object
  - you destroy an object by over-writing the variable that the class has been assigned to

Many Instances:
  - you can have multiple instances of the same class with different variable names
  - the different instances created with store the class variables within themselves

Inheritance:
  - instead of making a new class you can inherit all of an old class and then add to it within a new class
  - original class - parent
  - new class - child
  - class name(parent_class):
