#!/bin/bash
# Rename the release file based on the OS name

OS_NAME=${1:?"missing arg 1 for OS_NAME"}

VERSION=$(poetry version --short)

case "$OS_NAME" in
    "macos")
        ARCH_NAME=$([[ "$(arch)" = "arm64" ]] && echo "AppleSilicon" || echo "Intel")
        FILE_NAME="doggo-${VERSION}-macos-${ARCH_NAME}.dmg"
        mv ./dist/Doggo.dmg "./$FILE_NAME"
        ;;
    "windows")
        ARCH=$(python -c "import platform;print(platform.architecture()[0])")
        if [ "$ARCH" = "64bit" ]; then
            ARCH_NAME="x64"
        else
            ARCH_NAME="x32"
        fi
        FILE_NAME="doggo-${VERSION}-windows-${ARCH_NAME}.exe"
        mv ./dist/Doggo.exe "./$FILE_NAME"
        ;;
    "linux")
        ARCH_NAME=$(uname -m)
        FILE_NAME="doggo-${VERSION}-linux-${ARCH_NAME}.AppImage"
        mv ./dist/Doggo.AppImage "./$FILE_NAME"
        ;;
    *)
        echo "Unsupported OS: $OS_NAME"
        exit 1
        ;;
esac

echo "Renamed release file to $FILE_NAME"
