- the idea of a socket is to have 1 application service on a computer talking over a network to the same application service on another computer
- lots of different programming languages/programs will send data over the network and because of this we need a standardised way to push data across the network
- for this we use the "Wire Protocol"
- data going out of python onto the network gets "serialised" and pushed out onto the network
- data coming from the network gets "de-serialised" into a format that python can understand and then that gets put into python

XML:
  - eXtensible mark-up language
  - uses tags <person> </person>
  - it has start and end tags
  - it uses a hierarchical process to the data, there is a parent and child system to the tags
<person>
  <name>Sam</name>
  <id>001</id>
</person>
  - there is an XML tree/path to each bit of data, for example, Sam is in the /person/name path
  - each parent can have attributes, but, you can only have 1 bit of text per simple node

XML Schema:
  - this is a contract between your program and the program at the other end that will read the file
  - it allows the XML file to be validated against the criteria specified within the Schema
  - there are lots of XML Schema languages
  - XSD:
    - xs:element
    - xs:sequence
    - xs:complexType

If you write dates as YYY-MM-DD you can organise them properly with the computer

Reading XML files in python:
  - you can use the ElementTree library within python to be able to read in a search and find items within an XML file

JSON:
  - JavaScript Object Notation
  - you need to import json within the python file so python knows that you are importing data in the json file format
  - json is the preferred data format for python because when you read the data in it gets displayed as nested lists and dictionaries
  - json files can only deal with simple data structures, but, it's easy to read

Service Oriented Approach:
  - this is how we approach solving "how to deal with multiple different services that are in different places/locations"
  - multiple systems:
    - initially you may have a system programmed in only 1 language and in 1 place, but, as you expand you may push different bits of the system into different programs or locations
    - when you start to use multiple programming languages they all need to be able to properly talk to each other

Web Services:
  - API - Appliation Program Interface
  - this allows you to take an already established system for retrieving data or displaying data and incorporating it into your own program
  - for example, Google Maps API
  - Limiting rate:
    - often free APIs will only let you have a few requests per minutes or a certain amount per day which is how they stay free
  Security:
    - may APIs will require you to have an account to track what you are going and or to pay for the system
    - this means there needs to be some sort of security system identifier to allow you to prove you have an account and retrieve the API data
    - for example, Twitter API:
      - this uses the OAUTH system where the user has a secret token and secret key
      - using the import OAUTH and some commands in python you can generate a URL to the API that doesn't display the key or token but it can be verified by the Twitter API
