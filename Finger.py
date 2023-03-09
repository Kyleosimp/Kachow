def startstop_codon(dna, frame):
    """TO CHECK THE PRESENCE OF START CODON AND ITS POSITION"""
    start_codons = ['ATG', 'atg']
    stop_codons = ['TAA', 'TAG', 'TGA', 'taa', 'tag', 'tga']  # reference list of start and stop codons
    for i in range(frame, len(dna), 3):
        codon1 = dna[i:i+3]
        if codon1 in start_codons:
            position1 = dna.index(codon1)  # getting the index of the start codon
            ORF_start = position1+1
            for j in range(position1, len(dna), 3):
                codon2 = dna[j:j+3]
                if codon2 in stop_codons:
                    position2 = dna.index(codon2)  # getting the index of the stop codon
                    ORF_stop = position2+1
                    break  # terminating the loop when a stop codon is found
    try:
        return len(dna[position1:position2])+2
    except UnboundLocalError:
        None

def finding_ORF(frame, records):
    """TO IDENTIFY THE ORF IN THE READING FRAMES AND
    IDENTIFY THE LONGEST ORF IN EACH SEQUENCE AND THE POSITION OF THE START CODON"""
    sequences = [reads.seq for reads in records]  # creating a list of all the sequence reads as elements of the list
    ORF_lengths = {}
    positions = {}
    max_lenth_ORFs = []
    for read in range(len(records)):  # loop for accessing each sequence read from the list
        seq = str(sequences[read])
        a = startstop_codon(seq, frame)  # calling the codon reading function
        if a == None:  # assigning value for reads with no codons
            a = 0
        ORF_lengths[records[read].id] = a  # creating a dictionary of ORF lengths(value) and sequence IDs(key)
    max_len = max(ORF_lengths, key=ORF_lengths.get)  # getting the ID of the Sequence read containing the maximum length ORF
    # printing the result
    print("Longest ORF in Frame %d is of length %d and its ID is %s." % (frame+1, ORF_lengths[max_len], max_len))
