import numpy as np
var= np.array([[4, 3, 2], 
              [-2, 2, 3],
              [3, -5, 2]])
res= np.array([[25],
              [-10],
              [-4]])

sol = np.linalg.inv(var).dot(res)
print(sol)
