from animal.Animal import Animal


class Cat(Animal):
    # 构造方法
    def __init__(self, name, color, age, sex):
        self.hair = "短毛"
        super().__init__(name, color, age, sex)

    # 方法：会抓老鼠
    def catch(self):
        print(f"名叫{self.name}的{self.hair}猫会抓老鼠")

    # 重写叫方法
    def shout(self):
        print(f"名叫{self.name}的猫咪会喵喵叫")


if __name__ == '__main__':
    cat = Cat("咪咪", "白色", 3, "母")
    cat.introduce()
    cat.catch()
    cat.shout()
