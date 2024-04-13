import glob
from sys import stderr
paths: list[str] =glob.glob("raylib-5.0*")
cleaned_paths = [path for path in paths if not path.endswith(".tar") and not path.endswith(".gz")]
if len(cleaned_paths) == 0:
    if len(paths) != 0:
        print("Raylib gzip or tar was found but no raylib. Please unzip (gunzip <directory>) and untar (tar -xf <directory>) before proceeding", file=stderr)
        exit(1)
    print("No raylib found - please install the correct version from https://github.com/raysan5/raylib/releases", file=stderr)
    exit(1)
with open("makefile", "w+") as outf, open("makefile_template", "r") as inf:
    lns = inf.readlines()
    lns = [line.replace("{}", paths[0]) for line in lns]
    outf.writelines(lns)

print("Run `export LD_LIBRARY_PATH=%s/lib:$LD_LIBRARY_PATH`\nThen run `make` to compile\nThen run the program with ./game" % paths[0])