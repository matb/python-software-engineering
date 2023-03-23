import xml.etree.ElementTree

from experiment import Experiment
from xml_adapter import XMLAdapter


def main() -> None:

    tree = xml.etree.ElementTree.parse("config.xml")
    adapter = XMLAdapter(tree)
    experiment = Experiment(adapter)
    experiment.run()


if __name__ == "__main__":
    main()
