
all: file_examples file_examples2 tamidcat dup_examples dup_solution pipe_examples pipe_solution signal_examples signal_solution

file_examples: file_examples.c
	gcc -o file_examples file_examples.c

file_examples2: file_examples2.c
	gcc -o file_examples2 file_examples2.c

tamidcat: file_solution.c
	gcc -o file_solution file_solution.c

dup_examples: dup_examples.c
	gcc -o dup_examples dup_examples.c

dup_solution: dup_solution.c
	gcc -o dup_solution dup_solution.c

pipe_examples: pipe_examples.c
	gcc -o pipe_examples pipe_examples.c

pipe_solution: pipe_solution.c
	gcc -o pipe_solution pipe_solution.c

signal_examples: signal_examples.c
	gcc -o signal_examples signal_examples.c

signal_solution: signal_solution.c
	gcc -o signal_solution signal_solution.c

clean:
	rm out.txt file_examples file_examples2 file_solution dup_examples dup_solution pipe_examples pipe_solution signal_examples signal_solution