Name:           lives
Version:        2.4.1
Release:        1%{?dist}
Summary:        LiVES is a Video Editing System
Summary(ru):    Система видеоредактирования LiVES

License:        GPLv3
URL:            http://lives-video.com
Source0:        http://lives-video.com/releases/LiVES-%{version}.tar.bz2

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
BuildRequires:  fftw-devel
BuildRequires:  ffmpeg

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
Requires:   dvgrab
Requires:   icedax

%description
LiVES began in 2002 as the Linux Video Editing System.
Since it now runs on more operating systems: LiVES is a Video Editing System.
It is designed to be simple to use, yet powerful.
It is small in size, yet it has many advanced features.

%package devel
Summary:        headers for lives OSC library
Requires:       lives%{?_isa} = %{version}-%{release}

%description devel
Headers for lives OSC library

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

#Trivial patch for gtk3 >= 3.16.0
# sed -i 's/gtk_label_set_y_align/gtk_label_set_yalign/' src/widget-helper.c
#Workaround for GCC 5
# sed -i 's/LIVES_INLINE//' src/cvirtual.c


%build
%configure
make %{?_smp_mflags}


%install
mkdir -p %{buildroot}%{_bindir}
%make_install
rm %{buildroot}%{_bindir}/%{name}
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
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post -n weed -p /sbin/ldconfig

%postun -n weed -p /sbin/ldconfig


%files -f %{name}.lang
%{_bindir}/*%{name}*
%{_bindir}/midistart
%{_bindir}/midistop
%{_bindir}/sendOSC
%{_bindir}/smogrify
%{_libdir}/%{name}
%{_libdir}/libOSC*
%exclude %{_libdir}/libOSC*.so
%{_datadir}/applications/LiVES.desktop
%{_datadir}/%{name}
%exclude %{_defaultdocdir}/%{name}-%{version}
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/app-install/icons/%{name}.png

%files devel
%{_libdir}/libOSC*.so

%files doc
%{_defaultdocdir}/%{name}-%{version}
%doc README AUTHORS BUGS ChangeLog FEATURES
%license COPYING

%files -n weed
%{_libdir}/libweed*
%exclude %{_libdir}/libweed*.so

%files -n weed-devel
%{_includedir}/weed
%{_libdir}/pkgconfig/libweed*
%{_libdir}/libweed*.so


%changelog
* Wed Aug 11 2015 Vasiliy N. Glazov <vascom2@gmail.com> - 2.4.1-1
- Update to 2.4.1

* Thu May 07 2015 Vasiliy N. Glazov <vascom2@gmail.com> - 2.4.0-1
- Update to 2.4.0

* Thu Mar 26 2015 Vasiliy N. Glazov <vascom2@gmail.com> - 2.2.8-2
- Add Requires vdgrab and cdda2wav

* Mon Feb 09 2015 Vasiliy N. Glazov <vascom2@gmail.com> - 2.2.8-1
- Update to 2.2.8

* Thu Dec 25 2014 Vasiliy N. Glazov <vascom2@gmail.com> - 2.2.7-1
- Update to 2.2.7

* Sun Aug 17 2014 Vasiliy N. Glazov <vascom2@gmail.com> - 2.2.6-1
- Update to 2.2.6

* Sat Jul 05 2014 Vasiliy N. Glazov <vascom2@gmail.com> - 2.2.5-1
- Update to 2.2.5

* Mon Apr 21 2014 Vasiliy N. Glazov <vascom2@gmail.com> - 2.2.4-1
- Update to 2.2.4

* Fri Apr 18 2014 Vasiliy N. Glazov <vascom2@gmail.com> - 2.2.3-2
- Patching for compile in F20, F21

* Mon Apr 14 2014 Vasiliy N. Glazov <vascom2@gmail.com> - 2.2.3-1
- Update to 2.2.3

* Wed Dec 11 2013 Vasiliy N. Glazov <vascom2@gmail.com> - 2.2.2-1
- Update to 2.2.2

* Tue Dec 03 2013 Vasiliy N. Glazov <vascom2@gmail.com> - 2.2.0-1
- Update to 2.2.0

* Sun Oct 13 2013 Vasiliy N. Glazov <vascom2@gmail.com> - 2.0.6-1
- Update to 2.0.6

* Tue Jun 18 2013 Vasiliy N. Glazov <vascom2@gmail.com> - 2.0.5-1
- Update to 2.0.5

* Sun May 05 2013 Vasiliy N. Glazov <vascom2@gmail.com> - 2.0.4-1.R
- update to 2.0.4

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

* Sun Nov 20 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 1.4.7-3.R
- Corrected libpath in .pc files

* Mon Oct 17 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 1.4.7-2.R
- Added patch to compile in F16

* Sun Oct 16 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 1.4.7-1.R
- Update to 1.4.7

* Fri Oct 14 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 1.4.6-2.R
- Corrected spec for more robust builds

* Thu Sep 29 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 1.4.6-1.R
- Initial release
