from PIL import Image
import math





def getImageAsList(path):
    image = Image.open(path)
    image = image.resize((250, 250))


    height = image.size[0]
    width = image.size[1]
    print("Image sucesffully loaded\n", height, width)

    data = list(image.getdata())

    return (data, height, width)

def convertTo2d(data, height, width):
    #convert to a 2d array
    dataArr = [[(0, 0, 0) for i in range(width)] for j in range(height)]

    counter = 0

    for i in range(0, height):
        for j in range(0, width):
            dataArr[i][j] = data[counter]
            counter += 1

    return dataArr



def getImageAs2dArray(path):

    first = getImageAsList(path)
    return convertTo2d(first[0], first[1], first[2])




def getPixelValues(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            print(data[i][j])



def convertRGB_to_brightness(data):

    brightnessMap = [[0 for i in range(len(data[1]))] for i in range(len(data))]


    for i in range(len(data)):
        for j in range(len(data[i])):

            average = (data[i][j][0] + data[i][j][1] + data[i][j][2])/3
            if(average > 255):
                print("WARN")
        
            brightnessMap[i][j] = round(average)

    return brightnessMap


def convertValueToReletiveRange(value, newRange, oldRange):
    scaleFactor = newRange/oldRange

    newValue = value*scaleFactor
    return math.floor(newValue)-1




def convertBrightnessToAscii(brightness):
    ascii = [[' ' for i in range(len(brightness[1]))] for i in range(len(brightness))]
    chart = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    print(len(chart))

    for i in range(len(brightness)):
        for j in range(len(brightness[i])):
            
            ascii[i][j] = chart[convertValueToReletiveRange(brightness[i][j], 65, 255)]

    return ascii


path = r'C:\Users\micha\Desktop\ASCII image generator\.venv\duck.jpg'
data = getImageAs2dArray(path)
brightness_matrix = convertRGB_to_brightness(data)
asciiMatrix = convertBrightnessToAscii(brightness_matrix)





for i in range(len(asciiMatrix)):
    for j in range(len(asciiMatrix[i])):
        print(asciiMatrix[i][j] + asciiMatrix[i][j]+ asciiMatrix[i][j], end='')
    print()















        




