import random
# Soldier


class Soldier ():
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        self.health-=damage

# Viking


class Viking (Soldier):
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
    def receiveDamage(self, damage):
        self.health-=damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else: 
            return f"{self.name} has died in act of combat"
    def battleCry(self):
        return "Odin Owns You All!"


# Saxon


class Saxon (Soldier):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def receiveDamage(self, damage):
        self.health-=damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else: 
            return f"A Saxon has died in combat"
# War



class War ():
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]
    def addViking(self, viking):
        self.vikingArmy.append(viking)
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    def vikingAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        v_attack = saxon.receiveDamage(viking.strength)
        for e in self.saxonArmy:
            if e.health <= 0:
                self.saxonArmy.remove(e)
        return v_attack
    def saxonAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        s_attack = viking.receiveDamage(saxon.strength)
        for e in self.vikingArmy:
            if e.health <= 0:
                self.vikingArmy.remove(e)
        return s_attack
    def showStatus(self):
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
