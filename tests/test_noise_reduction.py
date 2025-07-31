# tests/test_noise_reduction.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tests.speech_noise_test import record_and_denoise_test

if __name__ == "__main__":
    record_and_denoise_test()
