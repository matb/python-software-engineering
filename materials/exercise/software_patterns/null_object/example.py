import typing
import dataclasses


@dataclasses.dataclass
class DataPoint:
    id: int
    first_name: str
    last_name: str
    subject: str
    score: int

    def human_evaluate(self):
        if self.evaluate():
            return "Passed"
        else:
            return "Failed"

    def evaluate(self):
        return self.score >= 80

    def did_pass(self):
        return self.evaluate()


class MockAPIWrapper:
    data = {1: dict(id=1, first_name="Matthias", last_name="Baumann", subject="Java", score=93),
            2: dict(id=1, first_name="Jana", last_name="Müller", subject="Java", score=98),
            3: dict(id=2, first_name="Marvin", last_name="Taschenberger", subject="Python", score=83)}

    def get(self, id: int) -> typing.Optional[DataPoint]:
        data = self.data.get(id)
        if data:
            return DataPoint(**data)
        return None


@dataclasses.dataclass
class DataPipeline:
    source: MockAPIWrapper
    ids: typing.List[int]

    def main(self):
        rate = self.process_score(self.ids)
        print(f"Current pass-rate = {rate}")

    def process_score(self, ids: typing.List[int]):

        passed = counter = 0
        for i in ids:
            if not i:
                continue
            counter += 1
            data = self.source.get(i)
            if data.did_pass():
                passed += 1
        return passed / counter


if __name__ == '__main__':
    api_wrapper = MockAPIWrapper()
    pipeline = DataPipeline(api_wrapper, [1, 2, 3, 4])
    pipeline.main()
