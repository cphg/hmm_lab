# HMM CpG island finder lab

## Task 1

Your first task is to hand-tune a basic CpG island finder. Our state space will have two states: CpG island and background. Our emission model will be very simple (simpler than other HMMs that model each nucleotide: instead of modeling individual nucletides, we'll model dinucleotides. So our model considers a sequence of dinucleotides, which have either two possibilities, either it *is* a CpG, or it is not. Thus, the input sequence is a string of 0 and 1, where 1 represents a CpG and 0 represents anything else.

In the file `cgi_hmm.py` you'll find:

- a simple HMM model for a CpG island finder.
- a function to encode a regular DNA sequence into the 0/1 dinucleotide representation
- a function to visualize a dinucleotide sequence together with a state sequence output from the HMM.

If you run the code, you can see the output of the viterbi parse, showing where the predicted islands are. Unfortunately, this model is not working because the parameters have been initialized randomly. Your task is to think about initiation, emission, and transition probabilities, and through trial-and-error, adjust the parameters to allow the model to make a reasonable segmentation of the `chunk.fa` sequence.

To complete the assignment, provide 2 things (7 points):

1. Your final code where you've parameterized the model by hand.
2. The output plot (produced by the `cgi_plot` function) showing your viterbi parse on the sequence in `chunk.fa`.


## Task 2

Answer the following question (3 points):

3. Describe the 3 different broad applications/problems an HMM can be applied to, and name an algorithm that is used to solve each one.