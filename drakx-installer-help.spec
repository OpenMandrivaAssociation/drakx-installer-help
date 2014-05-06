%define destdir %{_docdir}/installer-help

Name:           drakx-installer-help
Version:        4.2
Release:        1
Summary:        Installer help texts
License:        CC-BY-SA
Group:          Development/Other
URL:            https://abf.rosalinux.ru/moondrake/drakx-installer-help
# git clone git@abf.rosalinux.ru:moondrake/drakx-installer-help.git
# cd drakx-installer-help && make dist
Source0:        %{name}-%{version}.tar.xz
BuildArch:      noarch

%description
The help texts for the help buttons in drakx-installer-stage2.


%prep
%setup -q

%build
# nothing to do

%install
mkdir -p %{buildroot}%{destdir}

# HTML pages
install -p -m 644 *.html %{buildroot}%{destdir}

# images
install -p -m 644 *.png %{buildroot}%{destdir}

# translations
for lang in ca cs de el eo es et fr id nl pl pt pt_br ro ru sv tr uk; do
    for file in $lang/*.html $lang/*.png; do
        install -D -p -m 644 $file %{buildroot}%{destdir}/$file
    done
done

for file in $(find . -name "README"); do
     lang=`echo $file|sed 's,./\(.*\)/README,\1,'`
     [ "$file" == "./README" ] || cp $file README-$lang
done

for file in $(find . -name "COPYING"); do
     lang=`echo $file|sed 's,./\(.*\)/COPYING,\1,'`
     [ "$file" == "./COPYING" ] || cp $file COPYING-$lang
done

%files
%doc README NEWS
%doc README-*
%doc COPYING
%doc COPYING-*
%{destdir}/*.html
%{destdir}/*.png
%{destdir}/??/*.html
%{destdir}/??/*.png
%{destdir}/?????/*.html
%{destdir}/?????/*.png
