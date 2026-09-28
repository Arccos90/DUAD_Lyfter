class Human:
    def __init__(self, torso):
        self.torso = torso
  
class Head:
    def __init__(self):
        pass

class Torso:
    def __init__(self, left_arm, right_arm, left_leg, right_leg, head):
        self.left_arm = left_arm
        self.right_arm = right_arm
        self.left_leg = left_leg
        self.right_leg = right_leg
        self.head = head

class Arm:
    def __init__(self, hand):
        self.hand = hand
        

class Hand:
    def __init__(self):
        pass
class Leg:
    def __init__(self, foot):
        self.foot = foot

class Foot:
    def __init__(self):
        pass


right_hand = Hand()
left_hand = Hand()
right_foot = Foot()
left_foot = Foot()
right_arm = Arm (right_hand)
left_arm = Arm (left_hand)
right_leg = Leg(right_foot)
left_leg = Leg(left_foot)
head = Head()
torso = Torso (left_arm, right_arm, left_leg, right_leg, head)
human = Human (torso)

print(human.torso.right_arm.hand is right_hand)
print(human.torso.left_arm.hand is right_hand)