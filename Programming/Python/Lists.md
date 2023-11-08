Algorithms - a set of rules or steps used to solve a problem
Data Structures - a particular way of organising data in a computer
Variable - holds 1 item in a container
List - stores multiple items in the list container

Creating a  list:
  - listname[]
  - listname = list()

- you can have different data types in 1 list:
  - list["name", 9]
- you can have a list inside a list:
  - list[99, 100, [23, 24], 34]
- you can look at a specific sub space of a list:
  - print(list[2])
  - the sub space starts at 0 for the first item in a list
- lists are mutable, they can be manipulated, whereas variables are no mutable

Len function:
  - you can use the len(list) function to return how many items are in a list

Range function:
  - you can use the range function in for loops
  - range(len(listname))
  - using this allows you to know your position in a list

Concatenating lists:
  - use the + to concatenate two lists together
  - [4, 5] + [6, 7]

Slicing:
  - you can slice a list with the listname[2:5] - the second number is up to but not including
  - [:] - whole list
  - [:5] - start of list up to but not including 5
  - [1:] - from the sub item 1 in the list to the end of the list

List methods:
  - dir(listname)
  - shows avaliable methods that can be used on the list

In operator:
  - you can use the 'in' operator to return a boolean whehter you have a certain value in your list

Ordering lists:
  - use the .sort() method to organise a list
  - listname.sort()

List functions:
  - len()
  - max()
  - min()
  - sum()
  - sum / len gives you the average

While loops:
  - you can add items into a list using the .append function
  - for example, add numbers into a list and then work out the average of the number
  - using a list to calculate the average can use up a lot of memory if the list has billions or millions of items in it

Split:
  - you can split a string into a list using the .split() method
  - by default the split method will split by white space
  - if you want to split by a certain parameter you can pass that in .split(;), .split(,)

Double split:
  - split a variable by white space then split up one of the items that has appeared in the list futher
  - for example, split up the header from an email, then split up the email to get the email domain
