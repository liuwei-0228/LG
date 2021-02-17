class Animal:
    # 构造方法
    def __init__(self, name, color, age, sex):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex

    # 介绍
    def introduce(self):
        print(f"这是一只动物，名字叫{self.name},颜色是{self.color},年龄是{self.age}岁,性别是{self.sex}的")

    # 方法：叫
    def shout(self):
        print(f"一只名叫{self.name}的动物会叫")

    # 方法：跑
    def run(self):
        print(f"一只名叫{self.name}的动物会跑")


if __name__ == '__main__':
    animal = Animal("旺旺", "白色", 5, "公")
    animal.introduce()
    animal.shout()
    animal.run()
