Name:       rc-raid
Version:    1.0
Release:    1%{?dist}
Summary:    Ryzen Fakeraid dkms module for chipset 4xx and 3xx
License:    Properitary
URL:        https://github.com/lyra00/AMD-Fake-Raid.git

Source0: https://github.com/lyra00/AMD-Fake-Raid/archive/1.0.tar.gz

Requires: dkms
Requires: kernel-devel

%description
Ryzen Fake Raid DKMS (Dynamic Kernel Module Support)
-----
This DKMS driver provides Ryzen Fake Raid support for X370, B350, X470, B450 and X399 Mainboards.
Raid modes 0,1,10,5 are supported.
The module is rebuilt through the DKMS system when a new kernel or module
become available.
There is currently no smart support for Drives in FakeRaidMode

%define debug_package %{nil}

#--
%prep
%setup -q -n rcraid-1.0

%install
install -D -m 0644 *.c -t "%{buildroot}%{_usrsrc}/rcraid/"
install -m 0644 Makefile -t "%{buildroot}%{_usrsrc}/rcraid/"
install -m 0644 fedora/rcraid-dkms.dkms "%{buildroot}%{_usrsrc}/rcraid/dkms.conf"

# do after installation
%post
sed -i 's/PACKAGE_VERSION="#MODULE_VERSION#"/PACKAGE_VERSION="1.0"/g' %{_usrsrc}/rcraid/dkms.conf

/usr/bin/env dkms add -m rcraid -v 1.0 --rpm_safe_upgrade
/usr/bin/env dkms build -m rcraid -v 1.0
/usr/bin/env dkms install -m rcraid -v 1.0 --force

%preun
/usr/bin/env rmmod rcraid
/usr/bin/env dkms remove -m rcraid -v 1.0 --all --rpm_safe_upgrade

# Those files will be in the rpm
%files
%{_usrsrc}/rcraid-1.0
