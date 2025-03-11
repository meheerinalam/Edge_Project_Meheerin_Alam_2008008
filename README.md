# Edge_Project_Meheerin_Alam_2008008
# EEG-Brain-Signal-Emotion-Classification
This repository includes code for categorizing emotions based on EEG brain waves. This project has been done as a part of EDGE Project course F028 & F023: Basic Programming with Python. After applying preprocessing techniques to a dataset of EEG signals recorded during various emotional stimuli, the project trains a neural network model to categorize the emotions.

Summary
The process of converting characteristics to numerical values is known as "data preprocessing." Managing values that are missing. Standardization is used for feature scaling. String labels are converted to one-hot format after being encoded to numerical values.

TensorFlow Keras was used to create a basic feed-forward neural network for model training. Dense layers with dropout for regularization are part of the model architecture. The model is compiled using categorical crossentropy loss and the Adam optimizer. Training and validation splits are used to train the model.

Evaluation: - Performance is assessed through the use of confusion matrices and classification reports.

Requirements
Make sure you have the following dependencies installed:

-Python 3.x
-TensorFlow (>= 2.x)
-Keras (bundled with TensorFlow)
-NumPy
-Pandas
-Scikit-learn
-Matplotlib
-Seaborn
You can install the required packages using pip:

pip install tensorflow numpy pandas scikit-learn matplotlib seaborn
