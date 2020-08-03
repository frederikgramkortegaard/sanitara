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

# Command line Arguments

to configure the system, currently we're using a cli process. However, the development of a non-technical GUI solution is in the works.  Seen here, is a list of command line arguments used to configure the system:

:warning: **Work-in-Progress** Currently, the following command line arguments do _not_ work.

```
--deny-all
--allow-
    pornography
    whitelist
    blacklist
    ...
--allow-only-
    pornography
    whitelist
    blacklist
    ...
--verbose        # Used for debug purposes

--allow-requests # Used to allow a user to request access from
                 # whoever is listed as the administrator
                 # using SMS or the online GUI
```
