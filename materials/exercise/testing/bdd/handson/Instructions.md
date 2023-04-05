# Instructions 

We now want to expand our Monster Hunter code.

The new source code lies within the `game` directory 
were you can find three different files 
1. hero.py 
2. items.py
3. monsters.py 

#### 1. Hero 
the hero.py file contains the code for our hero,
that is able to carry around items and hit enemies 

#### 2. Items 
Here you can find the definition of different item types from consumables 
to our weapons the hero will need to slay creatures and save the day

#### 3. Monsters 
This file contains the definition of Monsters and a concrete implementation of the Wolf. 


## Task 
Create the Gherkins features with the following content:
1. If the hero has 0 items and adds a sword, he will have 1 item 
2. If the her0 has 5 items and add another, he will still have 5 items (the limit)
3. If the hero attacks a wolf with 10 HP using a sword doing three damage, the wolf will have 7hp left 
4. If the hero attacks that wolf using the same sword two more times  the wolf will have  0 hp left 
