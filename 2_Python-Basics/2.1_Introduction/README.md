# 2. Python Basics/2.1 Introduction

In this exercise, we will learn the use of the ```print``` Python function that will help us to output a message on the screen.

## Usage

To use the ```print``` function we will need to follow the next syntax:


```bash
print(object(s), sep=separator)
```

Let's see an example:
```bash
print(10)
```
This script will print the number ```10``` on the screen.


The parameter values include:
* object(s): Any object what we want to output on the screen, including text, numbers or variables.
* sep=separator: A way to specify how to separate objects. This is an optional parameter, and we will see examples in a while.

Note, if we want to print text on the screen we can use single or double-quotes. We always need to be consistent.

Let's see an example:
```bash
print("Hi!")
```
This script will print ```Hi!``` on the screen.

## Resources

Here are some useful resources for you to explore:
* [Python print() Function](https://www.w3schools.com/python/ref_func_print.asp)
* [Your Guide to the Python print() Function](https://realpython.com/python-print/)
* [A Basic Python main()](https://realpython.com/python-main-function/)
* [Python Comments](https://www.w3schools.com/python/python_comments.asp)
* [Python String format() method](https://www.w3schools.com/python/ref_string_format.asp)


## Exercises

### Task 2.1.1 

Your task is to print the number **100** on the screen. 
* Your result should look like this:
```bash
100
```

### Task 2.1.2

Your task is to print the result of the following calculation **10+100** on the screen.
* Your result should look like this:
```bash
110
```

### Task 2.1.3

Your task is to print the following message on the screen: **Hello, this is my first output!**
* Your result should look like this:
```bash
Hello, this is my first output!
```

### Task 2.1.4

Your task is to print the following two messages on the screen, one after the other: **Hello there!** and *This is my second output.*
* Your result should look like this:
```bash
Hello there!
This is my second output.
```

### Task 2.1.5

Your task is to print the following two messages on the screen, by concatenating the two texts in a single line as follows: **Hi** and **there!**
* Hint: Explore the use of **comma separator** in Python
* Your result should look like this:
```bash
Hi there!
```

### Task 2.1.6

Your task is to create a basic Python program using the **main()** method.

* Type and run the next script:

```bash
def main():
    print("Hello World!")

if __name__ == "__main__":
    main()
```

* Congratulations, you just created your first "Hello World!" program.

### Task 2.1.7

Your task is to create a basic Python program using the **main()** method.

* Type and run the next script:

```bash
def main():
    print("Hello World!")

if __name__ == "__main__":
    main()
```

* Your result should look like this:

```bash
Hello World!
```

* Congratulations, you just created your first "Hello World!" program.

### Task 2.1.8

Your task is to create a basic Python program using the **main()** method. The program should print the result of the following calculation:  ```10+20+30```

* Type and run the next script:

```bash
def main():
    print(10+20+30)

if __name__ == "__main__":
    main()
```

* Your result should look like this:

```bash
60
```

### Task 2.1.9

Your task is to add a comment to the following script. Your comment should state:  ```This is an example of adding three numbers```. 

* Add the comment before the print statement in the next script.
* If you don't remember how to use comments in Python, check [here](https://www.w3schools.com/python/python_comments.asp).

```bash
def main():
    print(10+20+30)

if __name__ == "__main__":
    main()
```

* Your result should look like this, as the comments are not shown on screen.

```bash
60
```

### Task 2.1.10

Your task is to explore the following script. As you can see we can use multiple ways of commenting. We use comment for:

* Explain Python code

* Make code more readable for our colleagues

* Prevent execution of certain scripts, as Python will ignore commented scripts

* Type and run the next script:

```bash
def main():
    # Add three numbers 
    print(10+20+30) 
    # print("something")

if __name__ == "__main__": # Use of main
    main()
```

* Your result should look like this, as the comments are not shown on screen.

```bash
60
```

### Task 2.1.11

Your task is to explore the following multiline comment script. 

* Type and run the next script:

```bash
"""
Create a main method,
and then run it!
"""
def main():
    # Add three numbers 
    print(10+20+30) 
    # print("something")

if __name__ == "__main__": # Use of main
    main()
```

* Your result should look like this, as the comments are not shown on screen.

```bash
60
```

### Task 2.1.12

Your task is to create a Python program using the ```main()``` method. The program should print the **A** and **B** using the **&** separator:

* Hint: As a reminder, you can use the ```sep=separator```

* Complete the missing part and run the next script:

```bash
def main():
    # Add your solution here 
    

if __name__ == "__main__": # Use of main
    main()
```

* Your result should look like this, as the comments are not shown on screen.

```bash
A&B
```

### Task 2.1.12

Your task is to type a Python program using the ```main()``` method. The program should print ```Hello World!```, using the ```format``` function.

* Hint: The ```format``` functions is an alternative way of printing.
* If you don't remember how to use the ```format``` method, click [here](https://realpython.com/python-formatted-output/)
* As an example, type and run the following script.

```bash
def main():
    # Using format to print
    print("Hello {0}".format("World"))
    # This prints the same results as the next
    # print("Hello World!")
    
if __name__ == "__main__": # Use of main
    main()
```

* Your result should look like this, as the comments are not shown on screen.

```bash
Hello World!
```

### Task 2.1.13

Your task is to create a Python program using the ```main()``` method. The program should print ```Bus number: 10```, using the ```format``` function. 

Follow the next specification:

* The text ```Bus number:``` should be inside the ```print``` statement
* The text ```10``` should be inside the ```format``` statement

```bash
def main():
    # Provide your solution here
    
    
if __name__ == "__main__": # Use of main
    main()
```

* Your result should look like this, as the comments are not shown on screen.

```bash
Bus number: 10
```

### Task 2.1.14

Your task is to create a Python program using the ```main()``` method. The program should print ```Names: John, Mary```, using the ```format``` function. 

Follow the next specification:

* The text ```Names:``` should be inside the ```print``` statement
* The texts ```John``` and ```Mary``` should be inside the ```format``` statement as two different entities
* Hint: Explore the use of ```{0}```,```{1}``` ,```{2}``` etc. as shown [here](https://realpython.com/python-formatted-output/)

* Your result should look like this, as the comments are not shown on screen.

```bash
Names: John, Mary
```

### Task 2.1.15

Your task is to create a Python program using the ```main()``` method. The program should construct a text with the city populations ```Berlin: 3645000, London: 8982000```, using the ```format``` function.

Follow the next specification:

* The texts ```Berlin``` and ```London``` should be inside the ```print``` statement
* The population numbers ```100``` and ```200``` should be inside the ```format``` statement as two different entities
* Hint: Explore the use of ```{0}```,```{1}``` ,```{2}``` etc. as shown [here](https://realpython.com/python-formatted-output/)

* Your result should look like this, as the comments are not shown on screen.

```bash
Berlin: 3645000, London: 8982000
```

