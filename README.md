# ACNH_crossing_combo
Given all genotypes you have, list all crossing output from all possible pairs

## Usage:  
Starting from line 9:
    Edit the **ftype**="tulips" to the type of flower  
    Edit the **had**=[] to all the flower genotypes you have (See below)  
    Edit the **test_cross** to the two genotypes you want to test.
Then run `python ACNH_flower_crossing_combo.py`

Flower genotypes credit to https://docs.google.com/spreadsheets/d/11pRCX8G0xGizSYWgVhoUSu7pE-MV7AOprBcgSY1whB4/htmlview?usp=sharing#  
However, make the flowing changes for input:  
For **windflowers**, replace **"Oo"** in this google form with **"Yy"**  
For **tulips, lilies and cosmos**, replace **"Ss"** with **"Ww"**.  
Basically, you should have RYW for every flower excpet roses.

## Output:  
The script will generate a html file in the same directory named "ACNH_result_cross.html".  
Crossing pairs with new (not in your input "had" list) identifiable offspring (the one with a color that could only originated from one possible genotype) will be listed on top. The new identifiable offspring will be marked with a border in the table.  
Notice this is for getting new genotype, not limited to only new color.

If **test_cross** is given, the script will generate a html file named "ACNH_result_test_cross.html". Each pair of test using one of your owned genotype are shown. You could identify one out of your two testing parents if that one could generate offspring with new color.