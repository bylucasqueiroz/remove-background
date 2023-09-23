import easygui
from PIL import Image
from rembg import remove

inputPath = easygui.fileopenbox(title='Select image file')
outputPath = easygui.filesavebox(title='Save file to..')

input = Image.open(inputPath)
output = remove(input)
output.save(outputPath)