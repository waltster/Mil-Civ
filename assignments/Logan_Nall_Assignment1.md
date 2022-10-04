# Find a company: Yelp!

Yelp is a way to branch out to new businesses whether trying to find a recommendation, leaving a review or posting a picture. 

### 1- How many models do they deploy in parallel? Also, mention the type of models, e.g., Deep-NN. Decision trees?
The Machine Learning Tech Lead reports that:
>Today there are hundreds of ML models powering Yelp in various forms, and ML adoption continues to accelerate. [1]

Given this information, I imagine that it safe to assume that not all of the hundreds of models are running parallel. A type of model used by Yelp is convolutional neural network for classifying picture in categories like food, drinks, or menus and even people's faces.

### 2- What ecosystem/framework/tools do they use for model deployment?
The ecosystem behind the machine learning at Yelp boils down to MLflow and MLeap. MLflow is mostly used for managing results and lifecycles. While MLeap is the bridge for the most used aspects at Yelp being:
* Spark
* XGBoost
* Scikit-learn
* Tensorflow

### 3- How do they load balance between the models?
Yelp seems to strike a balance by the ease of choosing and deploying models. When the Machine Learning Tech Lead talks about Yelp's process, they some it up like this:
>To serve models, we constructed a thin wrapper around MLeap that is responsible for fetching bundles from MLflow, loading the bundle into MLeap, and mapping requests into MLeap’s APIs. We created several deployment options for this wrapper, which allows developers to execute their model as a REST microservice, Flink stream processing application, or hosted directly inside Elasticsearch for ranking applications. [1]

### 4- How do they retire a model?
As a model preforms worse to their metrics they phase it out or implement a new version. Yelp also like to take advantage of open source solutions assisting in this process. [1]

### 5- How do they update a model? On what regularity do they update the models? Only what matters regarding model deployment, not about model training.
>According to online harassment tracker L1ght, in the first few weeks of the pandemic, there was a 40% increase in toxicity on popular gaming services including Discord. Anti-fraud experts saw a rise in various types of fraud last year across online platforms, including bank and insurance fraud. [4]

Yelp most notably updates models on a need basis. A timeframe in which Yelp would have been updating frequently is the start of the pandemic when more malicious users where online. Some of the things Yelp would need to look for are spam and would do so by:

>Photos flagged as spam are tracked by a fuzzy matching service so that if users try to reupload spam, it’s automatically discarded by the system. If there’s no similar spam match, it could end up in the content moderation team queue. [4]

### 6- What metrics do they use to monitor a model's performance and health?
The metrics that Yelp are the most concerned about in the models are relevancy and accuracy. Yelp does this by comparing the model against their data. Where this is implemented is in the user comments finding token words to describe the satisfaction of a business to mostly negative, negative, positive, and mostly posititve.

### 7- How long does it take for them to deploy a single model? (Consider model size as a confounding factor)
I could not find how long it takes to deploy a single model. However, I imagine some models take decent amount of time to deploy if they let to be deployed given some of the complex problems of Yelp. One such problem is bias given their diverse application where one type of business could be over recommended.

### 8- How do they decrease the cost of model deployment?
Originally Yelp had a few teams developing models but only in their team's scope. Having to keep up with the reasources for these independent models, Yelp brought together a central team to bring these models under one umbrella. A great move leading to better structure, access to experienced personnel, a stronger platform, and most importantly lower resource cost.

## References:
* [1] https://engineeringblog.yelp.com/2020/07/ML-platform-overview.html
* [2] https://digital.hbs.edu/platform-rctom/submission/machine-learning-at-yelp/
* [3] https://www.enterpriseappstoday.com/stats/yelp-statistics.html
* [4] https://venturebeat.com/ai/yelp-built-an-ai-system-to-identify-spam-and-inappropriate-photos/
