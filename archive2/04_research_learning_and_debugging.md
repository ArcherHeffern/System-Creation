# The Heart of Programming

If you find that you’re spending almost all your time on theory, start turning some attention to practical things; it will improve your theories. If you find that you’re spending almost all your time on practice, start turning some attention to theoretical things; it will improve your practice. - Donald Knuth

__The heart of programming is knowing theory, and how to turn it into code__  
Improving at theory requires knowing know to research  
Improving at code translation process requires practice, knowing how to use tools, debug, and a general knowledge of how to figure things out  

Theory is all encompassing, its not just algorithms, but also architecture patterns, business related, and more  
* Algorithms: Diffing  => Used in Git and React
* Architecture patterns: MVC (Model View Controller) => User interfaces
* Business: Lean / Agile (Used as baseline for creating CI/CD pipelines)
* And more: HTTP Protocol (Specification) => HTTP Server

So, how do we learn theory and figure things out?

1. Reading
2. Asking Questions

## Reading
For basic topics, resources such as *ChatGPT, Youtube, Random Articles* are helpful, however, they are less comprehensive and will not help you once you reach more advanced material, or work at a company with in house tooling  

The best way to learn and debug advanced issues is by reading...
* Code
* Documentation
* Stackoverflow
* Github Issues
* Wikipedia
* Whitepapers / research papers
* Books

### Code
You can often find source code for projects or libraries online. Just google for it or search on github. If you are having issues with a library in your project, look at the code!  

Pro Tip: When you install packages, use libraries, etc, the code exists on your computer, so take a look at it!  

[Malloc source](https://codebrowser.dev/glibc/glibc/malloc/malloc.c.html)  
[Linux OS source](https://github.com/torvalds/linux)

If the codebase is complex, use a debugger

### Documentation
Always find the documentation of the medium you are using  

bash / zsh: The command *man* (manual) provides the documentation of a command. Since its a command, it also has documentation
```bash
man man
```
Apropos lets you search descriptions for a keyword, this is good if you don't remember the name of a command
```bash
apropos <keyword>
```

If you want to learn about the internet, RFC (request for comment) are specifications for how all the internet works.   
* [IP Protocol](https://datatracker.ietf.org/doc/html/rfc791)

### Whitepapers / Research Papers
Whitepapers are opinionated research papers.  
You can find research papers and whitepapers on google scholar
* [Internet Whitepaper](https://web.stanford.edu/class/msande91si/www-spr04/readings/week1/InternetWhitepaper.htm)
* [Resiliant Overlay Networks](https://dl.acm.org/doi/abs/10.1145/502034.502048?casa_token=6IdQD6H1RKkAAAAA:N6-bkSvra14Fiq0WGZDyL5JBdtMD0rqyc9NMW3dSVjMLZJmuO-13JXdOLxppFsbJUtRchHM4SijB)

### Books 
Books and Papers are amazing, use google scholar, library databases, or ask professors what they recommend 
* The art of computer programming, Donald Knuth
* TCP / IP Illustrated, Richard Stevens

## Asking Questions
* stackoverflow
* reddit
* github issues

How do we ask a good question? 

1. Title: Be specific and imagine you’re asking a question to another person
2. Body:
    * What are the details of your problem?
    * What did you try, what happened and what were you expecting?

If you are providing code, simplify it as much as possible. This may even help you figure out the issue yourself!

## General Tips
* Break things, you learn a lot from debugging. I personally have broken my Operating System 3 times and learned a lot each time.
* Write things down!
* Having a large bredth of knowledge is important, I recommend [fireship's](https://www.youtube.com/c/fireship) X in 100 second videos
* Documentation and theory are much better than tutorials
* Don't get caught up in tutorial hell
* You don't need to know everything, so don't learn everything
* Learn at least 1 programming language truly in depth
* The goal is to code, so code 
* If you are going to learn from videos, stick to the short ones - None of that, "X in 1 hour", or "learn Y in 31 hours" 

# Whats Next
* Basic Application Architecture

# Homework
Watch [how to read](https://youtu.be/nqYmmZKY4sA?si=WmU-UNg3AoG5vD2e)
<!-- TODO: Create homework questions -->
Perform research on an interesting project idea and propose a MVP 