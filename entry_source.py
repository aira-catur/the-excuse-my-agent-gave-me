import os
from pathlib import Path

FINAL_MESSAGE = "Apologies for the delay: I hallucinated an email from you extending the deadline, and I believed me."


def emit(payload: str) -> None:
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / "entry.txt").write_text(payload, encoding="utf-8")


if __name__ == "__main__":
    emit(FINAL_MESSAGE)
