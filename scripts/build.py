#!/usr/bin/python3
from __future__ import annotations

import argparse
import logging

from importlib import metadata
from pathlib import Path

import PyInstaller.__main__
import pyinstaller_versionfile


logger = logging.getLogger(__name__)

# ------ Build config ------
APP_NAME = "Doggo"
PACKAGE_NAME = "doggo"
ASSETS_FOLDER = "assets"

# ------ Versionfile info ------
COMPANY_NAME = "u8slvn"
FILE_DESCRIPTION = APP_NAME
INTERNAL_NAME = APP_NAME
LEGAL_COPYRIGHT = "GNU General Public License v3.0 - u8slvn"
PRODUCT_NAME = APP_NAME


# ------ Build paths ------
BUILD_PATH = Path(__file__).parent.resolve()
ROOT_PATH = BUILD_PATH.parent.resolve()
PROJECT_PATH = BUILD_PATH.parent.joinpath("src").resolve()
PACKAGE_PATH = PROJECT_PATH.joinpath(PACKAGE_NAME).resolve()
ASSETS_PATH = PACKAGE_PATH.joinpath(ASSETS_FOLDER).resolve()
ROOT_ASSETS_PATH = ROOT_PATH.joinpath(ASSETS_FOLDER).resolve()


def build_pyinstaller_args(
    output_filename: str,
    versionfile_path: Path | None = None,
) -> list[str]:
    logger.info("Build Pyinstaller args.")
    build_args = []
    script_entrypoint = f"src/{PACKAGE_NAME}/__main__.py"

    logger.info(f"entrypoint: {script_entrypoint}")
    build_args += [script_entrypoint]

    logger.info(f"Path to search for imports: {PACKAGE_PATH}")
    build_args += ["-p", f"{PACKAGE_PATH}"]

    logger.info(f"Spec file path: {BUILD_PATH}")
    build_args += ["--specpath", f"{BUILD_PATH}"]

    logger.info(f"Output exe filename: {output_filename}")
    build_args += ["-n", output_filename]

    logger.info(f"Output file icon: {ROOT_ASSETS_PATH.joinpath('icon-src.png')}")
    build_args += ["--icon", f"{ROOT_ASSETS_PATH.joinpath('icon-src.png')}"]

    logger.info(f"Add assets folder: {ASSETS_PATH}")
    build_args += ["--add-data", f"{ASSETS_PATH}:./{ASSETS_FOLDER}"]
    for items in ASSETS_PATH.glob("**/*"):
        if not items.is_dir():
            continue
        logger.info(f"Add data: {items}:./{ASSETS_FOLDER}/{items.name}")
        build_args += ["--add-data", f"{items}:./{ASSETS_FOLDER}/{items.name}"]

    if os in ["windows"]:
        logger.info(f"Add splash image: {ROOT_ASSETS_PATH.joinpath('splash.png')}")
        build_args += ["--splash", f"{ROOT_ASSETS_PATH.joinpath('splash.png')}"]

        logger.info("Build options: onefile")
        build_args += [
            "--onefile",  # One compressed output file
        ]

    logger.info("Build options: noconsole, clean")
    build_args += [
        "--noconsole",  # Disable log window
        "--clean",  # Clean cache and remove temp files
    ]

    if versionfile_path is not None:
        logger.info(f"Versionfile path: {versionfile_path}")
        build_args += ["--version-file", f"{versionfile_path}"]

    print(" ".join(build_args))
    return build_args


def run_pyinstaller(build_args: list[str]) -> None:
    PyInstaller.__main__.run(build_args)


def get_package_version() -> str:
    return metadata.version(PACKAGE_NAME)


def generate_versionfile(package_version: str, output_filename: str) -> Path:
    logger.info("Generate versionfile.txt.")
    versionfile_path = BUILD_PATH.joinpath("versionfile.txt")
    pyinstaller_versionfile.create_versionfile(
        output_file=versionfile_path,
        version=package_version,
        company_name=COMPANY_NAME,
        file_description=FILE_DESCRIPTION,
        internal_name=INTERNAL_NAME,
        legal_copyright=LEGAL_COPYRIGHT,
        original_filename=f"{output_filename}.exe",
        product_name=PRODUCT_NAME,
    )

    return versionfile_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Until Zero build script.")
    parser.add_argument(
        "--os",
        metavar="os",
        required=True,
        choices=["windows", "macos", "linux"],
        type=str,
    )

    args = parser.parse_args()

    os = args.os

    package_version = get_package_version()
    output_filename = PACKAGE_NAME.title()

    versionfile_path = None

    if os == "windows":
        versionfile_path = generate_versionfile(
            package_version=package_version,
            output_filename=output_filename,
        )

    build_args = build_pyinstaller_args(
        output_filename=output_filename,
        versionfile_path=versionfile_path,
    )
    run_pyinstaller(build_args=build_args)
