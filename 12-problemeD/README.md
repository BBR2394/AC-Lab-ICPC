# Fibonacci Words

The Fibonacci word sequence of bit strings is defined as:

0 : 0  
1 : 1  
2 : 10  
3 : 101  
4 : 10110  
5 : 10110101  
6 : 1011010110110  
7 : 101101011011010110101  
8 : 1011010110110101101011011010110110  
9 : 1011010110110101101011011010110110101101011011010110101  

Given a bit pattern p and a number n, how often does p occur in F (n)?

## Input

The first line of each test case contains the integer n (0 ≤ n ≤ 100). The second line contains the bit
pattern p. The pattern p is nonempty and has a length of at most 100 000 characters.

## Output

For each test case, display its case number followed by the number of occurrences of the bit pattern p in
F (n). Occurrences may overlap. The number of occurrences will be less than 2 63 .

## Exec Test 

```bash
pytest Fibonacci_exo.py
```