C is weaky typed. This means you can cast one type into another very easily. Sockets use this as a form of polymorphism, where you can cast between 2 structs (sockaddr_in, sockaddr_en)  

Compile the code with `make all` to compile all programs, or `make <program_name>` for a specific one. Delete all binaries with `make clean`


If you can navigate the socket documentation, you can do anything. Good luck! I would suggest starting with socket(2) and ip(7)