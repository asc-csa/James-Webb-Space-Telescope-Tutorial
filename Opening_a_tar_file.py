# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 14:51:55 2022

@author: karora
"""

import tarfile

tar = tarfile.open(r'C:\Users\karora\Desktop\MOST_project\Raw_tar_file\240_GSC0471901018_2013_5071.tar', "r:")
tar.extractall(r'C:\Users\karora\Desktop\MOST_project\Extracted_file')
tar.close()