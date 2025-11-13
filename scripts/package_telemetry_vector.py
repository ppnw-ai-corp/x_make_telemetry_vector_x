from __future__ import annotations

import hashlib
import shutil
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DIST_DIR = PROJECT_ROOT / "dist"
BUILD_DIR = PROJECT_ROOT / "build"
ARTIFACT_DIR = PROJECT_ROOT / "artifacts" / "packages" / "x_make_telemetry_vector_x"


def run(cmd: list[str]) -> None:
    """Run a subprocess and raise if it fails."""
    try:
        subprocess.run(  # noqa: S603 - command assembled from trusted inputs
            cmd,
            cwd=PROJECT_ROOT,
            check=True,
        )
    except subprocess.CalledProcessError as exc:
        command_display = " ".join(cmd)
        message = f"Command {command_display} failed with code {exc.returncode}"
        raise SystemExit(message) from exc


def clean_directories() -> None:
    """Remove previous build artifacts to guarantee a clean build."""
    for directory in (DIST_DIR, BUILD_DIR):
        if directory.exists():
            shutil.rmtree(directory)
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)


def build_package() -> None:
    """Invoke python -m build to create wheel and sdist."""
    python_executable = Path(sys.executable)
    run([str(python_executable), "-m", "build"])


def compute_hashes() -> None:
    """Compute SHA256 hashes for the generated artifacts."""
    hash_path = ARTIFACT_DIR / "hashes.txt"
    with hash_path.open("w", encoding="utf-8") as hash_file:
        for artifact in sorted(DIST_DIR.glob("*")):
            digest = hashlib.sha256(artifact.read_bytes()).hexdigest()
            hash_file.write(f"{artifact.name} {digest}\n")


def main() -> None:
    clean_directories()
    build_package()
    compute_hashes()
    print(f"Build artifacts stored in {DIST_DIR}")
    print(f"Hash manifest written to {ARTIFACT_DIR / 'hashes.txt'}")


if __name__ == "__main__":
    main()
