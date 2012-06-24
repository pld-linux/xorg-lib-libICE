Summary:	Inter Client Exchange library
Summary(pl.UTF-8):	Biblioteka wymiany między klientami
Name:		xorg-lib-libICE
Version:	1.0.4
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libICE-%{version}.tar.bz2
# Source0-md5:	4ab4e67e0b8845aa201e984153087f4a
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-xtrans-devel
BuildRequires:	xorg-util-util-macros
Obsoletes:	libICE
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inter Client Exchange library.

%description -l pl.UTF-8
Biblioteka wymiany między klientami.

%package devel
Summary:	Header files for libICE library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libICE
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-proto-xproto-devel
Obsoletes:	libICE-devel

%description devel
Inter Client Exchange library.

This package contains the header files needed to develop programs that
use libICE.

%description devel -l pl.UTF-8
Biblioteka wymiany między klientami.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libICE.

%package static
Summary:	Static libICE library
Summary(pl.UTF-8):	Biblioteka statyczna libICE
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libICE-static

%description static
Inter Client Exchange library.

This package contains the static libICE library.

%description static -l pl.UTF-8
Biblioteka wymiany między klientami.

Pakiet zawiera statyczną bibliotekę libICE.

%prep
%setup -q -n libICE-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %{_libdir}/libICE.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libICE.so
%{_libdir}/libICE.la
%dir %{_includedir}/X11/ICE
%{_includedir}/X11/ICE/*.h
%{_pkgconfigdir}/ice.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libICE.a
