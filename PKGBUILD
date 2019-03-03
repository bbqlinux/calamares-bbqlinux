# Maintainer: Daniel Hillenbrand <codeworkx [at] bbqlinux [dot] org>

pkgname=calamares-bbqlinux
pkgver=3.2.4
pkgrel=1
pkgdesc="BBQLinux configuration for the calamares installer framework"
arch=('any')
url="https://github.com/bbqlinux/calamares-bbqlinux"
license=('GPL')
depends=('calamares')

package() {
  cd "$pkgdir"

  mkdir -p usr

  cp -R "$srcdir/etc/" etc
  cp -R "$srcdir/usr/share" usr/share

  install -Dm440 "$srcdir/etc/sudoers.d/calamares" etc/sudoers.d/calamares
  
  # Fix permissions
  chmod 0750 etc/sudoers.d
}
