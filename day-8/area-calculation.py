import math
heightInput=int(input('enter the height value of the  wall: '))
widthInput=int(input('enter the width value of the wall:'))
def calculate_area(height,width,coverage):
    number_of_cans=(height*width)/coverage
    paintRequire=math.ceil(number_of_cans)
    print(f"you have to buy of paint {paintRequire} of cans" )
calculate_area(height=heightInput,width=widthInput,coverage=5)