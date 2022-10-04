# ML in Spotify
### Assignment 1 - CSCE 585
### Vera Svensson - September 2022

### 1- How many models do they deploy in parallel? Mention the type of models?
The Spotify home screen is a personalized view built on machine learning. Spotify have several machine learning models running, just for the purpose of creating the optimal home screen experience. Three of them being *The Podcast Model* , *The Shortcut Model*, and *The Playlist Model*.[1] I found no number of exactly how many models they run in paralell. In their models they use methods like collaborative filtering and reinforcement learning. They build survival models to predict user behaviour and how satisfied customers are with their experience.[2][3]

### 2- What ecosystem/framework/tools do they use for model deployment?
In almost all steps of Spotify's ML stack they use Kubeflow. For training they also use Tensorflow. They deploy models using their own *Spotify Serving Platform*. They follow a classic ML workflow, which they group into the phases data management, experimentation and operationalization.[4]

### 3- How do they load balance between the models?
I couldn't find anything about how they load balance between ML models. Overall Spotify use the Round Robin strategy to load balance.[5]

### 4- How do they retire a model?
What I can find, Spotify hasn't retired models yet. Instead they make changes to already existing models.[1]

### 5- How do they update a model? On what regularity do they update the models? Only what matters regarding model deployment, not about model training.
To update a deployed model they, at first, had one solution where they would poll their internal storage directory several times a day to check if there was new revisions. If so, the new revision would simply be pulled and put to use. This was done manually. They have now moved on to a more effective process using the *Spotify serving platform*. With the platform they can push updated models from a Kubeflow pipeline instead of polling over and over again.[1]

### 6- What metrics do they use to monitor a model's performance and health?
As a baseline Spotify use non-ML solutions to compare the performance of their ML models. For metrics, Spotify use common metrics, such as accuracy and precicion, but also a lot of custom metrics, some specific for a singel feature or model. NDCG@k, or *normalized discounted cumulative gain*, being their most commonly used when evaluating their recommendations model. They've also implemented their own diversity metric.[1]

Some metrics are *online* metrics, meaning they can be collected from real users, for example from A/B tests. \cite{rise2} Spotify perform these A/B tests by testing different agents on real users and evaluate their performance.[3] However, they can't get all metrics they need from these tests, and therefor also need *offline* metrics.[1]

Spotify use a combination of Tensorflow Data Validation, Kubeflow and dashboards for monitoring deployed models. They use dashboards to get a bigger picture, something solely using metrics can't provide.[4]

### 7- How long does it take for them to deploy a single model?
I couldn't find anything about this.

### 8- How do they decrease the cost of model deployment?
They automaticly checks the models evaluations scores and deploy it if it meets the required score. This is done via Kubeflow. This lessens the workload and time needed to deploy models.[1]

To decrese the workload and time required to deploy a new feature, Spotify focus on reuse of models and concepts. They enable this by structuring their architecture into three layers: *Data*, *Shared Models* and *Features*. The *Shared Models* include models that are usefull for many different features, whereas *Features* includes feature specific models.[3]

# References

[1] A. Edmundson, "The Rise (and Lessons Learned) of ML Models to Personalize Content on Home (Part II)", Spotify R&D Engineering, November 2021. [Online] Available: https://engineering.atspotify.com/2021/11/the-rise-and-lessons-learned-of-ml-models-to-personalize-content-on-home-part-ii/ . [Accessed Sep. 07, 2022]

[2] Spotify Engineering, "How Spotify Uses ML to Create the Future of Personalization", Spotify R&D Engineering, December 2021. [Online] Available: https://engineering.atspotify.com/2021/12/how-spotify-uses-ml-to-create-the-future-of-personalization/. [Acessed Sep. 07, 2022]

[3] Spotify R&D, "VP of Personalization Oskar Stål Talks the Future of ML at TransformX", December 2021. [Online video] Available: https://www.youtube.com/watch?v=n16LOyba-SE . [Accessed sep. 07 2022]

[4] A. Edmundson, "The Rise (and Lessons Learned) of ML Models to Personalize Content on Home (Part I)", Spotify R&D Engineering, November 2021. [Online] Available: https://engineering.atspotify.com/2021/11/the-rise-and-lessons-learned-of-ml-models-to-personalize-content-on-home-part-i/ . [Accessed Sep. 07, 2022]

[5] Jin, "Spotify System Architecture", Geek Culture, November 2021. [Online] Available: [https://medium.com/geekculture/spotify-system-architecture-6bb418db6084 . [Accessed Sep 09, 2022]
