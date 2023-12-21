# bg_L2-S0-2.2.2

from graphics import Canvas

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 400


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    print("canvas created")
    #   Backgournd Layer 0
    # canvas.create_image_with_size(
    #     0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, "Background.jpg")
    print("BG-L0")
    #   Backgournd Layer 2
    canvas.create_image(0, CANVAS_HEIGHT-30, "road.png")
    print("BG-L2")
   # Karel Charecter
    canvas.create_image_with_size(
        100, CANVAS_HEIGHT-60, 50, 60, "Karel.png")
    print("Karel")


if __name__ == '__main__':
    main()
