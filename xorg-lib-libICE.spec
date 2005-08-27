
#
Summary:	Inter Client Exchange library
Summary(pl):	Biblioteka wymiany miêdzy klientami
Name:		xorg-lib-libICE
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/lib/libICE-%{version}.tar.bz2
# Source0-md5:	91ba0aa9ccfbff49f001fb49a73142b8
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-util-util-macros
BuildRequires:	xorg-lib-xtrans-devel
Obsoletes:	libICE
BuildRoot:	%{tmpdir}/libICE-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Inter Client Exchange library.

%description -l pl
Biblioteka wymiany miêdzy klientami.


%package devel
Summary:	Header files libICE development
Summary(pl):	Pliki nag³ówkowe do biblioteki libICE
Group:		X11/Development/Libraries
Requires:	xorg-lib-libICE = %{version}-%{release}
Requires:	xorg-proto-xproto-devel
Obsoletes:	libICE-devel

%description devel
Inter Client Exchange library.

This package contains the header files needed to develop programs that
use these libICE.

%description devel -l pl
Biblioteka wymiany miêdzy klientami.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libICE.


%package static
Summary:	Static libICE libraries
Summary(pl):	Biblioteki statyczne libICE
Group:		Development/Libraries
Requires:	xorg-lib-libICE-devel = %{version}-%{release}
Obsoletes:	libICE-static

%description static
Inter Client Exchange library.

This package contains the static libICE library.

%description static -l pl
Biblioteka wymiany miêdzy klientami.

Pakiet zawiera statyczn± bibliotekê libICE.


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
%doc AUTHORS ChangeLog
%attr(755,root,wheel) %{_libdir}/libICE.so.*


%files devel
%defattr(644,root,root,755)
%{_includedir}/X11/ICE/*.h
%{_libdir}/libICE.la
%attr(755,root,wheel) %{_libdir}/libICE.so
%{_pkgconfigdir}/ice.pc


%files static
%defattr(644,root,root,755)
%{_libdir}/libICE.a
