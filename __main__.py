import sys
import argparse
import game_process
import test


def _execute_game_outp_file(inp_file, outp):
    '''Here inp_file is opened file of sys.stdin, and outp is a string
       of file name or None if it is stdin.'''
    if outp is None:
        game_process.main(inp_file, sys.stdout)
    else:
        with open(outp, 'w') as fout:
            game_process.main(inp_file, fout)


def execute_game(inp, outp):
    '''Executes the process. If input is from stdin, inp is None.
       Except it is the string of the input file. The same as with outp. '''
    if inp is None:
        _execute_game_outp_file(sys.stdin, outp)
    else:
        with open(inp, 'r') as fin:
            _execute_game_outp_file(fin, outp)


def main():
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('--src', dest='inp',
                        help='Makes your input from mentioned file')
    parser.add_argument('--dst', dest='outp',
                        help='Makes output result into mentioned file')
    parser.add_argument('-t', '--test', dest='tst', action='store_true',
                        help='Executes unit tests')
    args = parser.parse_args()
    if args.tst:
        test.main()
        return
    execute_game(args.inp, args.outp)


if __name__ == '__main__':
    main()
