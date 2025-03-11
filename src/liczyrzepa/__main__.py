import argparse
from chart_creator import ChartCreator
from gui import GUI
from spreadsheet_saver import SpreadsheetSaver
from price_history import PriceHistory


def main():
    parser = construct_argument_parser()
    args = parser.parse_args()


def construct_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--chart",
        help="Show an interactive chart of the price history",
        action="store_true",
    )
    parser.add_argument(
        "-i", "--image", help="Save a chart of the price history as an image"
    )
    parser.add_argument(
        "-g",
        "--gui",
        help="Opens up GUI. Doesn't require any additional arguments",
        action="store_true",
    )
    parser.add_argument("-n", "--name", help="Name of the monitored value")
    parser.add_argument(
        "-r",
        "--read",
        help="Read the price history from a json file. If specified, overrides --name, --unit, --url and --xpath",
    )
    parser.add_argument(
        "-s",
        "--spreadsheet",
        help="Save the price history as a spreadsheet",
    )
    parser.add_argument("--url", help="The URL of a website you want to monitor")
    parser.add_argument("--unit", help="The unit of a measured value (e.g. $)")
    parser.add_argument(
        "-v",
        "--value",
        help="""
            Prints a current value of an element specified with --xpath found on a website specified with --url. If --write location was specified, this value will be appended to the price history
            """,
        action="store_true",
    )
    parser.add_argument(
        "-w", "--write", help="Write the price history as json to a specified location"
    )
    parser.add_argument(
        "-x", "--xpath", help="The XPath leading to an element you want to monitor"
    )
    return parser


if __name__ == "__main__":
    main()
