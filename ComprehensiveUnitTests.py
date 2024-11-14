import unittest

class Student:
    def __init__(self, student_id, name, age, major):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Major: {self.major}"

class StudentRegistrationSystem:
    def __init__(self):
        self.students = {}

    # CREATE
    def create_student(self, student_id, name, age, major):
        if student_id in self.students:
            print("Student with this ID already exists.")
            return False
        else:
            self.students[student_id] = Student(student_id, name, age, major)
            print("Student created successfully.")
            return True

    # READ
    def read_student(self, student_id):
        if student_id in self.students:
            print(str(self.students[student_id]) + "\n")
            return student_id
        else:
            print("Student not found.")

    def read_all_students(self):
        if not self.students:
            print("No students registered.")
            return []
        else:
            for student in self.students.values():
                print(str(student))
            return self.students.values()

    # UPDATE
    def update_student(self, student_id, name=None, age=None, major=None):
        if student_id in self.students:
            student = self.students[student_id]
            if name:
                student.name = name
            if age:
                student.age = age
            if major:
                student.major = major
            print("Student updated successfully.")
            return True
        else:
            print("Student not found.")
            return False

    # DELETE
    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print("Student deleted successfully.")
            return True
        else:
            print("Student not found.")
            return False
        
class TestStudentRegistrationSystem(unittest.TestCase):
    def setUp(self):
        self.system = StudentRegistrationSystem()

    # Test CREATE
    def test_create_student_successful(self):
        result = self.system.create_student(1, "Alice", 20, "Computer Science")
        self.assertTrue(result)
        self.assertIn(1, self.system.students)

    def test_create_student_duplicate_id(self):
        self.system.create_student(1, "Alice", 20, "Computer Science")
        result = self.system.create_student(1, "Bob", 22, "Mathematics")
        self.assertFalse(result)
        self.assertEqual(self.system.students[1].name, "Alice")

    # Test READ
    def test_read_student_successful(self):
        self.system.create_student(1, "Alice", 20, "Computer Science")
        result = self.system.read_student(1)
        self.assertEqual(result, 1)

    def test_read_student_not_found(self):
        result = self.system.read_student(2)
        self.assertIsNone(result)

    def test_read_all_students_no_students(self):
        result = self.system.read_all_students()
        self.assertEqual(result, [])

    def test_read_all_students_with_students(self):
        self.system.create_student(1, "Alice", 20, "Computer Science")
        self.system.create_student(2, "Bob", 22, "Mathematics")
        result = list(self.system.read_all_students())
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].name, "Alice")
        self.assertEqual(result[1].name, "Bob")

    # Test UPDATE
    def test_update_student_successful(self):
        self.system.create_student(1, "Alice", 20, "Computer Science")
        result = self.system.update_student(1, name="Alice Updated", age=21)
        self.assertTrue(result)
        self.assertEqual(self.system.students[1].name, "Alice Updated")
        self.assertEqual(self.system.students[1].age, 21)

    def test_update_student_not_found(self):
        result = self.system.update_student(2, name="Non-existent")
        self.assertFalse(result)

    def test_update_student_partial_data(self):
        self.system.create_student(1, "Alice", 20, "Computer Science")
        result = self.system.update_student(1, major="Physics")
        self.assertTrue(result)
        self.assertEqual(self.system.students[1].major, "Physics")
        self.assertEqual(self.system.students[1].age, 20)

    # Test DELETE
    def test_delete_student_successful(self):
        self.system.create_student(1, "Alice", 20, "Computer Science")
        result = self.system.delete_student(1)
        self.assertTrue(result)
        self.assertNotIn(1, self.system.students)

    def test_delete_student_not_found(self):
        result = self.system.delete_student(2)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
