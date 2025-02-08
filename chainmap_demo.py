import os
import argparse
from collections import ChainMap


def main():
    app_defaults = {'username': 'admin', 'password': 'adminpass'}
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username')
    parser.add_argument('-p', '--password')
    args = parser.parse_args()

    cmd_args = {key: val for (key, val) in vars(args).items() if val}
    chain = ChainMap(cmd_args, os.environ, app_defaults)
    print(chain['username'])
    return None


if __name__ == '__main__':
    main()
    os.environ['username'] = 'test'
    main()
