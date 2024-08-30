<p align="center">
  <a href="#readme" align="center">
      <img alt="Until Zero - タイマー | logo" src="https://raw.githubusercontent.com/u8slvn/doggo/main/assets/splash.png">
  </a>
</p>
<p align="center">
    <a href="https://github.com/u8slvn/doggo/releases"><img alt="GitHub tag (with filter)" src="https://img.shields.io/github/v/release/u8slvn/doggo"></a>
    <img src="https://img.shields.io/badge/python-3.12-blue" alt="Pypthon version">
    <a href="https://github.com/u8slvn/doggo/actions/workflows/ci.yaml"><img src="https://img.shields.io/github/actions/workflow/status/u8slvn/doggo/ci.yaml?label=CI" alt="CI"></a>
    <a href="https://github.com/u8slvn/doggo/actions/workflows/release.yaml"><img src="https://img.shields.io/github/actions/workflow/status/u8slvn/doggo/release.yaml?label=Build" alt="Build"></a>
    <a href="https://coveralls.io/github/u8slvn/doggo?branch=main"><img src="https://coveralls.io/repos/github/u8slvn/doggo/badge.svg?branch=main" alt="Coverage Status"></a>
    <a href="https://app.codacy.com/gh/u8slvn/doggo/dashboard"><img src="https://img.shields.io/codacy/grade/359900931def4b2cba3552678519ce2e" alt="Code Quality"></a>
    <a href="https://github.com/u8slvn/doggo"><img src="https://img.shields.io/github/license/u8slvn/doggo" alt="Project license"></a>
</p>

**Doggo** is a basic dog AI developed in Python and using pygame as a rendering engine. The dog just walks around the screen, changing states and direction randomly and dog's fur color is also picked randomly at start. State changes are based on a [Markov chain](https://en.wikipedia.org/wiki/Markov_chain), which is a simple model to represent a sequence of possible events in which the probability of each event depends only on the state attained in the previous event.

Here is a list of the dog states: *idle*, *idle and bark*, *walk*, *walk and bark*, *sit*, *sit and bark*, *lie down*, *lie down and bark*., *run*, *run and bark*, *stand*, *stand and bark*, *sleep*.

<p align="center">
    <img alt="doggo demo" src="https://raw.githubusercontent.com/u8slvn/doggo/main/assets/demo.gif">
</p>

**Project context**: A colleague of mine wanted to have a dog, but he couldn't because of lots of reasons. So I decided to make him a virtual dog and it was the opportunity for me to play with Markov chains.

<p align="center">
    📦 <a href="https://github.com/u8slvn/doggo/releases">⇩ Download latest release ⇩</a>📦
    <br/>
    <i>Note: release binaries are generated from the <a href="https://github.com/u8slvn/doggo/actions/workflows/release.yaml">release workflow</a> and are unsigned.<br />You may need to allow the execution of the binary in your system settings.</i>
</p>

## Controls

The project is designed as a simple pet widget to keep on your desktop. It's an always-on-top borderless window, so you need to click on it to get the focus before interacting with it.

* `ESC` to quit.
* `Left Click` to move the window around.

## Install and run

Make sure you have Python 3.12 installed on your machine. **Doggo** use [poetry](https://python-poetry.org/) to manage dependencies and virtual environment, so you need to install it too. Then, you can run the following commands at the root of the project:

```bash
poetry install
poetry run python -m doggo
```

## Build locally

If you want to build the project locally, you can use the script in `scripts/build.py`. It uses [PyInstaller](https://www.pyinstaller.org/) under the hood. Don't hesitate to update the script to fit your needs.

```bash
# Available os options: windows, linux, macos
poetry run python scripts/build.py --os <os>
```

The script will generate a `dist` folder at the root of the project with the executable inside.

## Development

For now, only one biome (mountain) is available. The feature to pick a biome randomly at start is already implemented, so I wish to add more in the future. Otherwise, I don't plan to add more features, like weathers or interactions, but the project is open to contributions. Just open a discussion before to make sure your idea fits the project.

## Licenses

* Code source under [GPL-3.0 License](https://www.gnu.org/licenses/gpl-3.0.en.html)
* Assets:
  * All assets under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
  * Excepting dog sprites in `src/doggo/assets/dogs` from **Pixel Dogs** by [Benvictus](https://benvictus.itch.io/pixel-dogs)
