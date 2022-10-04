# Machine Learning Usage: Coca-Cola

Coca-Cola deploys a machine learning system to support their customer loyalty program.
All packaged Coke products have a proof of purchase code that can be inputted into
the website `MyCodeRewards.com` or `MCR.com`. Coke found that this solution worked
well in the past before mobile devices became popular, but with the rise of mobile
devices they began to lose users and members of the loyalty program. The codes are
14-digit alphanumeric sequences and users quickly opted to stop using the rewards
program rather than inputting the long sequence [3].

To combat this issue, Coca-Cola deployed a M.L. system to automatically read the
reward code off the top of bottle caps or cardboard pieces and input them into
the system [2].

## 1. How many models do they deploy in parallel? Also, mention the type of models, e.g., Deep-NN. Decision trees?
While the sources were not as clear about the number of models that they deploy
at once, Coke has implemented a system of creating many small models that are
easy to distribute in mobile apps and do not take much computational time. Patrick
Brandt describes the technology in his article in the Google Developer Blog:

> Our research led us to a promising solution: Convolutional Neural Networks. CNNs are one of a family of "deep learning" neural networks that are at the heart of modern artificial intelligence products. Google has used CNNs to extract street address numbers from StreetView images. CNNs also perform remarkably well at recognizing handwritten digits. These number-recognition use-cases were a perfect proxy for the type of problem we were trying to solve: extracting strings from images that contain small character sets with lots of variance in the appearance of the characters. [1]

Coke deploys Convolutional Neural Networks trained to identify the printed digits.
This works well because the digits are printed using a dot-matrix printer and
the quality of the scan (i.e. rotation of the artifact and the lighting) make inference
the ideal approach.

## 2. What ecosystem/framework/tools do they use for model deployment?
Coke uses their mobile apps to deploy the models on customer devices, and they use
the associated app stores for each device to distribute the applications. For
web-based input on the mobile device, the model is deployed onto the server and
hosted using TensorFlow. Coke said in the interview that they like this mode of
deploying because it offers a lot of flexibility [3].

## 3. How do they load balance between the models?
Coca-Cola balances the load by using TensorFlow deployed natively on the device.
This reduces the strain on the remote server-side and allows for quick processing
and minimal data usage [1]. This is done by deploying the model on a mobile app,
or if the user is using the online site through a web-app that is load-balanced
on Google Cloud.

The article describes that they specifically chose TensorFlow because it offers a
degree of portability that was difficult to find elsewhere, specifically the
"write once, run anywhere" functionality [1].

## 4. How do they retire a model?
The model is not necessarily retired. The team at Coke has deployed an active-learning
component that allows users to input the characters that the model was unable to
decode and then this feedback is sent to the web server as part of the code validation.
This results in the server 1) knowing that the model failed, and 2) verifying the user's
correction and implementing it as active learning.

Additionally, models are retired when an update is pushed to the mobile app that renders
it obsolete or unusable.

## 5. How do they update a model? On what regularity do they update the models? Only what matters regarding model deployment, not about model training.
Models are updated as updates to the rewards mobile app [1, 3]. This allows the models
to be updated at the same time as the processing/API code as needed.  

## 6. What metrics do they use to monitor a model's performance and health?
When testing the model, the team at Coke generated several thousand simulation images
to both train and test the model. This included images with shadows, blurred text,
and rotation applied to the cap. This was used to initially test the model.

In production environments, the model uses active-learning. When the model cannot
identify a digit it asks the user to manually input the digit. This allows the model
to actively learn from its use. This offers both a statistic for true negatives and
allows for health metric.

## 7. How long does it take for them to deploy a single model? (Consider model size as a confounding factor)
I was not able to find this information. However, because of the deployment method
I can reason that it is not much longer than 5 minutes, since it is deployed alongside
and inside the mobile app.

## 8. How do they decrease the cost of model deployment?
They are able to decrease the cost of model deployment by deploying many smaller
models to the devices. This allows Coke to deploy models to the devices rather than on
the cloud. This directly reduces costs to their cloud infrastructure and allows
the computational burden to fall on the customers rather than the firm.

## Resources/Citations
* [1] Brandt, Patrick, "How Machine Learning with TensorFlow Enabled Mobile Proof-Of-Purchase at Coca-Cola." *Google Developers Blog*, 21 September 2017. developers.googleblog.com/2017/09/how-machine-learning-with-tensorflow.html. Accessed 6 September 2022.

* [2] Jarrell, Megan. "Artificial Intelligence at Coca-Cola – Two Current Use-Cases." *Emerg*, 19 July 2021. emerj.com/ai-sector-overviews/artificial-intelligence-at-coca-cola. Accessed 6 September 2022.

* [3] "The Coca-Cola Company using TensorFlow for digital marketing campaigns (TensorFlow Meets)." *YouTube*, uploaded by TensorFlow, 2 August 2018, www.youtube.com/watch?v=hZMmH5yHvIk. Accessed 6 September 2022.
