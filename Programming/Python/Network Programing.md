- you can establish a TCP/IP connection to a host by creating a socket.
- a socket is like a phone call to the other end
- TCP ports:
  - these determine the application that is going to be used on that socket
  - each port is used for a specific application
  - this is like deciding the specific purpose of the phone call you have made with the socket

HTTP:
  - using the hyper-text transfer protocol
  - you can GET request to retrieve a web page
  - this forms a simple we browser

Characters and Strings:
  - you can find the number value of a character using print(ord('a'))
  - this will give you the value of the character in ASCII
  - Unicode character set:
    - Unicode is an infinite character set that includes all of the character for every language
    - if you sent Unicode data across the network it would use up way too much data
      - UTF-32 - Unicode - Fixed length - Four bytes
      - UTF-16 - Unicode - Fixed length - Two bytes
      - UTF-8 - Unicode - Variable length - One-Four bytes
      - ASCII - 1 byte
    - Python3 strings internally are Unicode and most of the time it uses UTF-8
    - when you receive data from the network you need to .decode() to make sure it's in a displayable format for python
    - when you send data over the network you need to .encode() to make sure its in the correct UTF-8 format for sending over the network

Web browser:
  - you can build a web browser using the in built python library called urllib

Web scraping:
  - the action of retrieving information from a web page for data manipulation
  - BeautifulSoup4 is the best and easiest way to web scrap
