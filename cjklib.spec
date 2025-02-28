Summary:	Han character library for CJKV languages
Name:		cjklib
Version:	0.3
Release:	5
Group:		Development/Python
License:	LGPLv3+
URL:		https://code.google.com/p/cjklib/
Source0:	http://cjklib.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:	python-setuptools
Requires:	python-pkg-resources
Requires:	python-sqlalchemy >= 0.4.8
BuildArch:	noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-buildroot

%description
Cjklib provides language routines related to Han characters (characters
based on Chinese characters named Hanzi, Kanji, Hanja and chu Han
respectively) used in writing of the Chinese, the Japanese, infrequently
the Korean and formerly the Vietnamese language(s). Functionality is
included for character pronunciations, radicals, glyph components, stroke
decomposition and variant information. Cjklib is implemented in Python.

%prep
%setup -qn %{name}-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root=%{buildroot} --optimize=2
 
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING README TODO examples
%{_bindir}/*
%{python_sitelib}/*


%changelog
* Mon Nov 01 2010 Funda Wang <fwang@mandriva.org> 0.3-4mdv2011.0
+ Revision: 591552
- add requires

* Sun Oct 31 2010 Funda Wang <fwang@mandriva.org> 0.3-3mdv2011.0
+ Revision: 591062
- add requires

* Sun Oct 31 2010 Funda Wang <fwang@mandriva.org> 0.3-2mdv2011.0
+ Revision: 590789
- rebuild for py2.7

* Sat Oct 02 2010 Funda Wang <fwang@mandriva.org> 0.3-1mdv2011.0
+ Revision: 582464
- update to new version 0.3

* Sat Dec 12 2009 Funda Wang <fwang@mandriva.org> 0.2-1mdv2010.1
+ Revision: 477760
- import cjklib


