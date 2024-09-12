# lib/testing/teacher_test.py

import pytest
from teacher import Teacher

class TestTeacher:
    def test_is_class(self):
        '''is a class with the name "Teacher".'''
        alice = Teacher(first_name='Alice', last_name='Smith')
        assert isinstance(alice, Teacher)
        
    def test_knowledge_initialization(self):
        '''initializes with the knowledge list.'''
        alice = Teacher(first_name='Alice', last_name='Smith')
        assert len(alice.knowledge) == 8

    def test_teach_method(self):
        '''returns a random element from the knowledge list.'''
        alice = Teacher(first_name='Alice', last_name='Smith')
        knowledge = alice.knowledge
        taught_knowledge = alice.teach()
        assert taught_knowledge in knowledge
