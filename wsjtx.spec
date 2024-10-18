#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v20
# autospec commit: b2d28bb55a98
#
Name     : wsjtx
Version  : 2.7.0.rc7
Release  : 36
URL      : https://sourceforge.net/projects/wsjt/files/wsjtx-2.7.0-rc7/wsjtx-2.7.0-rc7.tgz
Source0  : https://sourceforge.net/projects/wsjt/files/wsjtx-2.7.0-rc7/wsjtx-2.7.0-rc7.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: wsjtx-bin = %{version}-%{release}
Requires: wsjtx-data = %{version}-%{release}
Requires: wsjtx-license = %{version}-%{release}
Requires: wsjtx-man = %{version}-%{release}
BuildRequires : asciidoc
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : pkgconfig(Qt5Multimedia)
BuildRequires : pkgconfig(Qt5SerialPort)
BuildRequires : pkgconfig(fftw3)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(libusb-1.0)
BuildRequires : pkgconfig(portaudio-2.0)
BuildRequires : qttools-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n wsjtx-2.7.0
cd %{_builddir}/wsjtx-2.7.0
pushd ..
cp -a wsjtx-2.7.0 buildavx2
popd
pushd ..
cp -a wsjtx-2.7.0 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1729274517
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DWSJT_GENERATE_DOCS:BOOL=OFF  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DWSJT_GENERATE_DOCS:BOOL=OFF  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd
pushd ../buildavx512/
mkdir -p clr-build-avx512
pushd clr-build-avx512
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v4
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -Wl,-z,x86-64-v4 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -Wl,-z,x86-64-v4 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -Wl,-z,x86-64-v4 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v4 -mprefer-vector-width=512 "
%cmake .. -DWSJT_GENERATE_DOCS:BOOL=OFF  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1729274517
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/wsjtx
cp %{_builddir}/wsjtx-2.7.0/COPYING %{buildroot}/usr/share/package-licenses/wsjtx/adb8e66537b20965af9486caf935e5194245b366 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
pushd ../buildavx512/
GOAMD64=v4
pushd clr-build-avx512
%make_install_v4  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/cablog
/V3/usr/bin/echosim
/V3/usr/bin/fcal
/V3/usr/bin/fmeasure
/V3/usr/bin/fmtave
/V3/usr/bin/fst4sim
/V3/usr/bin/ft8code
/V3/usr/bin/hash22calc
/V3/usr/bin/jt4code
/V3/usr/bin/jt65code
/V3/usr/bin/jt9
/V3/usr/bin/jt9code
/V3/usr/bin/message_aggregator
/V3/usr/bin/msk144code
/V3/usr/bin/q65code
/V3/usr/bin/q65sim
/V3/usr/bin/rigctl-wsjtx
/V3/usr/bin/rigctlcom-wsjtx
/V3/usr/bin/rigctld-wsjtx
/V3/usr/bin/udp_daemon
/V3/usr/bin/wsjtx
/V3/usr/bin/wsjtx_app_version
/V3/usr/bin/wsprd
/V4/usr/bin/cablog
/V4/usr/bin/echosim
/V4/usr/bin/fcal
/V4/usr/bin/fmeasure
/V4/usr/bin/fmtave
/V4/usr/bin/fst4sim
/V4/usr/bin/ft8code
/V4/usr/bin/hash22calc
/V4/usr/bin/jt4code
/V4/usr/bin/jt65code
/V4/usr/bin/jt9
/V4/usr/bin/jt9code
/V4/usr/bin/message_aggregator
/V4/usr/bin/msk144code
/V4/usr/bin/q65code
/V4/usr/bin/q65sim
/V4/usr/bin/rigctl-wsjtx
/V4/usr/bin/rigctlcom-wsjtx
/V4/usr/bin/rigctld-wsjtx
/V4/usr/bin/udp_daemon
/V4/usr/bin/wsjtx
/V4/usr/bin/wsjtx_app_version
/V4/usr/bin/wsprd
/usr/bin/cablog
/usr/bin/echosim
/usr/bin/fcal
/usr/bin/fmeasure
/usr/bin/fmtave
/usr/bin/fst4sim
/usr/bin/ft8code
/usr/bin/hash22calc
/usr/bin/jt4code
/usr/bin/jt65code
/usr/bin/jt9
/usr/bin/jt9code
/usr/bin/message_aggregator
/usr/bin/msk144code
/usr/bin/q65code
/usr/bin/q65sim
/usr/bin/rigctl-wsjtx
/usr/bin/rigctlcom-wsjtx
/usr/bin/rigctld-wsjtx
/usr/bin/udp_daemon
/usr/bin/wsjtx
/usr/bin/wsjtx_app_version
/usr/bin/wsprd

%files data
%defattr(-,root,root,-)
/usr/share/applications/message_aggregator.desktop
/usr/share/applications/wsjtx.desktop
/usr/share/pixmaps/wsjtx_icon.png
/usr/share/wsjtx/JPLEPH
/usr/share/wsjtx/cty.dat
/usr/share/wsjtx/cty.dat_copyright.txt
/usr/share/wsjtx/eclipse.txt

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/wsjtx/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/wsjtx/adb8e66537b20965af9486caf935e5194245b366

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/fcal.1.gz
/usr/share/man/man1/fmeasure.1.gz
/usr/share/man/man1/fmtave.1.gz
/usr/share/man/man1/fst4sim.1.gz
/usr/share/man/man1/ft8code.1.gz
/usr/share/man/man1/jt4code.1.gz
/usr/share/man/man1/jt65code.1.gz
/usr/share/man/man1/jt9.1.gz
/usr/share/man/man1/jt9code.1.gz
/usr/share/man/man1/message_aggregator.1.gz
/usr/share/man/man1/msk144code.1.gz
/usr/share/man/man1/qra64code.1.gz
/usr/share/man/man1/qra64sim.1.gz
/usr/share/man/man1/rigctl-wsjtx.1.gz
/usr/share/man/man1/rigctlcom-wsjtx.1.gz
/usr/share/man/man1/rigctld-wsjtx.1.gz
/usr/share/man/man1/udp_daemon.1.gz
/usr/share/man/man1/wsjtx.1.gz
/usr/share/man/man1/wsprd.1.gz
