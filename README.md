# Gerador Algorítmico de Áudio Lo-Fi para B-Rolls

Gera trilha ambiente sincronizada com cortes do vídeo — sem copyright.

## Stack

- Python, PyTorch, Audiocraft/MusicGen

## Pipeline

1. Análise de cortes (PySceneDetect / frame diff)
2. Espectrograma por segmento
3. MusicGen condicionado ao tempo de cena
4. Mix final alinhado à timeline

## Análise temporal

```
cuts = detect_scenes(video)
for segment in cuts:
    tempo_bpm = estimate_tempo(segment)
    track += generate_lofi(duration, bpm=tempo_bpm)
```

Ver [docs/SPECTROGRAM.md](docs/SPECTROGRAM.md)

## Uso

```bash
python -m src.generate --video input.mp4 --output output/mixed.mp4
```

## Dependências de compilação

Audiocraft requer PyTorch + ffmpeg. Ver [docs/BUILD.md](docs/BUILD.md)
