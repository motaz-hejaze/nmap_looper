# Please enter all connection data
# also to make this script work regardless your database schema ,
# You have to provide table name , subdomains column name , ports column name


connection_data = {
    "hostname": "localhost",
    "username": "myuser",
    "password": "mypassword",
    "database_name": "mydatabase",
    "table_name": "mytable",
    "subdomains_column_name": "mysubdomain",
    "ports_column_name": "myports",
}

nmap_command_args = []
