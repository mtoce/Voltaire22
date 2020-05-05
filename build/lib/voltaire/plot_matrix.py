import pandas as pd
import numpy as np

def confusion_matrix(y_true, y_pred):
  ''' Compute a confusion matrix using numpy for two np.arrays
  true and pred.

  Result is identical to: 
    "from sklearn.metrics import confusion_matrix" '''

  X = len(np.unique(y_true)) # Number of classes 
  result = np.zeros((X, X))
  labels = np.unique(y_true)
  columns = [f'Predicted {label}' for label in labels]
  index = [f'Actual {label}' for label in labels]

  for i in range(len(y_true)):
    result[y_true[i]][y_pred[i]] += 1
  result = pd.DataFrame((result), index=index, columns=columns)
  return result