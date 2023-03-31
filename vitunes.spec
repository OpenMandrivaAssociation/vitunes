%define debug_package %{nil}

Summary:	A curses media indexer and player for vi users
Name:		vitunes
Version:	2.3
Release:	11
Source0:	http://vitunes.org/files/%{name}-%{version}.tar.gz
License:	BSD
Group:		Sound
URL:		http://vitunes.org
Patch0:		vitunes-2.3-time-header.patch
Patch1:		vitunes-2.3-asneeded.patch

BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(taglib)

%description
vitunes is a curses-based music player 
and playlist manager for *nix whose goals are:
 * a minimalistic appearance
 * strong vi-like bindings 
 * quick playlist creation/management.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
cp Makefile.linux Makefile

%build
%make -f Makefile.linux

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
%makeinstall_std PREFIX=%{buildroot}%{_prefix}
chmod 0755 %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*



%changelog
* Wed Jan 11 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.3-1
+ Revision: 759718
- imported package vitunes

