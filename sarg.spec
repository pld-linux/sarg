Summary:	Squid log analyzer
Summary(pl):    Analizator logow Squida
Summary(pt_BR): Gerador de relatórios por usuário/ip/nome do squid
Summary(es): generador de informes del squid por utilizador/ip/nombre
Name:		sarg
Version:	1.2.1
Release:	1
License:        GPL
Group:          Networking/System
Group(pl):	Sieciowe/System
Source: 	http://web.onda.com.br/orso/%{name}-%{version}.tar.gz
URL: 	 	http://web.onda.com.br/orso/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:  	sqmgrlog
Requires:  	squid
Requires:	bash
Requires:	sh-utils

%define contentdir      /home/httpd/html/squid-reports

%description
Sarg - Squid Analysis Report Generator is a tool that allow you to view
"where" your users are going to on the Internet.
Sarg generate reports in html, with many fields, like:
users, IP Addresses, bytes, sites and times.

%description -l pt_BR
O Sarg (antigo Sqmgrlog) gera relatórios por usuário/ip/nome baseando-se no
arquivo de log do SQUID.
Os relatórios são gerados em HTML ou por email.

%description -l es
Sarg (era Sqmgrlog) genera informes por utilizador/ip/nombre hacia el fichero
de log del SQUID.
Los informes serán generados en HTML o correo.

%description -l pl
Sarg jest narzêdziem dziêki któremu mo¿esz sprawdzaæ jakie adresy w Internecie odwiedzaj± twoi 
u¿ytkownicy. Sarg generuje raporty w htmlu.

%prep
%setup -q 

%build
%configure2_13 \
	 --enable-sysconfdir=%{_sysconfdir}/%{name}

%{__make}

%install
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}/%{name},%{contentdir}}
%{__make} BINDIR=$RPM_BUILD_ROOT%{_bindir} SYSCONFDIR=$RPM_BUILD_ROOT%{_sysconfdir}/%{name} install
install  sarg.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/sarg.conf
cp -rf languages $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}

gzip -9nf README  CONTRIBUTORS ChangeLog

%post
alias sarg='sarg -l /var/log/squid/access.log'
echo "language Polish" >> /etc/sarg/sarg.conf
echo "charset Latin2" >> /etc/sarg/sarg.conf


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(755,root,root,644)
%{_bindir}/sarg
%config(noreplace) %{_sysconfdir}/%{name}/sarg.conf
%config(noreplace) %{_sysconfdir}/%{name}/exclude_codes
%{_sysconfdir}/%{name}/languages/*
%dir %{contentdir} 
%doc *.gz
