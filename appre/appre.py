import argparse

def modify_text_file(input_file, output_file, append_text, prepend_text, remove_spaces, to_uppercase, to_lowercase):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # Remove spaces if specified
            if remove_spaces:
                line = line.replace(" ", "")
            
            # Uppercase if specified
            if to_uppercase:
                line = line.upper()

            # Lowercase if specified
            if to_lowercase:
                line = line.lower()

            # Append/Prepend text to the start and end of each line
            modified_line = append_text + line.strip() + prepend_text
            
            # Write the modified line to the output file
            outfile.write(modified_line + '\n')

def main():
    parser = argparse.ArgumentParser(
        description='Modify a text file with specified options.',
        epilog='Example Usage:\n'
               'python appre.py -a -p -s input.txt output.txt "CTF{" "}FLAG"\n'
               'python appre.py -a -s -U input.txt output.txt "Prefix" "Suffix"'
    )
    parser.add_argument('input_file', help='Input file path')
    parser.add_argument('output_file', help='Output file path')
    parser.add_argument('append_text', help='Text to append')
    parser.add_argument('prepend_text', help='Text to prepend')
    parser.add_argument('-a', '--append', action='store_true', help='Append text to the start of each line')
    parser.add_argument('-p', '--prepend', action='store_true', help='Prepend text to the end of each line')
    parser.add_argument('-s', '--spaces', action='store_true', help='Remove all white spaces in each line')
    parser.add_argument('-U', '--upper', action='store_true', help='Make all letters Uppercase')
    parser.add_argument('-L', '--lower', action='store_true', help='Make all text lowercase')
    
    args = parser.parse_args()

    append_text = args.append_text if args.append else ''
    prepend_text = args.prepend_text if args.prepend else ''

    modify_text_file(args.input_file, args.output_file, append_text, prepend_text, args.spaces, args.upper, args.lower)

if __name__ == '__main__':
    main()
