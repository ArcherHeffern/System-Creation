#!/usr/bin/python3

from gzip import compress, decompress
from random import randint
from sys import argv, stderr
from os import fork, wait
from pathlib import Path
from random import randint

# Parallel processing of compression
# For performance improvements
# Processes many files using 1 process per file 

PROG_NAME = "compression"
VERSION = "0.1.0"
EXT_ERR_INVALID_PROC_NUMBER = 1
EXT_ERR_UNKNOWN_SYMBOL = 2
EXT_ERR_NO_FILES = 3

silent = True
def log(msg: str):
    if not silent:
        print(msg)


def main():
    # Argument parsing
    global silent
    _async = False
    compress = True
    dry_run = False
    num_processes = 1
    files = []
    for arg in argv[1:]:
        match arg:
            case '-h'|'--help':
                print_help()
                exit(0)
            case '-v'|'--version':
                print(f"{PROG_NAME} version {VERSION}")
                exit(0)
            case '-a'|'--async':
                _async = True
            case '--dry-run':
                dry_run = True
            case '-V'|'--verbose':
                silent = False
            case '-d'|'--decompress':
                compress = False
            case _:
                if arg.startswith("-n"):
                    try:
                        num_processes = int(arg[2:])
                    except:
                        print(f"Argument -n passed invalid value [{argv}]", file=stderr)
                        exit(EXT_ERR_INVALID_PROC_NUMBER)
                    if num_processes > 10:
                        print("Too many processes!", file=stderr)
                        exit(EXT_ERR_INVALID_PROC_NUMBER)
                    elif num_processes <= 0:
                        print("Must use more 1 or more processes", file=stderr)
                        exit(EXT_ERR_INVALID_PROC_NUMBER)
                elif Path(arg).is_file():
                    files.append(arg)
                else:
                    print("Error: Unknown symbol [{files}]", file=stderr)
                    exit(EXT_ERR_UNKNOWN_SYMBOL)
    if len(files) == 0:
        print_help()
        exit(EXT_ERR_NO_FILES)

    # Parallel processing
    buckets = []
    for _ in range(num_processes):
        buckets.append([])
    # Randomly distribute file among all buckets (Don't actually do this!)
    for file in files:
        buckets[randint(0, num_processes - 1)].append(file)
    log(buckets)
    if not dry_run:
        for bucket in buckets:
            if fork() == 0:
                for file in bucket:
                    process_file(file, compress)
                exit(0)
    
    if not _async:
        try:
            wait()
        except:
            ...
        log("Completed processing")


def print_help():
    """-v|--version and -h|--help are so conventional they will most likely not be mentioned""" 
    print("Usage: compression [-asd] [-nNUMBER] files ...")
    print("Description: Compresses each file using gzip, adds .gz extension to each file")
    print("-a|--async: Runs program asynchronously")
    print("-V|--verbose: Runs program silently")
    print("--dry-run: Simulates running the program without making any changes. Usually run with the --verbose option")
    print("-d|--decompress: Decompresses instead of compresses")
    print("-n: Number of processes to use. Default 1")


def process_file(filename: str, to_compress: bool):
    """Imagine this is a long running task"""
    if to_compress:
        with open(filename, 'rb') as in_file:
            in_data = in_file.read()
            out_data = compress(in_data)
        with open(filename + '.gz', 'wb') as out_file:
            out_file.write(out_data)
    else:
        with open(filename, 'rb') as in_file:
            in_data = in_file.read()
            out_data = decompress(in_data)
            out_data = out_data.decode()
        with open(filename.removesuffix(".gz") + ".out", 'w', encoding='utf-8') as out_file:
            out_file.write(out_data)
    log(f"{filename} finished processing")

    
    

if __name__ == "__main__":
    main()