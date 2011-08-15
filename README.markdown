# `hibernate-ips`

This project is an attempt to provide Hibernate support to Glassfish
3.1.1 using the [Glassfish Update
Center](http://java.net/projects/updatecenter2/).

## Status

This project is currently experimental.

## Installation

To install Hibernate support for Glassfish:

1. [Start a `pkg.depotd`
   server](http://dlc.sun.com/osol/docs/content/2009.06/IMGPACKAGESYS/depot_server.html)
   like this:
    
        pkg.depotd -d ~/pkg-working-directory -p 10000 --rebuild

    It may be possible in the future to avoid having to run such a
    server; see [this
    link](http://mail.opensolaris.org/pipermail/pkg-discuss/2010-May/022716.html)
    for details.

2. From the root of this project, run the following:
    
        mvn clean install -Drepourl=http://localhost:10000

3. With the `pkg.depotd` server still running, start Glassfish's
   `updatecenter` tool:
    
        $GLASSFISH_HOME/updatetool/bin/updatetool

4. In the update tool, press the `Edit Properties...` button.

5. In the resulting dialog box, press the `Add...` button.

6. Choose a name for the publisher.  This name looks like it must
   follow the rules of a valid hostname.

7. For "`Repository URL`", supply `http://localhost:10000`.

8. Press the `OK` button.

9. Press the `OK` button.

10. Choose the `Available Add-Ons` tree node.

11. From here you should be able to find a package named
    `hibernate-ips`.  Install this package like you would any other
    Update Center package.

12. Once you've gotten here, you may terminate the `pkg.depotd`
    server.  That's it!

## What Really Happens

This project simply arranges for the Glassfish Update Center to do all
the heavy lifting.  The heavy lifting, though, isn't that heavy.

A `hibernate-ips-<version>.jar` file is deposited in the
`$GLASSFISH_HOME/glassfish/lib` directory, the directory whose `.jar`
file contents form part of the Glassfish common classloader.  This
`.jar` file is empty, but contains a `MANIFEST.MF` file with a
`Class-Path:` header.  The elements in the `Class-Path:` header all
refer to other `.jar` files within the
`$GLASSFISH_HOME/glassfish/ips/hibernate-ips-<version>-dependencies`
directory, which is also created by this project, and which is full of
Hibernate's dependencies.  The net effect is that the
`hibernate-ips-<version>.jar` file serves as a kind of façade to the
contents of the related dependency directory.

## A Note On Dependencies

[Hibernate's
`pom.xml`](http://repo1.maven.org/maven2/org/hibernate/hibernate-core/3.6.6.Final/hibernate-core-3.6.6.Final.pom)
declares lots of dependencies.	`hibernate-entitymanager` does too.
Some of these dependencies are--in practice--mutually exclusive.  For
example, you'll usually have one cache provider, not several at once.

This project is set up to dump as many of Hibernate's transitive
dependencies as possible in
`$GLASSFISH_HOME/ips/hibernate-ips-<version>-dependencies`.  All of
these dependencies will be on the Glassfish common classpath, visible
to all applications.

The one dependency (and its transitive dependencies) that is excluded
is SwarmCache, because it requires a version of JGroups that is older
than the version of JGroups that is required by several other
dependencies.  SwarmCache is an older, less popular cache provider and
hence seemed like a dependency that should not be included by default.

The old version of Hibernate support for Glassfish used to package up
the no-longer-produced `hibernate3.jar` file, which was a kitchen sink
type of `.jar` file that packaged Hibernate along with several
unspecified dependencies into a single file.  Hibernate versions after
3.5 no longer produce this `.jar` file, requiring that the individual
developer declare dependencies on what he needs (which cache provider
to use, etc.).

Providing this kind of support for an application server, however,
means that by definition we don't know what dependencies the developer
is going to want.  So we include all of them that we can.

## Further Questions

[Alexis Moussine-Pouchkine's crash course on
IPS](http://blogs.oracle.com/alexismp/entry/ips_pkg_5_crash_course) is
helpful to understand what's going on here.

All other questions should be directed to the author, Laird Nelson, at
`ljnelson` at big horking email provider starting with `g`.
