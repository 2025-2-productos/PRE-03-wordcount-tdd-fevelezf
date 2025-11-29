# Ejemplo paea casos de uso
# python -m homework data/input data/output
import argparse
import sys

from homework.src._internals.read_all_lines import read_all_lines


def parse_args():

    parser = argparse.ArgumentParser(description="Count word in files.")
    parser.add_argument(
        "input", help="Path to the input folder conttaining files to process", type=str
    )
    parser.add_argument(
        "output", help="Path to the output folder to save results", type=str
    )

    parsed_args = parser.parse_args()

    return parsed_args.input, parsed_args.output


def main():
    input_folder, output_folder = parse_args()
    lines = read_all_lines(input_folder)
