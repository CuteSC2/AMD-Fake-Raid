#!/bin/bash

if [[ $EUID -ne 0 ]]; then
  echo "You must run this with superuser privileges.  Try \"sudo ./dkms-install.sh\"" 2>&1
  exit 1
else
  echo "About to run dkms install steps..."
fi

DRV_DIR=rcraid
DRV_NAME=rcraid
DRV_VERSION=1.0.0

cp -r ../../${DRV_DIR}/src /usr/src/${DRV_NAME}-${DRV_VERSION}

dkms add -m ${DRV_NAME} -v ${DRV_VERSION}
dkms build -m ${DRV_NAME} -v ${DRV_VERSION}
dkms install -m ${DRV_NAME} -v ${DRV_VERSION}
RESULT=$?

echo "Finished running dkms install steps."

exit $RESULT
