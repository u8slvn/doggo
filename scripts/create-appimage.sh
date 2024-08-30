#!/bin/bash

echo "Remove previous build if exists ..."
rm -rf ./dist/Doggo.AppImage

echo "Create AppImage ..."
appimage-builder --recipe AppImageBuilder.yml --skip-tests
