Name:             python-quantumclient
#Version:          0.2.26
Version:          2012.2 
#Release:          1%{?dist}
Release:          folsom 
Summary:          Python API and CLI for OpenStack quantum 

Group:            Development/Languages
License:          ASL 2.0
URL:              http://github.com/openstack/python-quantumclient
Source0:          http://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz

#
# patches_base=0.2
#

BuildArch:        noarch
BuildRequires:    python-setuptools

Requires:         python-httplib2
Requires:         python-prettytable
Requires:         python-setuptools

%description
This is a client for the OpenStack quantum API. There's a Python API (the
quantumclient module), and a command-line script (quantum). Each implements
100% of the OpenStack quantum API.

%prep
%setup -q

# TODO: Have the following handle multi line entries
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py

# Remove bundled egg-info
rm -rf python_quantumclient.egg-info

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

# Delete tests
rm -fr %{buildroot}%{python_sitelib}/tests

%files
%doc README
%doc LICENSE
%{_bindir}/quantum
%{python_sitelib}/quantumclient
%{python_sitelib}/quantumclient/*
%{python_sitelib}/*.egg-info


%changelog
