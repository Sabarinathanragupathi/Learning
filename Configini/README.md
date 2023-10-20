To use an INI file configuration in a FastAPI application, you can use a package like `configparser` to read and parse INI files and then load the configuration settings into your FastAPI application. Here's a step-by-step guide on how to do this:

1. Install the `configparser` library if you haven't already:

   ```bash
   pip install configparser
   ```

2. Create an INI configuration file (e.g., `config.ini`) with your application's settings. Here's an example:

   ```ini
   [app]
   env = prod
   auth0_domain = ingka-icow-prod.eu.auth0.com

   [database]
   db_host = localhost
   db_port = 5432
   db_name = mydatabase
   db_user = myuser
   db_password = mypassword
   ```

3. Create a Python module (e.g., `config_reader.py`) to read and parse the INI file:

   ```python
   import configparser

   class ConfigReader:
       def __init__(self, config_file_path):
           self.config = configparser.ConfigParser()
           self.config.read(config_file_path)

       def get_app_config(self):
           return self.config["app"]

       def get_database_config(self):
           return self.config["database"]
   ```

4. In your FastAPI application, create an instance of `ConfigReader` to read the INI file and access the configuration settings:

   ```python
   from fastapi import FastAPI
   from config_reader import ConfigReader

   app = FastAPI()

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

   @app.get("/")
   def read_root():
       return {
           "app_env": app_env,
           "auth0_domain": auth0_domain,
           "db_host": db_host,
           "db_port": db_port,
           "db_name": db_name,
           "db_user": db_user,
           "db_password": db_password,
       }
   ```

5. Now, when you run your FastAPI application and access the root route, it will display the configuration settings from the INI file.

   ```bash
   uvicorn your_app:app --host 0.0.0.0 --port 8000
   ```

   Access the endpoint in your browser or make a GET request to see the configuration settings.

This setup allows you to keep your configuration settings in an INI file and load them into your FastAPI application. You can access these settings wherever needed within your application.