#!/bin/sh

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install git python-virtualenv

git clone git@github.com:schematics/schematics-benchmark.git
cd schematics-benchmark/

virtualenv .
. bin/activate
pip install -U pip
pip install virtualenv git+https://github.com/spacetelescope/asv

asv machine --machine aws-ec2-micro --ram 1GB
./run.sh
asv gh-pages

sudo shutdown -h now
