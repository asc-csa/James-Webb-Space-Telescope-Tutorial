# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 15:51:46 2022

@author: karora
"""

import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
plt.style.use(astropy_mpl_style)


from astropy.utils.data import get_pkg_data_filename
from astropy.io import fits

#image_file = get_pkg_data_filename('extracted_tar_files/JWST/product/jw02738002002_gs-track_2022242044457_cal.fits')
#image_file = get_pkg_data_filename('extracted_tar_files/JWST/product/jw01521-o001_t001_miri_f770w_segm.fits')

image_file = get_pkg_data_filename(r'C:\Users\karora\Desktop\James_Webb_CADC\file.fits')

#jw01521-o001_t001_miri_f770w_segm -- good 2d image
#jw02738002002_gs-track_2022242044457_cal -- 3D working Image
 
#fits.info(image_file[0])

image_data = fits.getdata(image_file)

#print(image_data.shape)

#plt.axis ('off')
#plt.imshow(image_data[0,:,:],origin = 'lower' ,cmap='gray')  # 3D version
#plt.imshow(image_data,cmap='gray')  # 2D version

#fig, ax = plt.subplots()
#plt.subplots_adjust(0,0,10,10)

#img_cropped = image_data[77:141, 57:121, :]
#plt.imwrite(image_data,'test.png')
#colormap = matplotlib.cm.Greys
#reverse = math

#fig1 = plt.gcf()
#plt.imsave('test4.png',image_data,cmap = 'Greys_r')
#plt.show()

#fig1.savefig('test2.png')
#plt.colorbar()


#plt.savefig('test1.jpg')

