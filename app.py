import os
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///staff.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# --- Model ---

class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'role': self.role,
            'department': self.department
        }


# --- Seed Data ---

def seed_data():
    if Staff.query.count() == 0:
        sample = [
            Staff(name="Alice Johnson",   role="Software Engineer",   department="Technology"),
            Staff(name="Bob Smith",        role="Project Manager",     department="Operations"),
            Staff(name="Carol White",      role="UX Designer",         department="Product"),
            Staff(name="David Brown",      role="Data Analyst",        department="Analytics"),
            Staff(name="Emma Davis",       role="HR Manager",          department="Human Resources"),
            Staff(name="Frank Wilson",     role="DevOps Engineer",     department="Technology"),
            Staff(name="Grace Miller",     role="Marketing Lead",      department="Marketing"),
            Staff(name="Henry Taylor",     role="Finance Officer",     department="Finance"),
            Staff(name="Isla Anderson",    role="Product Manager",     department="Product"),
            Staff(name="Jack Thomas",      role="Support Specialist",  department="Customer Support"),
        ]
        db.session.add_all(sample)
        db.session.commit()
        print("Sample data loaded.")


# --- Front-end Route ---

@app.route('/')
def index():
    # Pass the API base URL to the template.
    # In Codespaces, set the CODESPACE_APP_URL environment variable to your
    # forwarded port URL, e.g.:
    #   export CODESPACE_APP_URL="https://xxxx-5000.app.github.dev"
    # Locally this is blank and relative URLs are used automatically.
    api_base = os.environ.get('CODESPACE_APP_URL', '').rstrip('/')
    return render_template('index.html', api_base=api_base)


# --- REST API ---

@app.route('/api/staff', methods=['GET'])
def get_staff():
    """Return all staff members."""
    staff = Staff.query.order_by(Staff.name).all()
    return jsonify([s.to_dict() for s in staff])


@app.route('/api/staff', methods=['POST'])
def add_staff():
    """Add a new staff member."""
    data = request.get_json()
    if not data or not all(k in data for k in ('name', 'role', 'department')):
        return jsonify({'error': 'name, role, and department are required.'}), 400

    member = Staff(
        name=data['name'].strip(),
        role=data['role'].strip(),
        department=data['department'].strip()
    )
    db.session.add(member)
    db.session.commit()
    return jsonify(member.to_dict()), 201


@app.route('/api/staff/<int:staff_id>', methods=['PUT'])
def update_staff(staff_id):
    """Update an existing staff member."""
    member = db.session.get(Staff, staff_id)
    if member is None:
        return jsonify({'error': 'Staff member not found.'}), 404

    data = request.get_json()
    member.name = data.get('name', member.name).strip()
    member.role = data.get('role', member.role).strip()
    member.department = data.get('department', member.department).strip()
    db.session.commit()
    return jsonify(member.to_dict())


@app.route('/api/staff/<int:staff_id>', methods=['DELETE'])
def delete_staff(staff_id):
    """Delete a staff member."""
    member = db.session.get(Staff, staff_id)
    if member is None:
        return jsonify({'error': 'Staff member not found.'}), 404

    db.session.delete(member)
    db.session.commit()
    return jsonify({'message': f'{member.name} deleted successfully.'})


# --- Run ---

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        seed_data()
    app.run(debug=True)
