# lib/testing/user_test.py

import pytest
from student import Student

class TestStudent:
    def test_is_class(self):
        '''is a class with the name "Student".'''
        john = Student(first_name='John', last_name='Doe')
        assert isinstance(john, Student)
        
    def test_knowledge_initialization(self):
        '''initializes with an empty knowledge list.'''
        john = Student(first_name='John', last_name='Doe')
        assert john.knowledge == []

    def test_learn_method(self):
        '''learns and appends new knowledge to the list.'''
        john = Student(first_name='John', last_name='Doe')
        john.learn("Python is awesome")
        assert john.knowledge == ["Python is awesome"]
