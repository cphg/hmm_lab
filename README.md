# CpG Island HMM

## Task 1

Your first task is to hand-tune a basic CpG island finder. Our model will be very simple (simpler than the one you read about). Our state space will have two states: CpG island and background. But instead of modeling individual nucletides, we'll model dinucleotides. So we're considering a sequence of dinucleotides, which have either two possibilities, either it *is* a CpG, or it is not.

In the file `cgi_hmm.py` you'll find a simple HMM model for a CpG island finder. If you run the code, you can see the output of the viterbi parse, showing where the predicted islands are. Unfortunately, this model is not working because the parameters have been initialized randomly.

Your task is to think about what the initiation, emission, and transition probabilities should be, and through trial-and-error, come up with parameters that allow the model to make a reasonable segmentation of the `chunk.fa` sequence.

To complete the assignment, provide 3 things (7 points):

1. Your final code where you've parameterized the model by hand.
2. The output plot (produced by the `cgi_plot` function) showing your viterbi parse on the sequence in `chunk.fa`.


## Task 2

Answer the following question (3 points):

3. Describe the 3 different broad applications/problems an HMM can be applied to, and name an algorithm that is used to solve each one.