import os
from flask import Flask, render_template, url_for
import json
import supabase
import dotenv
import logging

# We need to access the env file for api keys
dotenv_path = os.path.join(os.getcwd(), '.venv\\.env')
# Load the .env file
dotenv.load_dotenv(dotenv_path)

# Access the API key
SUPABASE_URL = os.environ.get('SUPABASE_URL')
SUPABASE_KEY = os.environ.get('SUPABASE_KEY')

print("Checking what your current credentials are:")
print("SUPABASE_URL:", SUPABASE_URL)
print("SUPABASE_KEY:", SUPABASE_KEY)

# Connect to the Supabase database
supabase_client = supabase.Client(SUPABASE_URL, SUPABASE_KEY)

# Create some random data for this projects
table_data = [
    {"name": "John", "age": 30, "country": "USA"},
    {"name": "Jane", "age": 25, "country": "Canada"},
    {"name": "Bob", "age": 40, "country": "Mexico"}
]


app = Flask(__name__)

@app.route('/')
def index():
    # Query table
    try:
        # result = supabase_client.from_('lil_old_table').select("*").execute()
        result = supabase_client.from_('lil_old_table').select('patient_id', 'created_at', 'patient_name', 'alive_status').execute()
        print(result.model_dump_json())
        database_data = result.data
        
        logging.info(f"Supabase data: {database_data}")
        print("")
        print(database_data)
        print("")
    except Exception as e:
        logging.error(f"Error querying supabase: {e}")
        
    return render_template('index.html', supabase_data=database_data, manual_table=table_data)

    # database_data = supabase_client.from_('lil_old_table').select('patient_id', 'created_at', 'patient_name', 'alive_status').execute()
    # return render_template('index.html', supabase_data=database_data, manual_table = table_data)

if __name__ == "__main__":
    app.run(debug=True)
    