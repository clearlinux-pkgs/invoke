#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x9C29BC560041E930 (jeff@bitprophet.org)
#
Name     : invoke
Version  : 1.4.1
Release  : 9
URL      : https://files.pythonhosted.org/packages/b6/08/b345475cfaaa542ae78a172d5b23979ad0577f15a32b16e5e54b2a7e80c6/invoke-1.4.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/b6/08/b345475cfaaa542ae78a172d5b23979ad0577f15a32b16e5e54b2a7e80c6/invoke-1.4.1.tar.gz
Source1  : https://files.pythonhosted.org/packages/b6/08/b345475cfaaa542ae78a172d5b23979ad0577f15a32b16e5e54b2a7e80c6/invoke-1.4.1.tar.gz.asc
Summary  : Pythonic task execution
Group    : Development/Tools
License  : BSD-2-Clause
Requires: invoke-bin = %{version}-%{release}
Requires: invoke-license = %{version}-%{release}
Requires: invoke-python = %{version}-%{release}
Requires: invoke-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
To find out what's new in this version of Invoke, please see `the changelog

%package bin
Summary: bin components for the invoke package.
Group: Binaries
Requires: invoke-license = %{version}-%{release}

%description bin
bin components for the invoke package.


%package license
Summary: license components for the invoke package.
Group: Default

%description license
license components for the invoke package.


%package python
Summary: python components for the invoke package.
Group: Default
Requires: invoke-python3 = %{version}-%{release}

%description python
python components for the invoke package.


%package python3
Summary: python3 components for the invoke package.
Group: Default
Requires: python3-core
Provides: pypi(invoke)

%description python3
python3 components for the invoke package.


%prep
%setup -q -n invoke-1.4.1
cd %{_builddir}/invoke-1.4.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588884625
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/invoke
cp %{_builddir}/invoke-1.4.1/LICENSE %{buildroot}/usr/share/package-licenses/invoke/eadf0675261da2116b63962716fbf09f4cb946ca
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/inv
/usr/bin/invoke

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/invoke/eadf0675261da2116b63962716fbf09f4cb946ca

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
