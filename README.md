# MANIM-practice
- Manim is an engine for programmatic animations
- There are two versions of manim; [Personal project of 3b1b](https://github.com/3b1b/manim) and [open source community version](https://github.com/ManimCommunity/manim/) for more stable usage.

## Installation (community version on MAC)
### Common
1. Install ffmpeg (media en/decoder)
2. Install Manim, Pycairo in pip

```shell
brew install ffmpeg
pipenv install pycairo manim
```

### Optional if need
- LaTeX (CLI, text program)
- SoX (audio inverter)
- OpenGL (graphic program)

### CLI usage
```shell
manim scene.py CreateCircle
```
- Options
    - '-ql': render a video with low quality
    - '-p': preview (with video encoder)
    - '--renderer=opengl': available a preview with opengl (won't be saved)