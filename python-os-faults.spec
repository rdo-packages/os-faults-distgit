# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %{expand:%{python%{pyver}_sitelib}}
%global pyver_install %{expand:%{py%{pyver}_install}}
%global pyver_build %{expand:%{py%{pyver}_build}}
# End of macros for py2/py3 compatibility
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global with_doc %{!?_without_doc:0}%{?_without_doc:1}

%global sname os-faults
%global pypi_name os_faults

%global common_desc \
OSFaults **OpenStack faultinjection library**The library does destructive \
actions inside an OpenStack cloud. It provides an abstraction layer over \
different types of cloud deployments. The actions are implemented as drivers \
(e.g. DevStack driver, Libvirt driver, IPMI driver).

Name:           python-%{sname}
Version:        0.2.5
Release:        1%{?dist}
Summary:        OpenStack fault-injection library

License:        ASL 2.0
URL:            http://git.openstack.org/cgit/openstack/%{sname}
Source0:        https://tarballs.openstack.org/%{sname}/%{pypi_name}-%{upstream_version}.tar.gz
BuildArch:      noarch

BuildRequires:  git
BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-pbr
BuildRequires:  python%{pyver}-setuptools
# Test requirements
BuildRequires:  python%{pyver}-pytest
BuildRequires:  python%{pyver}-ddt
BuildRequires:  python%{pyver}-mock
BuildRequires:  python%{pyver}-subunit
BuildRequires:  python%{pyver}-oslotest
BuildRequires:  python%{pyver}-testrepository
BuildRequires:  python%{pyver}-testscenarios
BuildRequires:  python%{pyver}-testtools
BuildRequires:  python%{pyver}-pyghmi
BuildRequires:  python%{pyver}-appdirs
BuildRequires:  python%{pyver}-jsonschema
BuildRequires:  python%{pyver}-oslo-concurrency
BuildRequires:  python%{pyver}-oslo-utils
BuildRequires:  python%{pyver}-oslo-serialization
BuildRequires:  python%{pyver}-oslo-i18n
BuildRequires:  openstack-macros
BuildRequires:  /usr/bin/which

# Handle python2 exception
%if %{pyver} == 2
BuildRequires:  libvirt-python
BuildRequires:  PyYAML
BuildRequires:  ansible
BuildRequires:  python-click
%else
BuildRequires:  python%{pyver}-libvirt
BuildRequires:  python%{pyver}-PyYAML
BuildRequires:  python3dist(ansible)
BuildRequires:  python%{pyver}-click
BuildRequires:  /usr/bin/pathfix.py
%endif

%description
%{common_desc}

%package -n     python%{pyver}-%{sname}
Summary:        OpenStack fault-injection library
%{?python_provide:%python_provide python%{pyver}-%{sname}}
%if %{pyver} == 3
Obsoletes: python2-%{sname} < %{version}-%{release}
%endif

Requires:       python%{pyver}-pbr >= 2.0.0
Requires:       python%{pyver}-appdirs >= 1.3.0
Requires:       python%{pyver}-jsonschema >= 2.6.0
Requires:       python%{pyver}-iso8601 >= 0.1.11
Requires:       python%{pyver}-oslo-concurrency >= 3.0.0
Requires:       python%{pyver}-oslo-i18n >= 3.15.3
Requires:       python%{pyver}-oslo-serialization >= 2.18.0
Requires:       python%{pyver}-oslo-utils >= 3.33.0
Requires:       python%{pyver}-pyghmi
Requires:       python%{pyver}-six >= 1.10.0
Requires:       /usr/bin/which

# Handle python2 exception
%if %{pyver} == 2
Requires:       ansible >= 2.2
Requires:       python-click
Requires:       PyYAML >= 3.10
%else
Requires:       python3dist(ansible) >= 2.2
Requires:       python%{pyver}-click
Requires:       python%{pyver}-PyYAML >= 3.10
%endif

%description -n python%{pyver}-%{sname}
%{common_desc}

%package -n     python%{pyver}-%{sname}-libvirt
Summary:        OpenStack fault-injection library libvirt plugin
%{?python_provide:%python_provide python%{pyver}-%{sname}-libvirt}

Requires:       python%{pyver}-%{sname} = %{version}-%{release}

# Handle python2 exception
%if %{pyver} == 2
Requires:       libvirt-python
%else
Requires:       python%{pyver}-libvirt
%endif


%description -n python%{pyver}-%{sname}-libvirt
%{common_desc}

It contains libvirt plugin for OpenStack faultinjection library.

%package -n      python%{pyver}-%{sname}-tests
Summary:         OpenStack fault-injection library
%{?python_provide:%python_provide python%{pyver}-%{sname}-tests}
Requires:        python%{pyver}-%{sname} = %{version}-%{release}

Requires:        python%{pyver}-pytest
Requires:        python%{pyver}-ddt
Requires:        python%{pyver}-mock
Requires:        python%{pyver}-subunit
Requires:        python%{pyver}-oslotest
Requires:        python%{pyver}-testrepository
Requires:        python%{pyver}-testscenarios
Requires:        python%{pyver}-testtools
Requires:        python%{pyver}-appdirs

%description -n  python%{pyver}-%{sname}-tests
%{common_desc}

It contains unittests for OpenStack faultinjection library.

%if 0%{?with_doc}
%package -n python-%{sname}-doc
Summary:        os_faults documentation

BuildRequires:    python%{pyver}-sphinx
BuildRequires:    python%{pyver}-appdirs
BuildRequires:    python%{pyver}-oslo-utils
BuildRequires:    python%{pyver}-oslo-serialization
BuildRequires:    python%{pyver}-oslo-i18n
BuildRequires:    python%{pyver}-jsonschema
BuildRequires:    python%{pyver}-sphinx_rtd_theme

# Handle python2 exception
%if %{pyver} == 2
BuildRequires:    PyYAML
BuildRequires:    python-click
BuildRequires:    ansible
%else
BuildRequires:    python%{pyver}-PyYAML
BuildRequires:    python%{pyver}-click
BuildRequires:    python3dist(ansible)
%endif

%description -n python-%{sname}-doc
%{common_desc}

It contains the documentation for OpenStack faultinjection library.
%endif

%prep
%autosetup -n %{pypi_name}-%{upstream_version} -S git
%py_req_cleanup

# The test relies on binary 'ansible-playbook' but ansible-python3
# in Fedora doesn't provide it, so need to hack test file.
sed -i 's/ansible-playbook/ansible-playbook-%{pyver}/' os_faults/ansible/executor.py

# sphinxcontrib-programoutput is required by os-faults while building
# sphinx doc theme. sphinxcontrib-programoutput is dependent on js-query
# while js-query starts pulling lots of node.js dependency.
# So, removing sphinxcontrib-programoutput dependency.

sed -i '/sphinxcontrib.programoutput/d' doc/source/conf.py
sed -i '/sphinx.ext.autosectionlabel/d' doc/source/conf.py

%build
%{pyver_build}

%if 0%{?with_doc}
%{pyver_bin} setup.py build_sphinx
rm -fr doc/build/html/.doctrees doc/build/html/.buildinfo
%endif

%install
FAULT_EXEC="os-inject-fault os-faults"
%{pyver_install}
for binary in $FAULT_EXEC; do
  # Create a versioned binary for backwards compatibility until everything is pure py3
  ln -s ${binary} %{buildroot}%{_bindir}/${binary}-%{pyver}
done
# Make executables
for file in %{buildroot}%{pyver_sitelib}/%{pypi_name}/ansible/modules/{freeze,kill}.py; do
   chmod a+x $file
   %if %{pyver} == 3
      # Fix shebangs for Python 3-only distros
      pathfix.py -pni "%{__python3} %{py3_shbang_opts}" $file
   %endif
done

%check
py.test-%{pyver} -vvvv --durations=10 "os_faults/tests/unit"

%files -n python%{pyver}-%{sname}
%license LICENSE
%doc README.rst
%{_bindir}/os-inject-fault
%{_bindir}/os-inject-fault-%{pyver}
%{_bindir}/os-faults
%{_bindir}/os-faults-%{pyver}
%{pyver_sitelib}/%{pypi_name}
%{pyver_sitelib}/%{pypi_name}-*-py?.?.egg-info
%exclude %{pyver_sitelib}/%{pypi_name}/tests
%exclude %{pyver_sitelib}/%{pypi_name}/drivers/power/libvirt.py*

%files -n python%{pyver}-%{sname}-libvirt
%license LICENSE
%{pyver_sitelib}/%{pypi_name}/drivers/power/libvirt.py*

%files -n python%{pyver}-%{sname}-tests
%license LICENSE
%{pyver_sitelib}/%{pypi_name}/tests

%if 0%{?with_doc}
%files -n python-%{sname}-doc
%license LICENSE
%doc doc/build/html
%endif

%changelog
* Mon Sep 23 2019 RDO <dev@lists.rdoproject.org> 0.2.5-1
- Update to 0.2.5

