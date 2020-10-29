Name:           perl-HTML-Parser
Version:        3.75
Release:        1
Summary:        HTML parser
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/HTML-Parser
Source0:        https://cpan.metacpan.org/authors/id/C/CA/CAPOEIRAB/HTML-Parser-%{version}.tar.gz

BuildRequires:  coreutils findutils glibc-common
BuildRequires:  perl-devel perl-generators perl-interpreter perl(Carp)
BuildRequires:  perl(Config) perl(Exporter) perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec) perl(FileHandle) perl(HTML::Tagset) >= 3
BuildRequires:  perl(HTTP::Headers) perl(IO::File) perl(SelectSaver)
BuildRequires:  perl(strict) perl(Test) perl(Test::More) perl(threads)
BuildRequires:  perl(URI) perl(vars) perl(XSLoader)
Requires:       perl(HTML::Tagset) >= 3 perl(HTTP::Headers) perl(IO::File) perl(URI)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(HTML::Tagset\\)$

%description
Objects of the HTML::Parser class will recognize markup and separate it
from plain text (alias data content) in HTML documents. As different kinds
of markup and text are recognized, the corresponding event handlers are invoked.

%package help
Summary:        Man pages for perl-HTML-Parser

%description help
Man pages for perl-HTML-Parser.

%prep
%autosetup -n  HTML-Parser-%{version} -p1
chmod -c a-x eg/*

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1
%make_build

%install
make pure_install DESTDIR=%{buildroot}


%check
make test

%files
%{perl_vendorarch}/HTML/
%{perl_vendorarch}/auto/HTML/
%exclude /usr/lib64/perl5/perllocal.pod

%files help
%doc Changes README TODO eg/
%{_mandir}/man3/*.3pm*

%changelog
* Thu Oct 29 2020 SimpleUpdate Robot <tc@openeuler.org> - 3.75-1
- Upgrade to version 3.75

* Mon Oct 21 2019 Zaiwang Li <lizaiwang1@huawei.com> - 3.72-16
- Init Package.

