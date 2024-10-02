---
Subject: Big Data Analytics
Teacher: "@RafaelBerlangaLlavori @RafaelBerlangaLlavori"
Topic: LLM
date: 2024-09-16
tags:
  - "#SJK006-BigDataAnalytics"
---
# 4.0  Learning Goals and Notes

- What natural language processing (NLP) is? 
- What a language model is? 
- Transformers: Encoders and Decoders 
- Automatic generation of texts and code 
- Instructed large language models 
- Practice with ChatGPT over Data Science problems

# 4.1 Natural language processing tasks

Tasks covered by a chatbot:
![[Pasted image 20240928181616.png]]

GPT is a Transformer decoder aimed at completing word sequences:

Training -> $p(w_i|w_0, ..., w_{i-1})$ -> Discrete conditional distribution of tokens

Based off of predicting the next token with the learnt model, and adding it to the current sequence. It stips when the sequence has a given length or the sequence probability drops notably.

How tokes are chosen to generate that highly probable sequence?
- *Greedy strategy*: get always the most likely next token
- ***Beam Search***: at each step keep the most likely k partial sequences and return the most likely one when the prediction stops
- ***Softmax temperature***: we can add a hyperparameter (𝞽) to the output discrete distribution to smooth it (creativity/hallucination)

## 4.1.1 Instructed LLMs

- Instructed models are LLMs that have been trained to complete instructions (PROMPT)
- *chatGPT*, *Llama-2* and *Bard* are instructed models.
- Outputs of these models have been supervised by humans through a mechanism called *Reinforcement Learning* from Human Feedback (RLHF).
- Instructed LLMs are aimed at reduce hallucinations (false predictions) and maximise the alignment with the ethical and legal principles of humans.
- The main limitation of some LLMs are the prompt and output sizes. (~ 4K-8K tokens)
	- We are forced to retrieve the relevant information to be included in the PROMPT
	- We need to integrate LLMs with other existing tools (LANGUAGE CHAINS and Plugins) to complement each other

# 4.2 Prompting ChatGPT

![[Pasted image 20240928182559.png]]

| **Context**  | describe without ambiguities the scenario and intent of the prompt                                          |
| ------------ | ----------------------------------------------------------------------------------------------------------- |
| **Input**    | what is being used as input                                                                                 |
| **Output**   | which is the desired output format (text, JSON, CSV, etc.) Few shot: write some few examples of input/ouput |
| **Rephrase** | adjust the prompt to be more precise about the intent and the output (errors in the output).                |
| **Validate** | detect errors, show them to the agent and find alternative outputs                                          |
## 4.2.1 Ways of prompting Chat GPT **for Data Science**

![[Pasted image 20240928182829.png]]

