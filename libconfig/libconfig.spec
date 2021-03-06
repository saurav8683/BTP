Name:		libconfig
Version:	1.4.10
Release:	1
Summary:	C/C++ Configuration File Library

Group:		System Environment/Libraries
License:	LGPL
URL:		http://hyperrealm.com/main.php?s=libconfig
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id} -u -n)

Packager:	Deneys S. Maartens  <dsm@tlabs.ac.za>

BuildRequires:	texinfo

%description
%{name} is a simple library for processing structured configuration
files. The file format is more compact and more readable than XML. And
unlike XML, it is type-aware, so it is not necessary to do string
parsing in application code. The library includes bindings for both
the C and C++ languages. It works on POSIX-compliant UNIX systems.

%package devel
Summary:	%{name} development package
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Development files for %{name}.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}
make html

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
ldconfig

%postun
ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING.LIB ChangeLog INSTALL NEWS README
%{_libdir}/%{name}.so*
%{_libdir}/%{name}++.so*

%files devel
%defattr(-,root,root,-)
%doc AUTHORS COPYING.LIB ChangeLog INSTALL NEWS README
%doc doc/%{name}.html
%doc test.cfg
%doc examples/c/*.c
%doc examples/c++/*.cpp
%{_infodir}
%{_includedir}
%{_libdir}/pkgconfig
%{_libdir}/%{name}.a
%{_libdir}/%{name}.la
%{_libdir}/%{name}++.a
%{_libdir}/%{name}++.la

%changelog
* Wed Aug 19 2007  Deneys S. Maartens  <dsm@tlabs.ac.za>  1.1.3-1
- create spec file

# -fin-
