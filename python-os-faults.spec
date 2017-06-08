%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global with_doc %{!?_without_doc:0}%{?_without_doc:1}

%global sname os-faults
%global pypi_name os_faults

%if 0%{?fedora}
# Disabling python 3 as Ansible is not yet ported to Python3.
# Package does not support python3.
%global with_python3 0
%endif

Name:           python-%{sname}
Version:        0.1.11
Release:        1%{?dist}
Summary:        OpenStack fault-injection library

License:        ASL 2.0
URL:            http://git.openstack.org/cgit/openstack/%{sname}
Source0:        https://tarballs.openstack.org/%{sname}/%{pypi_name}-%{upstream_version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  python-setuptools
# Test requirements
BuildRequires:  pytest
BuildRequires:  python-coverage
BuildRequires:  python-ddt
BuildRequires:  python-mock
BuildRequires:  python-subunit
BuildRequires:  python-oslotest
BuildRequires:  python-testrepository
BuildRequires:  python-testscenarios
BuildRequires:  python-testtools
BuildRequires:  python-pyghmi
BuildRequires:  libvirt-python
BuildRequires:  python-appdirs
BuildRequires:  python-jsonschema
BuildRequires:  PyYAML
BuildRequires:  ansible
BuildRequires:  python-oslo-utils
BuildRequires:  python-oslo-serialization
BuildRequires:  python-oslo-i18n
BuildRequires:  python-click

%description
OSFaults **OpenStack faultinjection library**The library does destructive
actions inside an OpenStack cloud. It provides an abstraction layer over
different types of cloud deployments. The actions are implemented as drivers
(e.g. DevStack driver, Fuel driver, Libvirt driver, IPMI driver).

%package -n     python2-%{sname}
Summary:        OpenStack fault-injection library
%{?python_provide:%python_provide python2-%{sname}}

Requires:       python-pbr >= 1.6
Requires:       ansible >= 2.0
Requires:       python-appdirs >= 1.3.0
Requires:       python-jsonschema >= 2.0.0
Requires:       python-click
Requires:       python-iso8601 >= 0.1.9
Requires:       python-oslo-i18n >= 1.5.0
Requires:       python-oslo-serialization >= 1.10.0
Requires:       python-oslo-utils >= 2.4.0
Requires:       python-pyghmi
Requires:       PyYAML >= 3.1.0
Requires:       python-six >= 1.9.0
Requires:       python-setuptools

%description -n python2-%{sname}
 OSFaults **OpenStack faultinjection library**The library does destructive
actions inside an OpenStack cloud. It provides an abstraction layer over
different types of cloud deployments. The actions are implemented as drivers
(e.g. DevStack driver, Fuel driver, Libvirt driver, IPMI driver).

%package -n     python2-%{sname}-libvirt
Summary:        OpenStack fault-injection library libvirt plugin

Requires:       python2-%{sname} = %{version}-%{release}
Requires:       libvirt-python

%description -n python2-%{sname}-libvirt
 OSFaults **OpenStack faultinjection library**The library does destructive
actions inside an OpenStack cloud. It provides an abstraction layer over
different types of cloud deployments. The actions are implemented as drivers
(e.g. DevStack driver, Fuel driver, Libvirt driver, IPMI driver).

It contains libvirt plugin for OpenStack faultinjection library.

%package -n      python2-%{sname}-tests
Summary:         OpenStack fault-injection library
Requires:        python2-%{sname} = %{version}-%{release}

Requires:        pytest
Requires:        python-coverage
Requires:        python-ddt
Requires:        python-mock
Requires:        python-subunit
Requires:        python-oslotest
Requires:        python-testrepository
Requires:        python-testscenarios
Requires:        python-testtools
Requires:        python-appdirs

%description -n  python2-%{sname}-tests
 OSFaults **OpenStack faultinjection library**The library does destructive
actions inside an OpenStack cloud. It provides an abstraction layer over
different types of cloud deployments. The actions are implemented as drivers
(e.g. DevStack driver, Fuel driver, Libvirt driver, IPMI driver).

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
BuildRequires:  python3-coverage
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

Requires:       python3-pbr >= 1.6
Requires:       python3-ansible >= 2.0
Requires:       python3-appdirs >= 1.3.0
Requires:       python3-jsonschema >= 2.0.0
Requires:       python3-click
Requires:       python3-iso8601 >= 0.1.9
Requires:       python3-oslo-i18n >= 1.5.0
Requires:       python3-oslo-serialization >= 1.10.0
Requires:       python3-oslo-utils >= 2.4.0
Requires:       python3-pyghmi
Requires:       python3-PyYAML >= 3.1.0
Requires:       python3-six >= 1.9.0
Requires:       python3-setuptools

%description -n python3-%{sname}
 OSFaults **OpenStack faultinjection library**The library does destructive
actions inside an OpenStack cloud. It provides an abstraction layer over
different types of cloud deployments. The actions are implemented as drivers
(e.g. DevStack driver, Fuel driver, Libvirt driver, IPMI driver).

%package -n      python3-%{sname}-tests
Summary:         OpenStack fault-injection library
Requires:        python3-%{sname} = %{version}-%{release}

Requires:        python3-pytest
Requires:        python3-coverage
Requires:        python3-ddt
Requires:        python3-subunit
Requires:        python3-oslotest
Requires:        python3-testrepository
Requires:        python3-testscenarios
Requires:        python3-testtools
Requires:        python3-appdirs

%description -n  python3-%{sname}-tests
 OSFaults **OpenStack faultinjection library**The library does destructive
actions inside an OpenStack cloud. It provides an abstraction layer over
different types of cloud deployments. The actions are implemented as drivers
(e.g. DevStack driver, Fuel driver, Libvirt driver, IPMI driver).

It contains unittests for OpenStack faultinjection library.

%package -n     python3-%{sname}-libvirt
Summary:        OpenStack fault-injection library libvirt plugin

Requires:       python3-%{sname} = %{version}-%{release}
Requires:       libvirt-python3

%description -n python3-%{sname}-libvirt
 OSFaults **OpenStack faultinjection library**The library does destructive
actions inside an OpenStack cloud. It provides an abstraction layer over
different types of cloud deployments. The actions are implemented as drivers
(e.g. DevStack driver, Fuel driver, Libvirt driver, IPMI driver).

It contains libvirt plugin for OpenStack faultinjection library.
%endif

%if 0%{?with_doc}
%package -n python-%{sname}-doc
Summary:        os_faults documentation

BuildRequires:    python-sphinx
BuildRequires:    python-appdirs
BuildRequires:    PyYAML
BuildRequires:    ansible
BuildRequires:    python-oslo-utils
BuildRequires:    python-oslo-serialization
BuildRequires:    python-oslo-i18n
BuildRequires:    python-jsonschema
BuildRequires:    python-click
BuildRequires:    python-sphinx_rtd_theme

%description -n python-%{sname}-doc
 OSFaults **OpenStack faultinjection library**The library does destructive
actions inside an OpenStack cloud. It provides an abstraction layer over
different types of cloud deployments. The actions are implemented as drivers
(e.g. DevStack driver, Fuel driver, Libvirt driver, IPMI driver).

It contains the documentation for OpenStack faultinjection library.
%endif

%prep
%autosetup -n %{pypi_name}-%{upstream_version} -S git
rm -f test-requirements.txt requirements.txt

# Remove pbr>=2.0.0 version as it is required for pike
sed -i 's/pbr>=2.0.0/pbr/g' setup.py

# sphinxcontrib-programoutput is required by os-faults while building
# sphinx doc theme. sphinxcontrib-programoutput is dependent on js-query
# while js-query starts pulling lots of node.js dependency.
# So, removing sphinxcontrib-programoutput dependency.

sed -i '/sphinxcontrib.programoutput/d' doc/source/conf.py
sed -i '/sphinx.ext.autosectionlabel/d' doc/source/conf.py

%build
%py2_build

%if 0%{?with_doc}
export PYTHONPATH="$( pwd ):$PYTHONPATH"
%{__python2} setup.py build_sphinx
rm -fr doc/build/html/.doctrees doc/build/html/.buildinfo
%endif

%if 0%{?with_python3}
%py3_build
%endif

%install
%if 0%{?with_python3}
%py3_install
# Make executables
for file in %{buildroot}%{python3_sitelib}/%{pypi_name}/ansible/modules/{freeze,fuel_network_mgmt,iptables,kill}.py; do
   chmod a+x $file
done
cp %{buildroot}/%{_bindir}/os-inject-fault %{buildroot}/%{_bindir}/os-inject-fault-3
ln -sf %{_bindir}/os-inject-fault-3 %{buildroot}/%{_bindir}/os-inject-fault-%{python3_version}
%endif

%py2_install
cp %{buildroot}/%{_bindir}/os-inject-fault %{buildroot}/%{_bindir}/os-inject-fault-2
ln -sf %{_bindir}/os-inject-fault-2 %{buildroot}/%{_bindir}/os-inject-fault-%{python2_version}
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
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-*-py?.?.egg-info
%exclude %{python2_sitelib}/%{pypi_name}/tests
%exclude %{python2_sitelib}/%{pypi_name}/drivers/libvirt_driver.py*

%files -n python2-%{sname}-libvirt
%license LICENSE
%{python2_sitelib}/%{pypi_name}/drivers/libvirt_driver.py*

%files -n python2-%{sname}-tests
%license LICENSE
%{python2_sitelib}/%{pypi_name}/tests

%if 0%{?with_python3}
%files -n python3-%{sname}
%license LICENSE
%doc README.rst
%{_bindir}/os-inject-fault-3
%{_bindir}/os-inject-fault-%{python3_version}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-*-py?.?.egg-info
%exclude %{python3_sitelib}/%{pypi_name}/tests
%exclude %{python3_sitelib}/%{pypi_name}/drivers/libvirt_driver.py*

%files -n python3-%{sname}-tests
%license LICENSE
%{python3_sitelib}/%{pypi_name}/tests

%files -n python3-%{sname}-libvirt
%license LICENSE
%{python3_sitelib}/%{pypi_name}/drivers/libvirt_driver.py*
%endif

%if 0%{?with_doc}
%files -n python-%{sname}-doc
%license LICENSE
%doc doc/build/html
%endif
%changelog
* Thu Jun 08 2017 Chandan Kumar <chkumar@redhat.com> 0.1.11-1
- Bump to version 0.1.11
- Remove pbr >= 2.0.0 version from setup.py
- Removed os-faults binary

* Fri Feb 10 2017 Alfredo Moralejo <amoralej@redhat.com> 0.1.10-1
- Update to 0.1.10

# REMOVEME: error caused by commit http://git.openstack.org/cgit/openstack/os-faults/commit/?id=19989b16257c9b8d527adc8fa88f35089c0a4194
