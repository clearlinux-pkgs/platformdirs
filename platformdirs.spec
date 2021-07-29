#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : platformdirs
Version  : 2.2.0
Release  : 6
URL      : https://files.pythonhosted.org/packages/58/cb/ee4234464290e3dee893cf37d1adc87c24ade86ff6fc55f04a9bf9f1ec4f/platformdirs-2.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/58/cb/ee4234464290e3dee893cf37d1adc87c24ade86ff6fc55f04a9bf9f1ec4f/platformdirs-2.2.0.tar.gz
Summary  : A small Python module for determining appropriate platform-specific dirs, e.g. a "user data dir".
Group    : Development/Tools
License  : MIT
Requires: platformdirs-license = %{version}-%{release}
Requires: platformdirs-python = %{version}-%{release}
Requires: platformdirs-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools
BuildRequires : setuptools_scm
BuildRequires : tox
BuildRequires : virtualenv

%description
the problem
===========
.. image:: https://github.com/platformdirs/platformdirs/workflows/Test/badge.svg
:target: https://github.com/platformdirs/platformdirs/actions?query=workflow%3ATest

%package license
Summary: license components for the platformdirs package.
Group: Default

%description license
license components for the platformdirs package.


%package python
Summary: python components for the platformdirs package.
Group: Default
Requires: platformdirs-python3 = %{version}-%{release}

%description python
python components for the platformdirs package.


%package python3
Summary: python3 components for the platformdirs package.
Group: Default
Requires: python3-core
Provides: pypi(platformdirs)

%description python3
python3 components for the platformdirs package.


%prep
%setup -q -n platformdirs-2.2.0
cd %{_builddir}/platformdirs-2.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1627573010
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/platformdirs
cp %{_builddir}/platformdirs-2.2.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/platformdirs/1a628675f3f38f1d4715ebd772a8160a0ea94dd4
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/platformdirs/1a628675f3f38f1d4715ebd772a8160a0ea94dd4

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
