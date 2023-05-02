# Write your Service tests here
from unittest import TestCase

from urllib import request

from . import run_streamlit


class TestRunService(TestCase):

    def setUp(self):
        
        self.process, self.base_url = run_streamlit(
            'app/wave_buoy.py',
        )
        
        return super().setUp()

    def tearDown(self):
        if hasattr(self, 'process'):
            self.process.terminate()
        return super().tearDown()
    
    def test_run_main(self):
        response = request.urlopen(self.base_url)
        assert response.getcode() == 200