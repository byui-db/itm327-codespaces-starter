import unittest
from airflow.models import DagBag

class TestDBTDag(unittest.TestCase):
    def setUp(self):
        self.dagbag = DagBag()

    def test_dag_loaded(self):
        dag_id = 'tutorial_dag'  # ← Use your real DAG ID here
        self.assertIn(dag_id, self.dagbag.dags)

    def test_no_import_errors(self):
        self.assertEqual(
            len(self.dagbag.import_errors),
            0,
            f"DAG import errors: {self.dagbag.import_errors}"
        )

if __name__ == "__main__":
    unittest.main()