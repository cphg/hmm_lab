import matplotlib.pyplot as plt
import numpy as np
from hmmlearn import hmm

np.random.seed(42)

def cgi_plot(states, cg_positions):
	"""
	Produce a basic plot showing where CpG dinucleotides occur
	in a sequence, and what state the model is in.
	"""
	fig, ax = plt.subplots(figsize=(100, 10))
	ax.plot(states)
	ax.set_title('States over time')
	ax.set_xlabel('Genome')
	ax.set_ylabel('State')
	cgs = np.argwhere(cg_positions.flatten()>0)
	ax.plot(cgs.flatten(), [-0.2]*len(cgs),'|', color='k')
	plt.yticks([-.2, 0, 1], ["CpGs", "bg", "Island"])
	return plt

def seq_to_cg(sequence):
	"""
	Convert a DNA sequence into CpG-dinucleotide encoding, where 1 represents
	a CpG and 0 represents anything else.
	"""
	cgmarks = np.zeros(len(sequence), dtype=np.uint32).reshape(len(sequence), 1)
	for i in range(0, len(sequence)):
		dinucleotide = sequence[i:(i+2)]
		if dinucleotide == "GC":
			cgmarks[i] = 1
		else:
			cgmarks[i] = 0
	return cgmarks

# Parameterize a basic CpG island finder.
# It has been initialized with random parameters
gen_model = hmm.CategoricalHMM(n_components=2, random_state=99)
gen_model.startprob_ = np.array([0.5, 0.5])
gen_model.transmat_ = np.array([[0.5, 0.5],
                                [0.5, 0.5]])
gen_model.emissionprob_ = \
    np.array([[50 / 100, 50 / 100],
              [50 / 100, 50 / 100]])

# A dummy demo sequence for you to test on
S = "GCTGGCATCGCGCGTACTACTATCAGCGCGCGCGCGCGCGCGACGGCGAGCGCGACGCGGCCGGCAGCAGCGACGACGGACGCTATACTATCATGCTACGACGATCGTATCTATGCTGGCATCGCGCGTACTACTATCAGCGCGCGCGCGCGCGCGACGGCGAGCGCGACGCGGCCGGCAGCAGCGACGACGGACGCTATACTATCATGCTACGACGATCGTATCTATGCTGGCATCGCGCGTACTACTATCAGCGCGCGCGCGCGCGCGACGGCGAGCGCGACGCGGCCGGCAGCAGCGACGACGGACGCTATACTATCATGCTACGACGATCGTATCTATGCTGGCATCGCGCGTACTACTATCAGCGCGCGCGCGCGCGCGACGGCGAGCGCGACGCGGCCGGCAGCAGCGACGACGGACGCTATACTATCATGCTACGACGATCGTATCTATGCTGGCATCGCGCGTACTACTATCAGCGCGCGCGCGCGCGCGACGGCGAGCGCGACGCGGCCGGCAGCAGCGACGACGGACGCTATACTATCATGCTACGACGATCGTATCTATGCTGGCATCGCGCGTACTACTATCAGCGCGCGCGCGCGCGCGACGGCGAGCGCGACGCGGCCGGCAGCAGCGACGACGGACGCTATACTATCATGCTACGACGATCGTATCTAT"

# Find the viterbi parse of this sequence and plot it
# At first this will not yield a good segmentation; you will need to tune the
# above parameters by hand to get a parse you're happy with.
cgmarks = seq_to_cg(S)
viterbi_path = gen_model.predict(cgmarks)
plt = cgi_plot(viterbi_path, cgmarks)
plt.savefig("cgi.png")


# Read in a sequence from a fasta file like this:
with open("chunk.fa", "r") as f:
	f.readline()  # discard
	S = f.read().replace("\n", "")

