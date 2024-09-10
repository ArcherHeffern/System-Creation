import glob
import re
from os import system
from sys import stderr

# Install correct version
# Gunzip 
# tar
# Update makefile
# Print help text
pre = "https://github.com/raysan5/raylib/releases/download/5.0/"
options = [
"raylib-5.0_linux_amd64",
"raylib-5.0_linux_i386",
"raylib-5.0_macos",
]

ext = ".tar.gz"

for i, opt in enumerate(options):
	print("%d) %s" % (i, opt))
v = None
while v is None:
	try:
		tmp = input("> ")
		if tmp in ["q", "quit", "exit"]:
			exit(0)
		tmp = int(tmp)
		if tmp < 0 or tmp >= len(options):
			raise ValueError()
		v = tmp
	except ValueError:
		print("Invalid Option")
name = options[v]
url = pre + name + ext

system("rm -rf %s > /dev/null 2>&1" % name)
print("Downloading raylib")
system("curl -L -o %s -s %s" % (name + ext, url))

if not glob.glob(name + ext):
    print("Failed to install raylib - please install the correct version from https://github.com/raysan5/raylib/releases", file=stderr)
    exit(1)

system("gunzip %s" % name + ext)
# TODO: Check if successful
system("tar xf *.tar")
system("rm *.tar")

system("rm game > /dev/null 2>&1")

with open("makefile", "w+") as outf, open("makefile_template", "r") as inf:
    lns = inf.readlines()
    lns = [line.replace("{}", name) for line in lns]
    outf.writelines(lns)

print()
if re.search("macos", name, flags=re.I) is not None:
	print("If you are on macos run the following:")
	print("export DYLD_LIBRARY_PATH=%s/lib:$DYLD_LIBRARY_PATH" % name)
else:
	print("If you are on linux/WSL run the following")
	print("export LD_LIBRARY_PATH=%s/lib:$LD_LIBRARY_PATH" % name)
print()
print("Run `make` to compile")
print("Run ./game to execute the program")
print("If make fails, its possible you are using the wrong architecture - run uname -m to check")
