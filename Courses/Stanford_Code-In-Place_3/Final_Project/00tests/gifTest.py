from graphics import Canvas

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 500


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # canvas.create_rectangle(20,20,100,100,"blue")
    while True:
        canvas.wait_for_click()
        canvas.create_image_with_size(0, 0, 100, 120, "robotrun_400.gif")


if __name__ == '__main__':
    main()
