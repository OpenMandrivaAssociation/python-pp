%define module	pp

Summary:	Parallel Python

Name:		python-%{module}
Version:	1.6.4
Release:	2
Source0:	http://www.parallelpython.com/downloads/pp/%{module}-%{version}.tar.bz2
License:	BSD-like
Group:		Development/Python
Url:		https://www.parallelpython.com/
BuildArch:	noarch
BuildRequires:  python-devel

%description
Parallel Python (pp) is a pure Python module that provides a parallel
code execution mechanism for SMP or cluster computers. It is lightweight,
easy to install, and integrates well with other Python software.

%prep
%setup -q -n %{module}-%{version}

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}
%__mv %{buildroot}%{_bindir}/ppserver.py %{buildroot}%{_bindir}/ppserver
%__lzma -z doc/ppserver.1
%__install -D -m 644 doc/ppserver.1.lzma %{buildroot}%{_mandir}/man1/ppserver.1.lzma

%clean

%files
%doc COPYING CHANGELOG README examples/
%{_bindir}/*
%{py_puresitedir}/*
%{_mandir}/man1/*


