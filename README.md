# InSpiria2021 - Hackathon

These are the scripts used for three of the problems. 

Dirty programming rules apply:
 * variable names can be single letters
 * Using `eval()` is OK
 * Programs can go into infinite loops, as long as they tell you something interesting
 * Copy-pasting pprint output wins over pickling results

 ## Puzzle #7: Mike's big oops:

 First run `oopser.py` to find out which ops correspond to which opcodes. It will eliminate any operation that does not produce the right results for the test samples, then it will loop on the opcodes and substract known operations until only one op per opcode remains.

 Then run `runner.py` to execute the sample program. Registers are printed after each op, so take the last one printed.

 ## Puzzle #4: Luc's fireflies:

 The first program, `chthulhu.py` runs the simulation and computes the stars alignment value based on the number of distinct X and Y coordinates. It prints the sky everytime a better alignment is found. It never terminates as the stars fly to infinity.

 The second program, `ftaghn.py` takes the last printed sky and prints it to the terminal so everyone can read the Elder God's message.

 ## Puzzle #5: Francois' deck permutation crypto:

 Problem: The algo pointed to by the link is O(N!). In this case N is 20. Any iterative solution, even optimized to assembly, will never terminate.
 
 Solution: Find an algo with better runtime characteristics

 After much Googling and Stack Overflowing, I end up with:

 https://stackoverflow.com/questions/6884708/ranking-and-unranking-of-permutations-with-duplicates
 
 Which is O(N) and will terminate in 20 iterations instead of 20!.

 The Stackoverflow answer gives details about the encryption part, but decryption can be deduced and was implemented in `permutation.py`.

## Puzzle #8: Mike's revenge:

Not enough time to finish. Partial code can be found in `runner_revenge.py`