## About
Sanitara is a machine-learning and heuristics based Parental Control system.

## How it Works


### The Models
As we've now established, a large part of sanitation comes from heuristics, however.  We've also
developed a model using sklearn to predict how child-friendly a website will be, based on its url.

To do this, we've using an a learn model - the SGD classifier.  And trained it on ~200.000 labeled domain names.\
Here are the metrics for our current model:


-> model_0 : 2020-08-01 19:42:40

#### Dataset:
 - lenght of Training set: `135955`
 - lenght of Test set: `58267`
 
#### Test size:
 - `30.0%`

#### Mean Accuracy:
 - `0.8973346834400261`
 
#### Metrics:

|   |precision|recall|f1-score|support|
|---|---|---|---|---|
|   |0|0.85|0.96|0.90|29133|
|   |1|0.96|0.83|0.89|29134|
|accuracy|||0.90|58267|
|macro avg|0.90|0.90|0.90|58267|
|weighted avg|0.90|0.90|0.90|58267|

#### Cross Validation:
 - fit_time: `[1.37127185 1.92903113 1.43998051 1.51016569 1.28997445]`
 - score_time: `[0.23392534 0.30216718 0.22985435 0.25978017 0.25476122]`
 - test_score: `[0.92016991 0.98741151 0.95873237 0.96645557 0.61770158]`
 - train_score: `[0.95832717 0.95061045 0.9569952  0.95640309 0.99188431]`



## Running the Service

### Requirements

### API

