import pytest
import os
from substring_quadrilateral import (
    read_file,
    find_largest_substrings,
    compute_area,
    compute_perimeter,
    replace_locations_with_underscore,
    write_output_file, compute_distance
)


def get_test_file_path(filename):
    return os.path.join(os.path.dirname(__file__), filename)


@pytest.fixture(scope="module")
def input_file_path():
    return get_test_file_path("test_input.txt")


@pytest.fixture(scope="module")
def output_file_path():
    return get_test_file_path("test_output.txt")


class TestSubstringQuadrilateral:

    def test_read_file(self, input_file_path):
        lines = read_file(input_file_path)
        assert len(lines) > 0
        assert all(isinstance(line, str) for line in lines)

    def test_find_largest_substrings(self, input_file_path):
        lines = read_file(input_file_path)
        substrings = find_largest_substrings(lines)
        assert len(substrings) > 0

    def test_compute_distance(self):
        assert compute_distance((0, 0), (3, 4)) == 5.0
        assert compute_distance((1, 1), (4, 5)) == 5.0

    def test_compute_perimeter(self):
        points = [(0, 0), (3, 4), (7, 8)]
        assert round(compute_perimeter(points), 2) == 21.29

    def test_compute_area(self):
        points = [(0, 0), (3, 4), (0, 8)]
        assert compute_area(points) == 12.0

    def test_replace_locations_with_underscore(self):
        lines = ['This is a test line.', 'Another test line.']
        locations = [(0, 8, 'test'), (1, 8, 'test')]
        output_lines = replace_locations_with_underscore(lines, locations)
        assert output_lines == ['This is _____t line.', 'Another _____line.']

    def test_write_output_file(self, output_file_path):
        lines = ['This is a test line.', 'Another test line.']
        write_output_file(output_file_path, lines)
        assert os.path.exists(output_file_path)
