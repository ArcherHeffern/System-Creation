# Understanding Large Codebases
__You will not, and should not understand everything__
* So many abstractions
* So much code
You can't just "read the code"  

So what to do? 
1. Talk with people familiar with the codebase
2. Read documentation. Look for 'README' files, etc
2. Run tests on parts or the whole codebase __with a debugger__. In doing so, try to understand the greater system (see the Carmack video for more on this)

# Advanced Debugging
All of what we learned about performing research is applicable here. The aspect of debugging we are focusing on here is in code debugging

## Logging
* keep logs of important events, when they happen, and other data that could be useful to diagnose issue
* Could be print statements, or logs written to a file with metadata such as time of execution or even more, its up to you.

* Looking for application logs is incredibly important for debugging production issues

## Debuggers
A life saver. Learn how to use them.

## Testing
There are many types of tests. I would suggest only creating what you think you need.

1. Unit tests
2. Integration tests
3. End to end tests
...and more! (I wouldn't stress about this)

# Monitoring Your System
This is advanced and not really something you will want in your personal projects.
It is good to be aware of this however.

Problem: How is our business applications performing? Do we need to fix something?
Solution: A Monitoring Service. The service will recieve logs and performance data from our main application, and will notify us (sms, email, etc) if our application is not performing well. 

# TLDR
1. You should not try to understand an entire codebase when joining a team
2. Use your best judgement for when to use these tools 

# Homework
1. Watch [https://youtu.be/tzr7hRXcwkw?si=0QH7WTWNUdgp0LDO](this) video where John Carmack goes into his tooling and general process. 
2. Clone [TODO](this) respository and do X (exercises in debugging and understanding large codebases)


# Supplementary Material
https://neetcode.io/courses/system-design-for-beginners/1 Watch: 6:20 for how to monitor your system

A very basic logging example
```python
# --- logger.py --- # 
class Logger:
    def __init__(self, active: bool, out_path: str):
        self.active = active
        self.out_path = out_path

    def __log(self, level: str, msg: str):
        if self.active:
            with open(self.out_path, "a") as f:
                f.write("[%s] msg".format(level))
    
    def log(msg: str):
        self.__log("Log", msg)

    def error(msg: str):
        self.__log("Error", msg)

# --- index.py --- # 
from logger import Logger
logger = Logger(True, "logs.txt")
def main():
    ...
    try:
        risky_function()
        logger.log("Risky function passed")
    except:
        logger.error("Risky function failed")
    ...

```