#!/bin/bash


echo "=== Get latest release version ==="

git fetch --tags

RELEASE=`git describe --abbrev=0 --tags --match "v*"`
RELEASE_PARTS=(${RELEASE//./ })


echo "=== Create new release version ==="

MAJOR=$(date +'%y')
MINOR=$(date +'%W')
if ${MINOR} = ${RELEASE_PARTS[1]}
then
  PATCH=$((RELEASE_PARTS[2] + 1))
else:
  PATCH=0
fi

export NEW_RELEASE="v$MAJOR.$MINOR.$PATCH"

echo "=== Supersede $RELEASE with $NEW_RELEASE ==="

git tag ${NEW_RELEASE}
