# ICPC
# 1998 problem D
the goal is to create a kind of search engine (like google)
the program take some data coresponding to the data per pages (the data where we are looking for information) and some query.
So according to the data, the program run the query and give us the best page to find the result.

# there is a little bug
when to result are the same but not in the good order

### how does it works
First of all, we have a Maximum (called Nmax) which is the maximum number of word used (here 5). And we applied a value to each word from a page/query, and we decrement this value for each keyword example : 
```
P Smalltalk programming computers
Q Smalltalk computers
```
For the Page : 
- "Smalltalk" has 5 has value
- "programming" has 4
- and "computers" has 3
For the query :
- "Smalltalk" has 5
- "computers" has 4

## compute a result
So, after applying a value, we can compute a result for the querys, example : 
```
P Smalltalk programming computers 
P computers programming
P computers Smalltalk
P programming
Q Smalltalk
Q programming
Q Smalltalk programming 
```
So we get as value : 
Page one : Smalltalk = 5, programming = 4, computers = 3
Page two : computers = 5, programming = 4
Page three : computers = 5, Smalltalk = 4
Page four : programming = 5
Query one : Smalltalk = 5
Query two : programming = 5
Query three : Smalltalk = 5, programming = 4

And we just need to multiply each same keyword for each page, 

- for the first query :
    - with the first page : 
    Q1 Smalltalk * P1 Smalltalk = 5 * 5 = 25
    - With the second page :
    There is no keyword Smalltalk on the second page so it is 0
    - With the third page :
    Q1 Smalltalk * P3 Smalltalk = 5 * 4 = 20
    - With the fourth page : 
    There is no keyword Smalltalk on the fourth page so it is 0

- for the second query:
    - With the first page :
    Q2 programming * P1 programming = 5 * 4 = 20
    - With the second page : 
    Q2 programming * P2 programming = 5 * 4 = 20
    - With the third page :
    There is no keyword Programming on the third page so it is 0
    - With the fourth page : 
    Q2 programming * P4 programming = 5 * 5 = 25


- for the third :
    - With the first page : 
    Q3 Smalltalk * P1 Smalltalk + Q3 programming * P1 programming = 5*5 + 4*4 = 21
    - With the second page :
    - 
    - With the third page :

    - With the fourth page : 


    
So, we get on the standard output : 
Q1 : P1 P3 
Q2 : P4 P1 P2
Q3 : P1 P4 P3 P2 

