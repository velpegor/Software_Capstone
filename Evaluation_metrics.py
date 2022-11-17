#Correlation coefficient 

from PIL import Image
import numpy as np
import math
import cmath
import numpy as np

def correlationCoefficient(X, Y):
    n = X.size
    sum_X = X.sum()
    sum_Y = Y.sum()
    sum_XY = (X*Y).sum()
    squareSum_X = (X*X).sum()
    squareSum_Y = (Y*Y).sum()
    corr = (n * sum_XY - sum_X * sum_Y)/(np.sqrt((n * squareSum_X - sum_X * sum_X)* (n * squareSum_Y - sum_Y * sum_Y))) 
    return corr


from PIL import Image

img1 = Image.open("/content/100[292].jpg_deface_rec_B.png").convert("L")
im1 = np.array(img1)/255

img2 = Image.open("/content/100[292].jpg_deface_real_B.png").convert("L")
im2 = np.array(img2)/255

print ('{0:.6f}'.format(correlationCoefficient(im1, im2)))

#SSIM
from IQA_pytorch import SSIM, utils
from PIL import Image
import torch
 
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
 
ref_path  = '/content/100[292].jpg_deface_real_B.png'
dist_path = '/content/100[292].jpg_deface_rec_B.png' 
 
ref = utils.prepare_image(Image.open(ref_path).convert("RGB")).to(device)
dist = utils.prepare_image(Image.open(dist_path).convert("RGB")).to(device)
 
model = SSIM(channels=3)
 
score = model(dist, ref, as_loss=False)
print('score: %.4f' % score.item())
