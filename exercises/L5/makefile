
all: files files2 tamidcat

files: files.c
	gcc -o files files.c

files2: files2.c
	gcc -o files2 files2.c

tamidcat: tamidcat.c
	gcc -o tamidcat tamidcat.c

dup_uses: dup_uses.c
	gcc -o dup_uses dup_uses.c

clean:
	rm files files2 tamidcat dup_uses out.txt