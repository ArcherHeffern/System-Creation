# Set up
All the following instructions will be for a debian based linux system, although they should be similar enough for other systems. 

1. Install [postgresql](https://www.postgresql.org/)  

```bash
sudo apt install postgresql
```

2. Check if its running as a daemon/service using your init system 

```bash
systemctl status postgresql
```

3. Enable password authentication

get terminal access to postgres 
```bash
sudo su postgres;
psql
```
and set password to password
```
\password
```

Edit pg_hba.conf to allow for password authentication
```conf
# Database administrative login by Unix domain socket
local   all             postgres                                peer
```
to...
```conf
# Database administrative login by Unix domain socket
local   all             postgres                                md5
```

Then reload postgres with
```shell
systemctl restart postgresql
```

Installing postgresql also gives us access to libpq, a library to interact with postgresql via IPC and its protocol.  

Compile and Run
```bash
gcc -I/usr/include/postgresql -o bank bank.c -lpq && ./bank
```

All the additional -I's and -l's are to tell the c compiler where to find libpq

# Resources
[Libpq](https://www.postgresql.org/docs/current/libpq.html)

What if you don't like being given libraries since you don't know how they work? You can always make your own library (or just interface yourself although that might get hairy)! Simply find the specification for how to communicate with postgresql, found on their website and implement it. You will find this to be tedious, so maybe stick with libraries ;)
- https://www.postgresql.org/docs/current/protocol.html