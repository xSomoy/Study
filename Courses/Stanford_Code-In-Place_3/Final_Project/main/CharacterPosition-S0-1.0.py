# Character Position S0-1.0

from graphics import Canvas

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 500


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # canvas.create_rectangle(20,20,100,100,"blue")
    canvas.create_image_with_size(
        100, CANVAS_HEIGHT-120, 100, 120, "Karel.png")


if __name__ == '__main__':
    main()
