# appre.py
## Text File Modifier
### appre.py is a simple Python script that allows you to modify a text file by appending/prepending text, removing spaces, and converting text to uppercase or lowercase.

## Usage
```bash
python appre.py input_file output_file append_text prepend_text [-a] [-p] [-s] [-U] [-L]
```
### Arguments
input_file: Path to the input text file.
output_file: Path to the output text file.
append_text: Text to append at the start of each line.
prepend_text: Text to prepend at the end of each line.
### Options
- -a, --append: Append text to the start of each line.
- -p, --prepend: Prepend text to the end of each line.
- -s, --spaces: Remove all white spaces in each line.
- -U, --upper: Make all letters uppercase.
- -L, --lower: Make all text lowercase.

## Example Usage
Example 1:
Append and prepend text, remove spaces, and make uppercase:

```bash
python appre.py input.txt output.txt "CTF{" "}FLAG" -a -p -s -U
```

Example 2:
Append and remove spaces, and make uppercase:

```bash
python appre.py input.txt output.txt "Prefix" -a -s -U
```
### Note
Use quotes (") around text containing spaces.
The order of options does not matter.
For more information, run:

```bash
python appre.py -h
```
