Summary:	KeePassX command line interface
Name:		kpcli
Version:	3.0
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Applications
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.pl
# Source0-md5:	b03cac8d6a7345ea45eaa52ccca18ed1
Source1:	http://downloads.sourceforge.net/%{name}/README
# Source1-md5:	4604f092c09bcb8b659465deb3b90f9b
URL:		http://kpcli.sourceforge.net/
Requires:	perl-Crypt-Rijndael
Requires:	perl-Term-ReadKey
Requires:	perl-Sort-Naturally
Requires:	perl-File-KeePass
# required one of Term::ReadLine::*
Requires:	perl-Term-ReadLine-Gnu
Requires:	perl-Term-ShellUI
Suggests:	perl-Clipboard
Suggests:	perl-Tiny-Capture
Suggests:	perl-Data-Password
Suggests:	perl-Crypt-PWSafe3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A command line interface (interactive shell) to work with KeePass 1.x or 2.x database files.

%prep
%setup -q -c -T
cp %{SOURCE0} kpcli.pl
cp %{SOURCE1} README

%install
rm -rf $RPM_BUILD_ROOT

%{__install} -d $RPM_BUILD_ROOT%{_bindir}
%{__install} kpcli.pl $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
