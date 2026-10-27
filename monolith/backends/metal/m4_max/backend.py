from ..base import MetalBackend


class Backend(MetalBackend):
    """M4 Max: the 40-core part measured (profile and kernel choices), the 32-core part a native fallback."""
    id = "m4_max"
