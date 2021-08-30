import numpy as np

def calculate(list):
  #Create a function named `calculate()` in `mean_var_std.py` that uses Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix. 
 
  #The input of the function should be a list containing 9 digits. The function should convert the list into a 3 x 3 Numpy array, and then return a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix. 
  
  if len(list) < 9:
    raise ValueError("List must contain nine numbers.")  
  else:

    np_values = np.array(list)
  
    # Reshape into 3x3 matrix
    np_array = np.reshape(list, (3,3))

    calculations = { 
    'mean':[
    np.mean(np_array,axis=0).tolist(),
    np.mean(np_array,axis=1).tolist(),
    np.mean(np_array).tolist()],
    'variance':[
    np.var(np_array,axis=0).tolist(),
    np.var(np_array,axis=1).tolist(),
    np.var(np_array).tolist()],
    'standard deviation':[
    np.std(np_array,axis=0).tolist(),
    np.std(np_array,axis=1).tolist(),
    np.std(np_array).tolist()],
    'max':[
    np.max(np_array,axis=0).tolist(),
    np.max(np_array,axis=1).tolist(),
    np.max(np_array).tolist()],
    'min':[
    np.min(np_array,axis=0).tolist(),
    np.min(np_array,axis=1).tolist(),
    np.min(np_array).tolist()],
    'sum':[
    np.sum(np_array,axis=0).tolist(),
    np.sum(np_array,axis=1).tolist(),
    np.sum(np_array).tolist()]
    }

  return calculations