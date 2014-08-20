# Maintainer: Daniel Hillenbrand <codeworkx [at] bbqlinux [dot] org>

pkgname=calamares-bbqlinux
pkgver=0.0.5
pkgrel=1
pkgdesc="BBQLinux configuration for the calamares installer"
arch=('i686' 'x86_64')
url="https://github.com/bbqlinux/calamares-bbqlinux"
license=('GPL')
depends=('calamares')

package() {
  cd "$pkgdir"

  mkdir -p usr

  cp -R "$srcdir/etc" etc
  cp -R "$srcdir/usr/share" usr/share
}
