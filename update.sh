#!/bin/bash
set -e -o pipefail -x

BASE_URL=https://gitlab.freedesktop.org/mesa/mesa/-/archive/
REPO=${1-$HOME/git/mesa}
function git() { command git -C $REPO "$@"; }

OLDVERSION=`sed -n -e '/^URL/{s,.*'$BASE_URL',,;s,/.*,,p}' Makefile`

git remote update -p
VERSION=`git rev-parse origin/main`
DESCRIPTION=`git describe $VERSION | sed s/-branchpoint-/+/`

if [ "$VERSION" == "$OLDVERSION" ] ; then
	echo "Nothing changed $OLDVERSION == $VERSION"
	exit 0
fi

echo "Updating from $OLDVERSION to $VERSION"

echo "PKG_NAME := mesa" > Makefile
echo "URL := $BASE_URL$VERSION/mesa-$DESCRIPTION.tar.bz2" >> Makefile
echo "" >> Makefile
echo "" >> Makefile
echo "include ../common/Makefile.common" >> Makefile
make autospec
make koji
nvr=$(rpmspec --srpm --query --queryformat='%{NVR}\n' mesa.spec)
koji wait-repo --build=$nvr dist-clear-build
# take care of rebuilds as per README.clear
for i in ../xf86-video-*; do
    command git -C $i pull
    make -C $i -j1 bump koji-nowait
done
