# enable tests by default, disable with --without tests
%bcond_without tests

Name:           python-rpm-spec
Version:        0.11
Release:        1%{?dist}
Provides:       python3-rpm-spec = 2:%{version}-%{release}
Obsoletes:      python3-rpm-spec < 2:0.7-1
Summary:        Python module for parsing RPM spec files

License:        MIT
URL:            https://github.com/bkircher/python-rpm-spec
Source0:        https://github.com/bkircher/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires: %{py3_dist flit}

%if %{with tests}
BuildRequires:  python3-pytest
%endif

%{?python_provide:%python_provide %{name}}

%description
python-rpm-spec is a Python module for parsing RPM spec files. RPMs are build
from a package's sources along with a spec file. The spec file controls how the
RPM is built. This module allows you to parse spec files and gives you simple
access to various bits of information that is contained in the spec file.

%prep
%autosetup -n %{name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r -x test

%build
%pyproject_wheel

%install
%pyproject_install


%check
%if %{with tests}
py.test-%{python3_version} -vv tests || :
%endif

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/*

%changelog
* Thu Aug 5 2021 Benjamin Kircher <bkircher@0xadd.de> - 0.11-1
- Update to 0.11, rename package to python-rpm-spec, use flit

* Thu Sep 14 2017 Benjamin Kircher <benjamin.kircher@gmail.com> - 0.7-3
- Amend missing Provides and Obsoletes

* Tue Sep 12 2017 Benjamin Kircher <benjamin.kircher@gmail.com> - 0.7-2
- Make package adhere naming guidelines

* Thu Aug 10 2017 Benjamin Kircher <benjamin.kircher@gmail.com> - 0.7-1
- New version

* Thu Jul 27 2017 Benjamin Kircher <benjamin.kircher@gmail.com> - 0.6-1
- New version

* Sat Mar 25 2017 Benjamin Kircher <benjamin.kircher@gmail.com> - 0.5-1
- New version

* Thu Feb 09 2017 Benjamin Kircher <benjamin.kircher@gmail.com> - 0.4-1
- New version, allow disabling tests

* Fri Jan 27 2017 Benjamin Kircher <benjamin.kircher@gmail.com> - 0.3-1
- New version

* Thu Jan 26 2017 Benjamin Kircher <benjamin.kircher@gmail.com> - 0.2-1
- Initial spec
