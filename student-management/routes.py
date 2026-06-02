from flask import render_template, request, jsonify, redirect
from app import app, db
from models import Student

# HOME PAGE

@app.route('/')
def home():

    students = Student.query.all()

    return render_template('students.html', students=students)


# =========================
# POST METHOD
# Add Student
# =========================

@app.route('/add_student', methods=['POST'])
def add_student():

    name = request.form['name']
    email = request.form['email']
    course = request.form['course']

    new_student = Student(
        name=name,
        email=email,
        course=course
    )

    db.session.add(new_student)

    db.session.commit()

    return redirect('/')


# =========================
# GET METHOD
# Get All Students API
# =========================

@app.route('/api/students', methods=['GET'])
def get_students():

    students = Student.query.all()

    return jsonify([student.to_dict() for student in students])


# =========================
# GET METHOD
# Get Single Student
# =========================

@app.route('/api/students/<int:id>', methods=['GET'])
def get_student(id):

    student = Student.query.get_or_404(id)

    return jsonify(student.to_dict())


# =========================
# PUT METHOD
# Update Student
# =========================

@app.route('/api/students/<int:id>', methods=['PUT'])
def update_student(id):

    student = Student.query.get_or_404(id)

    data = request.get_json()

    student.name = data.get('name', student.name)
    student.email = data.get('email', student.email)
    student.course = data.get('course', student.course)

    db.session.commit()

    return {
        "message": "Student updated successfully",
        "student": {
            "id": student.id,
            "name": student.name,
            "email": student.email,
            "course": student.course
        }
    }, 200


# =========================
# DELETE METHOD
# Delete Student
# =========================

@app.route('/api/students/<int:id>', methods=['DELETE'])
def delete_student(id):

    student = Student.query.get_or_404(id)

    db.session.delete(student)

    db.session.commit()

    return jsonify({
        "message": "Student Deleted Successfully"
    })