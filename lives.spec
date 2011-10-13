Name:           lives
Version:        1.4.6
Release:        1%{?dist}.R
Summary:        LiVES is a Video Editing System

License:        GPLv3
URL:            http://lives.sourceforge.net/
Source0:        http://www.xs4all.nl/~salsaman/lives/current/LiVES-%{version}.tar.bz2

BuildRequires:  gtk2-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  SDL-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  ffmpeg-devel
BuildRequires:  libunicap-devel
BuildRequires:  mjpegtools-devel
BuildRequires:  libdv-devel
BuildRequires:  libavc1394-devel
BuildRequires:  libv4l-devel
BuildRequires:  frei0r-devel
BuildRequires:  liboil-devel
BuildRequires:  libvisual-devel
BuildRequires:  doxygen
BuildRequires:  chrpath
BuildRequires:  bison
BuildRequires:  libtheora-devel
BuildRequires:  libvorbis-devel

Requires: mplayer
Requires: mencoder
Requires: sox
Requires: ImageMagick

%description
LiVES began in 2002 as the Linux Video Editing System.
Since it now runs on more operating systems: LiVES is a Video Editing System.
It is designed to be simple to use, yet powerful.
It is small in size, yet it has many advanced features.

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_bindir}/%{name}
%find_lang %{name}
cd $RPM_BUILD_ROOT/%{_bindir}/
ln -s %{name}-exe %{name}
find $RPM_BUILD_ROOT -name "*" -exec chrpath --delete {} \; 2>/dev/null


%files -f %{name}.lang
%{_bindir}/*%{name}*
%{_bindir}/midistart
%{_bindir}/midistop
%{_bindir}/sendOSC
%{_bindir}/smogrify
%{_libdir}/libweed*
%{_libdir}/%{name}
%{_libdir}/pkgconfig/libweed*
%{_datadir}/applications/LiVES.desktop
#%{_defaultdocdir}/%{name}-%{version}*
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.xpm
%{_includedir}/weed/weed*.h

%doc COPYING README AUTHORS BUGS ChangeLog FEATURES


%changelog
* Tue Sep 29 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 1.4.6-1.R
- Initial release
