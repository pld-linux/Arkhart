Summary:	Arkhart - A multiplayer roleplaying game.
Summary(pl):	Arkhart - wieloosobowa gra fabularna.
Name:		Arkhart
Version:	0.1.3
Release:	1
License:	GPL
Group:		Games
Source0:	http://arkhart.nekeme.net/download/releases/ark-%{version}.tar.gz
Source1:	http://arkhart.nekeme.net/download/releases/Arkhart-data-%{version}.tar.gz
Source2:	http://arkhart.nekeme.net/download/releases/worlded-%{version}.tar.gz
URL:		http://arkhart.nekeme.net/en/?name=Home
#Patch0:		
BuildRequires:	lua40-devel >= 4.0.1
BuildRequires:	SDL_mixer-devel
BuildRequires:	zlib-devel
BuildRequires:	libpng-devel
BuildRequires:	libjpeg-devel
#BuildRequires:	-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%package data
Summary:	Arkhart data
Summary(pl):	Dane dla gry Arkhart
Group:		Games
%description data
%description -l pl data

%package server
Summary:	Arkhart server
Summary(pl):	Serwer gry Arkhart
Group:		Games
Requires:	%{name}
%description server
%description -l pl server

%package client
Summary:	Arkhart client
Summary(pl):	Klient gry Arkhart
Group:		Games
Requires:	%{name}
%description client
%description -l pl client

%package devel
Summary:	Arkhart program library headers
Summary(pl):	Pliki naglowkowe gry Arkhart
Group:		Games
%description devel
%description -l pl devel

%package static
Summary:	Static library for Arjhart games
Summary(pl):	Biblioteki statyczne dla gry Arkhart
Group:		Games
%description static
%description -l pl static

%package WorldEd
Summary:	Arkhart World editor
Summary(pl):	Edytor swiatow dla gry Arkhart
Group:		Games
%description WorldEd
%description -l pl WorldEd

%prep
%setup -q -n Ark
#%patch0 -p0

%build
./configure \
	--with-lua-lib=/usr/lib \
	--with-lua-inc=/usr/include \
	--with-gl-libs=/usr/X11R6/lib \
	--with-gl-inc=/usr/X11R6/include

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT prefix=/usr install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ark-config
%attr(755,root,root) %{_bindir}/widgettest
%attr(644,root,root) %{_libdir}/libArk*.so.*.*.*
%attr(644,root,root) %{_libdir}/libArk*.la

%files client
%attr(755,root,root) %{_bindir}/arkclient

%files data

%files devel
%attr(644,root,root) %{_includedir}/Ark/*

%files static
%attr(644,root,root) %{_libdir}/*.a

%files WorldEd

%files server
%attr(755,root,root) %{_bindir}/arkhartd
