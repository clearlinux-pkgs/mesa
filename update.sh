#!/bin/bash -e

BASE_URL=https://gitlab.freedesktop.org/mesa/mesa/-/archive/
REPO=${1-$HOME/git/mesa}
function git() { command git -C $REPO "$@"; }

OLDVERSION=`sed -n -e '/^URL/{s,.*'$BASE_URL',,;s,/.*,,p}' Makefile`

git remote update -p
VERSION=`git rev-parse origin/master`
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
${MAKE-make} autospec
make koji
sleep 60
cd ..
# take care of rebuilds as per README.clear
for i in  xf86-video-*; do pushd $i ; git pull ; make bump ; make koji-nowait; popd; done
