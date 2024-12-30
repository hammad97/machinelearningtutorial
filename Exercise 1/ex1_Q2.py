import matplotlib.pyplot as plt
import numpy as np

#4.
def inverse_sq_mat(mat):
    #det = ad-bc
    det = mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0];
    
    invMat = np.array([[(mat[1][1]/det),   (-1*mat[0][1])/det],
                       [(-1*mat[1][0])/det, (mat[0][0])/det]])
    
    return invMat

# 1. 
matX = np.random.normal(2, 0.01, (100, 2))

# 2.
matY = np.random.uniform(2, 1, (100, 1))


# 3, 4, 5.

# 100x2 * 2x100 = 2x2
# 2x100 * 100x1 = 2x2
matB = np.matmul(matX.T, matY)
matA = np.matmul(matX.T, matX)

invMatA = inverse_sq_mat(matA)

matBeta = np.matmul(invMatA, matB)

matPredY = np.matmul(matX, matBeta)

# 6.
plt.scatter(matY, matPredY)
plt.xlabel("Original Y", size = 10)
plt.ylabel("Predicted Y", size = 10)
plt.title("Original vs Predicted Matrix Y", size = 12)
plt.show()


# 7.
matBetaAuto = np.linalg.lstsq(matX, matY, rcond = None)[0]

matPredYAuto = np.matmul(matX, matBetaAuto)
plt.scatter(matPredY, matPredYAuto)
plt.xlabel("Manual Prediction", size = 10)
plt.ylabel("Auto Prediction", size = 10)
plt.title("Manual vs Auto Predtion of Y", size = 12)
plt.show()
