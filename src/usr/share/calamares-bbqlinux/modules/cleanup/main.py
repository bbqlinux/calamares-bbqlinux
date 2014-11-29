#!/usr/bin/env python3
# === This file is part of Calamares - <http://github.com/calamares> ===
#
#   Copyright 2014, Teo Mrnjavac <teo@kde.org>
#
#   Calamares is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   Calamares is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with Calamares. If not, see <http://www.gnu.org/licenses/>.

import os
import subprocess

import libcalamares

from libcalamares.utils import chroot_call
from libcalamares.utils import check_chroot_call

def cleanup():
    root_mount_point = libcalamares.globalstorage.value("rootMountPoint")

    # Remove pacman init service
    if(os.path.exists("%s/etc/systemd/system/etc-pacman.d-gnupg.mount" % root_mount_point)):
        chroot_call(['rm', '-f', '/etc/systemd/system/etc-pacman.d-gnupg.mount'])
    if(os.path.exists("%s/etc/systemd/system/pacman-init.service" % root_mount_point)):
        chroot_call(['rm', '-f', '/etc/systemd/system/pacman-init.service'])

    # Init pacman keyring
    check_chroot_call(['rm', '-rf', '/etc/pacman.d/gnupg'])
    check_chroot_call(['pacman-key', '--init'])
    check_chroot_call(['pacman-key', '--populate', 'archlinux'])
    check_chroot_call(['pacman-key', '--populate', 'bbqlinux'])
    chroot_call(['pacman-key', '--refresh-keys'])

    # Remove liveuser service
    if(os.path.exists("%s/etc/systemd/system/prepare_livesystem.service" % root_mount_point)):
        chroot_call(['rm', '-f', '/etc/systemd/system/prepare_livesystem.service'])
    if(os.path.exists("%s/etc/systemd/system/multi-user.target.wants/prepare_livesystem.service" % root_mount_point)):
        chroot_call(['rm', '-f', '/etc/systemd/system/multi-user.target.wants/prepare_livesystem.service'])
    if(os.path.exists("%s/usr/bin/prepare_livesystem" % root_mount_point)):
        chroot_call(['rm', '-f', '/usr/bin/prepare_livesystem'])

    # Modify lightdm config
    lightdmconfig = open("%s/etc/lightdm/lightdm.conf" % root_mount_point, "r")
    newlightdmconfig = open("%s/etc/lightdm/lightdm.conf.new" % root_mount_point, "w")

    for line in lightdmconfig:
        line = line.rstrip("\r\n")
        if(line.startswith("greeter-session=")):
            newlightdmconfig.write("greeter-session=lightdm-gtk-greeter\n")
        elif(line.startswith("#greeter-session=")):
            newlightdmconfig.write("greeter-session=lightdm-gtk-greeter\n")
        else:
            newlightdmconfig.write("%s\n" % line)

    lightdmconfig.close()
    newlightdmconfig.close()

    chroot_call(['rm', '-f', '/etc/lightdm/lightdm.conf'])
    chroot_call(['mv', '-f', '/etc/lightdm/lightdm.conf.new', '/etc/lightdm/lightdm.conf'])

def run():
    cleanup()
    return None
