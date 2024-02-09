#!/usr/bin/python3
""""""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """"""
    def test_attributes(self):
        model = BaseModel()
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))

    def test_id_generation(self):
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_created_at(self):
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)

    def test_updated_at(self):
        model = BaseModel()
        self.assertIsInstance(model.updated_at, datetime)

    def test_save(self):
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(initial_updated_at, model.updated_at)

    def test_to_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertTrue(isinstance(model_dict, dict))
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(type(model_dict['created_at']), str)
        self.assertEqual(type(model_dict['updated_at']), str)

    def test_str(self):
        model = BaseModel()
        model_str = str(model)
        self.assertTrue(isinstance(model_str, str))

    def test_init_with_args(self):
        model = BaseModel(1, 2, 3)
        self.assertNotIn('1', model.__dict__.values())
        self.assertNotIn('2', model.__dict__.values())
        self.assertNotIn('3', model.__dict__.values())

    def test_init_with_kwargs(self):
        kwargs = {'id': '123', 'created_at': '2022-01-01T00:00:00', 'updated_at': '2022-01-01T00:00:00'}
        model = BaseModel(**kwargs)
        self.assertEqual(model.id, '123')
        self.assertEqual(model.created_at, datetime(2022, 1, 1, 0, 0, 0))
        self.assertEqual(model.updated_at, datetime(2022, 1, 1, 0, 0, 0))


if __name__ == '__main__':
    unittest.main()

