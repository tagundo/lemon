#!/bin/bash
clear
echo "Henol, please select need version to install:"
echo "0) tagundo (Stable, main branch -> ~/elichika3)"
echo "Actual version:"
echo "1) Latest (Slower, Stable, official contents of SIFAS only)"
echo "2) Single Player (Slower, Stable, Support modding contents & Improvement)"
echo ""
echo "Irrelevant versions:"
echo "3) Legacy (Faster, Stable, Limited features but also no modding support ATM)"
echo "4) Developement (NOT RECOMMENDED UNLESS YOU WANT HELP ME TO FIND THE ISSUE)"
echo ""
echo "6) tagundo (Test branch -> ~/elichika3_test, coexists with option 0)"
echo ""
echo "5) Cancel the SIFAS Local Server installation"
echo ""
read version
if [ -z $version ]
then
    echo "Empty version! Re-run installation script and choose correct version"
    rm install
    exit
elif [ $version = 0 ]
then
    curl -L https://raw.githubusercontent.com/tagundo/elichika/refs/heads/main/bin/install.sh | bash
elif [ $version = 1 ]
then
    curl -L https://raw.githubusercontent.com/arina999999997/elichika/master/bin/install.sh | bash
elif [ $version = 2 ]
then
    curl -L https://gitlab.com/tatara_hisoka/elichika/-/raw/main/bin/install.sh | bash
elif [ $version = 3 ]
then
    curl -L https://gitlab.com/tatara_hisoka/chichan/-/raw/main/bin/install.sh | bash
elif [ $version = 4 ]
then
    curl -L https://gitlab.com/tatara_hisoka/elichika/-/raw/developement/bin/install_dev.sh | bash
elif [ $version = 6 ]
then
    curl -L https://raw.githubusercontent.com/tagundo/elichika/refs/heads/main/bin/install_test.sh | bash
elif [ $version = 5 ]
then
    exit
else
    echo "Wrong version! Re-run installation script and choose correct version"
    exit
fi
