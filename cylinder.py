# Created by: Kay Lin
# Created on: 7th-Nov-2017
# Created for: ICS3U
# This program displays calculattion of volume of cylinder

def volume(radius, height):
    # enter radius and height(two parameters) and return them
    PI = 3.14
    
    V = ((2 * PI * (radius ** 2) * height))
    return V
    
# V function
height = raw_input('Enter height: ')
height = int(height)
radius = raw_input('Enter radius: ' )
radius = int(radius)
if height < 0 or radius < 0:
   print ('Please input valid number.')
else:
    volume_print = volume(radius, height)
    print('The volume of cylinder is ' + str(volume_print) + ' cm^3')
