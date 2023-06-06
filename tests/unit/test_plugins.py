import rush.plugins
from rush.core import discover_plugins


def test_plugins():
    plugins = discover_plugins(rush.plugins)

    assert len(plugins) == 1
