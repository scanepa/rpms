# $Id$
# Authority: dag

%define real_version 521e.pl8

Summary: Arc archiver 
Name: arc
Version: 5.21e
Release: 0
License: distributable 
Group: Applications/Archiving
URL: ftp://ftp.freebsd.org/pub/FreeBSD/distfiles/

Source: ftp://ftp.freebsd.org/pub/FreeBSD/distfiles/arc%{real_version}.tar.Z
Patch: arc-5.21e-timeh.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Arc file archiver and compressor. Long since superseded by zip/unzip
but useful if you have old .arc files you need to unpack.

%prep
%setup -c
%patch -p1

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 arc %{buildroot}%{_bindir}/arc
%{__install} -Dp -m0755 marc %{buildroot}%{_bindir}/marc
%{__install} -Dp -m0644 arc.1 %{buildroot}%{_mandir}/man1/arc.1
%{__install} -Dp -m0644 arc.1 %{buildroot}%{_mandir}/man1/marc.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Arc521.doc Arcinfo Changes.521 README
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Sun Jan 26 2003 Dag Wieers <dag@wieers.com>
- Initial package. (using DAR)
