from config_reader import ConfigReader


# Initialize the ConfigReader with the path to your config.ini file
config_reader = ConfigReader("config.ini")

# Access configuration settings
app_env = config_reader.get_app_config()["env"]
auth0_domain = config_reader.get_app_config()["auth0_domain"]

db_config = config_reader.get_database_config()
db_host = db_config["db_host"]
db_port = db_config["db_port"]
db_name = db_config["db_name"]
db_user = db_config["db_user"]
db_password = db_config["db_password"]

print({
        "app_env": app_env,
        "auth0_domain": auth0_domain,
        "db_host": db_host,
        "db_port": db_port,
        "db_name": db_name,
        "db_user": db_user,
        "db_password": db_password,
    }
)