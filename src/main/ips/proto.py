#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS HEADER.
#
# Copyright 2009-2011 Sun Microsystems, Inc. All rights reserved.
#
# The contents of this file are subject to the terms of either the GNU
# General Public License Version 2 only ("GPL") or the Common Development
# and Distribution License("CDDL") (collectively, the "License").  You
# may not use this file except in compliance with the License. You can obtain
# a copy of the License at https://glassfish.dev.java.net/public/CDDL+GPL.html
# or updatetool/LICENSE.txt.  See the License for the specific
# language governing permissions and limitations under the License.
#
# When distributing the software, include this License Header Notice in each
# file and include the License file at glassfish/bootstrap/legal/LICENSE.txt.
# Sun designates this particular file as subject to the "Classpath" exception
# as provided by Sun in the GPL Version 2 section of the License file that
# accompanied this code.  If applicable, add the following below the License
# Header, with the fields enclosed by brackets [] replaced by your own
# identifying information: "Portions Copyrighted [year]
# [name of copyright owner]"
#
# Contributor(s):
#
# If you wish your version of this file to be governed by only the CDDL or
# only the GPL Version 2, indicate your decision by adding "[Contributor]
# elects to include this software in this distribution under the [CDDL or GPL
# Version 2] license."  If you don't indicate a single choice of license, a
# recipient has the option to distribute your version of this file under
# either the CDDL, the GPL Version 2 or to extend the choice of license to
# its licensees as provided above.  However, if you add GPL Version 2 code
# and therefore, elected the GPL Version 2 license, then the option applies
# only if the new code is made subject to such option by the copyright
# holder.
#
import imp


pkg = {
    "name"          : "${project.artifactId}",

    # From http://www.unix.com/man-page/OpenSolaris/5/pkg/:
    #
    # "The version follows the package name, separated by an '@'.  It
    # consists of four sequences of numbers, separated by punctuation.
    # The elements in the first three sequences are separated by dots,
    # and the sequences are arbitrarily long.
    #
    # "The first part is the component version.  For components tightly
    # bound to OpenSolaris, this will usually be the value of 'uname
    # -r' for that version of OpenSolaris.  For a component with its
    # own development lifecycle, this sequence will be the dotted
    # release number, such as '2.4.10'.
    #
    # "The second part, following the comma, is the build version,
    # specifying what version of OpenSolaris the contents of the
    # package were built on, providing a minimum bound on which
    # OpenSolaris version the contents can be expected to run
    # successfully.
    #
    # "The third part, following the dash, is the branch version, a
    # versioning component, providing vendor-specific information.
    # This may be incremented when the packaging metadata is changed,
    # independently of the component, may contain a build number, or
    # some other information.
    #
    # "The fourth part, following the colon, is a timestamp.  It
    # represents when the package was published."
    "version"       : "${ipsCompatibleHibernateVersion},${glassfishVersion}-${ipsCompatibleProjectVersion}",

    "attributes"    : {
                        "pkg.summary" : "${project.name}",
                        "pkg.description" : "${project.description}",
                        "info.classification" : "Frameworks",
                      },

    "defaults"      : {
                        "file" : { "mode" : "0755", },
                        "dir" : { "mode" : "0775", },
                      },

    "dirtrees"      : [ "glassfish/${dependenciesDirectoryPath}" ],

    "info.maintainer" : "Laird Nelson <ljnelson@gmail.com>",

    "files"         : { "glassfish/lib/${project.artifactId}-${project.version}.jar" : { "mode" : "0755", }, },
    
    "licenses"      : {
                        "${basedir}/LICENSE.txt" : {"license" : "GNU LESSER GENERAL PUBLIC LICENSE"},
                      },

    "pkg.detailed_url" : "${project.url}",
    
}
