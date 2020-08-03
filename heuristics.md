# About
For the service, we use machine-learning based predictions were we decided it makes sense. Not _everything_ benefits from expensive traning. And has resultet in us using heuristics such as large datasets of known websites - external ratings and RegEx patterns as a first-defence against unwanted websites.

# Lookup Tables

Currently, we're only supporting lookup tables for know pornography- and phishing websites.

```
- Length of Pornography Table: 6021 domains
- Length of Phishing Table:    19387 domains
```

Furthermore, we support custom white- and blacklist functionality - allowing parents to specifically detail allowed websites.  Its is also possible to deny _any_ website not specified in the whitelist.

To edit the aforementioned lists, currently you need to go to\
```"/sanitara/sanitara/data/"``` and edit the files
```whitelist.csv / blacklist.csv```
