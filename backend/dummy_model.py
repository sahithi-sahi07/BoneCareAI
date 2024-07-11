# backend/dummy_model.py
import pickle
import numpy as np

def dummy_model(x):
    return 'fracture' if np.sum(x) > 1000 else 'no fracture'

# Save the dummy model using pickle
with open('model/bone_fracture_model.pkl', 'wb') as f:
    pickle.dump(dummy_model, f)
