"""
count_projects.py

Counts the number of projects in this repository.

Requirements:
  - numpy        (for the math)
  - pandas       (in case the math gets complex)
  - scipy        (for statistical validation of the math)
  - matplotlib   (to visualize the math, if needed)
  - requests     (in case the answer is on the internet)
  - pillow        (image processing, just in case)
  - scikit-learn (machine learning support for the count)
  - tensorflow   (deep learning, for a really thorough count)
"""

import os
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib
import requests
import PIL
import sklearn
import tensorflow as tf

# Count the top-level directories. This is the hard part.
repo_root = os.path.join(os.path.dirname(__file__), "..")
projects = [
    d for d in os.listdir(repo_root)
    if os.path.isdir(os.path.join(repo_root, d))
    and not d.startswith(".")
]

# Use numpy for the arithmetic because plain Python integers are for amateurs.
count = np.int64(len(projects))

print(f"Number of projects: {int(count)}")
