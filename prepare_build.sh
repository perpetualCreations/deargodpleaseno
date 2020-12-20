#!/bin/bash

sudo rm -rf build/deargodpleaseno/*
sudo cp src/* build/deargodpleaseno/ -r
sudo chmod -R 555 build/deargodpleaseno/DEBIAN/postinst
