%define module	pp
%define name	python-%{module}
%define version	1.6.1
%define release	%mkrel 1

Summary:	Parallel Python
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{module}-%{version}.tar.bz2
License:	BSD-like
Group:		Development/Python
Url:		http://www.parallelpython.com/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
%py_requires -d

%description
Parallel Python (pp) is a pure Python module that provides a parallel
code execution mechanism for SMP or cluster computers. It is lightweight,
easy to install, and integrates well with other Python software.

%prep
%setup -q -n %{module}-%{version}

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}
%__mv %{buildroot}%{_bindir}/ppserver.py %{buildroot}%{_bindir}/ppserver
%__lzma -z doc/ppserver.1
%__install -D -m 644 doc/ppserver.1.lzma %{buildroot}%{_mandir}/man1/ppserver.1.lzma

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING CHANGELOG README examples/
%_bindir/*
%py_puresitedir/*
%_mandir/man1/*
