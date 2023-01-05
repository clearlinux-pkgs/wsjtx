#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : wsjtx
Version  : 2.5.4
Release  : 28
URL      : https://sourceforge.net/projects/wsjt/files/wsjtx-2.5.4/wsjtx-2.5.4.tgz
Source0  : https://sourceforge.net/projects/wsjt/files/wsjtx-2.5.4/wsjtx-2.5.4.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: wsjtx-bin = %{version}-%{release}
Requires: wsjtx-data = %{version}-%{release}
Requires: wsjtx-filemap = %{version}-%{release}
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
Requires: wsjtx-filemap = %{version}-%{release}

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


%package filemap
Summary: filemap components for the wsjtx package.
Group: Default

%description filemap
filemap components for the wsjtx package.


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
%setup -q -n wsjtx-2.5.4
cd %{_builddir}/wsjtx-2.5.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672888027
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake .. -DWSJT_GENERATE_DOCS:BOOL=OFF
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake .. -DWSJT_GENERATE_DOCS:BOOL=OFF
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx512
pushd clr-build-avx512
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v4 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz -march=x86_64-v4 -mprefer-vector-width=512 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v4 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz -march=x86_64-v4 -mprefer-vector-width=512 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v4 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz -march=x86_64-v4 -mprefer-vector-width=512 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v4 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz -march=x86_64-v4 -mprefer-vector-width=512 "
export CFLAGS="$CFLAGS -march=x86-64-v4 -m64 -Wl,-z,x86-64-v4 -mprefer-vector-width=512"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v4 -m64 -Wl,-z,x86-64-v4 -mprefer-vector-width=512"
export FFLAGS="$FFLAGS -march=x86-64-v4 -m64 -Wl,-z,x86-64-v4 -mprefer-vector-width=512"
export FCFLAGS="$FCFLAGS -march=x86-64-v4 -m64 "
%cmake .. -DWSJT_GENERATE_DOCS:BOOL=OFF
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1672888027
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/wsjtx
cp %{_builddir}/wsjtx-%{version}/COPYING %{buildroot}/usr/share/package-licenses/wsjtx/adb8e66537b20965af9486caf935e5194245b366 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build-avx512
%make_install_v4  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/fcal
/usr/bin/fmeasure
/usr/bin/fmtave
/usr/bin/fst4sim
/usr/bin/ft8code
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
/usr/share/clear/optimized-elf/bin*

%files data
%defattr(-,root,root,-)
/usr/share/applications/message_aggregator.desktop
/usr/share/applications/wsjtx.desktop
/usr/share/pixmaps/wsjtx_icon.png
/usr/share/wsjtx/JPLEPH
/usr/share/wsjtx/cty.dat
/usr/share/wsjtx/cty.dat_copyright.txt

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/wsjtx/*

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-wsjtx

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
