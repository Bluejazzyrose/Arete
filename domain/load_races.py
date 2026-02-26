import pkgutil
import importlib
import domain.races


def load_all_races():
    package = domain.races
    package_path = package.__path__

    for _, module_name, _ in pkgutil.iter_modules(package_path):
        importlib.import_module(f"{package.__name__}.{module_name}")