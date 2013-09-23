#!/usr/bin/env python

import iptc

rule = iptc.Rule()
rule.protocol = "tcp"

match = iptc.Match(rule,"tcp")
match.dport = "8080"
rule.add_match(match)

match = iptc.Match(rule,'iprange')
match.src_range = "172.23.177.17"
rule.add_match(match)

rule.target = iptc.Target(rule,"DROP")
chain = iptc.Chain(iptc.Table(iptc.Table.FILTER),"INPUT")
chain.insert_rule(rule)
