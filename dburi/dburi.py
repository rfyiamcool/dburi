#coding:utf-8
import re
import os
import urllib
import urlparse

default_port = {
    'mongo': 27017,
    'mysql': 3306,
    'postgres': 5432,
    'redis': 6379,
    'hbase': 9090,
    'elasticsearch':9200
}

def parse_extra(str):
    qs = dict( (k, v if len(v)>1 else v[0] )
    for k, v in urlparse.parse_qs(str).iteritems() )
    return qs

def parse_db_str(conn_str):
    pattern = re.compile(r'''
            (?P<name>[\w\+]+)://
            (?:
                (?P<user>[^:/]*)
                (?::(?P<passwd>[^/]*))?
            @)?
            (?:
                (?P<host>[^/:]*)
                (?::(?P<port>[^/]*))?
            )?
            /?(?P<db>\w*)?\?*
            (?P<extra>(.*))?
            '''
            , re.X)
    m = pattern.match(conn_str)
    if m is not None:
        components = m.groupdict()
        for extra_k,extra_v  in parse_extra(components['extra']).iteritems():
            components[extra_k] = extra_v

        if components['db'] is not None:
            tokens = components['db'].split('?', 2)
            components['db'] = tokens[0]

        if components['passwd'] is not None:
            components['passwd'] = urllib.unquote_plus(components['passwd'])

        name = components['name']

        if components['port'] is None:
            components['port'] = default_port[name]
        else:
            components['port'] = int(components['port'])

        result = {}
        for key, value in components.iteritems():
            if value:
                result[key] = value

        return result
    else:
        raise ArgumentError(
            "Could not parse rfc1738 URL from string '%s', the format should match 'dialect+driver://username:password@host:port/database'" % name)

