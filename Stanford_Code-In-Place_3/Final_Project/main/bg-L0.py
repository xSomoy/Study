# Character Position S0.1

from graphics import Canvas

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 400


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
  
   
    #   Backgournd Layer 0 
    canvas.create_image(0, 0, "backgroud.jpg")
    
   # Karel Charecter
    canvas.create_image_with_size(
        100, CANVAS_HEIGHT-120, 100, 120, "Karel.png")

if __name__ == '__main__':
    main()
