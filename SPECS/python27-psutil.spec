%define __python /usr/bin/python%{pybasever}
%if 0%{?el5}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print (get_python_lib(1))")}
%endif

%global short_name psutil

%define pyver 27
%define pybasever 2.7
%define real_name python-psutil

# Filter Python modules from Provides
%{?filter_setup:
%filter_provides_in %{python_sitearch}/.*\.so$
%filter_setup
}

Name:           python%{pyver}-psutil
Version:        2.1.1
Release:        1.ius%{?dist}
Summary:        A process and system utilities module for Python

Group:          Development/Languages
License:        BSD
URL:            http://psutil.googlecode.com/
#Source0:        http://psutil.googlecode.com/files/%{short_name}-%{version}.tar.gz
Source0:        https://pypi.python.org/packages/source/p/%{short_name}/%{short_name}-%{version}.tar.gz

BuildRequires:  python27-devel

%if 0%{?el5}
BuildRequires:  python27-setuptools
BuildRequires:  gcc44
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
%endif

%description
psutil is a module providing an interface for retrieving information on all
running processes and system utilization (CPU, memory, disks, network, users) in
a portable way by using Python, implementing many functionalities offered by
command line tools such as: ps, top, df, kill, free, lsof, free, netstat,
ifconfig, nice, ionice, iostat, iotop, uptime, pidof, tty, who, taskset, pmap.

%prep
%setup -q -n %{short_name}-%{version}

# Remove shebangs
for file in psutil/*.py; do
  sed -i.orig -e 1d $file && \
  touch -r $file.orig $file && \
  rm $file.orig
done

%build
CFLAGS=$RPM_OPT_FLAGS %{__python} setup.py build


%install
%if 0%{?el5}
rm -rf $RPM_BUILD_ROOT
%endif

%{__python} setup.py install \
  --skip-build \
  --root $RPM_BUILD_ROOT

# Fix permissions
chmod 0755 $RPM_BUILD_ROOT%{python_sitearch}/*.so

%files
%doc CREDITS HISTORY LICENSE README
%{python_sitearch}/%{short_name}/
%{python_sitearch}/*.egg-info
%{python_sitearch}/*.so


%changelog
* Thu May 01 2014 Carl George <carl.george@rackspace.com> - 2.1.1-1.ius
- Latest sources from upstream

* Wed Apr 09 2014 Ben Harper <ben.harper@rackspace.com> - 2.1.0-1.ius
- Latest sources from upstream

* Tue Mar 11 2014 Ben Harper <ben.harper@rackspace.com> - 2.0.0-1.ius
- Latest sources from upstream

* Thu Dec 12 2013 Ben Harper <ben.harper@rackspace.com> - 1.2.1-1.ius
- Latest sources from upstream

* Mon Dec 09 2013 Ben Harper <ben.harper@rackspace.com> - 1.1.3-1.ius
- inital port from EPEL

* Fri Apr 19 2013 Michel Salim <salimma@fedoraproject.org> - 0.6.1-1
- Update to 0.6.1

* Tue Mar 19 2013 Michel Salim <salimma@fedoraproject.org> - 0.4.1-3.2
- Also generate egg-info on EL5

* Sat Mar 16 2013 Michel Salim <salimma@fedoraproject.org> - 0.4.1-3.1
- Conditionally declare and clean buildroot to support el5
- Fix declaration of Python macro, and make it apply only to el5

* Wed Apr 18 2012 Ralph Bean <rbean@redhat.com> - 0.4.1-3
- Added a conditional around with_python3 to support el6.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 16 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.4.1-1
- Update to 0.4.1

* Sun Nov 20 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0

* Mon Jul 18 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0

* Wed Mar 23 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.2.1-1
- Update to 0.2.1
- Spec cleanup

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 22 2010 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0

* Wed Aug 25 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.1.3-5
- rebuild with python3.2
  http://lists.fedoraproject.org/pipermail/devel/2010-August/141368.html

* Fri Jul 30 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.1.3-4
- bump, because previous build nvr already existed in F-14

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Apr 13 2010 ELMORABITY Mohamed <melmorabity@fedoraproject.org> 0.1.3-2
- Add missing popd in %%build

* Sat Mar 27 2010 ELMORABITY Mohamed <melmorabity@fedoraproject.org> 0.1.3-1
- Update to 0.1.3
- Remove useless call to 2to3 and corresponding BuildRequires
  python2-tools (this version supports Python 3)

* Sat Feb 20 2010 ELMORABITY Mohamed <melmorabity@fedoraproject.org> 0.1.2-4
- Change python-utils BuildRequires for python2-utils

* Sat Feb 20 2010 ELMORABITY Mohamed <melmorabity@fedoraproject.org> 0.1.2-3
- Add python3 subpackage

* Thu Jan 14 2010 ELMORABITY Mohamed <melmorabity@fedoraproject.org> 0.1.2-2
- Drop no-shebang patch for a sed command
- Drop test suite from %%doc tag

* Fri Jan  8 2010 ELMORABITY Mohamed <melmorabity@fedoraproject.org> 0.1.2-1
- Initial RPM release
