#!/bin/bash

path=$HOME/src/displaylink-debian
fname="linux-headers-$(uname -r)"
ctl_path="${path}/resources/linux-headers/${fname}.ctl"

# make the control file
equivs-control $ctl_path || exit 1

# fix the control file
python3 ./fix-ctl-file.py || exit 1

# build the package
tmp_dir=/tmp/displaylink-linux-headers
mkdir -p $tmp_dir
cd $tmp_dir || exit 1
equivs-build $ctl_path || exit 1

pkg_path="${tmp_dir}/${fname}_1.0_all.deb"

# install the package
sudo dpkg -i $pkg_path || exit 1

echo -e "\n...done installing dummy package for displaylink linux headers."
