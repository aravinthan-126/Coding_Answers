#This Below code is use function.
import matplotlib.pyplot as plt
import numpy as np
def create_chessboard(size=8):
    chessboard=np.zero((size,size))
    chessboard[1::2,::2]=1
    chessboard[::2,1::2]=1
    return chessboard
def plot_chessboard(chessbosrd):
    plt.figure(figure=(6,6))
    plt.imshow(chessboard,cmap='gray',interpolation='nearest')
    plt.xticks([])
    plt.yticks([])
chessboard=create_chessboard
plot_chessboard(chessboard)
#This Below code is without use function.
import matplotlib.pyplot as plt
import numpy as np
size=8
chessboard=np.zeros((size,size))
chessboard[1::2,::2]=1
chessboard[::2,1::2]=1
plt.figure(figure=(6,6))
plt.imshow(chessboard,cmap='gray',interpolation='nearest')
plt.xticks([])
plt.yticks([])
plt.show()