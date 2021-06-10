# 2. Python Basics/2.2 Texts

In this exercise, we will focus on the use and manipulation of text in Python, including printing special characters, storing text in variables, and various tools for manipulating text including:

* Using the text concatenation method
* Find the length of a text
* Changing the case of the text
* Replace characters
* Slicing text
* Counting characters

## Usage

A text (also known as String) is a sequence of characters and it is considered one of the most used data types. A common characteristic of Strings is that it is immutable, meaning that once created we cannot change it. From now on we can use both terms interchangeably during this module.

The most common wat to use text in Python is to store the textual data in a variable. The next example demonstrates the creation of a new variable called ```name``` in order to store the data ```Mary```. To do this, we need to follow the next syntax:


```bash
name = "Mary"
```

Let's see another example of a phrase:

```bash
text = "Python is amazing!"
```

We can simple, use the ```text``` variable to extract the required data, for example the next script prints the name ```Mary``` on the screen.


```bash
print(name) # In this case I will print the content of the name variable
```

## Resources

Here are some useful resources for you to explore:

* [Python String Concatenation](https://www.w3schools.com/python/gloss_python_string_concatenation.asp)
* [isupper(), islower(), lower(), upper() in Python and their applications](https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/)
* [Python slice String](https://www.w3schools.com/python/gloss_python_string_slice.asp)


## Exercises

### Task 2.2.1 

Your task is to create a variable called ```city``` to store the data: ```London``` , then print the content of the ```city``` variable on the screen. 

* Your result should look like this:

```bash
London
```

### Task 2.2.2

Your task is to create two variables, the first variable to be called ```city``` and will store the data: ```Berlin``` , and the second variable to be called ```population``` and will store the data: ```3645000```. Then print the content of the ```city``` and ```population``` using a colon (```:```)  in between. 

* Your result should look like this:

```bash
London: 3645000
```

### Task 2.2.3

Your task is to create two variables, the first variable to be called ```city``` and will store the data: ```London``` , and the second variable to be called ```population``` and will store the data: ```9000000```. Then print the content of the ```city``` and ```population``` using their labels as shown in the output below.

* Your result should look like this:

```bash
City: London
Population: 9000000
```

### Task 2.2.4

Your task is to print the following two messages on the screen, one after the other: **Hello there!** and **This is my second output**. Make sure that you create two variables (with your preferred variable name) to store the data.

* Your result should look like this:

```bash
Hello there!
This is my second output.
```

### Task 2.2.5

Your task is to print the following two messages on the screen, by concatenating the two texts in a single line as follows: **Hi** and **there!** Make sure that you create two variables (with your preferred variable name) to store the data.

* Hint: Explore the use of the ```plus separator(+)``` in Python
* Your result should look like this:

```bash
Hi there!
```

### Task 2.2.6

Your task is to create a basic Python program using the **main()** method and create two text variables to store details about your self. Print the results on screen, using the following format:

* Hello, I am Mary, I live in Berlin
* Make sure you replace **Mary** and **Berlin** with your own data
* Feel free to use the ```plus``` or the ```comma``` operator

* Your result should look like this:

```bash
Hello, I am Mary, I live in Berlin.
```

* Congratulations, you just learned how to concatenate text in Python.

### Task 2.1.7

Your task is to type and run the following program that uses the ```len``` function (```len``` is short for length). The ```len``` will help us to find the length of a string.

* Type and run the next script:

```bash
def main():
    len("Berlin")

if __name__ == "__main__":
    main()
```

* Your result should look like this:

```bash
6
```

### Task 2.1.8

Your task is to find the length of the text **I love Python**. Create a Python program using the **main()** method. The program should store the length of the text in a new variable called ```my_length```. Then print the result on the screen.

* Type and run the next script:

```bash
def main():
    # Your solution should be here

if __name__ == "__main__":
    main()
```

* Your result should look like this:

```bash
13
```

### Task 2.1.9

Your task is to type and run the following program that uses the ```lower``` function. The ```lower``` will help us to change the case of a string to lower case. 

* Type and run the next script:

```bash
def main():
    lower("Berlin")

if __name__ == "__main__":
    main()
```

* Your result should look like this:

```bash
berlin
```

### Task 2.1.10

Your task is to type and run the following program that uses the ```upper``` function. The ```upper``` will help us to change the case of a string to upper case. 

* Type and run the next script:

```bash
def main():
    upper("Berlin")

if __name__ == "__main__":
    main()
```

* Your result should look like this:

```bash
BERLIN
```

### Task 2.1.11

Your task is to type and run the following program that uses the ```replace``` function. The ```replace``` will help us to change the case of a string to upper case. 

* The ```replace``` takes two arguments, the text to find and the text to replace with.
* Type and run the next script:

```bash
def main():
	protein = "vlspadktnv"
	# replace valine with tyrosine
	print(protein.replace("v", "y"))
if __name__ == "__main__":
    main()
```

* Your result should look like this:

```bash
ylspadktny
```

### Task 2.1.12

Your task is to type and run the following program that uses the colon slicing operator ```:```. The ```operator``` will help us to extract part of the text into new variables. 

* Type and run the next script:

```bash
def main():
	text = "I live in Berlin"
	print(text[10:])
if __name__ == "__main__":
    main()
```

* Your result should look like this:

```bash
Berlin
```
