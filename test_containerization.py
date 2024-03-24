import unittest
import docker

class TestContainerization(unittest.TestCase):
    def test_docker_build(self):
        # Test building the Docker image
        client = docker.from_env()
        image, _ = client.images.build(path=".", tag="pdf-vector-search")
        self.assertIsNotNone(image)

    def test_docker_run(self):
        # Test running the Docker container
        client = docker.from_env()
        container = client.containers.run("pdf-vector-search", detach=True)
        self.assertTrue(container.status == "running")
        container.stop()
        container.remove()

if __name__ == '__main__':
    unittest.main()