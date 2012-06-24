%include /usr/lib/rpm/macros.python
Summary:	Python extension for Emacs
Summary(pl):	Rozszerzenie Python dla Emacsa
Name:		emacs-pymacs
Version:	0.15
Release:	3
License:	GPL v2
Group:		Applications/Editors/Emacs
Source0:	http://www.iro.umontreal.ca/~pinard/pymacs/pymacs-%{version}.tar.gz
# Source0-md5:	0c4b2598480d7f89fc35eec487276626
Patch0:		%{name}-userinstall.patch
URL:		http://www.iro.umontreal.ca/~pinard/pymacs/
BuildRequires:	emacs
BuildRequires:	python-devel >= 2.2
BuildRequires:	rpm-pythonprov
%pyrequires_eq    python
Requires:	emacs >= 21.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	pymacs

%description
Pymacs is a powerful tool which, once started from Emacs, allows
both-way communication between Emacs LISP and Python. Yet, Pymacs aims
Python as an extension language for Emacs. Within Emacs LISP code, one
may load and use Python modules. Python functions may themselves use
Emacs services, and handle LISP objects kept in LISP space.

%description -l pl
Pymacs jest pot�nym narz�dziem, kt�re po uruchomieniu z Emacsa
pozwala na dwukierunkow� komunikacj� pomi�dzy Emacs LISP oraz
Pythonem. Pymacs pozwala na �adowanie i u�ywanie modu��w Pythona z
Emacs LISP. Z kolei funkcje pythona mog� u�ywa� us�ug Emacsa oraz
obs�ugiwa� obiekty LISPa znajduj�ce si� w przestrzeni LISPa.

%prep
%setup -q -n pymacs-%{version}
%patch0 -p1

%build
./setup -u \
	-b %{_bindir} \
	-l %{_datadir}/emacs/site-lisp \
	-p %{py_sitedir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/emacs/site-lisp,%{py_sitedir}}

./setup \
	-b $RPM_BUILD_ROOT%{_bindir} \
	-l $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp \
	-p $RPM_BUILD_ROOT%{py_sitedir} \
	install

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog* README THANKS* TODO
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/*.py?
%{_datadir}/emacs/site-lisp/*.elc
