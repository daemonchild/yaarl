# [INSERT HEADER]

#   app.py
#   - Main Flask App Functions

# ---- Import Libraries ---- 

from flask import Flask, make_response, jsonify, request

# Import yaarl libraries
#import api
#import config
#import database
#from flask_sqlalchemy import SQLAlchemy

# ---- GLOBAL Variables ---- 

__appname = 'yaarl-api'
__appver  = '0.1'

# ---- Flask App Code ----

app = Flask(__name__)

# ---- Setup Database ---- 

#app.config ["SQLALCHEMY_DATABASE_URI"] = f"mysql://{config.db_user}:{config.db_pass}@{config.db_server}/{config.db_database}"

# ---- Global App Functions ---- 

@app.errorhandler(404)
def this_404(error):
    return json_response(tag="error", value="not found", status=404)

@app.errorhandler(503)
def this_503(error):
    return json_response(tag="error", value="database unavailable", status=503)

@app.errorhandler(500)
def this_500(error):
    return json_response(tag="error", value="server error", status=500)
    


# ---- Add API Routes - Use Method as Verb (Get, Delete etc) ----

# -- API Documentation --
#app.add_url_rule(rule="/api/logbook/schema", view_func=api.logbook_schema_get, methods=["GET"])
#app.add_url_rule(rule="/api/callsigns/schema", view_func=api.callsigns_schema_get, methods=["GET"])
#app.add_url_rule(rule="/api/userinfo/schema", view_func=api.userinfo_schema_get, methods=["GET"])

# -- User Info --
#app.add_url_rule(rule="/api/userinfo", view_func=api.userinfo_get, methods=["GET"])

# -- Lookbook API --
#app.add_url_rule(rule="/api/logbook/entry", view_func=api.logbook_entry_get, methods=["GET"])         
#app.add_url_rule(rule="/api/logbook/entry", view_func=api.logbook_entry_add, methods=["POST"])
#app.add_url_rule("/api/logbook/entry", view_func=api.logbook_entry_delete, methods=["DELETE"])
#app.add_url_rule("/api/logbook/entry", view_func=api.logbook_entry_edit, methods=["PUT"])


# -- Callsign API --

#app.add_url_rule(rule="/api/callsigns/entry", view_func=api.callsigns_entry_get, methods=["GET"])
#app.add_url_rule(rule="/api/callsigns/entry", view_func=api.callsigns_entry_post, methods=["POST"])

#app.add_url_rule(rule="/api/callsigns/lookup/qrz/<callsign>", view_func=api.callsign_lookup_qrz, methods=["GET"])
#app.add_url_rule(rule="/api/callsigns/country/<callsign>", view_func=api.prefix_lookup, methods=["GET"])

# -- Util API --

#app.add_url_rule(rule="/api/util/band", view_func=api.getBandFromFreq, methods=["GET"])


# ---- Main Application Loop ----
if __name__ == '__main__':

    #database.db.init_app(app=app)
    app.run(debug=True, host='localhost', port=7301)