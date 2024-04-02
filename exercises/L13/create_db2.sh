sql_commands=$(cat <<EOF
CREATE TABLE IF NOT EXISTS Account (account_id INT, username VARCHAR(20));
CREATE TABLE IF NOT EXISTS Product (product_id INT, name VARCHAR(20), price INT);
CREATE TABLE IF NOT EXISTS _Transaction (transaction_id INT, account_id INT, product_id INT);

INSERT INTO Account VALUES (0, "Timmy");
INSERT INTO Account VALUES (1, "Sarah");
INSERT INTO Account VALUES (2, "Bonnie");

INSERT INTO Product VALUES (0, "Tomato", 10);
INSERT INTO Product VALUES (1, "Apple", 15);
INSERT INTO Product VALUES (2, "Car", 10000);

INSERT INTO _Transaction VALUES (0, 0, 0);
INSERT INTO _Transaction VALUES (1, 0, 1);
INSERT INTO _Transaction VALUES (2, 1, 1);
INSERT INTO _Transaction VALUES (3, 1, 2);
INSERT INTO _Transaction VALUES (4, 2, 2);
EOF
)
dbname="LC2"


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