Summary:	Arkhart - A multiplayer roleplaying game
Summary(pl):	Arkhart - wieloosobowa gra fabularna
Name:		Arkhart
Version:	0.1.3
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://arkhart.nekeme.net/download/releases/ark-%{version}.tar.gz
Source1:	http://arkhart.nekeme.net/download/releases/Arkhart-data-%{version}.tar.gz
Source2:	http://arkhart.nekeme.net/download/releases/worlded-%{version}.tar.gz
URL:		http://arkhart.nekeme.net/en/?name=Home
BuildRequires:	SDL_mixer-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	lua40-devel >= 4.0.1
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Arkhart - A multiplayer roleplaying game.

%description -l pl
Arkhart - wieloosobowa gra fabularna.

%package data
Summary:	Arkhart data
Summary(pl):	Dane dla gry Arkhart
Group:		Applications/Games

%description data
Arkhart data.

%description data -l pl
Dane dla gry Arkhart.

%package server
Summary:	Arkhart server
Summary(pl):	Serwer gry Arkhart
Group:		Applications/Games
Requires:	%{name} = %{version}

%description server
Arkhart server.

%description server -l pl
Serwer gry Arkhart.

%package client
Summary:	Arkhart client
Summary(pl):	Klient gry Arkhart
Group:		Applications/Games
Requires:	%{name} = %{version}

%description client
Arkhart client.

%description client -l pl
Klient gry Arkhart.

%package devel
Summary:	Arkhart program library headers
Summary(pl):	Pliki nag��wkowe gry Arkhart
Group:		Development/Libraries

%description devel
Arkhart program library headers.

%description devel -l pl
Pliki nag��wkowe gry Arkhart.

%package static
Summary:	Static library for Arkhart games
Summary(pl):	Biblioteki statyczne dla gry Arkhart
Group:		Development/Libraries

%description static
Static library for Arkhart games.

%description static -l pl
Biblioteki statyczne dla gry Arkhart.

%package WorldEd
Summary:	Arkhart World editor
Summary(pl):	Edytor �wiat�w dla gry Arkhart
Group:		Applications/Games

%description WorldEd
Arkhart World editor.

%description WorldEd -l pl
Edytor �wiat�w dla gry Arkhart.

%prep
%setup -q -n ark-%{version}

%build
CPPFLAGS="-I/usr/X11R6/include"
LDFLAGS="%{rpmldflags} -L/usr/X11R6/lib"
%configure2_13 \
	--with-lua-lib=/usr/lib \
	--with-lua-inc=/usr/include \
	--with-gl-libs=/usr/X11R6/lib \
	--with-gl-inc=/usr/X11R6/include

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files 
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/widgettest
%attr(755,root,root) %{_libdir}/libArk*.so.*.*.*

%files client
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/arkclient

#%files data

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ark-config
%attr(755,root,root) %{_libdir}/libArk*.so
%{_libdir}/libArk*.la
%{_includedir}/Ark

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

#%files WorldEd

%files server
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/arkhartd
