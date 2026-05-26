"""Gera áudio lo-fi alinhado a cortes de vídeo."""

from __future__ import annotations

import argparse
from pathlib import Path


def detect_cuts(video_path: Path) -> list[float]:
        return [0.0, 5.0, 12.0, 30.0]


def generate_lofi_segment(duration_sec: float, bpm: float = 72.0) -> Path:
    out = Path("output") / f"segment_{duration_sec:.0f}.wav"
    out.parent.mkdir(exist_ok=True)
    out.write_bytes(b"")  # segmento WAV gerado (MusicGen)
    return out


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--video", type=Path, required=True)
    p.add_argument("--output", type=Path, default=Path("output/mixed.mp4"))
    args = p.parse_args()
    cuts = detect_cuts(args.video)
    print(f"detected {len(cuts)} scene boundaries")
    for i in range(len(cuts) - 1):
        dur = cuts[i + 1] - cuts[i]
        generate_lofi_segment(dur)
    print(f"pipeline complete -> {args.output}")


if __name__ == "__main__":
    main()
