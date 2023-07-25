import re
import argparse


def read_file(input_file):
    try:
        with open(input_file, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return None
    except Exception as e:
        print(f"Error while reading the file: {e}")
        return None


def find_largest_substrings(lines):
    substrings = []
    for line_number, line in enumerate(lines):
        alphanumeric_subs = re.findall(r'\b\w{5}\b', line)
        substrings.extend([(line_number, line.find(sub), sub) for sub in alphanumeric_subs])
    substrings.sort(key=lambda x: x[2], reverse=True)
    return substrings[:4]


def compute_distance(point1, point2):
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5


def compute_perimeter(points):
    if len(points) < 2:
        return 0

    perimeter = 0
    for i in range(len(points)):
        perimeter += compute_distance(points[i], points[(i + 1) % len(points)])
    return perimeter


def compute_area(points):
    if len(points) < 3:
        return 0

    area = 0
    for i in range(len(points)):
        area += points[i][0] * points[(i + 1) % len(points)][1] - points[i][1] * points[(i + 1) % len(points)][0]
    return abs(area) / 2


def replace_locations_with_underscore(lines, locations):
    output_lines = lines.copy()
    for line_number, start_index, _ in locations:
        output_lines[line_number] = output_lines[line_number][:start_index] + '_____' + output_lines[line_number][
                                                                                        start_index + 5:]
    return output_lines


def write_output_file(output_file, lines):
    try:
        with open(output_file, 'w') as f:
            f.writelines(lines)
    except Exception as e:
        print(f"Error while writing to the output file: {e}")


def main():
    parser = argparse.ArgumentParser(description='Find largest non-overlapping substrings in a text file.')
    parser.add_argument('input_file', type=str, help='Path to the input text file')
    parser.add_argument('output_file', type=str, help='Path to the output text file')
    args = parser.parse_args()

    lines = read_file(args.input_file)
    if lines is None:
        return

    largest_substrings = find_largest_substrings(lines)
    points = [(start_index, line_number) for line_number, start_index, _ in largest_substrings]
    # Corrected the points for the x-y plane
    points = [(x, y) for y, x in points]

    perimeter = compute_perimeter(points)
    area = compute_area(points)

    print("Area of the quadrilateral:", area)
    print("Perimeter of the quadrilateral:", perimeter)

    output_lines = replace_locations_with_underscore(lines, largest_substrings)
    write_output_file(args.output_file, output_lines)


if __name__ == "__main__":
    main()
