# $Id$
# Authority: dag
# Upstream: Charles Cazabon <software@discworld.dyndns.org>

Summary: Userspace utility for testing the memory subsystem for faults
Name: memtester
Version: 4.0.5
Release: 1
License: GPL
Group: System Environment/Base
URL: http://pyropus.ca/software/memtester/

Source: http://pyropus.ca/software/memtester/memtester-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
memtester is a userspace utility for testing the memory subsystem for faults.

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 memtester %{buildroot}%{_bindir}/memtester
%{__install} -Dp -m0644 memtester.8 %{buildroot}%{_mandir}/man8/memtester.8

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS CHANGELOG COPYING README*
%doc %{_mandir}/man8/memtester.8*
%{_bindir}/memtester

%changelog
* Tue Mar 15 2005 Dag Wieers <dag@wieers.com> - 4.0.5-1
- Updated to release 4.0.5.

* Fri Aug 27 2004 Dag Wieers <dag@wieers.com> - 4.0.4-1
- Updated to release 4.0.4.

* Thu Aug 19 2004 Dag Wieers <dag@wieers.com> - 4.0.3-1
- Initial package. (using DAR)
