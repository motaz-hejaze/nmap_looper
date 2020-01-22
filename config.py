# Please enter all connection data
# also to make this script work regardless your database schema ,
# You have to provide table name , subdomains column name , ports column name


connection_data = {
    "hostname": "localhost",
    "username": "motaz",
    "password": "kokowawa",
    "database_name": "nmap",
    "table_name": "subdomains",
    "subdomains_column_name": "subdomain",
    "ports_column_name": "ports",
}

nmap_command_args = []