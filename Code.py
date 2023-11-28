def combine_fastq(input_files, output_file):
    with open(output_file, 'w') as outfile:
        for input_file in input_files:
            with open(input_file, 'r') as infile:
                outfile.write(infile.read())

# Example usage
input_files = ['1.fastq', '2.fastq', '3.fastq']
output_file = 'combined.fastq'

combine_fastq(input_files, output_file)
