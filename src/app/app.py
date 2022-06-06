import json
from flask import Flask
from flask import render_template
from flask import request
import os

# Instantiate Flask
app = Flask(__name__)

# Static variables
DATABASE_FILE = "database.json"
TABLE_TEMPLATE_FILE = "table.html"

# Start with a fresh database
if os.path.exists(DATABASE_FILE):
    app.logger.debug("Removing initial %s database file upon startup." % DATABASE_FILE)
    os.remove(DATABASE_FILE)
app.data = { "characters": [] }

@app.route("/characters", methods=["GET"])
def get_characters():
    try:
        with open(DATABASE_FILE) as f:
            app.logger.info("Using existing %s database file." % DATABASE_FILE)
            app.data = json.load(f)
        f.close()
    except Exception as e:
        app.logger.warning("Unable to load JSON from existing %s database file." % DATABASE_FILE)
        app.logger.warning(e)
        app.logger.warning("Initializing new database.")
    return render_template(TABLE_TEMPLATE_FILE, characters=app.data)

@app.route("/characters", methods=["POST"])
def post_characters():      
    try:
        with open(DATABASE_FILE) as f:
            app.logger.info("Using existing %s database file." % DATABASE_FILE)
            app.data = json.load(f)
        f.close()
    except Exception as e:
        app.logger.warning("Unable to load JSON from existing %s database file." % DATABASE_FILE)
        app.logger.warning(e)
        app.logger.warning("Initializing new database.")

    new_data = request.get_json()
    for character in new_data["characters"]:
        app.logger.debug("Adding new character %s to database." % character['name'])
        app.data["characters"].append(character)

    with open(DATABASE_FILE, 'w') as f:
        app.logger.debug("Writing updated to data to %s database file." % DATABASE_FILE)
        json.dump(app.data, f)
    f.close()
    return ""
