- string is a data type
- each character in a string is indexed:
  - indexing starts from 0 and finishes at the end of the string
  - use [] to get an character from a string
  - you can't index longer than the string itself

len:
  - the len function states the length of the string
  - it does not take into account that string indexes start at 0

Loops in strings:
  - loop through each index of a string
  - you can use either a while loop or for loop to loop through a string
  - for loop achieves the same as a while loop in fewer lines
  - you can count the number of times a certain letter appears in a loop

String slicing:
  - you can display or store certain indexes from a string
  - for example, variable[4:9] - from the string variable characters 4 up to but no including 9 will be displayed or stored
  - [:4] - assumes the start of the string
  - [3:] - assumes the end of the string

String concatenation:
  - you can use the + to add two strings together, but it will not add spaces
  - using the , when adding strings or printing strings will add a space

In logical operator:
  - you as the question is a character in this string
  - for example, 'n' in 'banana'

String comparison:
  - you can ask if a string == another string
  -you can ask if a string is < or > another string
    - this works most of the time but can be a bit weird or display different results to what is expected

String libray:
  - strings are objects
  - string objects have built in functions
  - for example, 'Hi There'.lower() will print the string in lowercase
  - using this .function() is known as method calling, you are calling a pre-determine python method on the string
  - dir(your variable) - will display all the applicable methods
  - .find() - .find('the character or characters you want to find within a string')
  - .upper() - displays the uppercase but doesn't change the original variable
  - .lower() - displays the lowercase but doesn't change the original variable
  - Strip whitespace:
    - whitespace is any character that is not displayed, for example, space and tab
    - .lstrip() - left strip - gets ride of all space before the string
    - .rstrip() - right strip - gets ride of all space after the string
    - .strip() - gets rid of all spaces both sides of the string
  - .startswith() - asks the question does the string start with the specified character or characters and will return a true or false

Extracting:
  - for example, you can extract an email domain from a string
  - .find('@')
  - .find(' ', after@)
  - domain = string[@ + 1 : space position]

- Python 3 has all character sets installed so you can use none Latin characters and it will recognise them and they can still be treated as string
