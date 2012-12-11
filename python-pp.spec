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


%changelog
* Wed Feb 02 2011 Lev Givon <lev@mandriva.org> 1.6.1-1mdv2011.0
+ Revision: 635333
- Update to 1.6.1.

* Sat Nov 06 2010 Funda Wang <fwang@mandriva.org> 1.6.0-2mdv2011.0
+ Revision: 594077
- rebuild

* Mon Jul 12 2010 Lev Givon <lev@mandriva.org> 1.6.0-1mdv2011.0
+ Revision: 551268
- Update to 1.6.0.

* Thu Mar 19 2009 Lev Givon <lev@mandriva.org> 1.5.7-1mdv2009.1
+ Revision: 358156
- Update to 1.5.7.

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 1.5.6-2mdv2009.1
+ Revision: 323926
- rebuild

* Wed Nov 05 2008 Lev Givon <lev@mandriva.org> 1.5.6-1mdv2009.1
+ Revision: 300130
- import python-pp


