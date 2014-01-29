# Copyright (c) 2012 Bronto Software Inc.
# Licensed under the MIT License

from domain import JavaDomain
from extdoc import javadoc_role

def setup(app):
    app.add_domain(JavaDomain)

    app.add_config_value('javadoc_url_map', dict(), 'html')
    app.add_config_value('javadoc_java_version', '6', 'html')
    app.add_role('java:extdoc', javadoc_role)
