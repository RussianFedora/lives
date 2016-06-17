Name:           lives
Version:        2.6.3
Release:        2%{?dist}
Summary:        LiVES is a Video Editing System
Summary(ru):    Система видеоредактирования LiVES

License:        GPLv3
URL:            http://lives-video.com
Source0:        http://lives-video.com/releases/LiVES-%{version}.tar.bz2
Patch0:		lives-2.6.3-ffmpeg3.patch

BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libunicap)
BuildRequires:  pkgconfig(mjpegtools)
BuildRequires:  pkgconfig(libdv)
BuildRequires:  pkgconfig(libavc1394)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(frei0r)
BuildRequires:  pkgconfig(liboil-0.3)
BuildRequires:  doxygen
BuildRequires:  chrpath
BuildRequires:  bison
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  gettext
BuildRequires:  pkgconfig(schroedinger-1.0)
BuildRequires:  x264-devel
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  GLee-devel
BuildRequires:  pkgconfig(opencv)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  ladspa-devel
BuildRequires:  pkgconfig(fftw3)

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
%patch0 -p0 -b .ffmpeg3


%build
%configure --disable-rpath--disable-static
%make_build


%install
mkdir -p %{buildroot}%{_bindir}
%make_install
rm %{buildroot}%{_bindir}/%{name}
%find_lang %{name}
cd %{buildroot}/%{_bindir}/
ln -s %{name}-exe %{name}

#https://sourceforge.net/p/lives/bugs/216/
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

#https://sourceforge.net/p/lives/bugs/215/
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
* Tue Jun 14 2016 Arkady L. Shane <ashejn@russianfedora.pro> - 2.6.3-2.R
- rebuilt against new ffmpeg

* Mon May 30 2016 Vasiliy N. Glazov <vascom2@gmail.com> - 2.6.3-1
- Update to 2.6.3

* Tue Mar 29 2016 Vasiliy N. Glazov <vascom2@gmail.com> - 2.6.2-1
- Update to 2.6.2

* Mon Mar 28 2016 Vasiliy N. Glazov <vascom2@gmail.com> - 2.6.1-1
- Update to 2.6.1

* Thu Feb 04 2016 Vasiliy N. Glazov <vascom2@gmail.com> - 2.6.0-1
- Update to 2.6.0

* Mon Jan 25 2016 Vasiliy N. Glazov <vascom2@gmail.com> - 2.4.8-1
- Update to 2.4.8

* Wed Jan 20 2016 Vasiliy N. Glazov <vascom2@gmail.com> - 2.4.7-2
- Add patch fixes a hang in Merge in the Clip Editor

* Mon Jan 18 2016 Vasiliy N. Glazov <vascom2@gmail.com> - 2.4.7-1
- Update to 2.4.7

* Mon Dec 21 2015 Vasiliy N. Glazov <vascom2@gmail.com> - 2.4.6-1
- Update to 2.4.6

* Thu Dec 03 2015 Vasiliy N. Glazov <vascom2@gmail.com> - 2.4.5-1
- Update to 2.4.5

* Mon Nov 23 2015 Vasiliy N. Glazov <vascom2@gmail.com> - 2.4.4-1
- Update to 2.4.4

* Mon Nov 16 2015 Vasiliy N. Glazov <vascom2@gmail.com> - 2.4.3-1
- Update to 2.4.3

* Mon Sep 14 2015 Vasiliy N. Glazov <vascom2@gmail.com> - 2.4.2-1
- Update to 2.4.2

* Tue Aug 11 2015 Vasiliy N. Glazov <vascom2@gmail.com> - 2.4.1-1
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
