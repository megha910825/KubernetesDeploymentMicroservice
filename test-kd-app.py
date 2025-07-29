import unittest
from microservice import app

class MicroserviceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_deploy_endpoint(self):
        response = self.app.post('/deploy', json={'image': 'nginx'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('pod_name', response.json)

    def test_status_endpoint(self):
        # Assuming a pod named 'test-pod' exists
        response = self.app.get('/status/test-pod')
        self.assertEqual(response.status_code, 200)
        self.assertIn('status', response.json)

if __name__ == '__main__':
    unittest.main()

