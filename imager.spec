Name:           imager
Version:        0.1
Release:        alt1
Summary:        A simple image utility tool
Group:          Graphics
License:        MIT
URL:            https://github.com/vasthecat/imager
Source0:        %name-%version.tar

BuildRequires(pre): rpm-build-cmake
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  libcurl-devel
BuildRequires:  libSDL2-devel
BuildRequires:  libSDL2_image-devel

%description
A simple image utility tool from GitHub.

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%{_bindir}/%name
%{_datadir}/applications/%name.desktop


%changelog
* Tue Feb 03 2026 Andrew Guschin <guschin@altlinux.org> 0.1-alt1
- Initial package for ALT Linux.
