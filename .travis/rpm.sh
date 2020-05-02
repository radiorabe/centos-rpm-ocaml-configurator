#!/bin/bash
#
# RPM build wrapper for ocaml-configurator, runs inside the build container on travis-ci

set -xe

OBS_OS=`source /etc/os-release; echo $ID`

case $OBS_OS in
"centos")
    OBS_DIST="CentOS_7"
    yum -y install \
        epel-release
    ;;
"fedora")
    V=`source /etc/os-release; echo $VERSION_ID`
    OBS_DIST="Fedora_${V}"
    ;;
esac

curl -o /etc/yum.repos.d/liquidsoap.repo "https://download.opensuse.org/repositories/home:/radiorabe:/liquidsoap/${OBS_DIST}/home:radiorabe:liquidsoap.repo"

chown root:root ocaml-configurator.spec

mkdir -p /root/rpmbuild/SOURCES/
cp ocaml-configurator-0.11.0-pervasives-from-stdlib.patch /root/rpmbuild/SOURCES/

build-rpm-package.sh ocaml-configurator.spec
