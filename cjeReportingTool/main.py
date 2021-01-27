import argparse
import textwrap

import cjeReportingTool.cjeReportingTool as c


def parseArgs():
    """Parse arguments."""
    parser = argparse.ArgumentParser(
        prog='cjeReportingTool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
        This Tool made for CJE(Chishiki Joho Enshu 3) class at Univ. Tsukuba, klis.
        This package converts source code comment to markdown text using split words.'''))
    parser.add_argument('path',  metavar='path', nargs=1,
                        help='Read file path')
    parser.add_argument('outpath',  metavar='outpath', nargs=1,
                        help='Export file path')
    parser.add_argument('split_str',  metavar='split_str', nargs='?', default='##',
                        help='A symbol or string that separates comments from source code')
    parser.add_argument('prefix',  metavar='prefix', nargs='?', default='>',
                        help='A Prefix to be written out')
    return parser.parse_args()


def main():
    args = parseArgs()
    c.cjeReportingTool(
       args.path[0], args.outpath[0], args.split_str, args.prefix)


if __name__ == "__main__":
    main()
