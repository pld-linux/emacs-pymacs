Summary:	Python extension for Emacs
Summary(pl.UTF-8):	Rozszerzenie Python dla Emacsa
Name:		emacs-pymacs
Version:	0.22
Release:	1	
License:	GPL v2
Group:		Applications/Editors/Emacs
Source0:	http://pymacs.progiciels-bpi.ca/archives/Pymacs-%{version}.tar.gz
# Source0-md5:	73b7a641be100fd90a9be59ecf01fd98
URL:		http://pymacs.progiciels-bpi.ca/
BuildRequires:	emacs
BuildRequires:	python-devel >= 2.2
%pyrequires_eq    python
Requires:	emacs >= 21.1
Obsoletes:	pymacs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pymacs is a powerful tool which, once started from Emacs, allows
both-way communication between Emacs LISP and Python. Yet, Pymacs aims
Python as an extension language for Emacs. Within Emacs LISP code, one
may load and use Python modules. Python functions may themselves use
Emacs services, and handle LISP objects kept in LISP space.

%description -l pl.UTF-8
Pymacs jest potężnym narzędziem, które po uruchomieniu z Emacsa
pozwala na dwukierunkową komunikację pomiędzy Emacs LISP oraz
Pythonem. Pymacs pozwala na ładowanie i używanie modułów Pythona z
Emacs LISP. Z kolei funkcje pythona mogą używać usług Emacsa oraz
obsługiwać obiekty LISPa znajdujące się w przestrzeni LISPa.

%prep
%setup -q -n Pymacs-%{version}

%build
emacs -batch -f batch-byte-compile pymacs.el

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_emacs_lispdir}
install pymacs.elc $RPM_BUILD_ROOT%{_emacs_lispdir}

%{__python} setup.py install --root=$RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog* README THANKS* TODO doc/pymacs.pdf
%attr(755,root,root) %{_bindir}/*
%dir %{py_sitescriptdir}/Pymacs
%{py_sitescriptdir}/Pymacs/*.py[co]
%dir %{py_sitescriptdir}/Pymacs/Nn
%{py_sitescriptdir}/Pymacs/Nn/*.py[co]
%dir %{py_sitescriptdir}/Pymacs/Rebox
%{py_sitescriptdir}/Pymacs/Rebox/*.py[co]
%{_emacs_lispdir}/*.elc
