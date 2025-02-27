%define version       0.98
%define release       %mkrel 2

%define mecab_version 0.98

Name:       mecab-ruby
Summary:    Ruby binding of mecab
Version:    %{version}
Release:    %{release}
License:    LGPLv2+
Group:      System/Internationalization
URL:        https://mecab-ruby.sourceforge.jp/
Source0:    http://sourceforge.net/projects/mecab/files/%{name}/%{version}/%{name}-%{version}.tar.gz
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


