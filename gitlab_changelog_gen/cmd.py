import argparse

from gitlab_changelog_gen.config import Config
from gitlab_changelog_gen.generator import ChangeLogGenerator


def init_args():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("init", help="Init the config file in './chg-gen.config'")

    parser_output = subparsers.add_parser("output", help = "Output the changelog file")
    parser_output.add_argument("file", nargs='?', default="./CHANGELOG.md", help="The file to output the changelog")
    return parser


def main():
    parser = init_args()
    args = parser.parse_args()
    if args.command == 'init':
        cfg = Config.from_prompt()
        cfg.save()
    elif args.command == 'output':
        cfg = Config.load()
        gen = ChangeLogGenerator.from_config(cfg, output=args.file)
        gen.generate()
    else:
        parser.print_help()
