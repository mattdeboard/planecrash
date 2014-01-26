#!/usr/bin/env python
import boto
from boto.route53.record import ResourceRecordSets

def create_domains(subdomains):
    conn = boto.connect_route53()
    dns_zone = ResourceRecordSets(conn, 'Z3U4HAE1JOZU4U')

    for s in subdomains:
        url = '%s.courseload.com' % s
        file_url = 'file.' + url
        for u in [url, file_url]:
            change = dns_zone.add_change('CREATE', u, 'CNAME', ttl=3600)
            if u.startswith('file.'):
                change.add_value('filepool.courseload.com')
            else:
                change.add_value('nginxpool.courseload.com')
    return dns_zone.commit()

def get_records(subdomains):
    """Update DNS records to point to CloudFront auth server."""
    conn = boto.connect_route53()
    dns_zone = ResourceRecordSets(conn, 'Z3U4HAE1JOZU4U')

    for s in subdomains:
        url = 'file.%s.courseload.com.' % s
        change1 = dns_zone.add_change('DELETE', url, 'CNAME', ttl=3600)
        change1.add_value('filepool.courseload.com')
        change2 = dns_zone.add_change('CREATE', url, 'CNAME', ttl=300)
        change2.add_value('auth.content.courseload.com')

    return dns_zone.commit()

def get_records2():
    subdomains = [
        "asu.courseload.com",
        "cccti.courseload.com",
        "cityu.courseload.com",
        "internal.courseload.com",
        "jccc.courseload.com",
        "middlebury.courseload.com",
        "morgan.courseload.com",
        "northwestern.courseload.com",
        "osu.courseload.com",
        "sscok.courseload.com",
        "temple.courseload.com",
        "umich.courseload.com",
        "umichd.courseload.com",
        "umn.courseload.com",
        "unr.courseload.com"
    ]
    conn = boto.connect_route53()
    dns_zone = ResourceRecordSets(conn, 'Z3U4HAE1JOZU4U')

    for s in subdomains:
        change1 = dns_zone.add_change('DELETE', s, 'CNAME', ttl=3600)
        change1.add_value('nginxpool.courseload.com')
        change2 = dns_zone.add_change('CREATE', s, 'CNAME', ttl=300)
        change2.add_value('lb-00.ops.courseload.com')

    return dns_zone.commit()
    
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('oper', metavar='CREATE|UPDATE',
                        help=("Valid options: create|update"),
                        choices=['create', 'update'])
    parser.add_argument('domains', metavar='DOMAINS',
                        help=("Comma-separated list of subdomains. Example: "
                              "'indiana,berkeley,vt'"))
    args = parser.parse_args()
    argdict = vars(args)
    if argdict['oper'] == 'create':
        func = create_domains
    elif argdict['oper'] == 'update':
        func = get_records

    func(argdict['domains'].split(','))
