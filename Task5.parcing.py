import sys
import re
import numpy as np

def parse_file_with_pattern(pattern, file_path):
    if not isinstance(pattern, str) or not isinstance(file_path, str):
        raise ValueError("Both pattern and file_path must be strings")

    pattern_mapping = {'%s': '(.+)', '%d': '([-+]?\d+)', '%f': '([+-]?\d*\.-?\d*[eE]?[+-]?\d*?)'}

    for key, value in pattern_mapping.items():
        pattern = pattern.replace(key, value)

    compiled_pattern = re.compile(pattern)

    data = []

    with open(file_path, 'r') as file:
        for line in file:
            match_ = compiled_pattern.match(line)
            if match_:
                data.append(match_.groups())

    data_array = np.array(data).T.tolist()

    return data_array

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <file_path> <pattern>")
        sys.exit(1)

    file_path = sys.argv[1]
    pattern = sys.argv[2]
    data = parse_file_with_pattern(pattern, file_path)
    for i in data:
        print(i)