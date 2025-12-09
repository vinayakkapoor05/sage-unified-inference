from typing import Any, Dict, List

from sage_unified_inference import backends
from .backends.base import Backend


class BackendRegistry:
    def __init__(self) -> None:
        self._backends: Dict[str, Backend] = {}

    def register(self, backend: Backend) -> None:
        if backend.name in self._backends:
            raise ValueError(f"{backend.name} already registered.")
        self._backends[backend.name] = backend

    def get(self, name: str) -> Backend:
        try:
            return self._backends[name]
        except KeyError:
            raise KeyError(f"{name} does not exist.")

    def list_names(self) -> List[str]:
        return list(self._backends.keys())


registry = BackendRegistry()
