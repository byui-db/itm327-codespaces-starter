import unittest
from airflow.models import DagBag

class TestDBTDag(unittest.TestCase):
    def setUp(self):
        self.dagbag = DagBag()

    def test_dag_loaded(self):
        dag_id = "your_dag_id_here"  # Replace with your actual DAG ID
        self.assertIn(dag_id, self.dagbag.dags)
        self.assertGreater(len(self.dagbag.dags[dag_id].tasks), 0)

    def test_no_import_errors(self):
        self.assertEqual(len(self.dagbag.import_errors), 0, f"DAG import errors: {self.dagbag.import_errors}")

if __name__ == '__main__':
    unittest.main()