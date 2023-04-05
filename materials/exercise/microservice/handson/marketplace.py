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

# TODO: Implement two routes
# 1- To get a random Weapon from the app.state.weapon - e.g. as the starting weapon for the game
# 2- To get an enhanced version. Let the user decide which one he wants,
# and increase on or multiple of the attributes randomly
# Extra - give the weapon a fancy name by prepending the type with something like "Mighty". "Great" or similar
# Hint you can directly return the Weapon-Object - no need for manual transformation


if __name__ == '__main__':
    uvicorn.run(app)