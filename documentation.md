# Documentation

## Young Diagrams and Tableaux

### `youngDiagram`
```mathematica
printYoungDiagram[List[Integer]]
```
Takes a list of integers representing a partition and prints the associated Young diagram.

Tests if the list is sorted and raises a warning if this is not the case.

### `isSortedDescending`
```mathematica
isSortedDescending[List[Integer]]
```
Takes a list of integers and checks if it is sorted in (non-strict) descending order.

### `printYoungTableau`
```mathematica
printYoungTableau[List[List[Integer]], Options]
```
Takes a nested list of integers, as a ragged array representing the Young tableau.

Options:
* `boxSize` (default 50) the size of a single box in the diagram
* `FontSize` (default 25) the size of the font
* `ColorFunction` (identity) a function acting on the list of numbers before they are output. For example,
    ```mathematica
     ColorFunction -> (Insert[#, Red, 3] &)
    ```
    which sets all numbers from the third number on to be printed in red

Note `FontSize` and `ColorFunction` start with a capital as they repurpose existing _Mathematica_ options, `boxSize` doesn't, so starts with a lower case letter.

### `youngTableau`
```mathematica
youngTableau[List[List[Integer]]]
```
The internal representation of a Young tableau as a ragged array wrapped in the `youngTableau` head.
The `StandardForm` output is given by calling `printYoungTableau`.

### `sortRows`
```mathematica
sortRows[youngTableau[List[List[Integer]]]]
```
Sorts the rows of a Young tableau into ascending order, which is generally allowed without changing any of the properties we care about.

### `shuffleTableau`
```mathematica
shuffleTableau[youngTableau[List[List[Integer]]]]
```
Permutes the numbers in the given Young tableau randomly.
Useful for testing functions like `sortRows`.

## Garnir Relations

### `usesAllNumbers`
```mathematica
usesAllNumbers[youngTableau[List[List[Integer]]]]
```
Returns `True` for an $n$ box tableau if every integer from 1 to $n$ appears exactly once in the tableau.

### `compareRaggedLists`
```mathematica
compareRaggedLists[List[Integer], List[Integer]]
```
Takes two lists of integers, or any other orderable quantities, and compares them element-wise, returning a list of boolean results, terminates when the end of the shortest list is reached.

### `findMisordering`
```mathematica
findMisordering[youngTableau[List[List[Integer]]]]
```
Takes a Young tableau and finds the first point at which it fails to be a standard Young tableau, that is the first point at which the numbers increase going right or down.
This point is encoded as a list `{rowNumber, columnNumber}`.
For a standard tableau it returns `{-1, -1}`.

### `isStandardTableau`
```mathematica
isStandardTableau[youngTableau[List[List[Integer]]]]
```
Returns `True` if the Young tableau is standard, and `False` otherwise.
Just calls `findMisordering` and checks if the result is `{-1, -1}`.

### `printColorStrip`
```mathematica
printColorStrip[youngTableau[List[List[Integer]]], {a_Integer, b_Integer}]
```
Prints the Young tableau setting all numbers between `a` and `b` (inclusive) to be red.
Useful for demonstrating Garnir relations.

### `pair`
```mathematica
pair[a, b]
```
Container type for a pair of values, displays as $\langle a , b \rangle$ in `StandardForm`.

### `generatePermutedLists`
```mathematica
generatePermutedLists[list_List, k_Integer, left_, right_]
```
Splits the list at position `k` then produces all lists given by permuting elements between the two lists, up to reordering of the lists.

### `pairToSwaps`
```mathematica
pairToSwaps[pairs_]
```
Takes the output of `generatePermutedLists` and converts it into a list of two element lists, which can be interpreted as elements to be swapped.

### `generateSwaps`
```mathematica
generateSwaps[firstRow_List, secondRow_List]
```
Takes in two lists, representing the two strips of a non-standard Young tableau between the first two misordered points.
Returns a list of swaps to apply.

### `reshapeRaggedArray`
```mathematica
reshapeRaggedArray[list_List, template_]
```
Takes two lists, with the length of `list` being the same as the length of `Flatten[template]`, and then returns a list with the elements of `list` and the shape of `template`.


### `applySwaps`
```mathematica
applySwaps[youngTableau[numbers_], swaps_List]
```
Takes a Young tableau and a list of swaps to apply and then applies them.

### `applyGarnir`
```mathematica
applySwaps[youngTableau[List[List[Integer]]]]
```
Takes a Young tableau and applies the Garnir relations once to decompose it.
Returns a list of Young tableau's which sum with the original Young tableau to produce zero.

### `decomposeTableau`
```mathematica
decomposeTableau[youngTableau[List[List[Integer]]]]
```
Takes a Young tableau and recursively applies the Garnir relations until it is in standard form.
Returns a formal sum of Young tableau.

## Dimensions
### `hookLengths`
```mathematica
hookLengths[youngTableau[List[List[Inteeger]]]]
```
Takes a Young tableau and returns a Young tableau where the entries are the hook lengths, the number of boxes to the right and below, plus the box itself.

### `hookNumber`
```mathematica
hookNumber[youngTableau[List[List[Integer]]]]
```
Takes a Young tableau and returns the hook number, the product of the hook lengths.

### `hookFormula`
```mathematica
hookFormula[youngTableau[List[List[Integer]]]]
```
Takes an $n$ box Young tableau and returns the dimension of the irrep of $S_n$ it represents.
This is given by
$$\frac{n!}{\text{hook number}}$$


## Irreps of $S_n$
### `generateStandardTableaux`
```mathematica
generateStandardTableaux[youngTableau]
```
Takes a Young tableau and generates all standard tableau of the same shape.

### `standardTableauDotProduct`
```mathematica
standardTableauDotProduct[n X, m Y]
```
Takes two standard Young tableau of the same shape, `X` and `Y`, with optional numeric factors $n$ and $m$, and computes $nm(X \cdot Y)$, where the standard tableau are taken to define an orthonormal basis.

### `tableauToPermutation`
```mathematica
tableauToPermutation[youngTableau[List[List[Integer]]]]
```
Takes a Young tableau, and interprets it as the permutation required to produce it from the ordered tableau, with all numbers in order left to right, top to bottom.

### `applyPermutationToTableau`
```mathematica
applyPermutationToTableau[permutation_Cycles, youngTableau[List[List[Integer]]]]
```
Takes a permutation and applies it to the numbers in a Young tableau.

### `representation`
```mathematica
representation[permutation_Cycles, youngTableau[numbers_]]
```
Takes a permutation and returns its representation matrix in the irreducible representation labelled by the Young tableau.

### `testRepresentation`
```mathematica
testRepresentation[n_Integer, youngTableau[List[List[Integer]]]]
```
Takes a positive integer, $n$, and an $n$ box Young tableau, and checks that the multiplication table of the irreducible representation of $S_n$ labelled by the Young tableau is as expected.

### `testRepresentationSample`
```mathematica
testRepresentationSample[n_Integer, youngTableau[List[List[Integer]]], samples_Integer]
```
Similar to `testRepresentation`, but instead of generating the full group table randomly selects a number, `samples`, of group elements and tests the group table in the representation for these elements.

## Symmetrisers and Antisymmetrisers
### `symmetriser`
```mathematica
symmetriser[legs_List, youngTableau[List[List[Integer]]]]
```
Takes a list of integers, labelling the legs of a tensor, and returns a symmetriser over these legs in the irrep of $S_n$ labelled by the Young tableau.

### `antisymmetriser`
```mathematica
antisymmetriser[legs_List, youngTableau[List[List[Integer]]]]
```
Takes a list of integers, labelling the legs of a tensor, and returns an antisymmetriser over these legs in the irrep of $S_n$ labelled by the Young tableau.

### `testIdempotency`
```mathematica
testIdempotency[x]
```
Takes a matrix and returns `True` if that matrix is idempotent, that is $x^2 = x$.

## Young Projectors
### `getTableauRows`
```mathematica
getTableauRows[youngTableau[List[List[Integer]]]]
```
Takes a Young tableau and returns a list of the rows, which are themselves lists of integers.

### `getTableauColumns`
```mathematica
getTableauColumns[youngTableau[List[List[Integer]]]]
```
Takes a Young tableau and returns a list of the columns, which are themselves lists of integers.

### `youngProjector`
```mathematica
youngProjector[Y1, Y2]
```
Takes two Young tablueax and returns the projector associated with `Y1` in the irrep of $S_n$ associated with `Y2`.

## Shift
## `shift`
```mathematica
shift[currentLegs_List, shiftLegs_List, youngTableau[List[List[Integer]]]]
```
Takes a list of integers labelling the legs of a tensor on which an operator acts, and a list of integers labelling the legs of the tensor on which we _wish_ for the operator to act, and returns the permutation required to make this happen in the irrep of $S_n$ labelled by the given Young tableau.

## Hermitian Young Projectors
### `removeLastBox`
```mathematica
shift[youngTableau[List[List[Integer]]]]
```
Takes a Young tableau and returns a Young tableau with the box with the highest number removed.
Assumes that this number occurs only once.

## `hermitianYoungProjector`
```mathematica
hermitianYoungProjector[Y1, Y2]
```
Takes two Young tableau, and returns the Hermitian Young projector associated with `Y1` in the irrep of $S_n$ labelled by `Y2`.

## $3n$-$j$
### `threej`
```mathematica
threej[X, Z, Y]
```
Takes three Young tableaux and returns the $3j$ given by these in the convention of Cvitanovic's book.
Note that $Y$ must have as many boxes as $X$ and $Z$ combined.

### `sixj`
```mathematica
sixj[X, Y, Z, U, V, W]
```
Takes six Young tableaux and returns the $6j$ given by these in the convention of Cvitanovic's book.

## Yamanouchi Words
### `isWeaklyDecreasing`
```mathematica
isWeaklyDecreasing[List[Integer]]
```
Takes a list of integers and returns `True` if it is weakly decreasing, that is, if each successive element is at most as large as the previous element.

### `isLatticeWord`
```mathematica
isLatticeWord[List[Integer]]
```
Takes a list of integers and returns `True` if it is a lattice word, that is, if every prefix contains at least as many numbers $n$ as it does $n + 1$.

### `isYamanouchiWord`
```mathematica
isYamanouchiWord[List[Integer]]
```
Takes a list of integers and returns `True` if it is a Yamanouchi word, that is, if its reverse is a lattice word.

Note that sometimes the phrase "Yamanouchi word" is used as "lattice word" is used here, so without the reverse.