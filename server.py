from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/generate_emails": {"origins": "*"}}, allow_headers=['Access-Control-Allow-Origin'])

# Define your routes and functions as usual

def generate_email_ids(email, first_name, last_name):
    company_domain = email.split('@')[1]
    email_ids = []
    email_ids.append(f"{first_name}.{last_name}@{company_domain}")
    email_ids.append(f"{first_name}{last_name}@{company_domain}")
    email_ids.append(f"{first_name}@{company_domain}")
    email_ids.append(f"{first_name}_{last_name}@{company_domain}")
    return email_ids

@app.route('/generate_emails', methods=['POST'])
def generate_emails():
    data = request.json
    email = data['email']
    first_name = data['first_name']
    last_name = data['last_name']
    email_ids = generate_email_ids(email, first_name, last_name)
    return jsonify({'email_ids': email_ids})

if __name__ == '__main__':
    app.run(debug=True)
