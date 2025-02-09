#!/usr/bin/python3


class Fish:
    def swim(self):
        return ("The fish is swimming")

    def habitat(self):
        return ("The fish lives in water")


class Bird:
    def fly(self):
        return ("The bird is flying")

    def habitat(self):
        return ("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    def fly(self):
        return ("The flying fish is soaring!")

    def swim(self):
        return ("The flying fish is swimming!")

    def habitat(self):
        return ("The flying fish lives both in water and the sky!")


fish = FlyingFish()
print(fish.swim())
print(fish.fly())
print(fish.habitat())
