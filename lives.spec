Name:           lives
Version:        2.0.3
Release:        1%{?dist}
Summary:        LiVES is a Video Editing System
Summary(ru):    Система видеоредактирования LiVES

License:        GPLv3
URL:            http://lives.sourceforge.net/
Source0:        http://salsaman.home.xs4all.nl/lives/current/LiVES-%{version}.tar.bz2


BuildRequires:  gtk3-devel
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
#BuildRequires:  libvisual-devel
BuildRequires:  doxygen
BuildRequires:  chrpath
BuildRequires:  bison
BuildRequires:  libtheora-devel
BuildRequires:  libvorbis-devel
BuildRequires:  gettext
BuildRequires:  schroedinger-devel
BuildRequires:  x264-devel
BuildRequires:  libpng-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  GLee-devel
BuildRequires:  opencv-devel
BuildRequires:  bzip2-devel
BuildRequires:  ladspa-devel

Requires:   mplayer
Requires:   mencoder
Requires:   sox
Requires:   ImageMagick
Requires:   weed%{?_isa} = %{version}-%{release}
Requires:   ogmtools
Requires:   oggvideotools
Requires:   perl
Requires:   theora-tools
Requires:   youtube-dl

%description
LiVES began in 2002 as the Linux Video Editing System.
Since it now runs on more operating systems: LiVES is a Video Editing System.
It is designed to be simple to use, yet powerful.
It is small in size, yet it has many advanced features.

%package        doc
Summary:        Doc files for LiVES
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description doc
Doc files for LiVES

%package -n weed
Summary:        weed library for LiVES

%description -n weed
Library weed for LiVES

%package -n weed-devel
Summary:        headers for weed library
Requires:       weed%{?_isa} = %{version}-%{release}

%description -n weed-devel
Headers for weed library

%prep
%setup -q


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

find %{buildroot} -name "*" -exec chrpath --delete {} \; 2>/dev/null

find %{buildroot} -name "*.pc" \
    | while read f ;
    do
        sed -i -e "s!libdir=\${exec_prefix}/lib!libdir=\${exec_prefix}/%{_lib}!" "$f" ;
    done

%ifarch x86_64
    mv %{buildroot}/%{_bindir}/lives %{buildroot}/%{_bindir}/lives0
    echo -e "#!/bin/bash\n" > %{buildroot}/%{_bindir}/lives
    echo "export FREI0R_PATH=/usr/lib64/frei0r-1" >> %{buildroot}/%{_bindir}/lives
    echo -e "lives0\n" >> %{buildroot}/%{_bindir}/lives
    chmod +x %{buildroot}/%{_bindir}/lives
%endif
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} ';'


%post -n weed -p /sbin/ldconfig


%postun -n weed -p /sbin/ldconfig


%files -f %{name}.lang
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
%{_datadir}/app-install/icons/%{name}.png

%files doc
%{_defaultdocdir}/%{name}-%{version}
%doc COPYING README AUTHORS BUGS ChangeLog FEATURES

%files -n weed
%{_libdir}/libweed*
%exclude %{_libdir}/libweed*.so

%files -n weed-devel
%{_includedir}/weed
%{_libdir}/pkgconfig/libweed*
%{_libdir}/libweed*.so


%changelog
* Wed Apr 10 2013 Vasiliy N. Glazov <vascom2@gmail.com> - 2.0.3-1.R
- update to 2.0.3

* Mon Apr 08 2013 Vasiliy N. Glazov <vascom2@gmail.com> - 2.0.2-1.R
- update to 2.0.2

* Tue Jan 29 2013 Vasiliy N. Glazov <vascom2@gmail.com> - 1.8.2-1.R
- update to 1.8.2

* Sat Jan 26 2013 Vasiliy N. Glazov <vascom2@gmail.com> - 1.8.1-1.R
- update to 1.8.1

* Tue Dec 18 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 1.8.0-1.R
- update to 1.8.0

* Mon Oct 22 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 1.6.4-1.R
- update to 1.6.4

* Thu Aug 16 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 1.6.3-1.R
- update to 1.6.3

* Mon Jun 25 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 1.6.2-1.R
- update to 1.6.2

* Mon Feb 06 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 1.6.1-1.R
- update to 1.6.1

* Wed Jan 18 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 1.6.0-1.R
- update to 1.6.0

* Fri Dec 09 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 1.4.9-1.R
- Update to 1.4.9

* Mon Nov 20 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 1.4.7-3.R
- Corrected libpath in .pc files

* Mon Oct 17 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 1.4.7-2.R
- Added patch to compile in F16

* Sun Oct 16 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 1.4.7-1.R
- Update to 1.4.7

* Fri Oct 14 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 1.4.6-2.R
- Corrected spec for more robust builds

* Tue Sep 29 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 1.4.6-1.R
- Initial release
