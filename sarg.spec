Summary:	Squid log analyzer
Summary(es):	generador de informes del squid por utilizador/ip/nombre
Summary(pl):	Analizator logów Squida
Summary(pt_BR):	Gerador de relatórios por usuário/ip/nome do squid
Name:		sarg
Version:	1.2.1
Release:	1
License:	GPL v2
Group:		Networking
Source0:	http://web.onda.com.br/orso/%{name}-%{version}.tar.gz
Source1:	%{name}.conf
URL:		http://web.onda.com.br/orso/
BuildRequires:	autoconf
BuildRequires:	automake
Requires:	squid
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	sqmgrlog

%define		contentdir	/home/httpd/html/squid-reports

%description
Sarg - Squid Analysis Report Generator is a tool that allow you to
view "where" your users are going to on the Internet. Sarg generate
reports in html, with many fields, like: users, IP Addresses, bytes,
sites and times.

%description -l es
Sarg (era Sqmgrlog) genera informes por utilizador/ip/nombre hacia el
fichero de log del SQUID. Los informes serán generados en HTML o
correo.

%description -l pl
Sarg jest narzêdziem dziêki któremu mo¿esz sprawdzaæ jakie adresy w
Internecie odwiedzaj± twoi u¿ytkownicy. Sarg generuje raporty w
HTML-u.

%description -l pt_BR
O Sarg (antigo Sqmgrlog) gera relatórios por usuário/ip/nome
baseando-se no arquivo de log do SQUID. Os relatórios são gerados em
HTML ou por email.

%prep
%setup -q

%build
aclocal
%{__autoconf}
cp %{_datadir}/automake/config.* .
%configure \
	 --enable-sysconfdir=%{_sysconfdir}/%{name}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}/%{name},%{contentdir}}

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	SYSCONFDIR=$RPM_BUILD_ROOT%{_sysconfdir}/%{name}

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

#install  sarg.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/sarg.conf

cp -rf languages $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}

gzip -9nf README CONTRIBUTORS ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sarg
%doc *.gz
%dir %{contentdir}
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}/sarg.conf
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}/exclude_codes
%{_sysconfdir}/%{name}/languages
