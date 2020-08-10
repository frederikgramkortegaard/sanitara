<img src="resources/banner.png" style="width: 200%">

## About
Sanitara is a machine-learning and heuristics based Parental Control System, designed to give the user a prediction
about a given domain names' child-friendliness.

This is a PoC developed using the RAD (Rapid Application Development) method. Because of this, there still exists some bugs.

## How it Works
Currently, the service works by exposing an API, in which one can send
a domain name, and recieve a safety prediction via. a series of heuristics and machine learning models.  At this time, predictions for both phishing and pornography websites are complete and fully working as well as white- and blacklist functionality.

To see detailed metrics and in-depth explanations of how the models are built check out [models.md](./models.md). And for an explanation of which heuristics we use go to [heuristics.md](./heuristics.md)

## <a id="run_service">Running the Service</a>

:warning: **these are predictions, not facts**: not every result will be correct.

```bash
$ git clone https://github.com/frederikgram/sanitara.git
$ cd sanitara
$ python -m venv env
$ ./env/Scripts/activate.bat # Depends on system
$ pip install -r requirements.tx
$ python start_service.py
```
### Testing the Installation
```bash
$ curl http://127.0.0.1:8000/api/v1/predict/?message=https://www.pornhub.com
>>>
{
  "predictions": [
    {
      "name": "pornography",
      "prediction": 1,     # is pornography
      "err": null
    },
    {
      "name": "phishing",
      "prediction": 0,     # is not a phishing website
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
    }
  ],
  "err": null,
  "input": "https://www.pornhub.com"
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
--deny-all
--allow-
    pornography
    whitelist
    blacklist
    ...
--allow-only-
    whitelist
    ...
--verbose        # Used for debug purposes

--ensemble       # Takes the mean of every metric, if the resulting
                 # value is >= 0.5, the domain will be disallowed.

--allow-requests # Used to allow a user to request access from
                 # whoever is listed as the administrator
                 # using SMS or the online GUI
```
