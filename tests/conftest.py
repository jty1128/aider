import importlib_resources

from aider.models import register_litellm_models


def pytest_configure(config):
    """Load bundled model metadata so tests have access to the same
    model info corrections that the CLI loads via main()."""
    resource_metadata = importlib_resources.files("aider.resources").joinpath(
        "model-metadata.json"
    )
    register_litellm_models([str(resource_metadata)])
