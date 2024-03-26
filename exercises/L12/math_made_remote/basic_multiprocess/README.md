Basic multiprocess solution to using others programs. In this example we incorperate the connection logic straight into the querying logic. 

This is not optimal, and we can do better by creating a library to separate concerns

While we use forking and pipes in this example, it can very well be used with any IPC (interprocess communication) and if we use sockets, can be done between computers. 