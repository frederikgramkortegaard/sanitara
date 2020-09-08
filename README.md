<img src="resources/banner.png" style="width: 200%">

 :bookmark: [Fast forward to the predictive models](./models.md)

## About
Sanitara is a machine-learning and heuristics based Parental Control System, designed to give the user a prediction
about a given domain names' child-friendliness.

This is a PoC developed using the RAD (Rapid Application Development) method with _**the core models and functionality being completed in just 24 hours**_. Because of this, there still exists some bugs.

## How it Works
Currently, the service works by exposing an API, in which one can send
a domain name, and recieve a safety prediction via. a series of heuristics and machine learning models.  At this time, predictions for both phishing and pornography websites are complete and fully working as well as white- and blacklist functionality.

To see detailed metrics and in-depth explanations of how the models are built check out [models.md](./models.md). And for an explanation of which heuristics we use go to [heuristics.md](./heuristics.md)

## <a id="run_service">Running the Service</a>

:warning: **these are predictions, not facts**: not every result will be correct.

```bash
$ git clone https://github.com/frederikgram/sanitara.git
$ cd sanitara
$ python -m venv venv
$ ./env/Scripts/activate
(venv) pip install -r requirements.tx
(venv) python start_service.py
```
### Testing the Installation
```bash
$ curl http://127.0.0.1:8000/api/v1/predict/?message=https://www.badwebsite.com
>>>
{
  "predictions": [
    {
      "name": "pornography",
      "prediction": 0,     # is not pornography
      "err": null
    },
    {
      "name": "phishing",
      "prediction": 1,     # is a phishing website
      "err": null
    },
    {
      "name": "whitelist",
      "prediction": 0,     # was not found in whitelist
      "err": null
    },
    {
      "name": "blacklist",
      "prediction": 1,     # was found in blacklist
      "err": null
    },
    {
    "name": "regex",
    "prediction": 0,       # did not match any given regex pattern
    "err": null
    },
    {
    "name": "keyword",
    "prediction": 0,       # did not match any given keywords
    "err": null
    }
  ],
  "err": null,
  "input": "https://www.badwebsite.com"
}
```

### FastAPI
FastAPI is a framework designed to serve production quality APIs' without
to much effort or overhead. We're using this to deploy our machine learning models,
and automatically generate documentation for our API.

## Documentation
After running the service, as mentioned [here](#run_service). It's as simple as navigating to `http://127.0.0.1:8000/docs` to see the documentation as provided by [swagger](https://swagger.io)

### Command line Arguments

to configure the system, currently we're using a cli process. However, the development of a non-technical GUI solution is in the works.  Seen here, is a list of command line arguments used to configure the system:

:warning: **Work-in-Progress** Currently, the following command line arguments do _not_ work.

```

--(add or remove)-whitelist # Adds a website to the whitelist
--(add or remove)-blacklist # Adds a website to the blacklist
--(add or remove)-regex     # Adds a regex pattern to the blacklist
--(add or remove)-keyword   # Adds a keyword to the blacklist

--(allow or disallow)-
    pornography
    whitelist
    blacklist
    ...

--verbose        # Used for debug purposes

--ensemble       # Takes the mean of every metric, if the resulting
                 # value is >= 0.5, the domain will be disallowed.

--(allow or disallow)-requests 
                 # Used to allow a user to request access from
                 # whoever is listed as the administrator
                 # using SMS or the online GUI
```
