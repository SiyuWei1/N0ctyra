import tkinter as tk
import random

# 游戏配置
WIDTH = 600
HEIGHT = 400
SIZE = 20  # 蛇身和食物的大小
SPEED = 100  # 游戏刷新速度 (毫秒)


class SnakeGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Python 贪吃蛇")

        # 画布
        self.canvas = tk.Canvas(self.window, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        # 初始化状态
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.direction = "Right"
        self.food = self.create_food()
        self.score = 0
        self.running = True

        # 绑定按键
        self.window.bind("<KeyPress>", self.change_direction)

        # 开始游戏循环
        self.update()
        self.window.mainloop()

    def create_food(self):
        x = random.randint(0, (WIDTH - SIZE) // SIZE) * SIZE
        y = random.randint(0, (HEIGHT - SIZE) // SIZE) * SIZE
        return (x, y)

    def change_direction(self, event):
        new_dir = event.keysym
        # 防止 180 度掉头
        opposites = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
        if new_dir in opposites and new_dir != opposites.get(self.direction):
            self.direction = new_dir

    def update(self):
        if not self.running:
            return

        # 计算新蛇头坐标
        head_x, head_y = self.snake[0]
        if self.direction == "Up":
            head_y -= SIZE
        elif self.direction == "Down":
            head_y += SIZE
        elif self.direction == "Left":
            head_x -= SIZE
        elif self.direction == "Right":
            head_x += SIZE

        new_head = (head_x, head_y)

        # 碰撞检测：墙壁或自己
        if (head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT or
                new_head in self.snake):
            self.game_over()
            return

        self.snake.insert(0, new_head)

        # 吃到食物
        if new_head == self.food:
            self.score += 10
            self.food = self.create_food()
        else:
            self.snake.pop()

        self.draw()
        self.window.after(SPEED, self.update)

    def draw(self):
        self.canvas.delete("all")
        # 画食物
        self.canvas.create_oval(self.food[0], self.food[1], self.food[0] + SIZE, self.food[1] + SIZE, fill="red")
        # 画蛇
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0], segment[1], segment[0] + SIZE, segment[1] + SIZE, fill="green",
                                         outline="white")
        # 画分数
        self.canvas.create_text(50, 20, text=f"分数: {self.score}", fill="white", font=("Arial", 12))

    def game_over(self):
        self.running = False
        self.canvas.create_text(WIDTH // 2, HEIGHT // 2, text=f"游戏结束!\n最终得分: {self.score}", fill="yellow",
                                font=("Arial", 30), justify="center")


if __name__ == "__main__":
    SnakeGame()