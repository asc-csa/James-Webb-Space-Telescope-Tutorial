# James-Webb-Data

About:
The objective of this tutorial is to promote JWST data and data accessibility as a whole. 
The Tutorial covers the techniques involved in opening and extracting the JWST data and converting to an image.
Also demonstrating the method of determining the number of galaxies in the produced image.


Run the script:
pip install -r requirements.txt

Required Packages for use: tarfile, astroquery.cadc
 matplotlib, astropy , imutils , skimage, numpy , cv2.
 
 
 Expected Behavior: 
Opening_a_tar_file.py will extract and save the .fits files containing the JWST image data
Visualize_2D_fits.py will plot a single fits file and save it
Brightness_test.py will create and filter pixels based off a brightness threshold.
The pixels that remain will be documented and circled, presenting the user with an estimate of the number of galaxies in the image.
  


