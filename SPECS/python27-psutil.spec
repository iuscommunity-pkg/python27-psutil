%global pymajor 2
%global pyminor 7
%global pyver %{pymajor}.%{pyminor}
%global iusver %{pymajor}%{pyminor}
%global __python2 %{_bindir}/python%{pyver}
%global python2_sitelib  %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")
%global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")
%global __os_install_post %{__python27_os_install_post}
%global srcname psutil
%global src %(echo %{srcname} | cut -c1)

# Filter Python modules from Provides
%{?filter_setup:
%filter_provides_in %{python2_sitearch}/.*\.so$
%filter_setup
}

Name:           python%{iusver}-%{srcname}
Version:        5.2.1
Release:        1.ius%{?dist}
Summary:        A process and system utilities module for Python
Vendor:         IUS Community Project
Group:          Development/Languages
License:        BSD
URL:            https://github.com/giampaolo/psutil
Source0:        https://files.pythonhosted.org/packages/source/p/psutil/psutil-%{version}.tar.gz
BuildRequires:  python%{iusver}-devel
BuildRequires:  python%{iusver}-setuptools

%if 0%{?el5}
BuildRequires:  gcc44
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
%endif


%description
psutil is a module providing an interface for retrieving information on all
running processes and system utilization (CPU, memory, disks, network, users) in
a portable way by using Python, implementing many functionalities offered by
command line tools such as: ps, top, df, kill, free, lsof, free, netstat,
ifconfig, nice, ionice, iostat, iotop, uptime, pidof, tty, who, taskset, pmap.


%prep
%setup -q -n %{srcname}-%{version}
find %{srcname} -type f -name \*.py -print0 | xargs -0 sed -i -e '1 {/^#!\//d}'


%build
CFLAGS=$RPM_OPT_FLAGS %{__python2} setup.py build


%install
%{?el5:%{__rm} -rf %{buildroot}}
%{__python2} setup.py install --optimize 1 --skip-build --root %{buildroot}


%{?el5:%clean}
%{?el5:%{__rm} -rf %{buildroot}}

%files
%doc CREDITS HISTORY.rst LICENSE README.rst
%{python2_sitearch}/*


%changelog
* Fri Mar 24 2017 Carl George <carl.george@rackspace.com> - 5.2.1-1.ius
- Latest upstream

* Mon Mar 06 2017 Ben Harper <ben.harper@rackspace.com> - 5.2.0-1.ius
- Latest upstream

* Thu Feb 16 2017 Ben Harper <ben.harper@rackspace.com> - 5.1.3-1.ius
- Latest upstream

* Wed Feb 01 2017 Ben Harper <ben.harper@rackspace.com> - 5.1.0-1.ius
- Latest upstream

* Wed Dec 21 2016 Carl George <carl.george@rackspace.com> - 5.0.1-1.ius
- Latest upstream

* Tue Nov 08 2016 Ben Harper <ben.harper@rackspace.com> - 5.0.0-1.ius
- Latest upstream

* Mon Oct 24 2016 Carl George <carl.george@rackspace.com> - 4.4.0-1.ius
- Latest upstream

* Fri Sep 02 2016 Ben Harper <ben.harper@rackspace.com> - 4.3.1-1.ius
- Latest upstream

* Mon Jun 20 2016 Ben Harper <ben.harper@rackspace.com> - 4.3.0-1.ius
- Latest upstream

* Mon May 16 2016 Ben Harper <ben.harper@rackspace.com> - 4.2.0-1.ius
- Latest upstream
- update Source0 URL

* Mon Mar 21 2016 Carl George <carl.george@rackspace.com> - 4.1.0-1.ius
- Latest upstream
- Remove shebangs

* Thu Feb 18 2016 Ben Harper <ben.harper@rackspace.com> - 4.0.0-1.ius
- Latest upstream

* Tue Jan 26 2016 Ben Harper <ben.harper@rackspace.com> - 3.4.2-1.ius
- Latest upstream

* Fri Jan 15 2016 Ben Harper <ben.harper@rackspace.com> - 3.4.1-1.ius
- Latest upstream

* Mon Nov 30 2015 Ben Harper <ben.harper@rackspace.com> - 3.3.0-1.ius
- Latest upstream

* Tue Oct 06 2015 Ben Harper <ben.harper@rackspace.com> - 3.2.2-1.ius
- Latest upstream

* Thu Sep 03 2015 Ben Harper <ben.harper@rackspace.com> - 3.2.1-1.ius
- Latest upstream

* Thu Sep 03 2015 Ben Harper <ben.harper@rackspace.com> - 3.2.0-1.ius
- Latest upstream

* Wed Jul 15 2015 Ben Harper <ben.harper@rackspace.com> - 3.1.1-1.ius
- Latest upstream

* Tue Jun 30 2015 Carl George <carl.george@rackspace.com> - 3.0.1-1.ius
- Latest upstream

* Mon Jun 15 2015 Carl George <carl.george@rackspace.com> - 3.0.0-1.ius
- Latest upstream

* Wed Feb 04 2015 Ben Harper <ben.harper@rackspace.com> - 2.2.1-1.ius
- Latest upstream

* Wed Jan 07 2015 Carl George <carl.george@rackspace.com> - 2.2.0-1.ius
- Latest upstream
- Remove unnecessary chmod on so files

* Wed Oct 01 2014 Carl George <carl.george@rackspace.com> - 2.1.3-1.ius
- Latest upstream

* Mon Sep 22 2014 Carl George <carl.george@rackspace.com> - 2.1.2-1.ius
- Latest upstream

* Fri Jun 06 2014 Carl George <carl.george@rackspace.com> - 2.1.1-2.ius
- Override __os_install_post to fix .pyc/pyo magic
- Implement python packaging best practices

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
