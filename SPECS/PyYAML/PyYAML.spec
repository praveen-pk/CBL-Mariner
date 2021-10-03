Summary:        YAML parser and emitter for Python
Name:           PyYAML
Version:        3.13
Release:        7%{?dist}
License:        MIT
Vendor:         Microsoft Corporation
Distribution:   Mariner
Group:          Development/Libraries
URL:            https://pyyaml.org/
Source0:        https://pyyaml.org/download/pyyaml/%{name}-%{version}.tar.gz
Patch0:         PyYAML-CVE-2017-18342.patch
Patch1:         ConstructorError_fix.patch
Patch2:         change_default_loader.patch
Patch3:         PyYAML-lib3-CVE-2017-18342.patch

%description
YAML parser and emitter for Python

%package -n     python3-PyYAML
Summary:        YAML parser and emitter for Python
BuildRequires:  libyaml-devel
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-libs
Requires:       libyaml
Requires:       python3
Requires:       python3-libs
Provides:       python3-yaml = %{version}-%{release}

%description -n python3-PyYAML
YAML is a data serialization format designed for human readability and
interaction with scripting languages.  PyYAML is a YAML parser and
emitter for Python.

PyYAML features a complete YAML 1.1 parser, Unicode support, pickle
support, capable extension API, and sensible error messages.  PyYAML
supports standard YAML tags and provides Python-specific tags that allow
to represent an arbitrary Python object.

PyYAML is applicable for a broad range of tasks from complex
configuration files to object serialization and persistence.

%prep
%autosetup -p 1 -n PyYAML-%{version}

%build
%py3_build

%install
mkdir -p %{buildroot}%{_bindir}
python3 setup.py install --skip-build --prefix=%{_prefix} --root=%{buildroot}
chmod a-x examples/yaml-highlight/yaml_hl.py

%check
%python3 setup.py test

%files -n python3-PyYAML
%defattr(-,root,root,-)
%license LICENSE
%doc PKG-INFO README examples
%{python3_sitelib}/*

%changelog
* Fri Oct 01 2021 Thomas Crain <thcrain@microsoft.com> - 3.13-7
- Add license to python3 package
- Remove python2 package
- Lint spec

* Thu Feb 04 2021 Joe Schmitt <joschmit@microsoft.com> - 3.13-6
- Provide python3-yaml
- Update URLs to https

* Sat May 09 2020 Nick Samson <nisamson@microsoft.com> - 3.13-5
- Added %%license line automatically

* Tue Sep 03 2019 Mateusz Malisz <mamalisz@microsoft.com> 3.13-4
- Initial CBL-Mariner import from Photon (license: Apache2).

* Tue Apr 16 2019 Tapas Kundu <tkundu@vmware.com> 3.13-3
- Added lib3 changes for CVE-2017-18342
- change default loader for yaml.add_constructor
- Add custom constructors to multiple loaders

* Thu Mar 28 2019 Ankit Jain <ankitja@vmware.com> 3.13-2
- Fix for CVE-2017-18342

* Thu Sep 20 2018 Tapas Kundu <tkundu@vmware.com> 3.13-1
- Updated to release 3.13

* Tue May 16 2017 Kumar Kaushik <kaushikk@vmware.com> 3.12-2
- Adding python3 support.

* Tue Apr 18 2017 Dheeraj Shetty <dheerajs@vmware.com> 3.12-1
- Updated version to 3.12

* Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 3.11-2
- GA - Bump release of all rpms

* Wed Mar 04 2015 Mahmoud Bassiouny <mbassiouny@vmware.com>
- Initial packaging for Photon
