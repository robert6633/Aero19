import math
import numpy as np
# Calculates Rotation Matrix given euler angles.


theta = list()

n = input("1st rotation (phi):")
theta.append(int(n))
n = input("2nd rotation (theta):")
theta.append(int(n))
n = input("3rd rotation (psi):")
theta.append(int(n))
print ('theta: ',theta)
#3theta = np.deg2rad(theta)


def eulerAnglesToRotationMatrix(theta) :
     #phi = theta[0]
     #theta = theta[1]
     #psi = theta[2]
     R_1 = np.array([[1,         0,                  0                   ],
                    [0,         math.cos(theta[0]), math.sin(theta[0]) ],
                    [0,         -math.sin(theta[0]), math.cos(theta[0])  ]
                    ])
         
         
                     
     R_2 = np.array([[math.cos(theta[1]),    0,      -math.sin(theta[1])  ],
                    [0,                     1,      0                   ],
                    [math.sin(theta[1]),   0,      math.cos(theta[1])  ]
                    ])
                 
     R_3 = np.array([[math.cos(theta[2]),    math.sin(theta[2]),    0],
                    [-math.sin(theta[2]),    math.cos(theta[2]),     0],
                    [0,                     0,                      1]
                    ])
                     
    #R_full = np.array([[math.cos(theta)*math.cos(psi)   math.cos(theta)*math.sin(psi)   -math.sin(theta)],
       #                [math.sin(phi)*math.sin(theta)*math.cos(psi)-math.cos(phi)*sin(psi)  math.sin(phi)*math.sin(psi)*math.sin(theta)+math.cos(phi)*math.cos(psi) math.sin(phi)*math.cos(theta)], 
      #                 [math.cos(phi)*math.sin(theta)*math.sin(psi)+math.sin(phi)*math.sin(psi)  math.cos(phi)*math.sin(theta)*math.sin(psi)-math.sin(phi)*math.cos(psi)  math.cos(phi)*math.cos(theta)]]
     #R = np.dot(R_1, np.dot( R_3, R_2 ))
     R = R_2@R_1@R_3
     return R 
   # return R_full

print(eulerAnglesToRotationMatrix(theta))