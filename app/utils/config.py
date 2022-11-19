from pathlib import Path
import yaml

with open(Path.joinpath(Path(__file__).parent, "variables.yml")) as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)
