# Exercises (Modify this file)

Answer and complete the following exercises.

## Python Standard Library

1. How you name functions and member functions matter. Take a look at the [dictionary](https://docs.python.org/3/library/stdtypes.html#typesmapping) 
and [list](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) member functions in the SL. 
Do the names of the member functions correlate to what they do? That is, are they good 'verbs' where the name of the function describes the action the code is doing? A good example would be a function called 'pop' which only removes one element. A bad example would be a function called 'pop' where one element is removed **and** that value is returned. A better name would be 'popAndGet' or 'popAndReturn', which captures the two events happening.

Yes, the names correlate to what they do. And they are the good verbs. 


2. How does a dictionary differ from a list? (i.e. What is the underlying data structure of each container.)

A list is ordered collection that uses array to store elements, list allows indexed access and maintains order of insertion. Dictionary is unordered collection which uses a hash table to store key-value pairs, providing the effcient retrieval based on keys without order of element.

3. Does a list allow for random access? Meaning can I access any element(e.g. myList[7])?

Yes,list allows the order and also is a collection based on array, so it can surely allow the random access

4. Observe that all the container data structures (i.e. list, set, dictionary, etc.) can work with any data type (integers, floats, custom data types, etc.). 
What do you think are the pros/cons of a library that can work with any data type?

The pros are: First, this library has a wide range application since all data forms are accepted. Second, it provides a more generalized codebase, which is easy for further modification. Third, easy to use, this library provides flexibility for the choice of data types.

The cons are: First, it can be complex to allow any data type, this may increase the running time for users. Second, less efficient compared to specialized libraries designed for specific data types. Third, lack of optimization for types, since the library is generic 


## requests

1. Take a look at the requests API documentation here: https://requests.readthedocs.io/en/latest/  
Comment if the functions are well named in the Requests module (Follow the previous link to the documentation to see if you can find the Requests module (hint: look for API Reference)).

Yes, they are well named. 

2. Take a look at the [Requests](https://requests.readthedocs.io/en/latest/api/#lower-level-classes) class. APIs that have more than say 5 arguments in a function can be confusing or error prone to use. This is a heuristic of course, but do you see any member functions that include lots of arguments?

Yes. requests.prepare(), requests.send(), requests.adapters.HTTPAdapter() includes lots of arguments. 

3. Take another look at the Requests class. Note that many of the methods includes `**kwargs` as an argument. What is `**kwargs`? Why might it be good for a method to have a `**kwargs` argument? Why might it be bad?  

The '**kwargs' means the key word arguement, this allows variable number of keyword arguments in the function. The advantage for this can be flexibility in any number of keyword arguments, easy to handle the optional parameters with default values, and easy for future extension when need to add other parameters. The disadvantage for this can be lack of explicitness about the expected arguments, increasing challenges for debugging since there is not a defined set of expected arguments 

4. Take a look at the [Session class.] (https://requests.readthedocs.io/en/latest/api/#request-sessions) Not only can you read the API's for that class, you can also view the source code by clicking the 'source' text. 
Notice how some methods have arguments that are set to `None` while other arguments are not set to anything. Why is that? Can arguments be set to anything besides `None`? Why might it be good to set an argument by some predetermined value?

Some values are set to none whereas others are not is because setting an arguement to none is a common practice when method is designed to be flexible, allowing users to omit certain parameters if they are not needed and the method can be internally checked by "None", some parameters are left without a default value makes the method signature more explicit. 