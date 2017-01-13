#!/bin/bash

VERSION=`curl -s https://cgit.freedesktop.org/mesa/mesa/commit/ | grep parent | cut -f6 -d">" | cut -f1 -d"<"`
OLDVERSION=`cat Makefile | head -2 | tail -1 | cut -f7 -d"/" | cut -f1 -d"."`

if [ "$VERSION" == "$OLDVERSION" ] ; then
	echo "Nothing changed $OLDVERSION == $VERSION"
	exit 0
fi
	

echo "Updating from $OLDVERSION to $VERSION"

echo "PKG_NAME := mesa" > Makefile
echo "URL := https://cgit.freedesktop.org/mesa/mesa/snapshot/$VERSION.tar.gz" >> Makefile
echo "" >> Makefile
echo "" >> Makefile
echo "include ../common/Makefile.common" >> Makefile
make autospec
