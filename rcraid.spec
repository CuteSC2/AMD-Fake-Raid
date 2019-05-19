Name:       AMD-Fake-Raid
Version:    1.0
Release:    1%{?dist}
Summary:    Ryzen Fakeraid dkms module for chipset 4xx and 3xx
License:    Properitary
URL:        https://github.com/lyra00/AMD-Fake-Raid       

Source0: %{url}/tar.gz/%{name}-%{version}

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
%define NVdir   %{name}-%{version}

%prep
rm -rf %{NVdir}
git clone %{url}.git %{NVdir}
cd %{NVdir}

%install

install -D -m 0644 *.c -t "%{buildroot}%{_usrsrc}/AMD-Fake-Raid-%{version}/"
install -D -m 0644 *.h -t "%{buildroot}%{_usrsrc}/AMD-Fake-Raid-%{version}/"
install -D -m 0644 common_shell -t "%{buildroot}%{_usrsrc}/AMD-Fake-Raid-%{version}/"
install -D -m 0644 LICENSE_SDK -t "%{buildroot}%{_usrsrc}/AMD-Fake-Raid-%{version}/"
install -D -m 0644 *.i386 -t "%{buildroot}%{_usrsrc}/AMD-Fake-Raid-%{version}/"
install -D -m 0644 *.x86_64 -t "%{buildroot}%{_usrsrc}/AMD-Fake-Raid-%{version}/"   
install -m 0644 Makefile -t "%{buildroot}%{_usrsrc}/AMD-Fake-Raid-%{version}/"
install -m 0644 dkms.conf "%{buildroot}%{_usrsrc}/AMD-Fake-Raid-%{version}/dkms.conf"

# do after installation
%post
sed -i 's/PACKAGE_VERSION="#MODULE_VERSION#"/PACKAGE_VERSION="%{version}"/g' %{_usrsrc}/AMD-Fake-Raid/dkms.conf

/usr/bin/env dkms add -m AMD-Fake-Raid -v %{version} --rpm_safe_upgrade
/usr/bin/env dkms build -m AMD-Fake-Raid -v %{version}
/usr/bin/env dkms install -m AMD-Fake-Raid -v %{version} --force

%preun
/usr/bin/env rmmod AMD-Fake-Raid
/usr/bin/env dkms remove -m rcraid -v %{version} --all --rpm_safe_upgrade

# Those files will be in the rpm
%files
%{_usrsrc}/AMD-Fake-Raid-%{version}
