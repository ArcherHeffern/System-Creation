sql_commands=$(cat <<EOF
Create table If Not Exists User (id INT, name VARCHAR(20));
Create table If Not Exists Account (id INT, user_id INT, balance INT);
delete from User;
INSERT INTO User VALUES (0, 'Timmy');
INSERT INTO User VALUES (1, 'Sarah');
INSERT INTO User VALUES (2, 'Mancy');
delete from Account;
INSERT INTO Account VALUES (0, 0, 500);
INSERT INTO Account VALUES (1, 0, -100);
INSERT INTO Account VALUES (2, 1, 300);
EOF
)
dbname="LC"


if [ -e $dbname ]; then
    read -p "Warning, $dbname exists, are you sure you want to override it (y/n)? " out
    if [ $out != "y" ]; then
        echo "Exiting"
        exit 1
    fi
    rm $dbname
fi
echo "$sql_commands" | sqlite3 $dbname
echo "run \`sqlite3 ${dbname}\` to interact with database"