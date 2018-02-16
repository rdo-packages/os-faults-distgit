%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global with_doc %{!?_without_doc:0}%{?_without_doc:1}

%global sname os-faults
%global pypi_name os_faults

%if 0%{?fedora}
# Disabling python 3 as Ansible is not yet ported to Python3.
# Package does not support python3.
%global with_python3 0
%endif

%global common_desc \
OSFaults **OpenStack faultinjection library**The library does destructive \
actions inside an OpenStack cloud. It provides an abstraction layer over \
different types of cloud deployments. The actions are implemented as drivers \
(e.g. DevStack driver, Fuel driver, Libvirt driver, IPMI driver).

Name:           python-%{sname}
Version:        XXX
Release:        XXX
Summary:        OpenStack fault-injection library

License:        ASL 2.0
URL:            http://git.openstack.org/cgit/openstack/%{sname}
Source0:        https://tarballs.openstack.org/%{sname}/%{pypi_name}-%{upstream_version}.tar.gz
BuildArch:      noarch

BuildRequires:  git
BuildRequires:  python2-devel
BuildRequires:  python2-pbr
BuildRequires:  python2-setuptools
# Test requirements
BuildRequires:  python2-pytest
BuildRequires:  python2-ddt
BuildRequires:  python2-mock
BuildRequires:  python2-subunit
BuildRequires:  python2-oslotest
BuildRequires:  python2-testrepository
BuildRequires:  python2-testscenarios
BuildRequires:  python2-testtools
BuildRequires:  python2-pyghmi
BuildRequires:  libvirt-python
BuildRequires:  python2-appdirs
BuildRequires:  python2-jsonschema
BuildRequires:  PyYAML
BuildRequires:  ansible
BuildRequires:  python2-oslo-utils
BuildRequires:  python2-oslo-serialization
BuildRequires:  python2-oslo-i18n
BuildRequires:  python-click
BuildRequires:  openstack-macros

%description
%{common_desc}

%package -n     python2-%{sname}
Summary:        OpenStack fault-injection library
%{?python_provide:%python_provide python2-%{sname}}

Requires:       python2-pbr >= 2.0.0
Requires:       ansible >= 2.2
Requires:       python2-appdirs >= 1.3.0
Requires:       python2-jsonschema >= 2.6.0
Requires:       python-click
Requires:       python2-iso8601 >= 0.1.11
Requires:       python2-oslo-i18n >= 3.15.3
Requires:       python2-oslo-serialization >= 2.18.0
Requires:       python2-oslo-utils >= 3.33.0
Requires:       python2-pyghmi
Requires:       PyYAML >= 3.10
Requires:       python2-six >= 1.10.0

%description -n python2-%{sname}
%{common_desc}

%package -n     python2-%{sname}-libvirt
Summary:        OpenStack fault-injection library libvirt plugin

Requires:       python2-%{sname} = %{version}-%{release}
Requires:       libvirt-python

%description -n python2-%{sname}-libvirt
%{common_desc}

It contains libvirt plugin for OpenStack faultinjection library.

%package -n      python2-%{sname}-tests
Summary:         OpenStack fault-injection library
Requires:        python2-%{sname} = %{version}-%{release}

Requires:        python2-pytest
Requires:        python2-ddt
Requires:        python2-mock
Requires:        python2-subunit
Requires:        python2-oslotest
Requires:        python2-testrepository
Requires:        python2-testscenarios
Requires:        python2-testtools
Requires:        python2-appdirs

%description -n  python2-%{sname}-tests
%{common_desc}

It contains unittests for OpenStack faultinjection library.

%if 0%{?with_python3}
%package -n     python3-%{sname}
Summary:        OpenStack fault-injection library
%{?python_provide:%python_provide python3-%{sname}}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools

# Test requirements
BuildRequires:  python3-pytest
BuildRequires:  python3-ddt
BuildRequires:  python3-subunit
BuildRequires:  python3-oslotest
BuildRequires:  python3-testrepository
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
BuildRequires:  python3-pyghmi
BuildRequires:  libvirt-python3
BuildRequires:  python3-appdirs
BuildRequires:  python3-jsonschema
BuildRequires:  python3-PyYAML
BuildRequires:  python3-ansible
BuildRequires:  python3-oslo-utils
BuildRequires:  python3-oslo-serialization
BuildRequires:  python3-oslo-i18n
BuildRequires:  python3-click

Requires:       python3-pbr >= 2.0.0
Requires:       python3-ansible >= 2.2
Requires:       python3-appdirs >= 1.3.0
Requires:       python3-jsonschema >= 2.6.0
Requires:       python3-click
Requires:       python3-iso8601 >= 0.1.11
Requires:       python3-oslo-i18n >= 3.15.3
Requires:       python3-oslo-serialization >= 2.18.0
Requires:       python3-oslo-utils >= 3.33.0
Requires:       python3-pyghmi
Requires:       python3-PyYAML >= 3.10
Requires:       python3-six >= 1.10.0

%description -n python3-%{sname}
%{common_desc}

%package -n      python3-%{sname}-tests
Summary:         OpenStack fault-injection library
Requires:        python3-%{sname} = %{version}-%{release}

Requires:        python3-pytest
Requires:        python3-ddt
Requires:        python3-subunit
Requires:        python3-oslotest
Requires:        python3-testrepository
Requires:        python3-testscenarios
Requires:        python3-testtools
Requires:        python3-appdirs

%description -n  python3-%{sname}-tests
%{common_desc}

It contains unittests for OpenStack faultinjection library.

%package -n     python3-%{sname}-libvirt
Summary:        OpenStack fault-injection library libvirt plugin

Requires:       python3-%{sname} = %{version}-%{release}
Requires:       libvirt-python3

%description -n python3-%{sname}-libvirt
%{common_desc}

It contains libvirt plugin for OpenStack faultinjection library.
%endif

%if 0%{?with_doc}
%package -n python-%{sname}-doc
Summary:        os_faults documentation

BuildRequires:    python2-sphinx
BuildRequires:    python2-appdirs
BuildRequires:    PyYAML
BuildRequires:    ansible
BuildRequires:    python2-oslo-utils
BuildRequires:    python2-oslo-serialization
BuildRequires:    python2-oslo-i18n
BuildRequires:    python2-jsonschema
BuildRequires:    python-click
BuildRequires:    python-sphinx_rtd_theme

%description -n python-%{sname}-doc
%{common_desc}

It contains the documentation for OpenStack faultinjection library.
%endif

%prep
%autosetup -n %{pypi_name}-%{upstream_version} -S git
%py_req_cleanup

# sphinxcontrib-programoutput is required by os-faults while building
# sphinx doc theme. sphinxcontrib-programoutput is dependent on js-query
# while js-query starts pulling lots of node.js dependency.
# So, removing sphinxcontrib-programoutput dependency.

sed -i '/sphinxcontrib.programoutput/d' doc/source/conf.py
sed -i '/sphinx.ext.autosectionlabel/d' doc/source/conf.py

%build
%py2_build

%if 0%{?with_doc}
%{__python2} setup.py build_sphinx
rm -fr doc/build/html/.doctrees doc/build/html/.buildinfo
%endif

%if 0%{?with_python3}
%py3_build
%endif

%install
FAULT_EXEC="os-inject-fault os-faults"
%if 0%{?with_python3}
%py3_install
for binary in $FAULT_EXEC; do
  cp %{buildroot}/%{_bindir}/$binary %{buildroot}/%{_bindir}/$binary-3
  ln -sf %{_bindir}/$binary-3 %{buildroot}/%{_bindir}/$binary-%{python3_version}
done
# Make executables
for file in %{buildroot}%{python3_sitelib}/%{pypi_name}/ansible/modules/{freeze,fuel_network_mgmt,iptables,kill}.py; do
   chmod a+x $file
done
%endif

%py2_install
for binary in $FAULT_EXEC; do
  cp %{buildroot}/%{_bindir}/$binary %{buildroot}/%{_bindir}/$binary-2
  ln -sf %{_bindir}/$binary-2 %{buildroot}/%{_bindir}/$binary-%{python2_version}
done
# Make executables
for file in %{buildroot}%{python2_sitelib}/%{pypi_name}/ansible/modules/{freeze,fuel_network_mgmt,iptables,kill}.py; do
   chmod a+x $file
done

%check
py.test -vvvv --durations=10 "os_faults/tests/unit"

%if 0%{?with_python3}
py.test-3 -vvvv --durations=10 "os_faults/tests/unit"
%endif

%files -n python2-%{sname}
%license LICENSE
%doc README.rst
%{_bindir}/os-inject-fault
%{_bindir}/os-inject-fault-2
%{_bindir}/os-inject-fault-%{python2_version}
%{_bindir}/os-faults
%{_bindir}/os-faults-2
%{_bindir}/os-faults-%{python2_version}
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-*-py?.?.egg-info
%exclude %{python2_sitelib}/%{pypi_name}/tests
%exclude %{python2_sitelib}/%{pypi_name}/drivers/power/libvirt.py*

%files -n python2-%{sname}-libvirt
%license LICENSE
%{python2_sitelib}/%{pypi_name}/drivers/power/libvirt.py*

%files -n python2-%{sname}-tests
%license LICENSE
%{python2_sitelib}/%{pypi_name}/tests

%if 0%{?with_python3}
%files -n python3-%{sname}
%license LICENSE
%doc README.rst
%{_bindir}/os-inject-fault-3
%{_bindir}/os-inject-fault-%{python3_version}
%{_bindir}/os-faults-3
%{_bindir}/os-faults-%{python3_version}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-*-py?.?.egg-info
%exclude %{python3_sitelib}/%{pypi_name}/tests
%exclude %{python3_sitelib}/%{pypi_name}/drivers/power/libvirt.py*

%files -n python3-%{sname}-tests
%license LICENSE
%{python3_sitelib}/%{pypi_name}/tests

%files -n python3-%{sname}-libvirt
%license LICENSE
%{python3_sitelib}/%{pypi_name}/drivers/power/libvirt.py*
%endif

%if 0%{?with_doc}
%files -n python-%{sname}-doc
%license LICENSE
%doc doc/build/html
%endif
%changelog
