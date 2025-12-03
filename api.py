from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure MySQL connection
# NOTE: Ensure your password is correct. If using XAMPP/WAMP, password usually is empty strings
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/university_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --- Database Model ---
class Course(db.Model):
    __tablename__ = 'course'
    
    subject_code = db.Column(db.Integer, primary_key=True, autoincrement=False)
    subject_name = db.Column(db.String(100), nullable=False)
    lecturer = db.Column(db.String(100), nullable=False)
    venue = db.Column(db.String(100), nullable=False)
    capacity = db.Column(db.Integer)

    def to_dict(self):
        return {
            'subject_code': self.subject_code,
            'subject_name': self.subject_name,
            'lecturer': self.lecturer,
            'venue': self.venue,
            'capacity': self.capacity
        }

# Create tables if they don't exist
with app.app_context():
    db.create_all()

# --- Routes ---

@app.route('/')
def home():
    return jsonify({"message": "Hello, API is working!"})

# Create Course
@app.route('/api/courses', methods=['POST'])
def create_course():
    try:
        if not request.is_json:
            return jsonify({"error": "Content-Type must be application/json"}), 400
        
        data = request.get_json()
        required_fields = ['subject_code', 'subject_name', 'lecturer', 'venue', 'capacity']
        
        if not data or not all(field in data for field in required_fields):
            return jsonify({"error": "Missing required fields"}), 400
            
        new_course = Course(
            subject_code=data['subject_code'],
            subject_name=data['subject_name'],
            lecturer=data['lecturer'],
            venue=data['venue'],
            capacity=data['capacity'],
        )
        db.session.add(new_course)
        db.session.commit()
        return jsonify({"message": "Course created successfully", "course": new_course.to_dict()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Get All Courses
@app.route('/api/courses', methods=['GET'])
def get_courses():
    try:
        courses = Course.query.all()
        return jsonify({"courses": [course.to_dict() for course in courses]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get Single Course
@app.route('/api/course/<int:subject_code>', methods=['GET'])
def get_course(subject_code):
    try:
        course = Course.query.get(subject_code)
        if course is None:
            return jsonify({"error": "Course not found"}), 404
        return jsonify({"course": course.to_dict()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Update Course
@app.route('/api/course/<int:subject_code>', methods=['PUT'])
def update_course(subject_code):
    try:
        if not request.is_json:
            return jsonify({"error": "Content-Type must be application/json"}), 400
            
        course = Course.query.get(subject_code)
        if course is None:
            return jsonify({"error": "Course not found"}), 404
            
        data = request.get_json()
        
        if 'subject_name' in data: course.subject_name = data['subject_name']
        if 'lecturer' in data: course.lecturer = data['lecturer']
        if 'venue' in data: course.venue = data['venue']
        if 'capacity' in data: course.capacity = data['capacity']
            
        db.session.commit()
        return jsonify({"message": "Course updated successfully", "course": course.to_dict()})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Delete Course
@app.route('/api/course/<int:subject_code>', methods=['DELETE'])
def delete_course(subject_code):
    try:
        course = Course.query.get(subject_code)
        if course is None:
            return jsonify({"error": "Course not found"}), 404
            
        db.session.delete(course)
        db.session.commit()
        return jsonify({"message": "Course deleted successfully"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# --- Entry Point ---
if __name__ == '__main__':
    # This block only runs if you execute 'python api.py' directly
    app.run(debug=True, port=5000)