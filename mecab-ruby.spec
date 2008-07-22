%define version       0.96
%define release       %mkrel 3

%define mecab_version 0.96

Name:       mecab-ruby
Summary:    Ruby binding of mecab
Version:    %{version}
Release:    %{release}
License:    LGPL
Group:      System/Internationalization
URL:        http://mecab-ruby.sourceforge.jp/
Source0:    http://prdownloads.sourceforge.jp/mecab/19468/%{name}-%{version}.tar.bz2
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:      mecab >= %{mecab_version}
BuildRequires: mecab-devel >= %{mecab_version}
BuildRequires: ruby-devel

%description
Ruby binding of mecab.


%prep
%setup -q

%build
%define __libtoolize /bin/true
ruby extconf.rb
make

%install
rm -rf $RPM_BUILD_ROOT

install -d %{buildroot}/%{ruby_sitearchdir}
install -m 0755 MeCab.so %{buildroot}/%{ruby_sitearchdir}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%doc README
%{ruby_sitearchdir}/*.so


