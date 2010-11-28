# Default provider build options (MySQL, Postgres, SQLite, SQLCipher)

%define           IBMDB2   0
%define           ORACLE   0
%define           SYBASE   0
%define           LDAP     0
%define           MDB      0
%define           MYSQL    1
%define           ODBC     0
%define           POSTGRES 1
%define           FREETDS  0
%define           XBASE    0
%define           JAVA     0

%{?_with_db2:%define IBMDB2     1}
%{?_with_oracle:%define ORACLE  1}
%{?_with_sybase:%define SYBASE  1}
%{?_without_ldap:%define LDAP   0}
%{?_without_mdb:%define MDB     0}
%{?_without_mysql:%define MYSQL 0}
%{?_without_odbc:%define ODBC   0}
%{?_without_postgres:%define POSTGRES 0}
%{?_without_tds:%define FREETDS 0}
%{?_without_xbase:%define XBASE 0}
%{?_with_java:%define JAVA 1}

Name:             libgda
Epoch:            1
Version:          4.2.2
Release:          1%{?dist}
Summary:          Library for unified database access/ 
Group:            System Environment/Libraries
License:          LGPLv2+
URL:              http://www.gnome-db.org/
Source:           http://ftp.gnome.org/pub/GNOME/sources/%{name}/4.0/%{name}-%{version}.tar.bz2
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:    pkgconfig >= 0.8
BuildRequires:    glib2-devel >= 2.16
BuildRequires:	  gtk2-devel >= 2.20.0
BuildRequires:	  unique-devel >= 1.1.6
BuildRequires:	  gtksourceview2-devel >= 2.10.0
BuildRequires:	  goocanvas-devel >= 0.15
BuildRequires: 	  graphviz-devel >= 2.26.0
BuildRequires:	  iso-codes >= 3.15
BuildRequires:    libxslt-devel >= 1.0.9
BuildRequires:    sqlite-devel >= 3.6.0
BuildRequires:    gamin-devel >= 0.1.8
BuildRequires:    libtool
BuildRequires:    gobject-introspection-devel >= 0.6.5
BuildRequires:    libxml2-devel readline-devel db4-devel json-glib-devel
BuildRequires:    gtk-doc scrollkeeper intltool gettext flex bison perl(XML::Parser)
BuildRequires:    gnome-vfs2-devel >= 2.20
BuildRequires:    libsoup-devel
BuildRequires:	  java-1.6.0-openjdk >= 1.6.0.0
BuildRequires:    gnome-doc-utils
# note we do not provide these, they no longer exist
Obsoletes:        %{name}-sharp < %{epoch}:%{version}-%{release}
Obsoletes:        %{name}-sharp-devel < %{epoch}:%{version}-%{release}

Obsoletes:        %{name}-freetds < %{epoch}:3.99.0
Obsoletes:        %{name}-freetds-devel < %{epoch}:3.99.0
Obsoletes:        %{name}-ldap < %{epoch}:3.99.0
Obsoletes:        %{name}-ldap-devel < %{epoch}:3.99.0
Obsoletes:        %{name}-odbc < %{epoch}:3.99.0
Obsoletes:        %{name}-odbc-devel < %{epoch}:3.99.0
Obsoletes:        %{name}-xbase < %{epoch}:3.99.0
Obsoletes:        %{name}-xbase-devel < %{epoch}:3.99.0

%if %{FREETDS}
BuildRequires:    freetds-devel >= 0.82-2
%endif

%if %{MYSQL}
BuildRequires:    mysql-devel
%endif

%if %{POSTGRES}
BuildRequires:    postgresql-devel
%endif

%if %{ODBC}
BuildRequires:    unixODBC-devel
%endif

%if %{MDB}
BuildRequires:    mdbtools-devel
%endif

%if %{LDAP}
BuildRequires:    openldap-devel
%endif

%if %{XBASE}
BuildRequires:    xbase-devel
%endif

%if %{JAVA}
BuildRequires:    java-1.6.0-openjdk-devel
%endif

%description
libgda is a library that eases the task of writing
database programs.

%package devel
Summary:          Development libraries and header files for libgda
Group:            Development/Libraries
Requires:         glib2-devel >= 2.0.0
Requires:         libxslt-devel >= 1.0.9
Requires:         db4-devel libxml2-devel pkgconfig
Requires:         %{name} = %{epoch}:%{version}-%{release}

%description devel
This package contains the header files and libraries needed to write
or compile programs that use libgda.

%package ui
Summary:          Libgda UI extensions
Group:            Development/Libraries
Requires:         %{name} = %{epoch}:%{version}-%{release}

%description ui
libgda-ui extends libgda providing graphical widgets (Gtk+).

%package ui-devel
Summary:          Development libraries and header files for libgda-ui
Group:            Development/Libraries
Requires:         %{name}-ui = %{epoch}:%{version}-%{release}
Requires:         %{name}-devel = %{epoch}:%{version}-%{release}
Requires:	  gtk2-devel >= 2.20.0

%description ui-devel
This package contains the header files and libraries needed to write
or compile programs that use libgda-ui.

%package tools
Summary:	  Graphical tools for libgda
Group:		  Applications/Databases
Requires:	  %{name}-ui = %{epoch}:%{version}-%{release}

%description tools
This package provides libgda graphical tools.

%package sqlite
Summary:          SQLite provider for libgda
Group:            System Environment/Libraries
Requires:         %{name} = %{epoch}:%{version}-%{release}
Obsoletes:        gda-sqlite < %{epoch}:%{version}-%{release}
Provides:         gda-sqlite = %{epoch}:%{version}-%{release}
%description sqlite
This package includes the libgda SQLite provider.

%package sqlite-devel
Summary:          SQLite provider for libgda pkgconfig file
Group:            Development/Libraries
Requires:         pkgconfig
Requires:         %{name}-sqlite = %{epoch}:%{version}-%{release}
%description sqlite-devel
This package includes the pkgconfig file for the libgda SQLite provider.

%package sqlcipher
Summary:          SQLite provider for libgda
Group:            System Environment/Libraries
Requires:         %{name} = %{epoch}:%{version}-%{release}
Obsoletes:        gda-sqlite < %{epoch}:%{version}-%{release}
Provides:         gda-sqlite = %{epoch}:%{version}-%{release}
%description sqlcipher
This package includes the libgda SQLCipher provider.

%package sqlcipher-devel
Summary:          SQLite provider for libgda pkgconfig file
Group:            Development/Libraries
Requires:         pkgconfig
Requires:         %{name}-sqlite = %{epoch}:%{version}-%{release}
%description sqlcipher-devel
This package includes the pkgconfig file for the libgda SQLCipher provider.

%package web
Summary:          web provider for libgda
Group:            System Environment/Libraries
Requires:         %{name} = %{epoch}:%{version}-%{release}
%description web
This package includes the libgda web provider.

%package web-devel
Summary:          web provider for libgda pkgconfig file
Group:            Development/Libraries
Requires:         pkgconfig
Requires:         %{name}-web = %{epoch}:%{version}-%{release}
%description web-devel
This package includes the pkgconfig file for the libgda web provider.


%if %{FREETDS}
%package freetds
Summary:          FreeTDS provider for libgda
Group:            System Environment/Libraries
Requires:         %{name} = %{epoch}:%{version}-%{release}
Obsoletes:        gda-freetds < %{epoch}:%{version}-%{release}
Provides:         gda-freetds = %{epoch}:%{version}-%{release}
%description freetds
This package includes the libgda FreeTDS provider.

%package freetds-devel
Summary:          FreeTDS provider for libgda pkgconfig file
Group:            Development/Libraries
Requires:         pkgconfig
Requires:         %{name}-freetds = %{epoch}:%{version}-%{release}
%description freetds-devel
This package includes the pkgconfig file for the libgda FreeTDS provider.
%endif

%if %{IBMDB2}
%package ibmdb2
Summary:          IBM DB2 provider for libgda
Group:            System Environment/Libraries
Requires:         %{name} = %{epoch}:%{version}-%{release}
Obsoletes:        gda-ibmdb2 < %{epoch}:%{version}-%{release}
Provides:         gda-ibmdb2 = %{epoch}:%{version}-%{release}
%description ibmdb2
This package includes the libgda IBM DB2 provider.

%package ibmdb2-devel
Summary:          IBM DB2 provider for libgda pkgconfig file
Group:            Development/Libraries
Requires:         pkgconfig
Requires:         %{name}-ibmdb2 = %{epoch}:%{version}-%{release}
%description ibmdb2-devel
This package includes the pkgconfig file for the libgda IBM DB2 provider.
%endif

%if %{MYSQL}
%package mysql
Summary:          MySQL provider for libgda
Group:            System Environment/Libraries
Requires:         %{name} = %{epoch}:%{version}-%{release}
Obsoletes:        gda-mysql < %{epoch}:%{version}-%{release}
Provides:         gda-mysql = %{epoch}:%{version}-%{release}
%description mysql
This package includes the libgda MySQL provider.

%package mysql-devel
Summary:          MySQL provider for libgda pkgconfig file
Group:            Development/Libraries
Requires:         pkgconfig
Requires:         %{name}-mysql = %{epoch}:%{version}-%{release}
%description mysql-devel
This package includes the pkgconfig file for the libgda MySQL provider.
%endif

%if %{ODBC}
%package odbc
Summary:          ODBC provider for libgda
Group:            System Environment/Libraries
Requires:         %{name} = %{epoch}:%{version}-%{release}
Obsoletes:        gda-odbc < %{epoch}:%{version}-%{release}
Provides:         gda-odbc = %{epoch}:%{version}-%{release}
%description odbc
This package includes the libgda ODBC provider.

%package odbc-devel
Summary:          ODBC provider for libgda pkgconfig file
Group:            Development/Libraries
Requires:         pkgconfig
Requires:         %{name}-odbc = %{epoch}:%{version}-%{release}
%description odbc-devel
This package includes the pkgconfig file for the libgda ODBC provider.
%endif

%if %{ORACLE}
%package oracle
Summary:          Oracle provider for libgda
Group:            System Environment/Libraries
Requires:         %{name} = %{epoch}:%{version}-%{release}
Obsoletes:        gda-oracle < %{epoch}:%{version}-%{release}
Provides:         gda-oracle = %{epoch}:%{version}-%{release}
%description oracle
This package includes the libgda Oracle provider.

%package oracle-devel
Summary:          Oracle provider for libgda pkgconfig file
Group:            Development/Libraries
Requires:         pkgconfig
Requires:         %{name}-oracle = %{epoch}:%{version}-%{release}
%description oracle-devel
This package includes the pkgconfig file for the libgda Oracle provider.
%endif

%if %{POSTGRES}
%package postgres
Summary:          PostgreSQL provider for libgda
Group:            System Environment/Libraries
Requires:         %{name} = %{epoch}:%{version}-%{release}
Obsoletes:        gda-postgres < %{epoch}:%{version}-%{release}
Provides:         gda-postgres = %{epoch}:%{version}-%{release}
%description postgres
This package includes the libgda PostgreSQL provider.

%package postgres-devel
Summary:          PostgreSQL provider for libgda pkgconfig file
Group:            Development/Libraries
Requires:         pkgconfig
Requires:         %{name}-postgres = %{epoch}:%{version}-%{release}
%description postgres-devel
This package includes the pkgconfig file for the libgda PostgreSQL provider.
%endif

%if %{SYBASE}
%package sybase
Summary:          Sybase provider for libgda
Group:            System Environment/Libraries
Requires:         %{name} = %{epoch}:%{version}-%{release}
Obsoletes:        gda-sybase < %{epoch}:%{version}-%{release}
Provides:         gda-sybase = %{epoch}:%{version}-%{release}
%description sybase
This package includes the libgda Sybase provider.

%package sybase-devel
Summary:          Sybase provider for libgda pkgconfig file
Group:            Development/Libraries
Requires:         pkgconfig
Requires:         %{name}-sybase = %{epoch}:%{version}-%{release}
%description sybase-devel
This package includes the pkgconfig file for the libgda Sybase provider.
%endif

%if %{MDB}
%package mdb
Summary:          MDB provider for libgda
Group:            System Environment/Libraries
Requires:         %{name} = %{epoch}:%{version}-%{release}
Obsoletes:        gda-mdb < %{epoch}:%{version}-%{release}
Provides:         gda-mdb = %{epoch}:%{version}-%{release}
%description mdb
This package includes the libgda MDB provider.

%package mdb-devel
Summary:          MDB provider for libgda pkgconfig file
Group:            Development/Libraries
Requires:         pkgconfig
Requires:         %{name}-mdb = %{epoch}:%{version}-%{release}
%description mdb-devel
This package includes the pkgconfig file for the libgda MDB provider.
%endif

%if %{LDAP}
%package ldap
Summary:          LDAP provider for libgda
Group:            System Environment/Libraries
Requires:         %{name} = %{epoch}:%{version}-%{release}
Obsoletes:        gda-ldap < %{epoch}:%{version}-%{release}
Provides:         gda-ldap = %{epoch}:%{version}-%{release}
%description ldap
This package includes the libgda LDAP provider.

%package ldap-devel
Summary:          LDAP provider for libgda pkgconfig file
Group:            Development/Libraries
Requires:         pkgconfig
Requires:         %{name}-ldap = %{epoch}:%{version}-%{release}
%description ldap-devel
This package includes the pkgconfig file for the libgda LDAP provider.
%endif

%if %{XBASE}
%package xbase
Summary:          XBASE provider for libgda
Group:            System Environment/Libraries
Requires:         %{name} = %{epoch}:%{version}-%{release}
%description xbase
This package includes the GDA XBASE provider.

%package xbase-devel
Summary:          XBASE provider for libgda pkgconfig file
Group:            Development/Libraries
Requires:         %{name}-xbase = %{epoch}:%{version}-%{release}, pkgconfig
%description xbase-devel
This package includes the pkgconfig file for the libgda XBASE provider.
%endif

%if %{JAVA}
%package java
Summary:          Java JDBC provider for libgda
Group:            System Environment/Libraries
Requires:         %{name} = %{epoch}:%{version}-%{release}
%description java
This package includes the GDA Java JDBC provider.

%package java-devel
Summary:          Java JDBC provider for libgda pkgconfig file
Group:            Development/Libraries
Requires:         %{name}-java = %{epoch}:%{version}-%{release}, pkgconfig
%description java-devel
This package includes the pkgconfig file for the libgda Java JDBC provider.
%endif


%prep
%setup -q
# need to reconfigure autotools scripts against newer toolchain
autoreconf -fi


%build
CONFIG="--disable-static --disable-dependency-tracking --enable-system-sqlite --with-libsoup \
                         --enable-gtk-doc"

%if %{FREETDS}
CONFIG="$CONFIG --with-tds"
%else
CONFIG="$CONFIG --without-tds"
%endif

%if %{IBMDB2}
CONFIG="$CONFIG --with-ibmdb2"
%else
CONFIG="$CONFIG --without-ibmdb2"
%endif

%if %{MYSQL}
CONFIG="$CONFIG --with-mysql"
%else
CONFIG="$CONFIG --without-mysql"
%endif

%if %{POSTGRES}
CONFIG="$CONFIG --with-postgres"
%else
CONFIG="$CONFIG --without-postgres"
%endif

%if %{ODBC}
CONFIG="$CONFIG --with-odbc"
%else
CONFIG="$CONFIG --without-odbc"
%endif

%if %{ORACLE}
CONFIG="$CONFIG --with-oracle"
%else
CONFIG="$CONFIG --without-oracle"
%endif

%if %{SYBASE}
CONFIG="$CONFIG --with-sybase"
%else
CONFIG="$CONFIG --without-sybase"
%endif

%if %{MDB}
CONFIG="$CONFIG --with-mdb"
%else
CONFIG="$CONFIG --without-mdb"
%endif

%if %{LDAP}
CONFIG="$CONFIG --with-ldap"
%else
CONFIG="$CONFIG --without-ldap"
%endif

%if %{XBASE}
CONFIG="$CONFIG --with-xbase"
%else
CONFIG="$CONFIG --without-xbase"
%endif

%if %{JAVA}
CONFIG="$CONFIG --with-java"
%else
CONFIG="$CONFIG --without-java"
%endif

%configure $CONFIG
# Don't use rpath!
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
# workaround to fix linking failure for GI
export LD_LIBRARY_PATH=`pwd`/libgda/.libs:`pwd`/libgda-report/.libs:`pwd`/libgda-ui/.libs
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
# libgda/libgda.h is not installed ?
mv %{name}/%{name}.h $RPM_BUILD_ROOT/%{_includedir}/%{name}-4.0/%{name}/%{name}.h
# Cleanup unnecessary, unpackaged files
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
rm $RPM_BUILD_ROOT/%{_sysconfdir}/libgda-4.0/sales_test.db

%find_lang libgda-4.0


%post -p /sbin/ldconfig

%post devel
if which scrollkeeper-update >/dev/null 2>&1; then scrollkeeper-update; fi

%postun -p /sbin/ldconfig

%postun devel
if which scrollkeeper-update >/dev/null 2>&1; then scrollkeeper-update; fi


%clean
rm -rf $RPM_BUILD_ROOT


%files -f libgda-4.0.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog README NEWS
%config(noreplace) %{_sysconfdir}/libgda-4.0
%{_bindir}/gda-list-*-4.0
%{_bindir}/gda-sql-4.0
%{_bindir}/gda-test-connection-4.0
%{_bindir}/gda_trml2*
%{_bindir}/gda-list-config
%{_bindir}/gda-list-server-op
%{_bindir}/gda-sql
%{_datadir}/libgda-4.0/dtd/libgda-*.dtd
%{_datadir}/%{name}-4.0/language-specs
%{_datadir}/%{name}-4.0/import_encodings.xml
%{_datadir}/%{name}-4.0/information_schema.xml
%{_libdir}/%{name}-4.0.so.*
%{_libdir}/%{name}-report-4.0.so.*
%{_libdir}/%{name}-xslt-4.0.so.*
%dir %{_libdir}/%{name}-4.0
%dir %{_libdir}/%{name}-4.0/providers
# note this file really should be in its own subpackage too, but libgda
# needs to have atleast one provider present to be of any use.
%{_libdir}/libgda-4.0/providers/libgda-bdb.so
%{_datadir}/%{name}-4.0/bdb_specs*.xml
#%{_libdir}/girepository-1.0/Gda-4.0.typelib
%{_mandir}/man1/*

%files devel
%defattr(-,root,root,-)
%doc %{_datadir}/gtk-doc/html/libgda-4.0
%{_includedir}/%{name}-4.0/%{name}/*
%{_includedir}/%{name}-4.0/%{name}-report/*
%{_includedir}/%{name}-4.0/%{name}-xslt/*
%{_libdir}/%{name}-4.0.so
%{_libdir}/%{name}-report-4.0.so
%{_libdir}/%{name}-xslt-4.0.so
%{_libdir}/pkgconfig/libgda-4.0.pc
%{_libdir}/pkgconfig/libgda-bdb-4.0.pc
%{_libdir}/pkgconfig/libgda-report-4.0.pc
%{_libdir}/pkgconfig/libgda-xslt-4.0.pc
#%{_datadir}/gir-1.0/Gda-4.0.gir

%files ui
%defattr(-,root,root,-)
%{_libdir}/%{name}-ui-4.0.so.*
%dir %{_libdir}/%{name}-4.0/plugins
%{_libdir}/%{name}-4.0/plugins/gdaui-*.xml
%{_libdir}/%{name}-4.0/plugins/libgda-ui-plugins.so
%{_datadir}/libgda-4.0/dtd/gdaui-layout.dtd
%{_datadir}/%{name}-4.0/server_operation.glade
%{_datadir}/%{name}-4.0/ui/gdaui-*.xml
#%{_libdir}/girepository-1.0/Gdaui-4.0.typelib
%{_datadir}/%{name}-4.0/pixmaps/gdaui-generic.png

%files ui-devel
%defattr(-,root,root,-)
%{_bindir}/gdaui-demo-4.0
%{_includedir}/%{name}-4.0/%{name}-ui/*
%{_libdir}/%{name}-ui-4.0.so
%{_libdir}/pkgconfig/%{name}-ui-4.0.pc
# most of samples here requires libgda-ui
%{_datadir}/%{name}-4.0/demo/*
%{_datadir}/%{name}-4.0/pixmaps/bin-attachment-16x16.png
#%{_datadir}/gir-1.0/Gdaui-4.0.gir

%files tools
%defattr(-,root,root,-)
%doc %{_datadir}/gtk-doc/html/gda-browser
%{_bindir}/gda-browser-4.0
%{_bindir}/gda-control-center-4.0
%{_datadir}/applications/gda-browser-4.0.desktop
%{_datadir}/applications/gda-control-center-4.0.desktop
%{_datadir}/%{name}-4.0/icons/hicolor/*
%{_datadir}/%{name}-4.0/pixmaps/gda-browser*.png
%{_datadir}/%{name}-4.0/pixmaps/gda-control-center*.png
%{_datadir}/icons/hicolor/*/apps/gda-control-center.png
%{_datadir}/gnome/help/gda-browser/*
%{_datadir}/pixmaps/gda-browser-4.0.png

%files sqlite
%defattr(-,root,root,-)
%{_libdir}/%{name}-4.0/providers/%{name}-sqlite.so
%{_datadir}/%{name}-4.0/sqlite_specs*.xml

%files sqlite-devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/libgda-sqlite-4.0.pc

%files sqlcipher
%defattr(-,root,root,-)
%{_libdir}/%{name}-4.0/providers/%{name}-sqlcipher.so
%{_datadir}/%{name}-4.0/sqlcipher_specs*.xml

%files sqlcipher-devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/libgda-sqlcipher-4.0.pc

%files web
%defattr(-,root,root,-)
%{_libdir}/%{name}-4.0/providers/%{name}-web.so
%{_datadir}/%{name}-4.0/php/*
%{_datadir}/%{name}-4.0/web/*
%{_datadir}/%{name}-4.0/web_specs*.xml

%files web-devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/%{name}-web-4.0.pc

%if %{FREETDS}
%files freetds
%defattr(-,root,root,-)
%{_libdir}/libgda-4.0/providers/libgda-freetds.so

%files freetds-devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/libgda-freetds-4.0.pc
%endif

%if %{IBMDB2}
%files ibmdb2
%defattr(-,root,root,-)
%{_libdir}/libgda-4.0/providers/libgda-ibmdb2.so

%files ibmdb2-devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/libgda-imdb2-4.0.pc
%endif

%if %{MYSQL}
%files mysql
%defattr(-,root,root,-)
%{_libdir}/libgda-4.0/providers/libgda-mysql.so
%{_datadir}/%{name}-4.0/mysql_specs*.xml

%files mysql-devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/libgda-mysql-4.0.pc
%endif

%if %{ODBC}
%files odbc
%defattr(-,root,root,-)
%{_libdir}/libgda-4.0/providers/libgda-odbc.so

%files odbc-devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/libgda-odbc-4.0.pc
%endif

%if %{ORACLE}
%files oracle
%defattr(-,root,root,-)
%{_libdir}/libgda-4.0/providers/libgda-oracle.so

%files oracle-devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/libgda-oracle-4.0.pc
%endif

%if %{POSTGRES}
%files postgres
%defattr(-,root,root,-)
%{_libdir}/libgda-4.0/providers/libgda-postgres.so
%{_datadir}/%{name}-4.0/postgres_specs*.xml

%files postgres-devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/libgda-postgres-4.0.pc
%endif

%if %{SYBASE}
%files sybase
%defattr(-,root,root,-)
%{_libdir}/libgda-4.0/providers/libgda-sybase.so

%files sybase-devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/libgda-sybase-4.0.pc
%endif

%if %{MDB}
%files mdb
%defattr(-,root,root,-)
%{_libdir}/libgda-4.0/providers/libgda-mdb.so
%{_datadir}/%{name}-4.0/mdb_specs*.xml

%files mdb-devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/libgda-mdb-4.0.pc
%endif

%if %{LDAP}
%files ldap
%defattr(-,root,root,-)
%{_libdir}/libgda-4.0/providers/libgda-ldap.so

%files ldap-devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/libgda-ldap-4.0.pc
%endif

%if %{XBASE}
%files xbase
%defattr(-,root,root)
%{_libdir}/libgda-4.0/providers/libgda-xbase.so

%files xbase-devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/libgda-xbase-4.0.pc
%endif

%if %{JAVA}
%files java
%defattr(-,root,root)
%{_libdir}/libgda-4.0/providers/libgda-jdbc.so
%{_libdir}/libgda-4.0/providers/gdaprovider-4.0.jar
%{_datadir}/%{name}-4.0/jdbc_specs*.xml

%files java-devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/libgda-jdbc-4.0.pc
%endif


%changelog
* Sun Nov 28 2010 Piotr Pokora <piotrek.pokora@gmail.com> - 1:4.2.2-1
- New upstream 4.2.2 (initial spec file taken from pkgs.fedoraproject.org and updated)
