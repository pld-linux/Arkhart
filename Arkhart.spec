Summary:	Arkhart - A multiplayer roleplaying game.
Summary(pl):	Arkhart - wieloosobowa gra fabularna.
Name:		Arkhart
Version:	20030210
Release:	1
License:	GPL
Group:		Games
Source0:	http://arkhart.nekeme.net/Tmp/Ark.tar.bz2
Source1:	http://arkhart.nekeme.net/Tmp/Arkhart-data.tar.bz2
Source2:	http://arkhart.nemeke.net/Tmp/Worded.tar.bz2
URL:		http://arkhart.nekeme.net/en/?name=Home
#Patch0:		
BuildRequires:	lua40-devel >= 4.0.1
BuildRequires:	SDL_mixer-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%prep
%setup -q -n Ark
#%patch0 -p0

%build
%{__aclocal}
%{__libtoolize}
%{__autoconf}
%configure \
	--with-gl-libs=/usr/X11R6/lib \
	--with-gl-inc=/usr/X11R6/include

#%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {README,COPYING,INSTALL,TODO,ChangeLog,FAQ}.gz tutorial/*
