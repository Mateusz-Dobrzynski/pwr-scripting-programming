import argparse

def main():
    parser = construct_argument_parser()
    args = parser.parse_args()


def construct_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", help="Directory to traverse")
    return parser


if __name__ == "__main__":
    main()
