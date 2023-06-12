from graphics import Canvas

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 800


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # canvas.create_rectangle(20,20,100,100,"blue")
    canvas.create_image(0, 550, "Karel.png")
    a = input()


if __name__ == '__main__':
    main()
