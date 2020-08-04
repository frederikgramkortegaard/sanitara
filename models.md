### Pornography Prediction
To predict whether or not a given domain name will direct to a website containing pornography, we're using an sklearn model - the SGD classifier (besides our heuristics system).  Which we've trained on ~200.000 labeled domain names.  Here are the information and metrics for our current models:

#### Dataset:
{
    "size": {"training_set_length": 135955, "testing_set_length": 58267},
    "features": ["URL", "extension", "HTTP(S)", "external_review"],
    "labels": {"safe": 0, "not_safe": 1.0},
    "test_set_percentage": 30.0 
}
 
#### Metrics:
    - Mean Accuracy: 0.8973346834400261

||Label|precision|recall|f1-score|support|
|---|---|---|---|---|---|
||0|0.85|0.96|0.90|29133|
||1|0.96|0.83|0.89|29134|
|accuracy||||0.90|58267|
|macro avg||0.90|0.90|0.90|58267|
|weighted avg||0.90|0.90|0.90|58267|

##### Cross Validation:
    - fit_time:    [1.37127185 1.92903113 1.43998051 1.51016569 1.28997445]
     
    - score_time:  [0.23392534 0.30216718 0.22985435 0.25978017 0.25476122]
     
    - test_score:  [0.92016991 0.98741151 0.95873237 0.96645557 0.61770158]
    
    - train_score: [0.95832717 0.95061045 0.9569952  0.95640309 0.99188431] 

#### Parameters & Pipeline
:speech_balloon: The following parameters were found using sklearns' GridSearchCV functionality.
```python
sgd = Pipeline([
     ('vect', CountVectorizer(max_df=1.0, max_features=None, ngram_range=(1,1))),
     ('tfidf', TfidfTransformer(norm='l1', use_idf=True)),
     ('sgd', SGDClassifier(max_iter=50, penalty='l2', alpha=1e-05))
])
```
