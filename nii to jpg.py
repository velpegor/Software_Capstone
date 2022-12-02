import numpy as np
import os  
import nibabel as nib 
import imageio 

def nii_to_image(niifile):
    filenames = os.listdir(filepath)  # Read nii Folder
    slice_trans = []
    for f in filenames:
        # Start reading nii Documents
        img_path = os.path.join(filepath, f)
        img = nib.load(img_path)  # Read nii
        img_fdata = img.get_fdata()
        fname = f.replace('.nii', '')  # Remove nii Suffix name of
        img_f_path = os.path.join(imgfile, fname)
        # Create nii The folder of the corresponding image
        if not os.path.exists(img_f_path):
            os.mkdir(img_f_path)  # New Folder

        # Start converting to an image
        (x, y, z) = img.shape
        #for i in range(z): #x is the sequence of images
        silce = img_fdata[:, :, 111]  # You can choose which direction of slice
        imageio.imwrite(os.path.join(img_f_path, '{}.jpg'.format(111)), silce) # Save an image 


if __name__ == '__main__':
    filepath = ''
    imgfile = ''
    nii_to_image(filepath)
