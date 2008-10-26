Summary:	Midi router
Summary(pl.UTF-8):	Router midi
Name:		sfc
Version:	0.016
Release:	1
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://personal.telefonica.terra.es/web/soudfontcombi/%{name}-%{version}.tar.gz
# Source0-md5:	14fc67d9e2b5c922c6b848f9b9960dd5
URL:		http://personal.telefonica.terra.es/web/soudfontcombi/soundfontcombi.html
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf >= 2.58
BuildRequires:	fltk-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sfc (SoundFontCombi) is a midi router oriented to mix the sounds of
your sound devices, up to 8 sounds can be mixed or split, for do that
has 6 midi out ports and 2 midi in ports, up to six different devices
can be used to produce combinations of sounds like some synthesizers.

%description -l pl.UTF-8
Sfc (SoundFontCombi) to router midi do miksowania dźwięku z twoich
urządzeń, osiem ścieżek może być miksowane lub rozdzielone, aby
tego dokonać sfc posiada 6 portów midi out oraz 2 porty in, pozwala
on także na użycie do sześciu różnych urządzeń aby stworzyć
kombinację dźwięku zbliżoną do tej jaką generują syntezatory.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/sfc
%dir %{_datadir}/sfc
%{_datadir}/sfc/*
