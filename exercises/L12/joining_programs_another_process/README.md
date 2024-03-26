# Set up
All the following instructions will be for a debian based linux system, although they should be similar enough for other systems. 

Install [postgresql](https://www.postgresql.org/)  

```bash
sudo apt install postgresql
```

Check if its running as a daemon/service using your init system 

```bash
systemctl status postgresql
```

Installing postgresql also gives us access to libpq, a library to interact with postgresql via IPC and its protocol.  

Compile and Run
```bash
gcc -I/usr/include/postgresql -o bank bank.c -lpq && ./bank
```

All the additional -I's and -l's are to tell the c compiler where to find libpq

# Resources
[Libpq](https://www.postgresql.org/docs/current/libpq.html)