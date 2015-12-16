%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}

%global gem_name http_connection

Summary: RightScale's robust HTTP/S connection module
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.4.1
Release: 9%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/appoxy/http_connection
Source0: http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: %{?scl_prefix}rubygem(right_http_connection)

%description
Rightscale::HttpConnection is a robust HTTP(S) library. It implements a retry
algorithm for low-level network errors.

%prep

%build
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
%{?scl:scl enable %{scl} - << \EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/README.txt
%doc %{gem_docdir}
%exclude %{gem_cache}
%{gem_spec}


%changelog
* Fri Mar 21 2014 Vít Ondruch <vondruch@redhat.com> - 1.4.1-9
- Rebuid against new scl-utils to depend on -runtime package.
  Resolves: rhbz#1069109

* Thu May 30 2013 Josef Stribny <jstribny@redhat.com> - 1.4.1-8
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Wed Feb 27 2013 Vít Ondruch <vondruch@redhat.com> - 1.4.1-7
- Rebuild to fix documentation vulnerability due to CVE-2013-0256.

* Thu Jul 26 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.4.1-6
- Specfile cleanup

* Tue Apr 03 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.4.1-5
- Rebuilt for scl.

* Mon Jan 23 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.4.1-4
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 16 2011 Michal Fojtik <mfojtik@redhat.com> - 1.4.1-2
- Added rubygem-right_http_connection to Provide and Obsolete

* Thu Jun 16 2011 Michal Fojtik <mfojtik@redhat.com> - 1.4.1-1
- Renaming package rubygem-right_http_connection

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Mar 03 2010 Michal Fojtik <mfojtik@redhat.com> - 1.2.4-2
- Fixed duplicated files
- Fixed ruby dependency

* Wed Mar 03 2010 Michal Fojtik <mfojtik@redhat.com> - 1.2.4-1
- Initial package
