# tests/test_schema_generator.py

import unittest
from schema_generator import SchemaGenerator

class TestSchemaGen(unittest.TestCase):
    def test_basic_request(self):
        sg = SchemaGenerator()
        fields = sg.generate("Schema for collecting reviews on public services from youth")
        self.assertTrue(any(f["name"] == "id" for f in fields))
        self.assertTrue(len(fields) > 5)

if __name__ == "__main__":
    unittest.main()
