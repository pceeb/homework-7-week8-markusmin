### Pseudocode 

# USAGE:

# python3 misebastes_anacapa_addon.py ecoPCR_RF_barcodes.fasta anacapa_table.csv 

# Following three lines are for when the script actually works and you can just
# specify your anacapa file at the start!


### Finding identical barcodes

# Import Biopython tools

# find_identical_barcodes.py

import sys
import Bio
from Bio import SeqIO

def find_identical_barcodes(fasta_file):
    # Create our hash table to add the sequences
    sequences={}

    # Using the Biopython fasta parse we can read our fasta input
    for seq_record in SeqIO.parse(fasta_file, "fasta"):
        # Take the current sequence
        sequence = str(seq_record.seq).upper()
       # Concatenate the ID of the current sequence to another one that is 
       # already in the hash table
       # Replace "S." with "Sebastes "
		sequences[sequence] += ", " + seq_record.id.replace("S.","Sebastes ")

    # Write the sequences
	with open("seq_dict", "w+") as output_file:
		for sequence in sequences:
		output_file.write(sequences)
    # Create a file in the same directory where you ran this script
    with open("clear_2_" + fasta_file, "w+") as output_file:
        # Just read the hash table and write on the file as a fasta format
        for sequence in sequences:
            output_file.write(">" + sequences[sequence] + "\n" + sequence + "\n")

    print("CLEAN!!!\nPlease check clear_" + fasta_file)


### Appending the matching species column to an Anacapa taxonomy file

# Use a for loop to add new data in each line

def anacapa_addon(capa)

	import sys
	
	# assign the second argument where you specified the Anacapa taxonomy table
	# to infile, open as "capa"
	infile=sys.argv[2]
	capa=open(infile,'r')

	for line in capa:
		# Split the lines
		line2=line.strip() \n
		# Split the line into elements by semicolon
		Element=line2.split(';')
		print(Element[0])
		# split Element[0] by ; take the last element [-1]
		
		if len(Element) > 6
		name=Element [-1]
		# Figure out how to do regex where you look for keys in your dictionary that at least
		# have the name of the species from the Anacapa table
		matching_species = sequences[sequence[.*(name).*]
		print(Element[0] + matching_species + Element[1-8]
	# Write a new output file with your additional column added
	with open("misebastes_" + capa, "w+") as output_file:
		for line in capa:
			output_file.write(line + "\n")

userParameters = sys.argv[1:]

try:
    if len(userParameters) == 2:
    	find_identical_barcodes(userParameters[1])
    	anacapa_addon(userParameters[2])
    else:
        print("There is a problem!")
except:
    print("There is a problem!")








