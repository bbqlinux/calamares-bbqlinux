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

    # Localize Firefox and Thunderbird
    locale = libcalamares.globalstorage.value("lcLocale")
    if not locale:
        locale = 'en_GB'

    if (locale.startswith('bn_') == True):
        i18n = "bn-bd";
    elif (locale.startswith('en_US') == True):
        i18n = "en-us"
    elif (locale.startswith('en_') == True):
        i18n = "en-gb"
    elif (locale.startswith('es_AR') == True):
        i18n = "es-ar"
    elif (locale.startswith('es_') == True):
        i18n = "es-es"
    elif (locale.startswith('fy_') == True):
        i18n = "fy-nl"
    elif (locale.startswith('ga_') == True):
        i18n = "ga-ie"
    elif (locale.startswith('hy_') == True):
        i18n = "hy-am"
    elif (locale.startswith('nb_') == True):
        i18n = "nb-no"  
    elif (locale.startswith('nn_') == True):
        i18n = "nn-no"
    elif (locale.startswith('pa_') == True):
        i18n = "pa-in"
    elif (locale.startswith('pa_') == True):
        i18n = "pa-in"
    elif (locale.startswith('pt_BR') == True):
        i18n = "pt-br"
    elif (locale.startswith('pt_') == True):
        i18n = "pt-pt"
    elif (locale.startswith('sv_') == True):
        i18n = "sv-se"
    elif (locale.startswith('ta_') == True):
        i18n = "ta-lk"
    elif (locale.startswith('zh_TW') == True):
        i18n = "zh-tw"
    elif (locale.startswith('zh_') == True):
        i18n = "zh-cn"
    else:
        language_code = locale.split('_')[0]

        if (len(language_code) > 2):
            i18n = 'en-gb'
        else:
            i18n = language_code

    if (len(i18n) < 2):
        i18n = 'en-gb'

    chroot_call(['pacman', '-S', '--noconfirm', '--force', 'firefox-i18n-%s' % i18n])
    chroot_call(['pacman', '-S', '--noconfirm', '--force', 'thunderbird-i18n-%s' % i18n])

def run():
    cleanup()
    return None
