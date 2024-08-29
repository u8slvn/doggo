#!/bin/bash

create-dmg \
    --volname "Doggo" \
    --window-pos 200 200 \
    --window-size 460 350 \
    --icon "Doggo.app" 130 60 \
    --icon-size 64 \
    --hide-extension "Doggo.app" \
    --app-drop-link 325 60 \
    --format UDBZ \
    --no-internet-enable \
    "Doggo.dmg" \
    "./dist/Doggo.app"
