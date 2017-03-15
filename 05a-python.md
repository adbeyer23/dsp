# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Both lists and tuples are a sequence of objects, and unlike, for example, dictionaries, both maintain the order the objects are in. Both are iterable and both can hold any object. The biggest difference between the two is that lists are mutable and tuples are immutable. For example, lists can be appendable, but tuples cannot. Tuples use a bit less memory and and are a bit faster than lists. Because dictionaries require immutable keys, only tuples can work as keys for a dictionary.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets both contain multiple objects. However, sets cannot have duplicate elements, and lists can have them. A set's objects are unordered, while a list's objects are ordered. For example let's say we have a list of numbers 1,2,2,3,3,4. A list would produce the numbers as [1,2,2,3,3,4] while a set would produce {1,2,3,4}--getting rid of the duplicates. If you were to try to get the value at the zero index for list, python would produce a 1, and would produce an error for the set as sets are unorderable.  
When looking for an element, sets are faster than lists, because sets are based on hash tables, meaning if searching a list for an object, python only needs to check to see if object is at a position based on it's hash. With a list, elements are searched one by one to see if that elmeent matches the one you are looking for.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> A lambda function is a quick, anonymous function you can make for short-term use. Let's say that you want to make a simple, one-time use function that adds x +y. To make this function as a lambda function, all you would have to do is: add = lambda x,y: x+y. Calling add(1,2) would return 3. The word "lambda" works like a function "def", variables come after, and whatever is after the colon is whatever the function is returning. It is common to use lambda for custom sorting functions. Let's say you want to sort a list of tuples by the 3rd value. For example, [(1,5,2), (2,3,6), (-1,15,4)] could be sorted by calling the sorted function on this and passing lambda numbers: numbers[2] as the key. Sorted will call the lambda function on each tuple and sort based on what is returned by the function. And here, what is returned is the 3rd value of every tuple.

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions let one create lists in a very quick way using only one line. Let's say you have a list of numbers assigned to a variable called old_list,old_list= [1,2,3,4], and want to create a new list of numbers that adds 1 to each number in the  old list of numbers (so [2,3,4,5]). You could create a multi-lined for loop or simply new_list = [number+1 for number in numbers]. List comprehensions start with whatever you want to return (here it is number +1), then the variable you want to pass into what you want to return (number) an in what list you are interating over (numbers).  
    The function map works in a similar way to a list comprehension as it can be used to create a new list by calling a function over each item of a list. We could create a new list where we add 1 to each number in our list with a map function like so: new_list = list(map(lambda x: x+1, old_list)). The first parameter of map is the function you want to call on each item of the list (here I created an anonymous lambda function that simply returns the item  + 1), and the second paramter is the list of items you want to call the function on. The function map only creates a map object, so we have enclose this function in a list function to make a list of the numbers.  
    The function filter also creates a new list, but only creates a new list from values in which a function returns true.

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





