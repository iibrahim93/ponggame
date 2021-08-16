from user_paddle import UserPaddle
MOVE_DISTANCE = 20
POSITIONS = [(-650, 0), (-650, 20), (-650, 40), (-650, 60), (-650, 80), (-650, 100)]

class Paddle(UserPaddle):
    def __init__(self):
        super().__init__()
        self.goto(-650, 0)




