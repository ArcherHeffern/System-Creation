sql_commands=$(cat <<EOF
Create table If Not Exists Employees (id int, name varchar(20));
Create table If Not Exists EmployeeUNI (id int, unique_id int);
delete from Employees;
insert into Employees (id, name) values ('1', 'Alice');
insert into Employees (id, name) values ('7', 'Bob');
insert into Employees (id, name) values ('11', 'Meir');
insert into Employees (id, name) values ('90', 'Winston');
insert into Employees (id, name) values ('3', 'Jonathan');
delete from EmployeeUNI;
insert into EmployeeUNI (id, unique_id) values ('3', '1');
insert into EmployeeUNI (id, unique_id) values ('11', '2');
insert into EmployeeUNI (id, unique_id) values ('90', '3');
EOF
)
dbname="LC"


if [ -e $dbname ]; then
    read -p "Warning, $dbname exists, are you sure you want to override it?" out
    if [ $out != "n" ]; then
        exit 1
    fi
fi

echo "$sql_commands" | sqlite3 $dbname