Opening function:
  - use the open() command
  - open(filename, mode)
  - for example, open(mbox.txt, r)

- within a text file each new line is signified with a '\n' character so when you read a line there will be a newline character at the end of it

Reading files:
  - you can read a file character by character
  - you can read a file line by line
  - every line is ended with a \n
  - using a loop you can count the number of lines within a file using a counter
  - you can read a whole file into a string using the .read() method

 Searching through a file:
  - use a for loop and if statement with .startswith()
  - use the .rstrip() method to get rid of the \n from the text file
  - use the in operator to find lines that meet a certain criteria

User file input:
 - use an input to get the filename from the user
 - use a try and except statement in case the user enters a file name that doesn't exist and use the quit() command to exit the program it the file doesn't exist
