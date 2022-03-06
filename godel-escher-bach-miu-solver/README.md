# godel-escher-bach-miu-solver

A brute-force mechanistic program to attempt solving the MU problem.
Reference: Douglas Hofstadter's _Godel, Escher, Bach_, Chapter 1.

## Operation

1. Supply two arguments: 
    * The initial theorem (string) to which the transformation rules will be successively applied.
    * The number of iterations over which to apply the rules.

2. The initial theorem is added to a dictionary.

3. Each rule is evaluated on the theorem.  If the rule can be applied, the derived string is added to the dictionary.

4. Repeat applying each rule to each new string in the dictionary until the goal `MU` is acheived, or the target number of iterations is reached.

## Limitations

1. The program hasn't been fully optimized.

2. The path from a string to its descendants isn't tracked; every string created is just added to the bucket.

## Testing

Includes unit tests for each of the four rules.
