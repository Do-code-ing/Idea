import random

class Marine():
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.weapon_1 = None
        self.weapon_2 = None
        self.hit_index = 0
        self.damage = damage

    def __str__(self):
        return f"이름 : {self.name}, hp : {self.hp}, 공격력 : {self.damage}\n무기1: {self.weapon_1}, 무기2 : {self.weapon_2}"

    @classmethod
    def create(cls, information):
        information = information.split(" ")
        name = information[0]
        hp = int(information[1])
        damage = int(information[2])
        return cls(name, hp, damage)

    def attack(self):
        print(f"{self.damage}의 데미지를 입힙니다.")

    def damaged_to(self, damaged):
        if self.hp <= 0:
            print(f"{self.name}(은)는 죽어있어요.")
        else:
            self.hit_index = random.randint(0,1)
            if self.hit_index != 0:
                print("공격에 맞았습니다.")
                print(f"받은 데미지 {damaged}")
                print(f"현재 체력 : {self.hp}")
                self.hp -= damaged
                if self.hp <= 0:
                    print(f"{self.name}(은)는 죽었어요.")
            else:
                print("공격을 회피했습니다.")

    def install_weapon(self, weapon):
        if self.weapon_1 == None:
            print(f"{weapon} 장착")
            self.weapon_1 = weapon
            if self.weapon_1 == "무한의 대검":
                self.damage += 10
            else:
                self.damage += 11
        else:
            if self.weapon_2 == None:
                print(f"{weapon} 장착")
                self.weapon_2 = weapon
                if self.weapon_2 == "무한의 대검":
                    self.damage += 10
                else:
                    self.damage += 11
            else:
                print("이미 무기가 꽉 차있어요")

    def stimpack(self):
        if self.hp > 10:
            print("스팀팩 사용")
            self.hp -= 10
        else:
            print("체력 부족")

    def lose_damage(self, lose):
        print(f"공격력 {lose}만큼 잃었어요")
        self.damage -= lose





# m1 = Marine("마린", 40, 5)
# print(m1)
# m1.install_weapon("라바돈의 죽음 모자")
# m1.install_weapon("라바돈의 죽음 모자")
# print(m1)
# m2 = Marine.create("파이어벳 100 24")
# m2.install_weapon("무한의 대검")
# print(m2)

class C_Static():
    greeting_index = None
    def __init__(self, age, name):
        self.age = age
        self.name = name
        self.greet = "Hello"

    def hello(self):
        print(f"{self.name}/{self.age} : \"{self.greet}\"")

    @staticmethod
    def f_static(greeting):
        greeting_index = greeting
        return greeting_index

person = C_Static(15,"Jimmy")
person.f_static(1)
print(C_Static.greeting_index)

# 공부하던 부분 위 예제는 잘못된 사용
