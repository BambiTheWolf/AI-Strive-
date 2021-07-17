from altair.vegalite.v4.api import _dataset_name
from altair.vegalite.v4.schema.core import ScaleConfig
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA

heart_data_path = 'heart.csv'
heart_data = pd.read_csv(heart_data_path)

st.title('Heart Disease UCI')

st.write('''
It's possible to predict an heart attack?
''')

st.dataframe(heart_data)