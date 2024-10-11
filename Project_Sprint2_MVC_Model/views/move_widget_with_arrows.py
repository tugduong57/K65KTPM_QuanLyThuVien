
def move_widget_with_arrows(root, widget):
    # Đặt vị trí mặc định cho widget
    widget_position = {"x": 50, "y": 50}
    widget.place(x=widget_position["x"], y=widget_position["y"])

    # Hàm di chuyển widget
    def move_widget(dx, dy):
        widget_position["x"] += dx
        widget_position["y"] += dy
        widget.place(x=widget_position["x"], y=widget_position["y"])

    # Các hàm xử lý sự kiện
    def move_up(event):
        move_widget(0, -2)

    def move_down(event):
        move_widget(0, 2)

    def move_left(event):
        move_widget(-2, 0)

    def move_right(event):
        move_widget(2, 0)

    def print_position(event):
        print(f"Current position: x = {widget_position['x']}, y = {widget_position['y']}")

    # Gán phím mũi tên và phím Enter
    root.bind("<Up>", move_up)
    root.bind("<Down>", move_down)
    root.bind("<Left>", move_left)
    root.bind("<Right>", move_right)
    root.bind("<Return>", print_position)
