from argparse import ArgumentParser

from . import mapping

def main() -> None:
    parser = ArgumentParser( prog="igbloks", )

    parser.add_argument("-d", "--directory", help="Directory of the responses to map.", required=True)
    parser.add_argument("-n", "--namer", help="The bkid of the files you want to name the fields.", required=True)

    arguments = vars(parser.parse_args())
    mapping.schema_for_appid(arguments["d"])

if __name__ == "__main__":
    main()