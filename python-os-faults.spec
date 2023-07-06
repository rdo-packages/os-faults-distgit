%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
# we are excluding some BRs from automatic generator
%global excluded_brs doc8 bandit pre-commit hacking flake8-import-order pytest-html pytest-logging
# Exclude sphinx from BRs if docs are disabled
%if ! 0%{?with_doc}
%global excluded_brs %{excluded_brs} sphinx openstackdocstheme
%endif
%global with_doc %{!?_without_doc:0}%{?_without_doc:1}

%global sname os-faults
%global pypi_name os_faults

%{?dlrn: %global tarsources %{pypi_name}-%{upstream_version}}
%{!?dlrn: %global tarsources %{sname}}

%global common_desc \
OSFaults **OpenStack faultinjection library**The library does destructive \
actions inside an OpenStack cloud. It provides an abstraction layer over \
different types of cloud deployments. The actions are implemented as drivers \
(e.g. DevStack driver, Libvirt driver, IPMI driver).

Name:           python-%{sname}
Version:        XXX
Release:        XXX
Summary:        OpenStack fault-injection library

License:        Apache-2.0
URL:            http://git.openstack.org/cgit/openstack/%{sname}
Source0:        https://opendev.org/performa/%{sname}/archive/%{upstream_version}.tar.gz
BuildArch:      noarch

BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  openstack-macros
BuildRequires:  /usr/bin/which

BuildRequires: (python3dist(ansible) or ansible-core >= 2.11)


%description
%{common_desc}

%package -n     python3-%{sname}
Summary:        OpenStack fault-injection library

Requires:       (python3dist(ansible) >= 2.2 or ansible-core >= 2.11)
Requires:       /usr/bin/which

%description -n python3-%{sname}
%{common_desc}

%package -n     python3-%{sname}-libvirt
Summary:        OpenStack fault-injection library libvirt plugin

Requires:       python3-%{sname} = %{version}-%{release}

%description -n python3-%{sname}-libvirt
%{common_desc}

It contains libvirt plugin for OpenStack faultinjection library.

%package -n      python3-%{sname}-tests
Summary:         OpenStack fault-injection library
Requires:        python3-%{sname} = %{version}-%{release}

Requires:        python3-pytest
Requires:        python3-ddt
Requires:        python3-mock
Requires:        python3-subunit
Requires:        python3-oslotest
Requires:        python3-testrepository
Requires:        python3-testscenarios
Requires:        python3-testtools
Requires:        python3-appdirs

%description -n  python3-%{sname}-tests
%{common_desc}

It contains unittests for OpenStack faultinjection library.

%if 0%{?with_doc}
%package -n python-%{sname}-doc
Summary:        os_faults documentation

%description -n python-%{sname}-doc
%{common_desc}

It contains the documentation for OpenStack faultinjection library.
%endif

%prep
%autosetup -n %{tarsources} -S git

# The test relies on binary 'ansible-playbook' but ansible-python3
# in Fedora doesn't provide it, so need to hack test file.
sed -i 's/ansible-playbook/ansible-playbook-3/' os_faults/ansible/executor.py

# sphinxcontrib-programoutput is required by os-faults while building
# sphinx doc theme. sphinxcontrib-programoutput is dependent on js-query
# while js-query starts pulling lots of node.js dependency.
# So, removing sphinxcontrib-programoutput dependency.
sed -i '/sphinxcontrib.programoutput/d' doc/source/conf.py
sed -i '/sphinx.ext.autosectionlabel/d' doc/source/conf.py

sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini
sed -i "s/^deps = -c{env:.*_CONSTRAINTS_FILE.*/deps =/" tox.ini
sed -i /^minversion.*/d tox.ini
sed -i /^requires.*virtualenv.*/d tox.ini
sed -i 's/--html=[^\ ]*//;s/--self-contained-html//' tox.ini

# Exclude some bad-known BRs
for pkg in %{excluded_brs}; do
  for reqfile in doc/requirements.txt test-requirements.txt; do
    if [ -f $reqfile ]; then
      sed -i /^${pkg}.*/d $reqfile
    fi
  done
done

# Automatic BR generation
%generate_buildrequires
%if 0%{?with_doc}
  %pyproject_buildrequires -t -e %{default_toxenv},docs
%else
  %pyproject_buildrequires -t -e %{default_toxenv}
%endif

%build
%pyproject_wheel

%if 0%{?with_doc}
%tox -e docs
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install

FAULT_EXEC="os-inject-fault os-faults"
for binary in $FAULT_EXEC; do
  # Create a versioned binary for backwards compatibility until everything is pure py3
  ln -s ${binary} %{buildroot}%{_bindir}/${binary}-3
done
# Make executables
for file in %{buildroot}%{python3_sitelib}/%{pypi_name}/ansible/modules/{freeze,kill}.py; do
   chmod a+x $file
done

%check
%tox -e %{default_toxenv}

%files -n python3-%{sname}
%license LICENSE
%doc README.rst
%{_bindir}/os-inject-fault
%{_bindir}/os-inject-fault-3
%{_bindir}/os-faults
%{_bindir}/os-faults-3
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-*.dist-info
%exclude %{python3_sitelib}/%{pypi_name}/tests
%exclude %{python3_sitelib}/%{pypi_name}/drivers/power/libvirt.py*

%files -n python3-%{sname}-libvirt
%license LICENSE
%{python3_sitelib}/%{pypi_name}/drivers/power/libvirt.py*

%files -n python3-%{sname}-tests
%license LICENSE
%{python3_sitelib}/%{pypi_name}/tests

%if 0%{?with_doc}
%files -n python-%{sname}-doc
%license LICENSE
%doc doc/build/html
%endif

%changelog
