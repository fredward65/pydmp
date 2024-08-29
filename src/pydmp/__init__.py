from importlib import resources
try:
    import tomllib # type: ignore
except ModuleNotFoundError:
    import tomli as tomllib

# Version of the package
__version__ = "0.0.1"

# Read URL of the Real Python feed from config file
_cfg = tomllib.loads(resources.read_text("pydmp", "config.toml"))
# URL = _cfg["feed"]["url"]