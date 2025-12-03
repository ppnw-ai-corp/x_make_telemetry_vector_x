"""Expose telemetry toolkit objects without installing the package.

This shim exists so tooling can import the canonical telemetry helpers when the repo
root is directly on ``sys.path``. The real implementation lives in
``x_make_telemetry_vector_x.src.x_make_telemetry_vector_x`` and this module simply
re-exports its public surface so mypy/pyright/tests can resolve them.
"""

from __future__ import annotations

from .src.x_make_telemetry_vector_x import (
    DEFAULT_TELEMETRY_VERSION,
    TelemetryEvent,
    normalize_payload,
)

__all__ = ["DEFAULT_TELEMETRY_VERSION", "TelemetryEvent", "normalize_payload"]
