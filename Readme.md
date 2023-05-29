## Classification


Classifiers are the easiest models to get started with. For classification problems we suggest using ada, which generally tends to perform only very slightly worse than more capable models once fine-tuned, whilst being significantly faster and cheaper.

In classification problems, each input in the prompt should be classified into one of the predefined classes. For this type of problem, we recommend:

Use a separator at the end of the prompt, e.g. \n\n###\n\n. Remember to also append this separator when you eventually make requests to your model.
Choose classes that map to a single token. At inference time, specify max_tokens=1 since you only need the first token for classification.
Ensure that the prompt + completion doesn't exceed 2048 tokens, including the separator
Aim for at least ~100 examples per class
To get class log probabilities you can specify logprobs=5 (for 5 classes) when using your model
Ensure that the datase