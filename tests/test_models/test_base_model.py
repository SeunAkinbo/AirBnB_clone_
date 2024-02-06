#!/usr/bin/python3
'''The test_base_model class'''

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        '''Set up test environment'''
        self.base_model = BaseModel()

    def test_attributes(self):
        '''Test instance attributes'''
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_id_is_string(self):
        '''Test if id attribute is a string'''
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_and_updtaed_at_are_datetime(self):
        '''Test if created_at and updated_at are datetime objects'''
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_method(self):
        '''Test save method'''
        old_update_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(old_updated_at, self.base_model.updated_at)

    def test_str_method(self):
        '''Test str method'''
        expected_str = f"[BaseModel] ({self.base_model.id})\
                        {self.base_model.__dict__}"
        self.assertEqual(str(self.base_models), expected_str)

    def test_to_dict_method(self):
        '''Test to_dict method'''
        obj_dict = self.base_model.to_dict()
        self.assertTrue('__class__' in obj_dict)
        self.assertTrue('created_at' in obj_dict)
        self.assertTrue('updated_at' in obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['updated_at'],
                        self,base_model.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()
