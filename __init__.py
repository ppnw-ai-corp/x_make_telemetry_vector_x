"""Workspace shim that exposes the telemetry toolkit when the repo root is on sys.path.

The actual implementation lives inside :mod:`x_make_telemetry_vector_x.src.x_make_telemetry_vector_x`.
This shim simply re-exports the public surface so local tooling (mypy/pyright/tests)
can resolve the canonical objects without installing the package.
"""

from __future__ import annotations

from .src.x_make_telemetry_vector_x import (
    DEFAULT_TELEMETRY_VERSION,
    TelemetryEvent,
    normalize_payload,
)

__all__ = ["DEFAULT_TELEMETRY_VERSION", "TelemetryEvent", "normalize_payload"]
