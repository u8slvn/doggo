#!/bin/bash

echo "Remove previous build if exists ..."
rm -rf ./dist/Doggo.dmg

echo "Create DMG ..."
create-dmg \
    --volname "Doggo" \
    --window-pos 200 200 \
    --window-size 460 160 \
    --icon "Doggo.app" 130 80 \
    --icon-size 64 \
    --hide-extension "Doggo.app" \
    --app-drop-link 325 80 \
    --format UDBZ \
    --no-internet-enable \
    "./dist/Doggo.dmg" \
    "./dist/Doggo.app"
