#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : wsjtx
Version  : 2.1.2
Release  : 5
URL      : https://sourceforge.net/projects/wsjt/files/wsjtx-2.1.2/wsjtx-2.1.2.tgz
Source0  : https://sourceforge.net/projects/wsjt/files/wsjtx-2.1.2/wsjtx-2.1.2.tgz
Source1  : 0001-Fix-build-with-Qt-5.13-Qt-comes-with-its-std-hash-sp.patch
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: wsjtx-bin = %{version}-%{release}
Requires: wsjtx-data = %{version}-%{release}
Requires: wsjtx-license = %{version}-%{release}
Requires: wsjtx-man = %{version}-%{release}
BuildRequires : asciidoc
BuildRequires : buildreq-cmake
BuildRequires : libusb-dev
BuildRequires : pkgconfig(Qt5Multimedia)
BuildRequires : pkgconfig(Qt5SerialPort)
BuildRequires : pkgconfig(fftw3)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(libudev)
BuildRequires : qttools-dev
BuildRequires : texinfo

%description
__       __   ______      _____  ________      __    __
|  \  _  |  \ /      \    |     \|        \    |  \  |  \
| $$ / \ | $$|  $$$$$$\    \$$$$$ \$$$$$$$$    | $$  | $$
| $$/  $\| $$| $$___\$$      | $$   | $$ ______ \$$\/  $$
| $$  $$$\ $$ \$$    \  __   | $$   | $$|      \ >$$  $$
| $$ $$\$$\$$ _\$$$$$$\|  \  | $$   | $$ \$$$$$$/  $$$$\
| $$$$  \$$$$|  \__| $$| $$__| $$   | $$       |  $$ \$$\
| $$$    \$$$ \$$    $$ \$$    $$   | $$       | $$  | $$
\$$      \$$  \$$$$$$   \$$$$$$     \$$        \$$   \$$

%package bin
Summary: bin components for the wsjtx package.
Group: Binaries
Requires: wsjtx-data = %{version}-%{release}
Requires: wsjtx-license = %{version}-%{release}

%description bin
bin components for the wsjtx package.


%package data
Summary: data components for the wsjtx package.
Group: Data

%description data
data components for the wsjtx package.


%package doc
Summary: doc components for the wsjtx package.
Group: Documentation
Requires: wsjtx-man = %{version}-%{release}

%description doc
doc components for the wsjtx package.


%package license
Summary: license components for the wsjtx package.
Group: Default

%description license
license components for the wsjtx package.


%package man
Summary: man components for the wsjtx package.
Group: Default

%description man
man components for the wsjtx package.


%prep
%setup -q -n wsjtx-2.1.2
cd %{_builddir}/wsjtx-2.1.2

%build
## build_prepend content
cp $RPM_SOURCE_DIR/0001-Fix-build-with-Qt-5.13-Qt-comes-with-its-std-hash-sp.patch wsjtx.patch
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1579642545
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake .. -DWSJT_GENERATE_DOCS:BOOL=OFF
make  %{?_smp_mflags}  VERBOSE=1
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
## build_prepend content
cp $RPM_SOURCE_DIR/0001-Fix-build-with-Qt-5.13-Qt-comes-with-its-std-hash-sp.patch wsjtx.patch
## build_prepend end
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -O3 -fno-lto -march=haswell "
export FCFLAGS="$CFLAGS -O3 -fno-lto -march=haswell "
export FFLAGS="$CFLAGS -O3 -fno-lto -march=haswell "
export CXXFLAGS="$CXXFLAGS -O3 -fno-lto -march=haswell "
export CFLAGS="$CFLAGS -march=haswell -m64"
export CXXFLAGS="$CXXFLAGS -march=haswell -m64"
%cmake .. -DWSJT_GENERATE_DOCS:BOOL=OFF
make  %{?_smp_mflags}  VERBOSE=1
popd
mkdir -p clr-build-avx512
pushd clr-build-avx512
## build_prepend content
cp $RPM_SOURCE_DIR/0001-Fix-build-with-Qt-5.13-Qt-comes-with-its-std-hash-sp.patch wsjtx.patch
## build_prepend end
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -O3 -fno-lto -march=skylake-avx512 "
export FCFLAGS="$CFLAGS -O3 -fno-lto -march=skylake-avx512 "
export FFLAGS="$CFLAGS -O3 -fno-lto -march=skylake-avx512 "
export CXXFLAGS="$CXXFLAGS -O3 -fno-lto -march=skylake-avx512 "
export CFLAGS="$CFLAGS -march=skylake-avx512 -m64 "
export CXXFLAGS="$CXXFLAGS -march=skylake-avx512 -m64 "
%cmake .. -DWSJT_GENERATE_DOCS:BOOL=OFF
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1579642545
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/wsjtx
cp %{_builddir}/wsjtx-2.1.2/COPYING %{buildroot}/usr/share/package-licenses/wsjtx/adb8e66537b20965af9486caf935e5194245b366
pushd clr-build-avx512
%make_install_avx512  || :
popd
pushd clr-build-avx2
%make_install_avx2  || :
popd
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/fcal
/usr/bin/fmeasure
/usr/bin/fmtave
/usr/bin/ft8code
/usr/bin/haswell/avx512_1/fcal
/usr/bin/haswell/avx512_1/fmeasure
/usr/bin/haswell/avx512_1/fmtave
/usr/bin/haswell/avx512_1/ft8code
/usr/bin/haswell/avx512_1/jt4code
/usr/bin/haswell/avx512_1/jt65code
/usr/bin/haswell/avx512_1/jt9
/usr/bin/haswell/avx512_1/jt9code
/usr/bin/haswell/avx512_1/message_aggregator
/usr/bin/haswell/avx512_1/msk144code
/usr/bin/haswell/avx512_1/qra64code
/usr/bin/haswell/avx512_1/qra64sim
/usr/bin/haswell/avx512_1/rigctl-wsjtx
/usr/bin/haswell/avx512_1/rigctlcom-wsjtx
/usr/bin/haswell/avx512_1/rigctld-wsjtx
/usr/bin/haswell/avx512_1/udp_daemon
/usr/bin/haswell/avx512_1/wsjtx
/usr/bin/haswell/avx512_1/wsprd
/usr/bin/haswell/fcal
/usr/bin/haswell/fmeasure
/usr/bin/haswell/fmtave
/usr/bin/haswell/ft8code
/usr/bin/haswell/jt4code
/usr/bin/haswell/jt65code
/usr/bin/haswell/jt9
/usr/bin/haswell/jt9code
/usr/bin/haswell/message_aggregator
/usr/bin/haswell/msk144code
/usr/bin/haswell/qra64code
/usr/bin/haswell/qra64sim
/usr/bin/haswell/rigctl-wsjtx
/usr/bin/haswell/rigctlcom-wsjtx
/usr/bin/haswell/rigctld-wsjtx
/usr/bin/haswell/udp_daemon
/usr/bin/haswell/wsjtx
/usr/bin/haswell/wsprd
/usr/bin/jt4code
/usr/bin/jt65code
/usr/bin/jt9
/usr/bin/jt9code
/usr/bin/message_aggregator
/usr/bin/msk144code
/usr/bin/qra64code
/usr/bin/qra64sim
/usr/bin/rigctl-wsjtx
/usr/bin/rigctlcom-wsjtx
/usr/bin/rigctld-wsjtx
/usr/bin/udp_daemon
/usr/bin/wsjtx
/usr/bin/wsprd

%files data
%defattr(-,root,root,-)
/usr/share/applications/message_aggregator.desktop
/usr/share/applications/wsjtx.desktop
/usr/share/pixmaps/wsjtx_icon.png
/usr/share/wsjtx/JPLEPH

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/WSJT-X/AUTHORS
/usr/share/doc/WSJT-X/BUGS
/usr/share/doc/WSJT-X/COPYING
/usr/share/doc/WSJT-X/INSTALL
/usr/share/doc/WSJT-X/NEWS
/usr/share/doc/WSJT-X/README
/usr/share/doc/WSJT-X/THANKS
/usr/share/doc/WSJT-X/changelog.Debian.gz
/usr/share/doc/WSJT-X/copyright

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/wsjtx/adb8e66537b20965af9486caf935e5194245b366

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/jt4code.1.gz
/usr/share/man/man1/jt65code.1.gz
/usr/share/man/man1/jt9.1.gz
/usr/share/man/man1/jt9code.1.gz
/usr/share/man/man1/message_aggregator.1.gz
/usr/share/man/man1/rigctl-wsjtx.1.gz
/usr/share/man/man1/rigctlcom-wsjtx.1.gz
/usr/share/man/man1/rigctld-wsjtx.1.gz
/usr/share/man/man1/udp_daemon.1.gz
/usr/share/man/man1/wsjtx.1.gz
/usr/share/man/man1/wsprd.1.gz
