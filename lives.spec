Name:           lives
Version:        1.4.7
Release:        2%{?dist}.R
Summary:        LiVES is a Video Editing System

License:        GPLv3
URL:            http://lives.sourceforge.net/
Source0:        http://salsaman.home.xs4all.nl/lives/current/LiVES-%{version}.tar.bz2
Patch1:         lives-compile.patch

BuildRoot:      /{name}-%{version}-%{release}-root-%(%{__id_u} -n)

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
BuildRequires:  gettext

Requires: mplayer
Requires: mencoder
Requires: sox
Requires: ImageMagick
Requires: weed

%description
LiVES began in 2002 as the Linux Video Editing System.
Since it now runs on more operating systems: LiVES is a Video Editing System.
It is designed to be simple to use, yet powerful.
It is small in size, yet it has many advanced features.

%package        doc
Summary:        Doc files for LiVES
Requires:       %{name} = %{version}

%description doc
Doc files for LiVES

%package -n weed
Summary:        weed library for LiVES

%description -n weed
weed library for LiVES

%package -n weed-devel
Summary:        headers for weed library
Requires:       weed = %{version}

%description -n weed-devel
headers for weed library

%prep
%setup -q
%patch1 -p1 -b .codec_media


%build
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm %{buildroot}/%{_bindir}/%{name}
%find_lang %{name}
cd %{buildroot}/%{_bindir}/
ln -s %{name}-exe %{name}

find %{buildroot} -name "*.a" -delete
find %{buildroot} -name "*.la" -delete
find %{buildroot} -name "*" -exec chrpath --delete {} \; 2>/dev/null


%clean
rm -rf %{buildroot}


%post -n weed -p /sbin/ldconfig


%postun -n weed -p /sbin/ldconfig


%files -f %{name}.lang
%defattr(-, root, root, -)
%{_bindir}/*%{name}*
%{_bindir}/midistart
%{_bindir}/midistop
%{_bindir}/sendOSC
%{_bindir}/smogrify
%{_libdir}/%{name}
%{_datadir}/applications/LiVES.desktop
%{_datadir}/%{name}
%exclude %{_defaultdocdir}/%{name}-%{version}
%{_datadir}/pixmaps/%{name}.xpm

%files doc
%defattr(-, root, root, -)
%{_defaultdocdir}/%{name}-%{version}
%doc COPYING README AUTHORS BUGS ChangeLog FEATURES

%files -n weed
%defattr(-, root, root, -)
%{_libdir}/libweed*
%exclude %{_libdir}/libweed*.so

%files -n weed-devel
%defattr(-, root, root, -)
%{_includedir}/weed
%{_libdir}/pkgconfig/libweed*
%{_libdir}/libweed*.so

%changelog
* Mon Oct 17 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 1.4.7-2.R
- Added patch to compile in F16

* Sun Oct 16 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 1.4.7-1.R
- Update to 1.4.7

* Fri Oct 14 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 1.4.6-2.R
- Corrected spec for more robust builds

* Tue Sep 29 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 1.4.6-1.R
- Initial release
