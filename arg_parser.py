import argparse


class ArgumentParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument(
            "src", type=str, help="Pick a video to convert to a PDF."
        )
        self.parser.add_argument(
            "-i",
            "--interval",
            type=float,
            default=1.0,
            help="Allow the script to identify new frames per [-i] seconds.",
        )
        self.parser.add_argument(
            "-o",
            "--output",
            type=str,
            default="new_folder",
            help="Choose directory for where to store your files.",
        )

    def run(self, args):
        argsList = self.parser.parse_args(args)
        return argsList
