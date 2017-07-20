# https://www.tensorflow.org/tutorials/wide

import pandas as pd

COLUMNS = ["PassengerId", "Survived", "Pclass", "Name", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"]
TEST_COLUMNS = ["PassengerId", "Pclass", "Name", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"]

df_train = pd.read_csv("train.csv", names=COLUMNS, skipinitialspace=True, skiprows=1)
df_test = pd.read_csv("test.csv", names=TEST_COLUMNS, skipinitialspace=True, skiprows=1)

CATEGORICAL_COLUMNS = ["Pcalss", "Sex", "SibSp", "Parch", "Embarked"]
CONTINUOUS_COLUMNS = ["PassengerId", "Age", "Ticket", "Fare"]
LABEL_COLUMN = "Survived"

def input_fn(df):
  # Creates a dictionary mapping from each continuous feature column name (k) to
  # the values of that column stored in a constant Tensor.
  continuous_cols = {k: tf.constant(df[k].values)
                     for k in CONTINUOUS_COLUMNS}

  # Creates a dictionary mapping from each categorical feature column name (k)
  # to the values of that column stored in a tf.SparseTensor.
  categorical_cols = {k: tf.SparseTensor(
      indices=[[i, 0] for i in range(df[k].size)],
      values=df[k].values,
      dense_shape=[df[k].size, 1])
                      for k in CATEGORICAL_COLUMNS}

  # Merges the two dictionaries into one.
  feature_cols = dict(continuous_cols.items() + categorical_cols.items())

  # Converts the label column into a constant Tensor.
  label = tf.constant(df[LABEL_COLUMN].values)

  # Returns the feature columns and the label.
  return feature_cols, label

def train_input_fn():
  return input_fn(df_train)

def eval_input_fn():
  return input_fn(df_test)


