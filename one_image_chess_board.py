from PIL import Image, ImageDraw

def draw_chessboard():
    # Size of the chessboard image
    image_size = (1000, 1000)

    # Number of rows and columns on the chessboard
    rows = 8
    columns = 8

    # Size of each square in pixels
    square_size = image_size[0] // columns

    # Create a blank white image
    image = Image.new("RGB", image_size, "white")
    draw = ImageDraw.Draw(image)

    # Draw the chessboard squares
    for row in range(rows):
        for col in range(columns):
            x0, y0 = col * square_size, row * square_size
            x1, y1 = x0 + square_size, y0 + square_size

            # Check if the square is light or dark and alternate colors
            color = "white" if (row + col) % 2 == 0 else "black"
            draw.rectangle([x0, y0, x1, y1], fill=color)

            # Map the chess coordinates to the center of each square
            chess_coordinates = (chr(ord('a') + col), rows - row)
            text_position = (x0 + square_size // 2, y0 + square_size // 2)

            # Draw the chess coordinates on the squares
            draw.text(text_position, str(chess_coordinates), fill="black")

    # Save or display the image
    image.save("chessboard.png")
    image.show()

# Call the function to draw the chessboard
draw_chessboard()
