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
while not v:
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

system("rm -rf %s" % name)

print("Downloading raylib")
system("curl -L -o %s -s %s" % (name + ext, url))

if not glob.glob(name + ext):
    print("Failed to install raylib - please install the correct version from https://github.com/raysan5/raylib/releases", file=stderr)
    exit(1)

system("gunzip %s" % name + ext)
# TODO: Check if successful
system("tar xf *.tar")
system("rm *.tar")

with open("makefile", "w+") as outf, open("makefile_template", "r") as inf:
    lns = inf.readlines()
    lns = [line.replace("{}", name) for line in lns]
    outf.writelines(lns)

print()
print("If you are on macos run the following")
print("export DYLD_LIBRARY_PATH=raylib-5.0_macos/lib:$DYLD_LIBRARY_PATH")
print("If you are on linux/WSL install the following")
print("export LD_LIBRARY_PATH=%s/lib:$LD_LIBRARY_PATH")
print()
print("Run `make` to compile")
print("Run ./game to execute the program")
