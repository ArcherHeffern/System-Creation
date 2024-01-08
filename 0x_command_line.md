# TODO
This Lesson is a heavy Work In Progress
* Terminal, Shell, Command Line, Bash
* SSH
* Services
* Executables vs Builtins (Explain a shell beforehand?)
* Improve the exmplaination of directories and moving around in terminal

# Prereq
Windows users should have installed WSL prior to this lesson

# Terminal User Interface
We usually use a graphical user interface to interact with a computer.  

The terminal is a text based interface to interact with the computer.  

It has a lot more powerful programs avaliable because making GUI's is hard and not fun

This is a critical tool as a developer due to the powerful programs avaliable and being able to manage a computer on a more fine grained level. 

Proficiency in terminal is one of the major skills is expect from my PMs / Tech Leads. Aside from being able to more effectively debug other engineers computers, Tamid projects frequently work on remote machines, which is generally entirely terminal based. 

*Show LINUX Commands Image so students can get a feel for what sort of tools are avalible: Note this list is nowhere near exhaustive*

## Getting Started
If you are on mac, open the `terminal` program  
If you are on windows, open up `wsl`

Run `ls` in your terminal. This should output all the files and directories in your current working directory. 

The terminal abstraction says you are at a location in the directory tree

Lets now see the documentation, run `man ls`.

## The Basics
moving around: `cd [directory|..| ]`: Moves you into a directory if 
ls, pwd, cd, mv, cp, scp, ssh, nano, mkdir, touch

Editing files with `nano` (or `vim`/`emacs` for tryhards)

## Running Commands With Parameters
Commands typically can be run with multiple behaviors. For example, the `head` command typically prints the first 10 lines of a file. However, you can run `head -n5` for it to instead print out 5. 

There are typically 5 forms of parameters you will see: 
1. command --something
2. command --something=value
3. command -s
4. command -sValue
5. command subcommand

Using multiple parameters is generally fine, of course, make sure to read the docs for conflicts

According to the [GNU standards](https://www.gnu.org/prep/standards/html_node/Command_002dLine-Interfaces.html), every program should have these flags: --help and --version

## Documentation
__Executables__
* Read official documentation with `man`, `man -k`, and `man -K`
* Search using fragments with `apropos`.

__Builtins__
* Read official documentation with `help` and `help -d`. 

You can find out whether a command is an executable, shell builtin or an alias by using `type` command.

__Other resources__
* [IEEE Utility Argument Syntax](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap12.html): Note: IEEE is the group that makes standards nowadays 
* [ExplainShell.com](ExplainShell.com) to deconstruct a shell commands 
* `curl cheat.sh/command` will give a brief cheat sheet with common examples 

__Notes__
* Some commands only show portions of their man pages, in this case, google the documentation. One case of this is the `update-alternatives` command
* Some commands don't have man pages and instead print their docuementation when invoked with the -h or --help flags (See "Running Commands With Parameters Section)

## Installing More Commands
Just like how programming languages have package managers, so do computers. You will have to search which one your operating system uses.  

*Note: MacOS does not include a package manager by default, for this you should install [Homebrew](https://brew.sh/). Follow the instructions on the site.*  

You can also install programs online from websites, especially github. This process will be a bit more complicated as you will have to install the program in the correct place and make it "discoverable".

### Making Programs Discoverable: PATH Variable
All the programs you run are on your computer in some directory, and to run a program, you usually have to specify its location. So how come we have been able to run commands so far without doing so? 

The PATH environment variable

## Dotfiles
This is a more advanced feature so just be aware of it.

Many commands look for files written in syntaxes they determine to alter their behavior.   

Examples  
Vim: is a command line text editor that looks pretty boring 
If I create a file .vimrc in my HOME directory 

~/.vimrc
```vimscript
set relativenumber
```

Then I have relative numbers on the sidebar.

These config files are generally located in /etc/, $HOME/, or $HOME/.config/ although make sure to read the docs.

# Next Steps
Bash is a full on programming language, I would not recommend learning it unless you actually need to. It's overcomplicated and full of sharp edges everywhere.  

Since man is a program, it also has a manpage. Run `man man` and read it top to bottom, left to right. Afterwards, check out the commands it references at the bottom. If you read man correctly, you should know how to also specify the section number. 

Skim the `bash` or whichever shell you are using's man page (`man bash`). 

The best way to learn terminal is by using it as much as possible. Personally I switched to Ubuntu for this reason, but you don't need to be such a nerd. 

Some nice things to know are:
* The file hierarchy (`man hier`)
* Services
* SSH
* Redirections
* SCP
* Mounting and Disk management

# Additional Material
[The art of command line](https://github.com/jlevy/the-art-of-command-line#readme)  
[Learn Enough Command Line Tutorial](https://www.learnenough.com/command-line-tutorial)  
[Xmind Linux Commands Guide](https://xmind.app/m/WwtB/)  