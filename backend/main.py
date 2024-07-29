# CRUD: Create Read Update Delete

# create:
# - first_name
# - last_name
# - email

from flask import request, jsonify
from config import app, db
from models import Contact

# Decorator
@app.route("/contacts", methods = ["GET"])
def get_contacts():
    contacts = Contact.query.all()
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    
    return jsonify({"contacts": json_contacts})

if __name__ == "__main__":
    
    # Get the context and create the database
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)
    
    
    
    