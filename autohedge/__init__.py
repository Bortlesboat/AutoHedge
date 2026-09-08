from autohedge.env_loader import load_env

load_env()

__all__ = ["AutoHedge"]


def __getattr__(name):
    if name == "AutoHedge":
        from autohedge.main import AutoHedge

        return AutoHedge
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
