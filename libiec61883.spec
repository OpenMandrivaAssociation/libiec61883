%define	name	libiec61883
%define	version	1.2.0
%define	release	%mkrel 7

%define	major	0
%define	libname	%mklibname iec61883_ %{major}
%define	libnamedev %{libname}-devel

Name:	%name
Version: %version
Release: %release
License: LGPL
Group:	System/Libraries
Source: http://linux1394.org/dl/%{name}-%{version}.tar.gz
URL:	http://linux1394.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libraw1394-devel >= 1.2.0
Summary: Streaming library for IEEE1394

%description 
The libiec61883 library provides an higher level API for streaming DV,
MPEG-2 and audio over IEEE1394.  Based on the libraw1394 isochronous
functionality, this library acts as a filter that accepts DV-frames,
MPEG-2 frames or audio samples from the application and breaks these
down to isochronous packets, which are transmitted using libraw1394.

%package -n %{libname}
Group:	  System/Libraries
Summary:  Streaming library for IEEE1394
Provides: %{name}

%description -n %{libname}
The libiec61883 library provides an higher level API for streaming DV,
MPEG-2 and audio over IEEE1394.  Based on the libraw1394 isochronous
functionality, this library acts as a filter that accepts DV-frames,
MPEG-2 frames or audio samples from the application and breaks these
down to isochronous packets, which are transmitted using libraw1394.

%package -n %{libnamedev}
Summary:  Development libs for libiec61883
Group:    Development/C
Provides: %{name}-devel = %{version}-%{release}
Requires: %{libname} = %{version}

%description -n %{libnamedev}
Development libraries needed to build applications against libiec61883

%package -n %{name}-utils
Summary:  Utilities for use with libiec61883
Group:    Communications
Requires: %{name} = %{version}

%description -n	%{name}-utils
Utilities that make use of iec61883

%prep
%setup -q
perl -pi -e's,noinst,bin,' examples/Makefile.am

%build
autoreconf -i
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README
%{_libdir}/libiec61883.so.%{major}*

%files -n %{libnamedev}
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_libdir}/*a
%{_includedir}/*
%{_libdir}/pkgconfig/libiec61883.pc
%doc examples/*.c

%files utils
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/*/*




%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-5mdv2011.0
+ Revision: 661474
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-4mdv2011.0
+ Revision: 602559
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-3mdv2010.1
+ Revision: 520869
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.2.0-2mdv2010.0
+ Revision: 425567
- rebuild

* Sun Feb 22 2009 Emmanuel Andry <eandry@mandriva.org> 1.2.0-1mdv2009.1
+ Revision: 343905
- New version 1.2.0
- check major

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.1.0-4mdv2009.0
+ Revision: 222887
- rebuild
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Sun Jan 21 2007 Stefan van der Eijk <stefan@mandriva.org> 1.1.0-2mdv2007.0
+ Revision: 111581
- rebuild
- move man pages to utils package

* Sun Jan 21 2007 Stefan van der Eijk <stefan@mandriva.org> 1.1.0-1mdv2007.1
+ Revision: 111416
- fix setup
- add manpages
- 1.1.0 release
- Import libiec61883

* Fri Jan 27 2006 Christiaan Welvaart <cjw@daneel.dyndns.org> 1.1.0-0.20060103.2mdk
- add version to provides for devel package

* Tue Jan 03 2006 Austin Acton <austin@mandriva.org> 1.1.0-0.20060103.1mdk
- 1.1.0 snapshot

* Sun Apr 24 2005 Stefan van der Eijk <stefan@eijk.nu> 1.0.0-1mdk
- initial Mandriva package
- 1.0.0

* Wed Apr 06 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Fixes for building properly on x86_64.

* Tue Mar 29 2005 Jarod Wilson <jarod@wilsonet.com>
- Fixed utils so they build properly

* Sat Feb 26 2005 Jarod Wilson <jarod@wilsonet.com>
- Rolled in utils

* Wed Feb 23 2005 Jarod Wilson <jarod@wilsonet.com>
- Initial build

