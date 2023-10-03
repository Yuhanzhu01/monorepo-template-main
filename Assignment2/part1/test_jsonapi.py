import unittest
import json

from jsonapi import Student, MyEncoder, StudentDecoder

class TestStudentSerialization(unittest.TestCase):
    def test_student_serialization(self):
        # Arrange
        student1 = Student(12, "sb")
        expected_json = '{"id": 12, "name": "sb", "__extended_json_type__": "Student"}'

        # Act
        stu_encode = json.dumps(student1, cls=MyEncoder)

        # Assert
        self.assertEqual(stu_encode, expected_json)

    def test_student_deserialization(self):
        # Arrange
        encoded_json = '{"id": 12, "name": "sb", "__extended_json_type__": "Student"}'
        expected_student = Student(12, "sb")

        # Act
        decoded_student = json.loads(encoded_json, cls=StudentDecoder)

        # Assert
        self.assertEqual(decoded_student.id, expected_student.id)
        self.assertEqual(decoded_student.name, expected_student.name)
        self.assertIsInstance(decoded_student, Student)

if __name__ == '__main__':
    unittest.main()
