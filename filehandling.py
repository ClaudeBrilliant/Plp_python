
def process_file(input_filename, output_filename):
    # Read the contents of the input file
    try:
        with open(input_filename, 'r') as input_file:
            file_contents = input_file.read()
    except FileNotFoundError:
        print(f"Error: {input_filename} not found.")
        return
    
    # Count the number of words
    word_count = len(file_contents.split())
    
    # Convert text to uppercase
    uppercase_contents = file_contents.upper()
    
    # Write processed text and word count to output file
    with open(output_filename, 'w') as output_file:
        output_file.write(f"Word Count: {word_count}\n\n")
        output_file.write(uppercase_contents)
    
    print(f"Processing complete. Processed text written to {output_filename}")
    print(f"Total words: {word_count}")
