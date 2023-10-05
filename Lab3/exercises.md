# Exercises

Update your answers to the following questions, make sure to commit this file and your improved code as well!


## Task 1 - oop.py

1. Is MObject an abstract or a concrete class? Explain why:

	- MObject is a concrete class. Since this class is actually initiated and create the object based on the codes. Also there is no abstractmethod decorator for this class, then I consider this is the concrete class too. 

2. The 'Image' class has commented code for a `__del__` method. What does this commented-out method do?
	- the '__del__' is called a finalizer, which is trying to delete the instance and clean up the memory

3. What class does Texture inherit from?

	- the Texture inherit from image

4. What methods and attributes does the Texture class inherit from 'Image'? 

	- the texture class inherits all methods and attributes from image class

5. Do you think a texture should have a 'has-a' (composition) or 'is-a'(inheritance) relationship with 'Image'? If you think it is a 'has-a' relationship, refactor the code. As long as you defend your decision in the response below it could be either--but defend your position well!

	- I think texture should  has a "has-a" relationship with image, so it should be "the image has texture". For my understanding, texture is one of the features of the image rather than one type of the image. I have refactored the code in texture class by adding all functions related to the attributes of the image class


6. I did not declare a constructor for Texture. Does Python automatically create constructors for us? 

	- Yes, python creates the constructors

## Task 2 - Singleton

1. Refactor the singleton.py file such that:
  - The first time the logger is constructed, it will print out:
  	-  `Logger created exactly once`
  - If the logger is already initialized, it will print:
  	-  `logger already created`
Note: You do not 'have' a constructor, but you construct the object in the *instance* member function where you will create an object.  
Hint: Look at Lecture 3 slides for an example of creating a Singleton in Python

2. Are singleton's in Python thread safe? Why or why not?

Yes, but we need to define this properly. If I have defined the using logic in __init__ so this is thread safe, if I haven't define inside the __init__, I would consider this is not thread safe since there is a global variable and this can be interrupted between threads, which leads to multiple instances in a multithreads situation. That why I believe the thread-safe is conditionally since the designer need to define the __init__ properly.
  
