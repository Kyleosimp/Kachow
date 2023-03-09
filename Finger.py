import re
import pathlib

def read_file_as_string(file_name):
    with open(file_name, 'r') as file:
        return file.read()

def main():
    # replace the file path with your own
    data = read_file_as_string("src/zincFinger.txt")
    # header regex
    header_pattern = re.compile(".+zinc finger.+")
    # body regex
    # replace the regex with your own found on lines 21 and 25 in the brackets
    body_pattern = re.compile("[FSYCWLPHQRIMTNKVADEG\n]+C[FSYCWLPHQRIMTNKVADEG\n]{2}C[FSYCWLPHQRIMTNKVADEG\n]{17}C[FSYCWLPHQRIMTNKVADEG\n]{2}C[FSYCWLPHQRIMTNKVADEG\n]+")
    # zinc finger regex
    # replace the regex with your own found on lines 21 and 25 in the brackets
    zinc_pattern = re.compile("C[FSYCWLPHQRIMTNKVADEG\n]{2}C[FSYCWLPHQRIMTNKVADEG\n]{17}C[FSYCWLPHQRIMTNKVADEG\n]{2}C")

    # find and print your outputs with proper formatting using a for while loop
    for header_matcher in header_pattern.finditer(data):
        for zinc_matcher in zinc_pattern.finditer(data):
            if zinc_matcher.start() < header_matcher.end():
                continue
            body_matcher = body_pattern.search(data, header_matcher.end())
            if not body_matcher or zinc_matcher.start() > body_matcher.end():
                continue

            # print statements
            print(f"{header_matcher.group()}\n")
            print(f"Contains the zinc finger site: {zinc_matcher.group()}\n")
            start, end = body_matcher.start() + body_matcher.group().index(zinc_matcher.group()), body_matcher.start() + body_matcher.group().index(zinc_matcher.group()) + len(zinc_matcher.group())
            print(f"at locations: {start} {end}\n")

            # split the body_matcher.group() into an array of strings
            body_array = body_matcher.group().split("\n")

            # find the new index position of the zinc_matcher.group() in the body_array
            new_index_position = next(i for i, line in enumerate(body_array) if zinc_matcher.group() in line)

            # find the new index length of the zinc_matcher.group() in the body_array
            new_index_length = len(zinc_matcher.group())

            # print the body_matcher.group() with a line of spaces between each line, stop at the zinc_matcher.group()
            print("\n\n".join(body_array[:new_index_position]) + "\n")

            # continue printing the body_matcher.group() with a line of spaces between each line, start at the zinc_matcher.group()
            for i, line in enumerate(body_array[new_index_position:], start=new_index_position):
                print(line)
                if zinc_matcher.group() in line:
                    print("*" * new_index_length)
                print()
