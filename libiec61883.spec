%define	major	0
%define	libname	%mklibname iec61883_ %{major}
%define	devname %{libname}-devel

Summary:	Streaming library for IEEE1394
Name:		libiec61883
Version:	1.2.0
Release:	14
License:	LGPLv2
Group:		System/Libraries
Url:		http://linux1394.org
Source0:	http://linux1394.org/dl/%{name}-%{version}.tar.gz
Patch0:		libiec61883-automake-1.13.patch
BuildRequires:	pkgconfig(libraw1394) >= 1.2.0

%description 
The libiec61883 library provides an higher level API for streaming DV,
MPEG-2 and audio over IEEE1394.  Based on the libraw1394 isochronous
functionality, this library acts as a filter that accepts DV-frames,
MPEG-2 frames or audio samples from the application and breaks these
down to isochronous packets, which are transmitted using libraw1394.

%package -n %{libname}
Group:		System/Libraries
Summary:	Streaming library for IEEE1394
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
The libiec61883 library provides an higher level API for streaming DV,
MPEG-2 and audio over IEEE1394.  Based on the libraw1394 isochronous
functionality, this library acts as a filter that accepts DV-frames,
MPEG-2 frames or audio samples from the application and breaks these
down to isochronous packets, which are transmitted using libraw1394.

%package -n %{devname}
Summary:	Development libs for libiec61883
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
Development libraries needed to build applications against libiec61883

%package -n %{name}-utils
Summary:	Utilities for use with libiec61883
Group:		Communications

%description -n	%{name}-utils
Utilities that make use of iec61883

%prep
%setup -q
%apply_patches
sed -i -e's,noinst,bin,' examples/Makefile.am
autoreconf -fi

%build
%configure2_5x \
	--disable-static
%make

%install
%makeinstall

%files -n %{libname}
%{_libdir}/libiec61883.so.%{major}*

%files -n %{devname}
%doc AUTHORS COPYING NEWS README
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/libiec61883.pc
%doc examples/*.c

%files utils
%{_bindir}/*
%{_mandir}/*/*

