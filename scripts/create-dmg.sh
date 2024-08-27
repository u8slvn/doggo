#!/bin/bash

ARCH_NAME=$([[ "$(arch)" = "arm64" ]] && echo "AppleSilicon" || echo "Intel")
VERSION=$(poetry version --short)

mkdir ./dist/dmg
mv ./dist/doggo-*.app ./dist/dmg/Doggo.app

create-dmg \
    --volname "Doggo" \
    --hide-extension "Doggo.app" \
    "doggo-$VERSION-$ARCH_NAME.dmg" \
    "./dist/dmg/Doggo.app"
