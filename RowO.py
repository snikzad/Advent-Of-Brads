from __future__ import division
from RS import RationalSlopes
from pythonic_slicer import VarBySlice
import numpy
import itertools
import sys
from osgeo import gdal
from PIL import Image, ImageDraw
'''
Shayla Nikzad 2016-06-19
Finds slope coresponding to a minimum variance
generates jpeg with line superimposed
fname = tiff file
fname2 = jpg file
N = for Rational Slopes
p = point line passes through
'''
def Orientation(fname,fname2,N,p):
    #determines list of slopes
    slopes = RationalSlopes(N)

    #opens NDVI data
    data = gdal.Open(fname)
    rb=data.GetRasterBand(1)
    matrix=numpy.matrix(rb.ReadAsArray())
    
    #finds slope_optimal-->minimum variance
    variance = 1000000
    for item in slopes:
        temp=VarBySlice(matrix,p,item)
        if temp < variance:
            variance = temp
            slope_optimal = item
    print(variance)
            
    #visualizes data
    im = Image.open(fname2)
    draw = ImageDraw.Draw(im)
    print(im.size)
    p2 = (im.size[0]*(slope_optimal[1]/slope_optimal[0]))+p[1]
    draw.line((0,p[1],im.size[0],p2), fill = "yellow", width = 3)
    del draw
    im.save("whyareyoubeingadick.jpg")
    
    return slope_optimal




                
   




