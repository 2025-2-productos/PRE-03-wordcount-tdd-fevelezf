import sys

from ...wordcount import (
    count_words,
    parse_args,
    preprocess_lines,
    split_lines_into_words,
    write_word_counts,
)
from ..read_all_lines import read_all_lines


def test_parse_args():
    """
    Llamada en el prompt
    $ python -m homework data/input/ data/output/
    """

    test_args = ["homework", "data/input/", "data/output/"]
    sys.argv = test_args

    input_folder, output_folder = parse_args()

    assert input_folder == "data/input/"
    assert output_folder == "data/output/"


def test_read_all_lines():
    """Test read_all_lines function"""
    input_folder = "data/input/"
    lines = read_all_lines(input_folder)
    assert len(lines) > 0
    assert any(
        "Analytics refers to the systematic computational analysis of data " in line
        for line in lines
    )


def test_preprocess_lines():
    """Test preprocess_lines function"""
    lines = ["Hello, World! ", "Python is GREAT."]
    preprocessed = preprocess_lines(lines)
    assert preprocessed == ["hello, world!", "python is great."]


def test_split_lines_into_words():
    """Test split_lines_into_words function"""
    lines = ["hello world", "python is great"]
    words = split_lines_into_words(lines)
    assert words == ["hello", "world", "python", "is", "great"]


def test_count_words():
    """Test count_words function"""
    words = ["hello", "world", "hello", "python"]
    word_counts = count_words(words)
    assert word_counts == {"hello": 2, "world": 1, "python": 1}
