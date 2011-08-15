# `hibernate-ips`

This project is an attempt to provide Hibernate support to Glassfish
3.1.1 using the Glassfish Update Center.

## Status

This project is currently experimental.

## Installation

To install Hibernate support for Glassfish:

1. Start a `pkg.depot` server like this:
   > `pkg.depotd -d ~/pkg-working-directory -p 10000 --rebuild`

2. From the root of this project, run the following:
   > `mvn clean install -Drepourl=http://localhost:10000`

3. With the `pkg.depotd` server still running, start Glassfish's
   `updatecenter` tool:
   > `$GLASSFISH_HOME/updatetool/updatetool`

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

## Further Questions

Questions should be directed to the author, Laird Nelson, at ljnelson
at big horking email provider starting with `g`.
