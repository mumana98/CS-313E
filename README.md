# CS 313E Elements of Software Design

### Table of Contents

- [Description](#description)
- [Assignment 1](#Assignment-1)
- [Assignment 2](#Assignment-2)
- [Assignment 3](#Assignment-3)
- [Assignment 4](#Assignment-4)
- [Assignment 5](#Assignment-5)
- [Assignment 6](#Assignment-6)
- [Assignment 7](#Assignment-7)
- [Assignment 8](#Assignment-8)
- [Assignment 9](#Assignment-9)
- [Assignment 10](#Assignment-10)
- [Assignment 11](#Assignment-11)
- [Assignment 12](#Assignment-12)
- [Assignment 13](#Assignment-13)
- [Assignment 14](#Assignment-14)
- [Assignment 15](#Assignment-15)
- [Assignment 16](#Assignment-16)
- [Assignment 17](#Assignment-17)
- [Assignment 18](#Assignment-18)
- [Assignment 19](#Assignment-19)
- [Assignment 20](#Assignment-20)
- [Assignment 21](#Assignment-21)
---

## Description

A collection of all assignments completed in the CS 313E Elements of Software Design course taken at the University of Texas at Austin.

#### Technologies

- Python

[Back To The Top](#CS-313E-Elements-of-Software-Design)

---

## Assignment 1
### Game of Nim
Nim is a game of strategy played between two players. The players take turns in removing one or more counters from a given heap of counters among several distinct heaps. In normal play the player who takes the last counter wins. The more common variation (known as misere play) of Nim where the player who takes the last counter loses.

[Back To The Top](#CS-313E-Elements-of-Software-Design)

---

## Assignment 2
### Cryptography
Cryptography is an ancient study of secret writing. There is a wealth of literature in this field. An extremely readable book on this subject is The Code Book by Simon Singh. This is a field of study that is of particular relevance in Computer Science. Given the widespread use of computers, one of the things people are interested in is making transactions over the internet more secure.

There are two classes of ciphers - substitution ciphers and transposition ciphers. The substitution ciphers replace individual characters in a string. Transposition ciphers on the other hand scramble the characters in the string. We will look at two representative ciphers in both the classes. The transposition cipher that you will implement is called Rail Fence Cipher. For the subsitution cipher we have chosen the Vigenere Cipher.

[Back To The Top](#CS-313E-Elements-of-Software-Design)

---

## Assignment 3
### Baby Names
Complete a program that allows a user to query a data base of the 1000 most popular baby names in the United States per decade for the past 11 decades under the constraints described below. As always, you may add helper functions and should do so to provide structure to the program and reduce redundancy. One additional constraint: You must use a Dictionary in the solution. You are encouraged to use functions in the String, List and Dictionary classes to make the program easier to write. The Dictionary class has lots of functions that can make your job easier and one of the goals of this assignment is to learn those functions.

Your program will be processing a file with data obtained from the Social Security Administration. They provide a web site showing the distribution of names chosen for children over the last 100 years in the US (www.ssa.gov/OACT/babynames/).

The data represent the 1000 most popular boy and girl names for children born in the US going back to 1900. The data can be boiled down to a single text file as shown below. On each line we have the name, followed by the rank of that name in 1900, 1910, 1920, ..., 2000 (11 numbers). A rank of 1 was the most popular name that year, while a rank of 997 was not very popular. A 0 means the name did not appear in the top 1000 that year at all. The lines are in alphabetical order.

[Back To The Top](#CS-313E-Elements-of-Software-Design)

---

## Assignment 4
### Basic Geometry
This assignment is on object oriented programming. You will be developing two classes that are fundamental in Geometry - Point and Line. In main() you will test the various functions that you have written for the classes.

[Back To The Top](#CS-313E-Elements-of-Software-Design)

---

## Assignment 5
### Infinite Spiral of Numbers
Consider the natural numbers laid out in a square spiral, with 1 occupying the center of the spiral. 

This spiral has several interesting features. The southeast diagonal has several prime numbers (3, 13, 31, 57, and 91) along it. The southwest diagonal has a weaker concentration of prime numbers (5, 17, 37) along it.

To construct the spiral we start with 1 at the center, with 2 to the right, and 3 below it, 4 to the left, and so on. A part of the problem for this assignment is to figure out the rule to fill the spiral for an arbirary size. Once you have that rule you can complete the rest of the assignment.

[Back To The Top](#CS-313E-Elements-of-Software-Design)

---

## Assignment 6
### Pancake Sort
A cook has made a stack of pancakes on a skillet. But the pancakes are all of different sizes. Since the cook has OCD he wants to rearrange the pancakes so that they are in order - the largest pancake is on the bottom and the smallest pancake is on the top. He has a flat spatula that he can insert anywhere in the stack of pancakes and then he can flip all the pancakes on top of the spatula so that they are in reverse order. Using just this one operation of reversing a sub-stack of pancakes devise an algorithm that will allow the cook to sort the stack of pancakes in the fewest number of flips.

Your input is going to be in a file called pancakes.txt. The diameters of the pancakes are expressed as positive integers. There is one or more spaces between each integer. The number of pancakes will vary from 1 to 100. The first number represents the top of the pancake stack and the last number represents the bottom of the pancake stack.

Create an algorithm to sort the stack of pancakes. You may NOT use the built-in sort() function. You may only use the built-in max() and min() functions. You may also reverse, slice and concatenate lists using the built-in Python syntax.

[Back To The Top](#CS-313E-Elements-of-Software-Design)

---

## Assignment 7
### Work Till You Drop
Vyasa has to complete a programming assignment overnight. He has to write n lines of code before morning. He is dead tired and he tries drinking some black coffee to keep him awake. But each time he drinks a cup of coffee he stays awake for a short amount of time but his productivity goes down by a constant factor k

This is how he plans to write the program. He will write the first v lines of code, then drink his first cup of coffee. Since his productivity has gone down by a factor of k he will write v // k lines of code. He will have another cup of coffee and then write v // k ** 2 lines of code. He will have another cup of coffee and write v // k ** 3 lines of code and so on. He will collapse and fall asleep when v // k ** p becomes 0.

Now Vyasa does want to complete his assignment and maximize on his sleep. So he wants to figure out the minimum allowable value of v for a given productivity factor that will allow him to write at least n lines of code before he falls asleep.

[Back To The Top](#CS-313E-Elements-of-Software-Design)

---

## Assignment 8
### Recursion Exercises
These problems are taken from the Java Section of Coding Bat but modified for Python.

For each function that you wish to write, remove the comment symbol (#). Write your code and test it on the command line. 

[Back To The Top](#CS-313E-Elements-of-Software-Design)

---

## Assignment 9
### Recursion Exercises
These problems are taken from the Java Section of Coding Bat but modified for Python.

For each function that you wish to write, remove the comment symbol (#). Write your code and test it on the command line. 

[Back To The Top](#CS-313E-Elements-of-Software-Design)

---

## Assignment 10
### Nesting Boxes
Imagine a room full of boxes. Each box has a length, width, and height. Since the boxes can be rotated those terms are inter- changeable. The dimensions are integral values in a consistent system of units. The boxes have rectangular surfaces and can be nested inside each other. A box can nest inside another box if all its dimensions are strictly less than the corresponding dimensions of the other. You may only nest a box such that the corresponding surfaces are parallel to each other. A box may not be nested along the diagonal. You cannot also put two or more boxes side by side inside another box.

The list of boxes is given in a file called boxes.txt. The first line gives the number of boxes n. The next n lines gives a set of three integers separated by one or more spaces. These integers represent the 3 dimensions of a box. Since you can rotate the boxes, the order of the dimensions does not matter. It may be to your advantage to sort the dimensions in ascending order.

[Back To The Top](#CS-313E-Elements-of-Software-Design)

---

## Assignment 11
### Eight Queens Problem

The Eight Queens Problem is a fairly old problem that has been well discussed and researched. The first published reference to this problem was in a German Chess magazine in 1848 by Max Bezzel. In 1850, Franz Nauck published all 92 solutions of the problem for an 8x8 board. S. Gunther in 1874 suggested a method for finding solutions by using determinants and J.W.L. Glaisher extended this method. E. Dijkstra published a detailed description of the solution of the problem as a depth-first backtracking algorithm.

The original statement of the problem ran as follows - how can we place eight queens on a regular chess board such that no queen can capture another. It turns out there is no unique solution but 92 possible solutions of which only 12 are distinct. The 12 distinct solutions can generate all other solutions through reflections and / or rotations. 

[Back To The Top](#CS-313E-Elements-of-Software-Design)

---

## Assignment 12
### Reducible Words

What is the longest English word that remains a valid English word as you remove one letter at a time from the word?

The letters can be removed anywhere from the word one at a time but you may not rearrange the remaining letters to form a valid word. Every time you remove a letter the remaining letters form a valid English word. Eventually you will end up with a single letter and that single letter must also be a valid English word. A valid English word is one that is found in the Oxford English Dictionary or the Webster's Dictionary.

For want of a better term we will call such words reducible words. Here are two examples of reducible words:

1: sprite. If you remove the r you get spite. Remove the e and you get spit. Remove the s and you get pit. Remove the p and you get it. Remove the t and you get i or I which is a valid English word.

2: string. Take away the r and you have sting. Take away the t and you have sing. Take away the g and you have sin. Take away the s and you have in. Take away the n and you have i or I which is a valid English word.

So all reducible words will reduce to one of three letters - a, i, and o. We will not accept any other letter as the final one letter word.

[Back To The Top](#CS-313E-Elements-of-Software-Design)

---

## Assignment 13
### Greatest Path Sum in a Grid

Assume that you have square grid of positive integers. You want to start at the top left corner in the grid and work your way down to the bottom right corner. The constraint that you have is that you can only move either to the right or down from your current position in the grid. You want to take the path that gives you the greatest sum.

[Back To The Top](#CS-313E-Elements-of-Software-Design)

---

## Assignment 14
### Radix Sort

In this assignment you will modify the Radix Sort algorithm so that it sorts strings that have a mix of lower case letters and digits - similar to your UT EIDs.

In this version of Radix Sort we use Queues very naturally. Let us consider the following set of positive integers: 311, 96, 495, 137, 158, 84, 145, 63

We will sort these numbers with three passes. The number of passes is dependent on the number of digits of the largest number - in this case it is 495.
In the first pass we will go through and sort the numbers according to the digits in the units place (or the right most digit) and place the numbers in 10 queues for each of the digits 0 through 9. After this has been done we will dequeue the numbers in all the queues and enqueue them in an eleventh queue.

In the second pass, we will go through and sort the numbers according to the digits in the tens place and enqueue the numbers in the 10 queues. After this has been done, we will dequeue the numbers in all the queues and enqueue them in the eleventh queue - and so on.

[Back To The Top](#CS-313E-Elements-of-Software-Design)

---

## Assignment 15
### Singly Linked List

In this assignment you will be writing helper methods for the LinkedList class and test them. For the time being assume that the data that you are handling are integers. Later on when you use objects of other classes you will write compare functions for those classes and you can use your LinkedList class as is.

[Back To The Top](#CS-313E-Elements-of-Software-Design)

---

## Assignment 16
### Circular Linked List

The problem that you are going to solve is known as Josephus problem and it is stated as follows. There is a group of soldiers surrounded by an overwhelming enemy force. There is no hope for victory without reinforcements, so they make a pact to commit suicide.
They form a circle and a number n is picked from a hat. One of their names is also picked from a hat. Beginning with the soldier whose name is picked, they begin to count clockwise around the circle. When the count reaches n, that soldier is executed, and the count begins again with the next man. The process continues so that each time the count reaches n, a man is removed from the circle. Once a soldier is removed from the circle he is no longer counted. The last soldier remaining was supposed to take his own life. According to legend the last soldier remaining was Josephus and instead of taking his own life he joined the enemy forces and survived.

The problem is: given a number n, the ordering of the men in the circle, and the man from whom the count begins, to determine the order in which the men are eliminated from the circle and which man escapes. For example, suppose that n equals 3 and there are five men named A, B, C, D, and E. We count three men, starting at A, so that C is eliminated first. We then begin at D and count D, E, and back to A, so that A is eliminated next. Then we count B, D, and E (C has already been eliminated) and finally B, D, and B, so that D is the man who escapes.

You will use a circular linked list. You have worked on the linear linked list in your previous home work. To make a circular linked list you need to make the next field in the last link of the linked list point back to the first link instead of being null. From any point in a circular list it is possible to reach any other point in the list. Thus any link can be the first or last link. One useful convention is to let the external pointer to the circular list point to the last link and to allow the following link be the first link. We also have the convention that a null pointer represents an empty circular list.

Instead of giving the soldiers names you will assign them numbers serially starting from 1 (one). This way you can use the Link class that we discussed. In your program you will read the data from a file called josephus.txt. The first line gives the number of soldiers. The second line gives the soldier from where the counting starts. The third line gives the elimination number.

[Back To The Top](#CS-313E-Elements-of-Software-Design)

---

## Assignment 17
### Expression Tree

For this assignment you will read a file expression.txt and create an expression tree. The expression will be a valid infix expression with the all the necessary parentheses so that there is no ambiguity in the order of the expression. You will evaluate the expression and print the result. You will also write the prefix and postfix versions of the same expression without any parentheses.

In an expression tree the nodes are either operators or operands. The operators will be in the set ['+', '-', '*', '/', '//', '%', '**']. The operands will be either integers or floating point numbers. All the operand nodes will be leaves of the expression tree. All the operator nodes will have exactly two children.

[Back To The Top](#CS-313E-Elements-of-Software-Design)

---

## Assignment 18
### Encryption / Decryption with Binary Search Trees

In this assignment you will create a simple encryption scheme using a binary search tree. To encode a sentence, insert each letter into a binary tree using the ASCII value as a comparative measure.

To encode the sentence meet me, start by inserting the letters "m", followed by "e" and followed by "t" into the binary tree. In the first insertion, the binary tree is empty, so "m" becomes the root node of the tree. The "e" is inserted next. Since "e" is less than "m", it becomes the left child of "m" node. The second "e" is not inserted as there is an "e" in the tree already. The "t" becomes the right child of the "m" node. The next character is the space character and is considered less than any letter and becomes the left most leaf.

To encode, use the following convention: assign the root node of the tree a "*" character. Every other character in the tree, assign a character string based on how many "lefts" and how many "rights" are involved in the tree traversal. For "left" traversals, use a "<", for "right" traversals use a ">". In the above example, "e" will be represented as "<" and "t" will become ">". The space character will become "<<". To complete the code, every character must be separated by a marker called the delimiter. Use "!" (the exclamation mark) as a delimiter for the code.

Using these conventions, the string "meet me" when encrypted becomes "*!<!<!>!<<!*!<".

For this assignment we are only going to encrypt lower case letters "a" through "z" and the space character. When the input string is given for encryption, convert it to lower case. Only encrypt the lower case letters and spaces. Ignore all digits, punctuation marks, and special characters. Basically, you will drop the the digits, punctuation marks and special characters.

For the encryption to work, a key has to be given. This key is used to create the binary search tree. The encryption key for this assignment will be pangrams. A pangram is a sentence where every letter of the alphabet is used at least once.

[Back To The Top](#CS-313E-Elements-of-Software-Design)

---

## Assignment 19
### Binary Trees

In this assignment you will be adding to the classes Node and Tree that we developed in our lectures. There are several short methods that you will have to write.

Write a method is_similar() that takes as input two binary trees and returns true if the nodes have the same key values and are arranged in the same order and false otherwise.

def is_similar (self, pNode):

Write a method print_level() that takes as input the level and prints out all the nodes at that level. If that level does not exist for that binary search tree it prints nothing. Use the convention that the root is at level 1.

def print_level (self, level):

Write a method get_height() that returns the height of a binary tree. Recall that the height of a tree is the longest path length from the root to a leaf.

def get_height (self):

Write a method num_nodes() that returns the number of nodes in the left subtree from the root and the number of nodes in the right subtree from the root and the root itself. This function will be useful to determine if the tree is balanced.

def num_nodes (self):

[Back To The Top](#CS-313E-Elements-of-Software-Design)

---

## Assignment 20
### Graph Traversal

In this assignment you will be creating a graph from an input data file called graph.txt. The first line in that file will be a single integer v. This number will denote the number of vertices to follow. The next v lines will be the labels for the vertices. There will be one label to a line. Assume that the labels are unique. The next line after the labels for vertices will be a single number e. This number will denote the number of edges to follow. There will be one edge per line. Each edge will be of the form - fromVertex, toVertex, and weight. If the weight is not given, assign a default weight of 1 to that edge. After the list of edges there will be a label for the starting vertex. This will be the starting vertex for both the Depth First Search and Breadth First Search. After that there will be two cities and you will have to delete the edges connecting the two cities and print the adjacency matrix. Then there will be a single city and you will delete this vertex and all edges from and to this vertex. You will print the list of vertices and the adjacency matrix showing all edges from it and all edges to it have been deleted. To delete a vertex from the graph - remove it from the vertex list and remove the corresponding row and column for this vertex.

[Back To The Top](#CS-313E-Elements-of-Software-Design)

---

## Assignment 21
### Topological Sort

In this assignment you will be creating a graph from an input gif file called dag.gif. You will complete the topo.txt file.

The first line in that file will be a single integer v. This number will denote the number of vertices to follow. The next v lines will be the labels for the vertices in alphabetical order. There will be one label to a line. The labels are unique. The next line after the labels for vertices will be a single number e. This number will denote the number of edges to follow. There will be one edge per line. Each edge will be of the form - fromVertex and toVertex. Assign a default weight of 1 to each edge.

Here is the outline of the code that we developed in class that you will be modifying. You will use topo.txt instead of graph.txt as your input file. You can add an Edge class if you want to. You may use any of the functions that you wrote for the GraphTraversal class in your last assignment. You can add more functions as needed. You will first test if the given Graph does not contain a cycle and then do a topological sort on that Graph. For your output, the vertices on a given level must be printed in alphabetical order.

[Back To The Top](#CS-313E-Elements-of-Software-Design)

---