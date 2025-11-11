import dns.resolver

#Must be a name
target_domain = 'google.com'

#Type of records from DNS
records_type = ['A','AAAA','CNAME','MX','TXT','SOA']

resolver = dns.resolver.Resolver()
for type in records_type:
    try:
        answer = resolver.resolve(target_domain,type)
    except dns.resolver.NoAnswer:
        continue

    print(f'{type} records for {target_domain}')
    for data in answer:
        print(f" {data}") 