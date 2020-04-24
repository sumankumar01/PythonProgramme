class Enemy(object):

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives
        self.alive = True

    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print("i took {} poins damage have {} left".format(damage, self.hit_points))
        else:
            self.lives -= 1
            if self.lives > 0:
                print("{0.name} lost a live ".format(self))
            else:
                print("{0.name} dead a live ".format(self))
                self.alive = False

    def __str__(self):
        return "Name: {0.name}, lives: {0.lives}. hit: {0.hit_points}".format(self)


class Troll(Enemy):

    def __init__(self, name):
        # super(Troll, self).__init__(name=name, lives=1, hit_points=23)
        super().__init__(name=name, lives=1, hit_points=23)

    def grunt(self):
        print("Me {0.name}, {0.name} stop me".format(self))


# Enemy.__init__(self, name=name, lives=1, hit_points=23)


class vampire(Enemy):

    def __init__(self, name):
        super().__init__(name=name, lives=3, hit_points=12)
