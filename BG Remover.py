from rembg import remove
import easygui
from PIL import Image

inputPath = easygui.fileopenbox(title="Select image file from: ")
outputPath = easygui.filesavebox(title="Save file to: ")

input = Image.open(inputPath)
output = remove(input)
output.save(outputPath)
