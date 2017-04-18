#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mesa
Version  : 1
Release  : 86
URL      : https://cgit.freedesktop.org/mesa/mesa/snapshot/9f0dd85aa65b5eba783d6023b51deacd529cf918.tar.gz
Source0  : https://cgit.freedesktop.org/mesa/mesa/snapshot/9f0dd85aa65b5eba783d6023b51deacd529cf918.tar.gz
Summary  : Mesa OpenGL library
Group    : Development/Tools
License  : MIT
Requires: mesa-lib
Requires: mesa-data
Requires: mesa-extras
BuildRequires : Mako-python
BuildRequires : bison
BuildRequires : elfutils-dev
BuildRequires : flex
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libgcrypt-dev
BuildRequires : libpthread-stubs-dev
BuildRequires : llvm-dev
BuildRequires : nettle-dev
BuildRequires : nettle-dev32
BuildRequires : pkgconfig(32dri2proto)
BuildRequires : pkgconfig(32dri3proto)
BuildRequires : pkgconfig(32expat)
BuildRequires : pkgconfig(32glproto)
BuildRequires : pkgconfig(32libdrm)
BuildRequires : pkgconfig(32presentproto)
BuildRequires : pkgconfig(32pthread-stubs)
BuildRequires : pkgconfig(32x11-xcb)
BuildRequires : pkgconfig(32xcb)
BuildRequires : pkgconfig(32xcb-dri2)
BuildRequires : pkgconfig(32xcb-dri3)
BuildRequires : pkgconfig(32xcb-present)
BuildRequires : pkgconfig(32xcb-sync)
BuildRequires : pkgconfig(32xdamage)
BuildRequires : pkgconfig(32xext)
BuildRequires : pkgconfig(32xfixes)
BuildRequires : pkgconfig(32xshmfence)
BuildRequires : pkgconfig(32xvmc)
BuildRequires : pkgconfig(32xxf86vm)
BuildRequires : pkgconfig(32zlib)
BuildRequires : pkgconfig(dri2proto)
BuildRequires : pkgconfig(dri3proto)
BuildRequires : pkgconfig(expat)
BuildRequires : pkgconfig(glproto)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libunwind)
BuildRequires : pkgconfig(libva)
BuildRequires : pkgconfig(presentproto)
BuildRequires : pkgconfig(pthread-stubs)
BuildRequires : pkgconfig(valgrind)
BuildRequires : pkgconfig(wayland-scanner)
BuildRequires : pkgconfig(x11-xcb)
BuildRequires : pkgconfig(xcb)
BuildRequires : pkgconfig(xcb-dri2)
BuildRequires : pkgconfig(xcb-dri3)
BuildRequires : pkgconfig(xcb-present)
BuildRequires : pkgconfig(xcb-sync)
BuildRequires : pkgconfig(xdamage)
BuildRequires : pkgconfig(xfixes)
BuildRequires : pkgconfig(xshmfence)
BuildRequires : pkgconfig(xvmc)
BuildRequires : pkgconfig(xxf86vm)
BuildRequires : pkgconfig(zlib)
BuildRequires : python-dev
BuildRequires : scons
BuildRequires : sed
BuildRequires : vulkan-sdk-dev
BuildRequires : vulkan-sdk-dev32
BuildRequires : wayland-dev
BuildRequires : wayland-dev32
BuildRequires : wayland-protocols-dev
Patch1: better-error.patch
Patch2: swr.patch

%description


%package data
Summary: data components for the mesa package.
Group: Data

%description data
data components for the mesa package.


%package dev
Summary: dev components for the mesa package.
Group: Development
Requires: mesa-lib
Requires: mesa-data
Provides: mesa-devel
Requires: mesa-extras

%description dev
dev components for the mesa package.


%package dev32
Summary: dev32 components for the mesa package.
Group: Default
Requires: mesa-lib32
Requires: mesa-data
Requires: mesa-dev

%description dev32
dev32 components for the mesa package.


%package extras
Summary: extras components for the mesa package.
Group: Default

%description extras
extras components for the mesa package.


%package lib
Summary: lib components for the mesa package.
Group: Libraries
Requires: mesa-data

%description lib
lib components for the mesa package.


%package lib32
Summary: lib32 components for the mesa package.
Group: Default
Requires: mesa-data

%description lib32
lib32 components for the mesa package.


%prep
%setup -q -n 9f0dd85aa65b5eba783d6023b51deacd529cf918
%patch1 -p1
%patch2 -p1
pushd ..
cp -a 9f0dd85aa65b5eba783d6023b51deacd529cf918 build32
popd

%build
export LANG=C
export SOURCE_DATE_EPOCH=1492455292
unset LD_AS_NEEDED
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
%reconfigure --disable-static --enable-dri \
--enable-dri3 \
--enable-glx \
--enable-gles2 \
--enable-xorg \
--enable-shared-glapi \
--enable-xorg \
--enable-glx-tls \
--enable-xvmc \
--enable-va \
--enable-glx-tls \
--enable-texture-float \
--enable-gbm \
--sysconfdir=/usr/share/mesa \
--with-egl-platforms=x11,drm,wayland \
--with-vulkan-drivers=intel --with-dri-drivers="i965"  --with-gallium-drivers="swrast,swr,radeonsi,r600,nouveau"
make V=1  %{?_smp_mflags}
pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%reconfigure --disable-static --enable-dri \
--enable-dri3 \
--enable-glx \
--enable-gles2 \
--enable-xorg \
--enable-shared-glapi \
--enable-xorg \
--enable-glx-tls \
--enable-xvmc \
--enable-va \
--enable-glx-tls \
--enable-texture-float \
--enable-gbm \
--sysconfdir=/usr/share/mesa \
--with-egl-platforms=x11,drm,wayland \
--with-vulkan-drivers=intel --disable-va \
--with-dri-drivers="i965,swrast" \
--without-gallium-drivers \
--disable-gallium-llvm --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1492455292
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/mesa/drirc
/usr/share/vulkan/icd.d/intel_icd.i686.json
/usr/share/vulkan/icd.d/intel_icd.x86_64.json

%files dev
%defattr(-,root,root,-)
%exclude /usr/lib64/libEGL.so
%exclude /usr/lib64/libGL.so
%exclude /usr/lib64/libGLESv1_CM.so
%exclude /usr/lib64/libGLESv2.so
%exclude /usr/lib64/libXvMCnouveau.so
%exclude /usr/lib64/libXvMCr600.so
%exclude /usr/lib64/libgbm.so
%exclude /usr/lib64/libglapi.so
%exclude /usr/lib64/libswrAVX.so
%exclude /usr/lib64/libswrAVX2.so
%exclude /usr/lib64/libvulkan_intel.so
%exclude /usr/lib64/libwayland-egl.so
/usr/include/*.h
/usr/include/EGL/egl.h
/usr/include/EGL/eglext.h
/usr/include/EGL/eglextchromium.h
/usr/include/EGL/eglmesaext.h
/usr/include/EGL/eglplatform.h
/usr/include/GL/gl.h
/usr/include/GL/gl_mangle.h
/usr/include/GL/glcorearb.h
/usr/include/GL/glext.h
/usr/include/GL/glx.h
/usr/include/GL/glx_mangle.h
/usr/include/GL/glxext.h
/usr/include/GL/internal/dri_interface.h
/usr/include/GLES/egl.h
/usr/include/GLES/gl.h
/usr/include/GLES/glext.h
/usr/include/GLES/glplatform.h
/usr/include/GLES2/gl2.h
/usr/include/GLES2/gl2ext.h
/usr/include/GLES2/gl2platform.h
/usr/include/GLES3/gl3.h
/usr/include/GLES3/gl31.h
/usr/include/GLES3/gl32.h
/usr/include/GLES3/gl3ext.h
/usr/include/GLES3/gl3platform.h
/usr/include/KHR/khrplatform.h
/usr/include/vulkan/vulkan_intel.h
/usr/lib64/pkgconfig/dri.pc
/usr/lib64/pkgconfig/egl.pc
/usr/lib64/pkgconfig/gbm.pc
/usr/lib64/pkgconfig/gl.pc
/usr/lib64/pkgconfig/glesv1_cm.pc
/usr/lib64/pkgconfig/glesv2.pc
/usr/lib64/pkgconfig/wayland-egl.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libEGL.so
/usr/lib32/libGL.so
/usr/lib32/libGLESv1_CM.so
/usr/lib32/libGLESv2.so
/usr/lib32/libgbm.so
/usr/lib32/libglapi.so
/usr/lib32/libvulkan_intel.so
/usr/lib32/libwayland-egl.so
/usr/lib32/pkgconfig/32dri.pc
/usr/lib32/pkgconfig/32egl.pc
/usr/lib32/pkgconfig/32gbm.pc
/usr/lib32/pkgconfig/32gl.pc
/usr/lib32/pkgconfig/32glesv1_cm.pc
/usr/lib32/pkgconfig/32glesv2.pc
/usr/lib32/pkgconfig/32wayland-egl.pc
/usr/lib32/pkgconfig/dri.pc
/usr/lib32/pkgconfig/egl.pc
/usr/lib32/pkgconfig/gbm.pc
/usr/lib32/pkgconfig/gl.pc
/usr/lib32/pkgconfig/glesv1_cm.pc
/usr/lib32/pkgconfig/glesv2.pc
/usr/lib32/pkgconfig/wayland-egl.pc

%files extras
%defattr(-,root,root,-)
/usr/lib64/libEGL.so
/usr/lib64/libGL.so
/usr/lib64/libGLESv1_CM.so
/usr/lib64/libGLESv2.so
/usr/lib64/libXvMCnouveau.so
/usr/lib64/libXvMCr600.so
/usr/lib64/libgbm.so
/usr/lib64/libglapi.so
/usr/lib64/libswrAVX.so
/usr/lib64/libswrAVX2.so
/usr/lib64/libvulkan_intel.so
/usr/lib64/libwayland-egl.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/dri/i965_dri.so
/usr/lib64/dri/kms_swrast_dri.so
/usr/lib64/dri/nouveau_dri.so
/usr/lib64/dri/nouveau_drv_video.so
/usr/lib64/dri/r600_dri.so
/usr/lib64/dri/r600_drv_video.so
/usr/lib64/dri/radeonsi_dri.so
/usr/lib64/dri/radeonsi_drv_video.so
/usr/lib64/dri/swrast_dri.so
/usr/lib64/libEGL.so.1
/usr/lib64/libEGL.so.1.0.0
/usr/lib64/libGL.so.1
/usr/lib64/libGL.so.1.2.0
/usr/lib64/libGLESv1_CM.so.1
/usr/lib64/libGLESv1_CM.so.1.1.0
/usr/lib64/libGLESv2.so.2
/usr/lib64/libGLESv2.so.2.0.0
/usr/lib64/libXvMCnouveau.so.1
/usr/lib64/libXvMCnouveau.so.1.0
/usr/lib64/libXvMCnouveau.so.1.0.0
/usr/lib64/libXvMCr600.so.1
/usr/lib64/libXvMCr600.so.1.0
/usr/lib64/libXvMCr600.so.1.0.0
/usr/lib64/libgbm.so.1
/usr/lib64/libgbm.so.1.0.0
/usr/lib64/libglapi.so.0
/usr/lib64/libglapi.so.0.0.0
/usr/lib64/libswrAVX.so.0
/usr/lib64/libswrAVX.so.0.0.0
/usr/lib64/libswrAVX2.so.0
/usr/lib64/libswrAVX2.so.0.0.0
/usr/lib64/libwayland-egl.so.1
/usr/lib64/libwayland-egl.so.1.0.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/dri/i965_dri.so
/usr/lib32/dri/swrast_dri.so
/usr/lib32/libEGL.so.1
/usr/lib32/libEGL.so.1.0.0
/usr/lib32/libGL.so.1
/usr/lib32/libGL.so.1.2.0
/usr/lib32/libGLESv1_CM.so.1
/usr/lib32/libGLESv1_CM.so.1.1.0
/usr/lib32/libGLESv2.so.2
/usr/lib32/libGLESv2.so.2.0.0
/usr/lib32/libgbm.so.1
/usr/lib32/libgbm.so.1.0.0
/usr/lib32/libglapi.so.0
/usr/lib32/libglapi.so.0.0.0
/usr/lib32/libwayland-egl.so.1
/usr/lib32/libwayland-egl.so.1.0.0
