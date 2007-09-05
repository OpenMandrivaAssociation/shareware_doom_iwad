Name:		shareware_doom_iwad
BuildArch:	noarch
Version:	1.9
Release:	%mkrel 0
Summary:	Doom v1.9 shareware iwad.
# http://www.3ddownloads.com/showfile.php3?file_id=7486
Source0:	%{name}.zip
License:	Shareware
Group:		Games/Arcade
URL:		http://www.doomworld.com/classicdoom/info/shareware.php
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
%description
Shareware Doom v1.9 iwad.

%install
unzip -o %{SOURCE0}
install -D -m 644 DOOM1.WAD %{buildroot}/%{_gamesdatadir}/doom/doom1.wad

%clean
rm -rf %{buildroot}

%files
%{_gamesdatadir}/doom/doom1.wad
