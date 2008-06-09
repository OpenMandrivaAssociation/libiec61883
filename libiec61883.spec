%define	name	libiec61883
%define	version	1.1.0
%define	release	%mkrel 3

%define	major	0
%define	libname	%mklibname iec61883_ %{major}
%define	libnamedev %{libname}-devel

Name:	%name
Version: %version
Release: %release
License: LGPL
Group:	System/Libraries
Source: http://linux1394.org/dl/%{name}-%{version}.tar.bz2
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
%{_libdir}/libiec61883.so.*

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


