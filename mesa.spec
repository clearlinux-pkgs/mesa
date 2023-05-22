#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
#
Name     : mesa
Version  : 23.1+1760.g32b150344e0
Release  : 466
URL      : https://gitlab.freedesktop.org/mesa/mesa/-/archive/32b150344e035dd0badf8c83813358ec3d045fb7/mesa-23.1+1760-g32b150344e0.tar.bz2
Source0  : https://gitlab.freedesktop.org/mesa/mesa/-/archive/32b150344e035dd0badf8c83813358ec3d045fb7/mesa-23.1+1760-g32b150344e0.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause MIT
Requires: mesa-data = %{version}-%{release}
Requires: mesa-lib = %{version}-%{release}
Requires: mesa-license = %{version}-%{release}
BuildRequires : Vulkan-Headers-dev
BuildRequires : Vulkan-Loader-dev
BuildRequires : Vulkan-Loader-dev32
BuildRequires : Vulkan-Tools
BuildRequires : bison
BuildRequires : buildreq-meson
BuildRequires : directx-headers-staticdev
BuildRequires : directx-headers-staticdev32
BuildRequires : elfutils-dev32
BuildRequires : expat-dev
BuildRequires : expat-dev32
BuildRequires : flex
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : glslang
BuildRequires : libX11-dev32
BuildRequires : libXv-dev32
BuildRequires : libclc-dev
BuildRequires : libgcrypt-dev
BuildRequires : libglvnd-dev
BuildRequires : libpthread-stubs-dev
BuildRequires : libva-dev
BuildRequires : libvdpau-dev
BuildRequires : llvm-dev32
BuildRequires : nettle-dev
BuildRequires : nettle-dev32
BuildRequires : pkgconfig(32dri3proto)
BuildRequires : pkgconfig(32libdrm_intel)
BuildRequires : pkgconfig(32libudev)
BuildRequires : pkgconfig(32xdamage)
BuildRequires : pkgconfig(32xext)
BuildRequires : pkgconfig(32xfixes)
BuildRequires : pkgconfig(32xshmfence)
BuildRequires : pkgconfig(32xvmc)
BuildRequires : pkgconfig(DirectX-Headers)
BuildRequires : pkgconfig(dri3proto)
BuildRequires : pkgconfig(libdrm_intel)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(presentproto)
BuildRequires : pkgconfig(valgrind)
BuildRequires : pkgconfig(xdamage)
BuildRequires : pkgconfig(xfixes)
BuildRequires : pkgconfig(xshmfence)
BuildRequires : pkgconfig(xvmc)
BuildRequires : pypi-mako
BuildRequires : valgrind
BuildRequires : wayland-dev
BuildRequires : wayland-dev32
BuildRequires : wayland-protocols-dev
BuildRequires : wayland-protocols-dev32
BuildRequires : zlib-dev
BuildRequires : zlib-dev32
BuildRequires : zstd-dev
BuildRequires : zstd-dev32
Patch1: 0001-Revert-mesa-Enable-asm-unconditionally-now-that-gen_.patch
Patch2: asmbuild.patch

%description
This local copy of a SHA1 implementation based on the sources below.
Why:
- Some libraries suffer from race condition and other issues. For example see
commit ade3108bb5b0 ("util: Fix race condition on libgcrypt initialization").

%package data
Summary: data components for the mesa package.
Group: Data

%description data
data components for the mesa package.


%package dev
Summary: dev components for the mesa package.
Group: Development
Requires: mesa-lib = %{version}-%{release}
Requires: mesa-data = %{version}-%{release}
Provides: mesa-devel = %{version}-%{release}
Requires: mesa = %{version}-%{release}
Requires: libglvnd-dev

%description dev
dev components for the mesa package.


%package dev32
Summary: dev32 components for the mesa package.
Group: Default
Requires: mesa-lib32 = %{version}-%{release}
Requires: mesa-data = %{version}-%{release}
Requires: mesa-dev = %{version}-%{release}

%description dev32
dev32 components for the mesa package.


%package lib
Summary: lib components for the mesa package.
Group: Libraries
Requires: mesa-data = %{version}-%{release}
Requires: mesa-license = %{version}-%{release}

%description lib
lib components for the mesa package.


%package lib32
Summary: lib32 components for the mesa package.
Group: Default
Requires: mesa-data = %{version}-%{release}
Requires: mesa-license = %{version}-%{release}

%description lib32
lib32 components for the mesa package.


%package license
Summary: license components for the mesa package.
Group: Default

%description license
license components for the mesa package.


%prep
%setup -q -n mesa-32b150344e035dd0badf8c83813358ec3d045fb7
cd %{_builddir}/mesa-32b150344e035dd0badf8c83813358ec3d045fb7
%patch1 -p1
%patch2 -p1
pushd ..
cp -a mesa-32b150344e035dd0badf8c83813358ec3d045fb7 build32
popd
pushd ..
cp -a mesa-32b150344e035dd0badf8c83813358ec3d045fb7 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1684771165
unset LD_AS_NEEDED
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dplatforms=wayland,x11 \
-Ddri3=enabled \
-Dgallium-drivers=r300,r600,radeonsi,nouveau,virgl,svga,swrast,iris,crocus,i915,zink \
-Dcpp_std=gnu++17 \
-Dgallium-va=enabled \
-Dgallium-xa=enabled \
-Dgallium-opencl=icd \
-Dvulkan-drivers=intel,amd \
-Dshared-glapi=enabled \
-Dglvnd=true \
-Dllvm=enabled \
-Dshared-llvm=enabled \
-Dselinux=false \
-Dosmesa=true \
-Dzstd=enabled \
-Dshader-cache=enabled \
-Dopengl=true  builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dplatforms=wayland,x11 \
-Ddri3=enabled \
-Dgallium-drivers=r300,r600,radeonsi,nouveau,virgl,svga,swrast,iris,crocus,i915,zink \
-Dcpp_std=gnu++17 \
-Dgallium-va=enabled \
-Dgallium-xa=enabled \
-Dgallium-opencl=icd \
-Dvulkan-drivers=intel,amd \
-Dshared-glapi=enabled \
-Dglvnd=true \
-Dllvm=enabled \
-Dshared-llvm=enabled \
-Dselinux=false \
-Dosmesa=true \
-Dzstd=enabled \
-Dshader-cache=enabled \
-Dopengl=true  builddiravx2
ninja -v -C builddiravx2
pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
meson --libdir=lib32 --prefix=/usr --buildtype=plain -Dplatforms=wayland,x11 \
-Ddri3=enabled \
-Dgallium-drivers=r300,r600,radeonsi,nouveau,virgl,svga,swrast,iris,crocus,i915,zink \
-Dcpp_std=gnu++17 \
-Dgallium-va=enabled \
-Dgallium-xa=enabled \
-Dgallium-opencl=icd \
-Dvulkan-drivers=intel,amd \
-Dshared-glapi=enabled \
-Dglvnd=true \
-Dllvm=enabled \
-Dshared-llvm=enabled \
-Dselinux=false \
-Dosmesa=true \
-Dzstd=enabled \
-Dshader-cache=enabled \
-Dopengl=true -Dgallium-opencl=disabled \
-Dasm=false \
-Dgallium-drivers=r300,r600,radeonsi,nouveau,virgl,svga,swrast,iris,crocus,i915 \
-Dglvnd=false builddir
ninja -v -C builddir
popd

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mesa
cp %{_builddir}/mesa-32b150344e035dd0badf8c83813358ec3d045fb7/docs/license.rst %{buildroot}/usr/share/package-licenses/mesa/b27952910869458b2b165aaf1d70b77d3bd1be06 || :
cp %{_builddir}/mesa-32b150344e035dd0badf8c83813358ec3d045fb7/src/amd/vulkan/radix_sort/LICENSE %{buildroot}/usr/share/package-licenses/mesa/46aace8adc5b06990d9ee2b6bd555ea03c4df7a1 || :
cp %{_builddir}/mesa-32b150344e035dd0badf8c83813358ec3d045fb7/src/imgui/LICENSE.txt %{buildroot}/usr/share/package-licenses/mesa/1871c6c7ddab444838aa6a57e6fa085d4e4de683 || :
cp %{_builddir}/mesa-32b150344e035dd0badf8c83813358ec3d045fb7/src/mapi/glapi/gen/license.py %{buildroot}/usr/share/package-licenses/mesa/98d051673de64cfd533ded6d75f1526f5f4f27af || :
pushd ../build32/
DESTDIR=%{buildroot} ninja -C builddir install
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
## Remove excluded files
rm -f %{buildroot}*/usr/include/EGL/egl.h
rm -f %{buildroot}*/usr/include/EGL/eglext.h
rm -f %{buildroot}*/usr/include/GLES/egl.h
rm -f %{buildroot}*/usr/include/GLES/gl.h
rm -f %{buildroot}*/usr/include/GLES/glext.h
rm -f %{buildroot}*/usr/include/GLES/glplatform.h
rm -f %{buildroot}*/usr/include/GLES2/gl2.h
rm -f %{buildroot}*/usr/include/GLES2/gl2ext.h
rm -f %{buildroot}*/usr/include/GLES2/gl2platform.h
rm -f %{buildroot}*/usr/include/GLES3/gl3.h
rm -f %{buildroot}*/usr/include/GLES3/gl31.h
rm -f %{buildroot}*/usr/include/GLES3/gl32.h
rm -f %{buildroot}*/usr/include/GLES3/gl3ext.h
rm -f %{buildroot}*/usr/include/GLES3/gl3platform.h
rm -f %{buildroot}*/usr/include/KHR/khrplatform.h
rm -f %{buildroot}*/usr/include/EGL/eglplatform.h
rm -f %{buildroot}*/usr/include/GL/gl.h
rm -f %{buildroot}*/usr/include/GL/glcorearb.h
rm -f %{buildroot}*/usr/include/GL/glext.h
rm -f %{buildroot}*/usr/include/GL/glx.h
rm -f %{buildroot}*/usr/include/GL/glxext.h
rm -f %{buildroot}*/usr/share/vulkan/icd.d/intel_icd.i686.json
rm -f %{buildroot}*/usr/share/vulkan/icd.d/radeon_icd.i686.json
## install_append content

#sed 's/lib64/lib32/' %{buildroot}/usr/share/vulkan/icd.d/intel_icd.x86_64.json > %{buildroot}/usr/share/vulkan/icd.d/intel_icd.i686.json
#sed 's/lib64/lib32/' %{buildroot}/usr/share/vulkan/icd.d/radeon_icd.x86_64.json > %{buildroot}/usr/share/vulkan/icd.d/radeon_icd.i686.json
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/drirc.d/00-mesa-defaults.conf
/usr/share/drirc.d/00-radv-defaults.conf
/usr/share/glvnd/egl_vendor.d/50_mesa.json
/usr/share/vulkan/icd.d/intel_icd.x86_64.json
/usr/share/vulkan/icd.d/radeon_icd.x86_64.json

%files dev
%defattr(-,root,root,-)
/usr/include/EGL/eglext_angle.h
/usr/include/EGL/eglmesaext.h
/usr/include/GL/internal/dri_interface.h
/usr/include/GL/osmesa.h
/usr/include/gbm.h
/usr/include/xa_composite.h
/usr/include/xa_context.h
/usr/include/xa_tracker.h
/usr/lib64/pkgconfig/dri.pc
/usr/lib64/pkgconfig/gbm.pc
/usr/lib64/pkgconfig/osmesa.pc
/usr/lib64/pkgconfig/xatracker.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/pkgconfig/32dri.pc
/usr/lib32/pkgconfig/32egl.pc
/usr/lib32/pkgconfig/32gbm.pc
/usr/lib32/pkgconfig/32gl.pc
/usr/lib32/pkgconfig/32glesv1_cm.pc
/usr/lib32/pkgconfig/32glesv2.pc
/usr/lib32/pkgconfig/32osmesa.pc
/usr/lib32/pkgconfig/32xatracker.pc
/usr/lib32/pkgconfig/dri.pc
/usr/lib32/pkgconfig/egl.pc
/usr/lib32/pkgconfig/gbm.pc
/usr/lib32/pkgconfig/gl.pc
/usr/lib32/pkgconfig/glesv1_cm.pc
/usr/lib32/pkgconfig/glesv2.pc
/usr/lib32/pkgconfig/osmesa.pc
/usr/lib32/pkgconfig/xatracker.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/dri/crocus_dri.so
/V3/usr/lib64/dri/i915_dri.so
/V3/usr/lib64/dri/iris_dri.so
/V3/usr/lib64/dri/kms_swrast_dri.so
/V3/usr/lib64/dri/nouveau_dri.so
/V3/usr/lib64/dri/nouveau_drv_video.so
/V3/usr/lib64/dri/r300_dri.so
/V3/usr/lib64/dri/r600_dri.so
/V3/usr/lib64/dri/r600_drv_video.so
/V3/usr/lib64/dri/radeonsi_dri.so
/V3/usr/lib64/dri/radeonsi_drv_video.so
/V3/usr/lib64/dri/swrast_dri.so
/V3/usr/lib64/dri/virtio_gpu_dri.so
/V3/usr/lib64/dri/virtio_gpu_drv_video.so
/V3/usr/lib64/dri/vmwgfx_dri.so
/V3/usr/lib64/dri/zink_dri.so
/V3/usr/lib64/gallium-pipe/pipe_crocus.so
/V3/usr/lib64/gallium-pipe/pipe_i915.so
/V3/usr/lib64/gallium-pipe/pipe_iris.so
/V3/usr/lib64/gallium-pipe/pipe_nouveau.so
/V3/usr/lib64/gallium-pipe/pipe_r300.so
/V3/usr/lib64/gallium-pipe/pipe_r600.so
/V3/usr/lib64/gallium-pipe/pipe_radeonsi.so
/V3/usr/lib64/gallium-pipe/pipe_swrast.so
/V3/usr/lib64/gallium-pipe/pipe_vmwgfx.so
/V3/usr/lib64/libEGL_mesa.so
/V3/usr/lib64/libEGL_mesa.so.0
/V3/usr/lib64/libEGL_mesa.so.0.0.0
/V3/usr/lib64/libGLX_mesa.so
/V3/usr/lib64/libGLX_mesa.so.0
/V3/usr/lib64/libGLX_mesa.so.0.0.0
/V3/usr/lib64/libMesaOpenCL.so
/V3/usr/lib64/libMesaOpenCL.so.1
/V3/usr/lib64/libMesaOpenCL.so.1.0.0
/V3/usr/lib64/libOSMesa.so
/V3/usr/lib64/libOSMesa.so.8
/V3/usr/lib64/libOSMesa.so.8.0.0
/V3/usr/lib64/libgbm.so
/V3/usr/lib64/libgbm.so.1
/V3/usr/lib64/libgbm.so.1.0.0
/V3/usr/lib64/libglapi.so
/V3/usr/lib64/libglapi.so.0
/V3/usr/lib64/libglapi.so.0.0.0
/V3/usr/lib64/libvulkan_intel.so
/V3/usr/lib64/libvulkan_radeon.so
/V3/usr/lib64/libxatracker.so
/V3/usr/lib64/libxatracker.so.2
/V3/usr/lib64/libxatracker.so.2.5.0
/V3/usr/lib64/vdpau/libvdpau_nouveau.so
/V3/usr/lib64/vdpau/libvdpau_nouveau.so.1
/V3/usr/lib64/vdpau/libvdpau_nouveau.so.1.0
/V3/usr/lib64/vdpau/libvdpau_nouveau.so.1.0.0
/V3/usr/lib64/vdpau/libvdpau_r600.so
/V3/usr/lib64/vdpau/libvdpau_r600.so.1
/V3/usr/lib64/vdpau/libvdpau_r600.so.1.0
/V3/usr/lib64/vdpau/libvdpau_r600.so.1.0.0
/V3/usr/lib64/vdpau/libvdpau_radeonsi.so
/V3/usr/lib64/vdpau/libvdpau_radeonsi.so.1
/V3/usr/lib64/vdpau/libvdpau_radeonsi.so.1.0
/V3/usr/lib64/vdpau/libvdpau_radeonsi.so.1.0.0
/V3/usr/lib64/vdpau/libvdpau_virtio_gpu.so
/V3/usr/lib64/vdpau/libvdpau_virtio_gpu.so.1
/V3/usr/lib64/vdpau/libvdpau_virtio_gpu.so.1.0
/V3/usr/lib64/vdpau/libvdpau_virtio_gpu.so.1.0.0
/usr/lib64/dri/crocus_dri.so
/usr/lib64/dri/i915_dri.so
/usr/lib64/dri/iris_dri.so
/usr/lib64/dri/kms_swrast_dri.so
/usr/lib64/dri/nouveau_dri.so
/usr/lib64/dri/nouveau_drv_video.so
/usr/lib64/dri/r300_dri.so
/usr/lib64/dri/r600_dri.so
/usr/lib64/dri/r600_drv_video.so
/usr/lib64/dri/radeonsi_dri.so
/usr/lib64/dri/radeonsi_drv_video.so
/usr/lib64/dri/swrast_dri.so
/usr/lib64/dri/virtio_gpu_dri.so
/usr/lib64/dri/virtio_gpu_drv_video.so
/usr/lib64/dri/vmwgfx_dri.so
/usr/lib64/dri/zink_dri.so
/usr/lib64/gallium-pipe/pipe_crocus.so
/usr/lib64/gallium-pipe/pipe_i915.so
/usr/lib64/gallium-pipe/pipe_iris.so
/usr/lib64/gallium-pipe/pipe_nouveau.so
/usr/lib64/gallium-pipe/pipe_r300.so
/usr/lib64/gallium-pipe/pipe_r600.so
/usr/lib64/gallium-pipe/pipe_radeonsi.so
/usr/lib64/gallium-pipe/pipe_swrast.so
/usr/lib64/gallium-pipe/pipe_vmwgfx.so
/usr/lib64/libEGL_mesa.so
/usr/lib64/libEGL_mesa.so.0
/usr/lib64/libEGL_mesa.so.0.0.0
/usr/lib64/libGLX_mesa.so
/usr/lib64/libGLX_mesa.so.0
/usr/lib64/libGLX_mesa.so.0.0.0
/usr/lib64/libMesaOpenCL.so
/usr/lib64/libMesaOpenCL.so.1
/usr/lib64/libMesaOpenCL.so.1.0.0
/usr/lib64/libOSMesa.so
/usr/lib64/libOSMesa.so.8
/usr/lib64/libOSMesa.so.8.0.0
/usr/lib64/libgbm.so
/usr/lib64/libgbm.so.1
/usr/lib64/libgbm.so.1.0.0
/usr/lib64/libglapi.so
/usr/lib64/libglapi.so.0
/usr/lib64/libglapi.so.0.0.0
/usr/lib64/libvulkan_intel.so
/usr/lib64/libvulkan_radeon.so
/usr/lib64/libxatracker.so
/usr/lib64/libxatracker.so.2
/usr/lib64/libxatracker.so.2.5.0
/usr/lib64/vdpau/libvdpau_nouveau.so
/usr/lib64/vdpau/libvdpau_nouveau.so.1
/usr/lib64/vdpau/libvdpau_nouveau.so.1.0
/usr/lib64/vdpau/libvdpau_nouveau.so.1.0.0
/usr/lib64/vdpau/libvdpau_r600.so
/usr/lib64/vdpau/libvdpau_r600.so.1
/usr/lib64/vdpau/libvdpau_r600.so.1.0
/usr/lib64/vdpau/libvdpau_r600.so.1.0.0
/usr/lib64/vdpau/libvdpau_radeonsi.so
/usr/lib64/vdpau/libvdpau_radeonsi.so.1
/usr/lib64/vdpau/libvdpau_radeonsi.so.1.0
/usr/lib64/vdpau/libvdpau_radeonsi.so.1.0.0
/usr/lib64/vdpau/libvdpau_virtio_gpu.so
/usr/lib64/vdpau/libvdpau_virtio_gpu.so.1
/usr/lib64/vdpau/libvdpau_virtio_gpu.so.1.0
/usr/lib64/vdpau/libvdpau_virtio_gpu.so.1.0.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/dri/crocus_dri.so
/usr/lib32/dri/i915_dri.so
/usr/lib32/dri/iris_dri.so
/usr/lib32/dri/kms_swrast_dri.so
/usr/lib32/dri/nouveau_dri.so
/usr/lib32/dri/nouveau_drv_video.so
/usr/lib32/dri/r300_dri.so
/usr/lib32/dri/r600_dri.so
/usr/lib32/dri/r600_drv_video.so
/usr/lib32/dri/radeonsi_dri.so
/usr/lib32/dri/radeonsi_drv_video.so
/usr/lib32/dri/swrast_dri.so
/usr/lib32/dri/virtio_gpu_dri.so
/usr/lib32/dri/virtio_gpu_drv_video.so
/usr/lib32/dri/vmwgfx_dri.so
/usr/lib32/libEGL.so
/usr/lib32/libEGL.so.1
/usr/lib32/libEGL.so.1.0.0
/usr/lib32/libGL.so
/usr/lib32/libGL.so.1
/usr/lib32/libGL.so.1.2.0
/usr/lib32/libGLESv1_CM.so
/usr/lib32/libGLESv1_CM.so.1
/usr/lib32/libGLESv1_CM.so.1.1.0
/usr/lib32/libGLESv2.so
/usr/lib32/libGLESv2.so.2
/usr/lib32/libGLESv2.so.2.0.0
/usr/lib32/libOSMesa.so
/usr/lib32/libOSMesa.so.8
/usr/lib32/libOSMesa.so.8.0.0
/usr/lib32/libgbm.so
/usr/lib32/libgbm.so.1
/usr/lib32/libgbm.so.1.0.0
/usr/lib32/libglapi.so
/usr/lib32/libglapi.so.0
/usr/lib32/libglapi.so.0.0.0
/usr/lib32/libvulkan_intel.so
/usr/lib32/libvulkan_radeon.so
/usr/lib32/libxatracker.so
/usr/lib32/libxatracker.so.2
/usr/lib32/libxatracker.so.2.5.0
/usr/lib32/vdpau/libvdpau_nouveau.so
/usr/lib32/vdpau/libvdpau_nouveau.so.1
/usr/lib32/vdpau/libvdpau_nouveau.so.1.0
/usr/lib32/vdpau/libvdpau_nouveau.so.1.0.0
/usr/lib32/vdpau/libvdpau_r600.so
/usr/lib32/vdpau/libvdpau_r600.so.1
/usr/lib32/vdpau/libvdpau_r600.so.1.0
/usr/lib32/vdpau/libvdpau_r600.so.1.0.0
/usr/lib32/vdpau/libvdpau_radeonsi.so
/usr/lib32/vdpau/libvdpau_radeonsi.so.1
/usr/lib32/vdpau/libvdpau_radeonsi.so.1.0
/usr/lib32/vdpau/libvdpau_radeonsi.so.1.0.0
/usr/lib32/vdpau/libvdpau_virtio_gpu.so
/usr/lib32/vdpau/libvdpau_virtio_gpu.so.1
/usr/lib32/vdpau/libvdpau_virtio_gpu.so.1.0
/usr/lib32/vdpau/libvdpau_virtio_gpu.so.1.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mesa/1871c6c7ddab444838aa6a57e6fa085d4e4de683
/usr/share/package-licenses/mesa/46aace8adc5b06990d9ee2b6bd555ea03c4df7a1
/usr/share/package-licenses/mesa/98d051673de64cfd533ded6d75f1526f5f4f27af
/usr/share/package-licenses/mesa/b27952910869458b2b165aaf1d70b77d3bd1be06
