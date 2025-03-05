import pickle
import numpy as np
from sklearn.linear_model import LinearRegression

# Simulated dataset (for training)
X_train = np.array([[1], [3], [5], [7], [10]])  # Years of experience
y_train = np.array([50, 60, 75, 85, 95])  # Matching scores based on HR hiring trends

# Train a simple model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
with open("resume_score_model.pkl", "wb") as f:
    pickle.dump(model, f)

# Function to predict score
def predict_resume_score(experience):
    with open("resume_score_model.pkl", "rb") as f:
        model = pickle.load(f)
    return model.predict(np.array([[experience]])).tolist()[0]
