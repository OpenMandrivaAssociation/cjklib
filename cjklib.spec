Summary:	Han character library for CJKV languages
Name:		cjklib
Version:	0.3
Release:	%mkrel 2
Group:		Development/Python
License:	LGPLv3+
URL:		http://code.google.com/p/cjklib/
Source0:	http://cjklib.googlecode.com/files/%{name}-%{version}.tar.gz
%py_requires -d
BuildRequires:	python-setuptools
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
