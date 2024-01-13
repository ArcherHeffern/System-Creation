# TODO
This Lesson is a heavy Work In Progress
* Terminal, Shell, Command Line, Bash
* SSH
* Services
* Executables vs Builtins (Explain a shell beforehand?)
* Improve the exmplaination of directories and moving around in terminal

# Lesson Plans
1. What is the terminal
2. What is shell (program) and its derivatives
3. How to use terminal commands
4. How to learn how to use terminal commands
5. How to install more terminal commands

# Prereq
Windows users MUST have installed and been able to run WSL (Ubuntu machine) prior to this lesson  
Mac users MUST have installed [homebrew](https://brew.sh/) prior to this lesson  

# Command Line: Terminal User Interface and Shell
We usually use a graphical user interface to interact with a computer.  

The command line is a text based to interact with the computer.   

It has a lot more powerful programs avaliable because making GUI's is hard and not fun  

This is a critical tool as a developer due to the powerful programs avaliable and being able to manage a computer on a more fine grained level.  

Proficiency in terminal is one of the major skills is expect from my PMs / Tech Leads. Aside from being able to more effectively debug other engineers computers, Tamid projects frequently work on remote machines, which is generally entirely terminal based.  

*Show LINUX Commands Image so students can get a feel for what sort of tools are avalible: Note this list is nowhere near exhaustive*  

Since one of the big uses of the command line is to manage your operating system, we will also learn about about operating systems after this

A quick distinction:
The terminal is a text based UI to interact with the computer.   
The shell is the actual program (Controller) executing the commands and doing the heavy lifting  

Honestly I don't really care about the distinction, but just know there are 2 terms. Also the shell is the actual thing we care about.  

There are also many types of shells and terminals  

## A big picture view
* Operating systems
* Shells

Operating Systems: Linux (Debian, Ubuntu, Red Hat, Fedora, Arch), MacOS, Windows
Shells: sh, csh, bash, zsh, fish, powershell

We pretty much only care about linux (Pick your poison) and `sh` derived shells such as `bash` and more recently `zsh`

## Getting Started
If you are on mac, open the `terminal` program  
If you are on windows, open up `wsl`  

__4 Basic Things I'd like Everyone to Know:__
1. How to run terminal commands
2. How to learn how to use terminal commands
3. How to install more terminal commands
4. Finding more terminal commands to install
5. Basic commands

1. Run `ls` in your terminal. This should output all the files and directories in your current working directory. 

2. Lets now see the documentation, run `man ls`. Also since `man` is a command, run `man man` to see its documentation
* Run `ls -l`

3. While this command is stable and ships with every machine to exist, its kinda boring and outdated. Lets install a newer version from online! For this we use a command line package manager! Run `brew install exa` or `apt install exa`. If you get any errors, read them.
* Read the documentation
* Run `exa` and then `exa -l`

4. View the package manager website, look at what other people are using, etc

## The Essentials
### Directory and File Management
 * cd: Move around: This is technically a shell builtin - not a command - Don't worry about the difference. Just know reading the documentation is a little different, as stated in the documentation section
 * ls: List files
 * pwd: Print working directory
 * mv: Move a file or directory
 * cp: Copy
 * mkdir: Make directory
 * touch: Create file
 * cat: Write out contents of a file to stdout
 * nano: Terminal text editor
    * vim: Advanced Terminal text editor for nerds (Install with package manager)
    * emacs: Advanced Terminal text editor for nerds (Install with package manager)

### Remote Machines
ssh: Securely login to a computer over the network
scp: Securely copy a file or directory to a computer over network 

*Practice ssh and scp with your instructors remote machine*

## man 
1. How to read the man pages
2. How to follow man pages
3. Man also give info about other things

## Remote Machines
`ssh`  
`scp`  

# Next Steps
Shells are full on programming languages, I would not recommend learning them unless you actually need to. They are overcomplicated and full of sharp edges everywhere.  

I would highly recommend reading the documentation and command discovery section below  

Since man is a program, it also has a manpage. Run `man man` and read it top to bottom, left to right. Afterwards, check out the commands it references at the bottom. If you read man correctly, you should know how to also specify the section number. 

Skim the `bash` or whichever shell you are using's man page (`man bash`). 

The best way to learn terminal is by using it as much as possible. Personally I switched to Ubuntu for this reason, but you don't need to be such a nerd. 

Some nice things to know are:
* The file hierarchy (`man hier`)
* Services

# Spelling Out What I Taught Earlier and Additional Information 
## Spelling out
### Running Commands With Parameters
Commands typically can be run with multiple behaviors. For example, the `head` command typically prints the first 10 lines of a file. However, you can run `head -n5` for it to instead print out 5. 

There are typically 5 forms of parameters you will see: 
1. command --something
2. command --something=value
3. command -s
4. command -sValue
5. command subcommand

Using multiple parameters is usually fine, make sure to read the docs for conflicts

According to the [GNU standards](https://www.gnu.org/prep/standards/html_node/Command_002dLine-Interfaces.html), every program should have these flags: --help and --version

### Documentation
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
* man is also used for other types of docuemntation (programming languages such as perl and C), general operating system things, etc

### Installing More Commands
Just like how programming languages have package managers, so do computers. You will have to search which one your operating system uses.  

*Note: MacOS does not include a package manager by default, for this you should install [Homebrew](https://brew.sh/). Follow the instructions on the site.*  

You can also install programs online from websites, especially github. This process will be a bit more complicated as you will have to install the program in the correct place and make it "discoverable".

### Command Discovery
* Go to your package manager website
* Find interesting projects on github
* See what your friends are doing
* man pages are (usually) located at /usr/share/man/ which means you can find docuementation topics there
* system commands are located at /bin, /sbin, /usr/bin, and /usr/sbin so you can find commands there as well

## Additional Features
### Making Programs Discoverable: PATH Variable
This is a problem many people run into, and is suprisingly difficult to find the solution for due to lack of resources online. 

This is usually faced when you install software not using a package manager.   

All the programs you run are on your computer in some directory, and to run a program, you usually have to specify its location. So how come we have been able to run commands so far without doing so?  

Bash is a programming language in addition to an interface with the operating system, and just like most programming languages, there are variables.  

Bash has the PATH variable, a very official variable that states what file paths to check for commands.  

To make your command discoverable, you must update the PATH variable  

Personally edit the .bashrc (Is run everytime a new terminal is made by bash) with
```bash
PATH=$PATH:/new/path
```

Then to reload run `source ~/.bashrc`

### Dotfiles
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

# Homework 
<!-- TODO -->

# Additional Material
[The art of command line](https://github.com/jlevy/the-art-of-command-line#readme)  
[Learn Enough Command Line Tutorial](https://www.learnenough.com/command-line-tutorial)  
[Xmind Linux Commands Guide](https://xmind.app/m/WwtB/)  