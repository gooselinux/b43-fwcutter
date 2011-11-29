Name:           b43-fwcutter
Version:        012
Release:        2.2%{?dist}
Summary:        Firmware extraction tool for Broadcom wireless driver

Group:          System Environment/Base
License:        BSD
URL:            http://bu3sch.de/b43/fwcutter/
Source0:        http://bu3sch.de/b43/fwcutter/%{name}-%{version}.tar.bz2
Source1:        README.Fedora
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Patch1:		0001-fwcutter-mklist.py-Update-to-new-library-and-skip-so.patch
Patch2:		0002-fwcutter-Add-two-new-sources-for-478.104-firmware.patch
Patch3:		0003-fwcutter-Use-ARRAY_SIZE.patch
Patch4:         b43-fwcutter-add-COPYING-file.patch

%description
This package contains the 'b43-fwcutter' tool which is used to
extract firmware for the Broadcom network devices.

See the README.Fedora file shipped in the package's documentation for
instructions on using this tool.

%prep
%setup -q
%patch1 -p2
%patch2 -p2
%patch3 -p2

# Add COPYING file
%patch4 -p2

cp %{SOURCE1} .

%build
CFLAGS="$RPM_OPT_FLAGS" make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m0755 b43-fwcutter $RPM_BUILD_ROOT%{_bindir}/b43-fwcutter
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m0644 b43-fwcutter.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/b43-fwcutter
%{_mandir}/man1/*
%doc COPYING README README.Fedora

%changelog
* Tue Jul 27 2010 John W. Linville <linville@redhat.com> 012-2.2
- Add COPYING file

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 012-2.1
- Rebuilt for RHEL 6

* Fri Aug 28 2009 Bill Nottingham <notting@redhat.com> 012-2
- Update with some patches from git

* Mon Aug 24 2009 John W. Linville <linville@redhat.com> 012-1
- Update for b43-fwcutter-012

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 011-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May  7 2009 Ville Skyttä <ville.skytta at iki.fi> - 011-5
- Build with $RPM_OPT_FLAGS.

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 011-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 15 2008 John W. Linville <linville@redhat.com> 011-3
- Update for b43-fwcutter-011

* Mon Jan 21 2008 John W. Linville <linville@redhat.com> 010-2
- Update for b43-fwcutter-010

* Thu Aug 23 2007 John W. Linville <linville@redhat.com> 008-1
- Import skeleton from bcm43xx-fwcutter-006-3
- Initial build
