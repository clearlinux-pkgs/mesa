#!/bin/bash
set -e -o pipefail -x

get_crates() {
  # Rust crates for NVK, used as Meson subprojects
  local crates
  declare -A crates=(
    equivalent      1.0.1
    hashbrown       0.14.1
    indexmap        2.2.6
    once_cell       1.8.0
    paste           1.0.14
    pest            2.8.0
    pest_derive     2.8.0
    pest_generator  2.8.0
    pest_meta       2.8.0
    proc-macro2     1.0.86
    quote           1.0.33
    roxmltree       0.20.0
    rustc-hash      2.1.1
    syn             2.0.68
    ucd-trie        0.1.6
    unicode-ident   1.0.12
  )

  local aline="ARCHIVES ="
  for crate in "${!crates[@]}"; do
    local ver="${crates[$crate]}"
    local nv="${crate}-${ver}"
    aline="${aline} https://static.crates.io/crates/${crate}/${nv}.crate ./subprojects/${nv}"
  done

  echo "$aline"
}

if ! test `find "timestamp" -mmin +1500`
then
    echo "not old enough"
    exit
fi

BASE_URL=https://gitlab.freedesktop.org/mesa/mesa/-/archive/
REPO=${1-$HOME/git/mesa}
function git() { command git -C $REPO "$@"; }

git rev-parse HEAD > timestamp

OLDVERSION=`sed -n -e '/^URL/{s,.*'$BASE_URL',,;s,/.*,,p}' Makefile`

git remote update -p
VERSION=`git rev-parse origin/main`
DESCRIPTION=`git describe $VERSION | sed s/-branchpoint-/+/`

if [ "$VERSION" == "$OLDVERSION" ] ; then
	echo "Nothing changed $OLDVERSION == $VERSION"
	exit 0
fi

echo "Updating from $OLDVERSION to $VERSION"
echo "Updating from $OLDVERSION to $VERSION" > message
echo "" >> message
echo `git shortlog $OLDVERSION..$VERSION >> message`

echo "PKG_NAME := mesa" > Makefile
echo "URL := $BASE_URL$VERSION/mesa-$DESCRIPTION.tar.bz2" >> Makefile
echo get_crates >> Makefile
echo "" >> Makefile
echo "" >> Makefile
echo "include ../common/Makefile.common" >> Makefile
make autospec CLEANUP=1
git commit --amend -F message || :
make koji
nvr=$(rpmspec --srpm --query --queryformat='%{NVR}\n' mesa.spec)
koji wait-repo --build=$nvr dist-clear-build
# take care of rebuilds as per README.clear
for i in ../xf86-video-*; do
    command git -C $i pull
    make -C $i -j1 bump koji-nowait
done
