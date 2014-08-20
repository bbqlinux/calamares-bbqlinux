#!/usr/bin/env python3
# encoding: utf-8
# === This file is part of Calamares - <http://github.com/calamares> ===
#
#   Copyright 2014, Daniel Hillenbrand <codeworkx [at] bbqlinux [dot] org>
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
from libcalamares.utils import check_chroot_call

def cleanup():
    root_mount_point = libcalamares.globalstorage.value("rootMountPoint")

    # Remove livemedia configuration
    check_chroot_call(['pacman', '-R', '--noconfirm', 'bbqlinux-livemedia'])

    if(os.path.exists("%s/etc/skel/Desktop/BBQLinux-Installer.desktop" % root_mount_point)):
        check_chroot_call(['rm', '-f', '/etc/skel/Desktop/BBQLinux-Installer.desktop'])
    if(os.path.exists("%s/usr/share/applications/bbqlinux-installer-launcher.desktop" % root_mount_point)):
        check_chroot_call(['rm', '-f', '/usr/share/applications/bbqlinux-installer-launcher.desktop'])
    if(os.path.exists("%s/etc/skel/.config/autostart/bbqlinux-greeter.desktop" % root_mount_point)):
        check_chroot_call(['rm', '-f', '/etc/skel/.config/autostart/bbqlinux-greeter.desktop'])

    # Remove liveuser service
    if(os.path.exists("%s/etc/systemd/system/prepare_livesystem.service" % root_mount_point)):
        check_chroot_call(['rm', '-f', '/etc/systemd/system/prepare_livesystem.service'])
    if(os.path.exists("%s/etc/systemd/system/multi-user.target.wants/prepare_livesystem.service" % root_mount_point)):
        check_chroot_call(['rm', '-f', '/etc/systemd/system/multi-user.target.wants/prepare_livesystem.service'])
    if(os.path.exists("%s/usr/bin/prepare_livesystem" % root_mount_point)):
        check_chroot_call(['rm', '-f', '/usr/bin/prepare_livesystem'])

    # Remove calamares
    check_chroot_call(['pacman', '-R', '--noconfirm', 'calamares', 'calamares-bbqlinux'])

def run():
    cleanup()
    return None
