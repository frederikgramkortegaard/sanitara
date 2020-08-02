<img src="resources/banner.png" style="width: 200%">

## About
Sanitara is a machine-learning and heuristics based Parental Control System, designed to give the user a prediction
about a given domain names' child-friendlyness.

This is a PoC developed using the RAD (Rapid Application Development) method. Because of this, there still exists some bugs.

## How it Works
Currently, the service works by exposing an API, in which one can send
a domain name, and recieve a safety prediction via. a series of 
data formatting, heuristics and machine learning models.  At this time, predictions for both phishing and pornography websites are complete and fully working.

To see detailed metrics and in-depth explanations of how the models are built.
Take a look at [models.md](./models.md)  and for an explanation of which heuristics we use [heuristics.md](./heuristics.md)

## <a id="run_service">Running the Service</a>
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
      "name": "phishing",
      "prediction": 0,
      "err": null,
    },
    {
      "name": "pornography",
      "prediction": 1,
      "err": null,
    }
  ],
  "err": null,
  "input": "https://www.pornhub.com"
}

  # 1.0 is the label for a website that is not safe.
```

### FastAPI
FastAPI is a framework designed to serve production quality APIs' without
to much effort or overhead. We're using this to deploy our machine learning models,
and automatically generate documentation for our API.

## Documentation
After running the service, as mentioned [here](#run_service). It's as simple as navigating to `http://127.0.0.1:8000/docs` to see the documentation as provided by [swagger](https://swagger.io)
