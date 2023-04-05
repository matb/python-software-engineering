import random
import copy

import fastapi
import pydantic
import uvicorn


app = fastapi.FastAPI()


class Weapon(pydantic.BaseModel):
    type: str
    accuracy: float
    range: int
    damage: int
    speed: float


@app.on_event("startup")
def set_store():
    app.state.weapons = {
        "Sword": Weapon(
            type="Sword",
            accuracy=0.8,
            range=5,
            damage=10,
            speed=1
        ),
        "Hammer": Weapon(
            type="Hammer",
            accuracy=0.6,
            range=5,
            damage=15,
            speed=0.5
        ),
        "Bow": Weapon(
            type="Bow",
            accuracy=0.7,
            range=30,
            damage=5,
            speed=1.5
        ),
    }

    app.state.weapon_prefixes = ["Mighty", "Great", "Holy"]

# TODO: Implement two routes
# 1- To get a random Weapon from the app.state.weapons - e.g. as the starting weapon for the game
# 2- To get an enhanced version. Let the user decide which one he wants,
# and increase on or multiple of the attributes randomly
# Extra - give the weapon a fancy name by prepending the type with something like "Mighty". "Great" or similar
# Hint you can directly return the Weapon-Object - no need for manual transformation


@app.get("/api/v1/marketplace/weapon")
def get_random_weapon():
    weapons = app.state.weapons.keys()
    choice = random.choice(list(weapons))
    return app.state.weapons[choice]


@app.get("/api/v1/marketplace/weapon/{weapon-type}")
def get_randomized_weapon(weapon_type:str):
    weapon_original = app.state.weapons[weapon_type]
    weapon = copy.deepcopy(weapon_original)
    weapon.damage *= random.random() * random.randint(1,4)
    weapon.accuracy += (random.random() - 0.5) / 10
    weapon.type = f"{random.choice(app.state.weapon_prefixes)} {weapon.type}"
    return weapon


if __name__ == '__main__':
    uvicorn.run(app)