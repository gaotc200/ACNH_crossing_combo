# ACNH_crossing_combo
Given all genotypes you have, list all crossing output from all possible pairs

## Usage:  
In line 10, edit the **ftype**="tulips" to the type of flower  
In line 11, edit the **haved**=[] to all the flower genotypes you have (See below)  
Then run `python ACNH_flower_crossing_combo.py`

Flower genotypes credit to https://docs.google.com/spreadsheets/d/11pRCX8G0xGizSYWgVhoUSu7pE-MV7AOprBcgSY1whB4/htmlview?usp=sharing#  
However, make the flowing changes for input:  
For **windflowers**, replace **"Oo"** in this google form with **"Yy"**  
For **tulips, lilies and cosmos**, replace **"Ss"** with **"Ww"**.  
Basically, you should have RYW for every flower excpet roses.

## Output:  
The script will generate a tsv file in the same directory named "<ftype>.tsv".  
- Each 2 rows represents a crossing pair, with the first row indicating genotypes, and second row indicating colors.
- The first and second columns are parents.  
- The rest columns are all possible outcome.

You could do any further filters as you wish. Examples:  
- For a crossing pair, if a color only appear once in the possible outcomes, then this one is identifiable (given your current genotypes pool).
- Search a certain genotype or color, see if there exist a certain crossing pair and if the desired one could be identified by color selection.
