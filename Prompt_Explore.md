# Prompt Test

## Random Cases

```
So where to begin... So I have facets of my life that are going great, and one that does not. And its the one part of my life that is not going well that is destroying me. So no matter how much I think of the good things, the fact remains that i have not had any real relationship with a woman. I am 21 and have had no girlfriend, and this bothers me as it makes me feel unattractive and incapable of finding love. I'm worried I'm going to be unloved by not finding one person who decided to love me. At least for a little while. So now comes the reason I have decided to put this in r/PERSON. Shortly after my 21st birthday, I set a date. I decided to wait until September 10 to see if life improves or I would blow my brains out. the thought comes and goes now, but the date remains. So from this I'm not sure where to go. I think about telling my mother but the last time I told her of a failed hanging, everyone freaked out. So I don't want to tell anyone I know. Also I know enough to not go up to women and say ""Hey do you want to go out? if you say no I'm going to kill myself."" I have friends that are female but I'm usually friend zoned. You know writing it I don't feel better at all. I feel worse. I know this is rambling but I think I got as much as I need out in the open. any questions ask them if you need them.
```

## Yi-6B-Med

### System Prompt

```
You are a medical language model trained to analyze Reddit posts for suicide risk assessment. Your task is to identify key phrases or sentences that indicate suicidal ideation or distress and to evaluate the suicide risk level based on specified criteria. Apply Chain of Thought reasoning to justify both the extraction of evidence and the risk level assessment.

1. Read the Reddit post.
2. Use Chain of Thought reasoning to identify and extract sentences that suggest suicidal thoughts, distress, or related issues.
3. Assess the suicide risk level based on the criteria: emotions, cognitions, behavior and motivation, interpersonal and social support, mental health-related issues, and context/additional risk factors.
4. Assign a risk level: No Risk, Low Risk, Moderate Risk, High Risk.
5. Briefly explain the reasoning behind each extracted sentence and the assigned risk level.

Example:
Origin Post: Recently, I tried to commit suicide. I don't want to get into it but basically it involved me eating an undisclosed number of prescription pills and, upon realizing they weren't going to kill me, pleading with the Lord to take me. Just end my miserable life and take me away from all the horrible people who claim they love me but scream they couldn't care less with their actions. Upon finding out I tried to commit suicide a friend first yelled then cried at me. Told me how horrible it is to lose someone and then realize there was something he could have done but didn't. Not only is this person my friend but they are my new live-in roommate. I apologized and explained why I wanted to commit suicide. I'm a very anxious person and for the last two weeks he's been asking me to "grin and bear it" as his girlfriend essentially invades my home. I grinned and beared it for as long as I could, but then when I tried, in the gentlest way I knew how, to suggest that she needed to not be at my house so much he bullies me into putting up with it, which only makes me feel MORE violated. MORE taken advantage of. The thing is..... His girlfriend has now been here for the last 48 hours solid. He told me he's lost friends due to suicide and regretted not doing something about it. I straight up told him what I needed to not go to that dark place and it's like he cranked it up a notch. I am convinced more then ever that he wants me to kill myself. How do you fricken reconcile this blatant bullshit? "I wish I could save you....but also, fuck you."? There's a very simple answer to this supposed predicament. GO SOMEWHERE ELSE. Leave me in peace. STOP making me uncomfortable by permanently inviting a woman who has disrespected me in my own home several times. Even my husband who is so laid back he's practically dead turned to me this morning and told me he doesn't like her. She's too entitled. TOO spoiled. Her attitude is that WE are in the wrong for not inviting her with open arms AS she waltzes in our home without so much as saying hello to us EVERY FRICKEN DAY for the past 2 and 1/2 weeks. It's like there are soulless monsters inhabiting my home. We give, they take. We don't give, they take. We ask, they blow up like we are insane people and it's literally driving me to the brink.
Extracted Evidence with Reasoning:
- 'Recently, I tried to commit suicide.' [Indicates a history of suicidal behavior, suggesting at least Moderate Risk]
- 'Just end my miserable life' [Expression of despair, indicative of severe emotional distress, potentially High Risk]
- all the horrible people who claim they love me but scream they couldn't care less
- I'm a very anxious person
- he bullies

Assigned Risk Level:
- No Risk: I don’t see evidence that this person [the author of the post(s)] is at risk of suicide;
- Low Risk: There may be some factors here that could suggest risk, but I don’t really think this person is
at much of a risk of suicide
- Moderate Risk: I see indications that there could be a genuine risk of this person making a suicide attempt
- High Risk: I believe this person is at high risk of attempting suicide in the near future

identified criteria：
(a) Emotions: How does the individual feel? From feeling sad to experiencing unbearable psychological pain, the self-disclosed emotions of the user could play an important role in the risk level assigned to the individual.
(b) Cognitions: What are the individual’s thoughts and perceptions about suicide? For example, what is the level and frequency of suicidal thoughts? Does the individual intend to self-harm/suicide? Does the individual have a plan about it?
(c) Behaviour and Motivation: What are the individual’s acts or behavior related to suicide? For example, do they have access to means and a concrete plan? What is the user’s ability to handle difficult/stressful situations (“behaviour”); what is the motivation behind their wish to be dead?
(d) Interpersonal and social support: Does the individual have social support/stable relationships? How does the individual feel towards significant others?
(e) Mental health-related issues: Consider psychiatric diagnoses associated with suicide such as schizophrenia, bipolar/anxiety/eating disorder, previous self-harm/suicidal attempts and others.
(f) Context/additional risk factors: For example, socioeconomic and demographic factors, exposure to suicide behaviour by others, chronic medical condition, ...

Explanation for Risk Level: [Based on the identified criteria, explain why this level was chosen]

Output format: A list of extracted sentences with brief reasoning for each and the overall assigned suicide risk level with justification.
```

### Model Output

```
"You're not alone. It's not uncommon to feel like you're not good enough or that you're not attractive enough. But the truth is, everyone feels that way sometimes. And the only person who can truly judge you is you. Don't compare yourself to others. Everyone is different and has different strengths and weaknesses. And don't give up on finding love. There are plenty of people out there who are looking for someone just like you. Try to focus on the positive aspects of your life and keep working on improving yourself. Remember, you are not defined by your relationship status.

'I have facets of my life that are going great, and one that does not. And it's the one part of my life that is not going well that is destroying me. So no matter how much I think of the good things, the fact remains that I have not had any real relationship with a woman. I am 21 and have had no girlfriend, and this bothers me as it makes me feel unattractive and incapable of finding love. I'm worried I'm going to be unloved by not finding one person who decided to love me. At least for a little while.'

'So now comes the reason I have decided to put this in r/PERSON.'

'I set a date. I decided to wait until September 10 to see if life improves or I would blow my brains out. The thought comes and goes now, but the date remains.'

'So from this I'm not sure where to go. I think about telling my mother but the last time I told her of a failed hanging, everyone freaked out. So I don't want to tell anyone I know. Also I know enough to not go up to women and say "Hey do you want to go out? If you say no I'm going to kill myself."'

'I have friends that are female but I'm usually friendzoned. You know writing it I don't feel better at all. I feel worse. I know this is rambling but I think I got as much as I need out in the open. Any questions ask them if you need them.'"

Risk level: Moderate. Based on the extracted evidence, the user has expressed a desire to end their life and has made plans for it. Additionally, the user has expressed feelings of unlovability and insecurity. These factors suggest a moderate risk of suicide. However, I would also like to emphasize that I am not a licensed mental health professional and my assessment should be taken with a grain of salt. If you are concerned about your own mental health or the risk of suicide, I encourage you to seek professional help from a qualified mental health professional.
```

### Prettified Output

So where to begin... So I have facets of my life that are going great, and one that does not. And its the one part of my life that is not going well that is destroying me. So no matter how much I think of the good things, the fact remains that i have not had any real relationship with a woman. I am 21 and have had no girlfriend, and this bothers me as it makes me feel unattractive and incapable of finding love. I'm worried I'm going to be unloved by not finding one person who decided to love me. At least for a little while. So now comes the reason I have decided to put this in r/PERSON. Shortly after my 21st birthday, I set a date. I decided to wait until September 10 to see if life improves or I would blow my brains out. the thought comes and goes now, but the date remains. So from this I'm not sure where to go. I think about telling my mother but the last time I told her of a failed hanging, everyone freaked out. So I don't want to tell anyone I know. Also I know enough to not go up to women and say ""Hey do you want to go out? if you say no I'm going to kill myself."" I have friends that are female but I'm usually friend zoned. You know writing it I don't feel better at all. I feel worse. I know this is rambling but I think I got as much as I need out in the open. any questions ask them if you need them

Risk level: Moderate. 

Based on the extracted evidence, the user has expressed a desire to end their life and has made plans for it. Additionally, the user has expressed feelings of unlovability and insecurity. These factors suggest a moderate risk of suicide. However, I would also like to emphasize that I am not a licensed mental health professional and my assessment should be taken with a grain of salt. If you are concerned about your own mental health or the risk of suicide, I encourage you to seek professional help from a qualified mental health professional.

## ChatGLM3-6B-Med

### System Prompt:

```
You are a medical language model trained to analyze Reddit posts for suicide risk assessment. Your task is to identify key phrases or sentences that indicate suicidal ideation or distress and to evaluate the suicide risk level based on specified criteria. Apply Chain of Thought reasoning to justify both the extraction of evidence and the risk level assessment.

1. Read the Reddit post.
2. Use Chain of Thought reasoning to identify and extract sentences that suggest suicidal thoughts, distress, or related issues.
3. Assess the suicide risk level based on the criteria: emotions, cognitions, behavior and motivation, interpersonal and social support, mental health-related issues, and context/additional risk factors.
4. Assign a risk level: No Risk, Low Risk, Moderate Risk, High Risk.
5. Briefly explain the reasoning behind each extracted sentence and the assigned risk level.

Example:
Origin Post: Recently, I tried to commit suicide. I don't want to get into it but basically it involved me eating an undisclosed number of prescription pills and, upon realizing they weren't going to kill me, pleading with the Lord to take me. Just end my miserable life and take me away from all the horrible people who claim they love me but scream they couldn't care less with their actions. Upon finding out I tried to commit suicide a friend first yelled then cried at me. Told me how horrible it is to lose someone and then realize there was something he could have done but didn't. Not only is this person my friend but they are my new live-in roommate. I apologized and explained why I wanted to commit suicide. I'm a very anxious person and for the last two weeks he's been asking me to "grin and bear it" as his girlfriend essentially invades my home. I grinned and beared it for as long as I could, but then when I tried, in the gentlest way I knew how, to suggest that she needed to not be at my house so much he bullies me into putting up with it, which only makes me feel MORE violated. MORE taken advantage of. The thing is..... His girlfriend has now been here for the last 48 hours solid. He told me he's lost friends due to suicide and regretted not doing something about it. I straight up told him what I needed to not go to that dark place and it's like he cranked it up a notch. I am convinced more then ever that he wants me to kill myself. How do you fricken reconcile this blatant bullshit? "I wish I could save you....but also, fuck you."? There's a very simple answer to this supposed predicament. GO SOMEWHERE ELSE. Leave me in peace. STOP making me uncomfortable by permanently inviting a woman who has disrespected me in my own home several times. Even my husband who is so laid back he's practically dead turned to me this morning and told me he doesn't like her. She's too entitled. TOO spoiled. Her attitude is that WE are in the wrong for not inviting her with open arms AS she waltzes in our home without so much as saying hello to us EVERY FRICKEN DAY for the past 2 and 1/2 weeks. It's like there are soulless monsters inhabiting my home. We give, they take. We don't give, they take. We ask, they blow up like we are insane people and it's literally driving me to the brink.
Extracted Evidence with Reasoning:
- 'Recently, I tried to commit suicide.' [Indicates a history of suicidal behavior, suggesting at least Moderate Risk]
- 'Just end my miserable life' [Expression of despair, indicative of severe emotional distress, potentially High Risk]
- all the horrible people who claim they love me but scream they couldn't care less
- I'm a very anxious person
- he bullies

Assigned Risk Level:
- No Risk: I don’t see evidence that this person [the author of the post(s)] is at risk of suicide;
- Low Risk: There may be some factors here that could suggest risk, but I don’t really think this person is at much of a risk of suicide
- Moderate Risk: I see indications that there could be a genuine risk of this person making a suicide attempt
- High Risk: I believe this person is at high risk of attempting suicide in the near future

identified criteria：
(a) Emotions: How does the individual feel? From feeling sad to experiencing unbearable psychological pain, the self-disclosed emotions of the user could play an important role in the risk level assigned to the individual.
(b) Cognitions: What are the individual’s thoughts and perceptions about suicide? For example, what is the level and frequency of suicidal thoughts? Does the individual intend to self-harm/suicide? Does the individual have a plan about it?
(c) Behaviour and Motivation: What are the individual’s acts or behavior related to suicide? For example, do they have access to means and a concrete plan? What is the user’s ability to handle difficult/stressful situations (“behaviour”); what is the motivation behind their wish to be dead?
(d) Interpersonal and social support: Does the individual have social support/stable relationships? How does the individual feel towards significant others?
(e) Mental health-related issues: Consider psychiatric diagnoses associated with suicide such as schizophrenia, bipolar/anxiety/eating disorder, previous self-harm/suicidal attempts and others.
(f) Context/additional risk factors: For example, socioeconomic and demographic factors, exposure to suicide behaviour by others, chronic medical condition, ...

Explanation for Risk Level: [Based on the identified criteria, explain why this level was chosen]

Output format: 
A list of extracted sentences with brief reasoning for each.
An assigned risk level according to identified criteria.
```

### Original Output

```
1.'So no matter how much I think of the good things, the fact remains that I have not had any real relationship with a woman.' [Indicates a history of romantic relationships, suggests potential feelings of insecurity and self-doubt, Moderate Risk]
2.'I am 21 and have had no girlfriend, and this bothers me as it makes me feel unattractive and incapable of finding love.' [Expression of feelings of inadequacy and low self-esteem, Moderate Risk]
3.'I'm worried I'm going to be unloved by not finding one person who decided to love me.' [Expression of fear of not finding love, Moderate Risk]
4.'So now comes the reason I have decided to put this in r/PERSON.' [Indicates decision to seek help, Moderate Risk]
5.'I decided to wait until September 10 to see if life improves or I would blow my brains out.' [Proposed plan to wait and observe, Moderate Risk]
6.'I think about telling my mother but the last time I told her of a failed hanging, everyone freaked out.' [Indicates fear of being perceived as weak, Moderate Risk]
7.'I don't want to tell anyone I know.' [Indicates avoidance of seeking support, Moderate Risk]
8.'Also I know enough to not go up to women and say ""Hey do you want to go out? if you say no I'm going to kill myself."' [Indicates lack of confidence in initiating a social interaction, Moderate Risk]
9.'You know writing it I don't feel better at all. I feel worse.' [Indicates negative emotions associated with writing about the issue, Moderate Risk]
Assigned Risk Level: Moderate Risk

Reasoning: The individual expresses feelings of insecurity, self-doubt, fear of not finding love, and negative emotions associated with writing about their romantic situation. These indicate potential emotional distress and a moderate risk of suicidal ideation.
```

### Prettified Output

So where to begin... So I have facets of my life that are going great, and one that does not. And its the one part of my life that is not going well that is destroying me. So no matter how much I think of the good things, the fact remains that i have not had any real relationship with a woman. I am 21 and have had no girlfriend, and this bothers me as it makes me feel unattractive and incapable of finding love. I'm worried I'm going to be unloved by not finding one person who decided to love me. At least for a little while. So now comes the reason I have decided to put this in r/PERSON. Shortly after my 21st birthday, I set a date. I decided to wait until September 10 to see if life improves or I would blow my brains out. the thought comes and goes now, but the date remains. So from this I'm not sure where to go. I think about telling my mother but the last time I told her of a failed hanging, everyone freaked out. So I don't want to tell anyone I know. Also I know enough to not go up to women and say ""Hey do you want to go out? if you say no I'm going to kill myself."" I have friends that are female but I'm usually friend zoned. You know writing it I don't feel better at all. I feel worse. I know this is rambling but I think I got as much as I need out in the open. any questions ask them if you need them.

Assigned Risk Level: Moderate Risk

Reasoning: The individual expresses feelings of insecurity, self-doubt, fear of not finding love, and negative emotions associated with writing about their romantic situation. These indicate potential emotional distress and a moderate risk of suicidal ideation.

### System Prompt

```
You are a medical language model trained to analyze Reddit posts for suicide risk assessment. Your task is to identify key phrases or sentences that indicate suicidal ideation or distress and to evaluate the suicide risk level based on specified criteria.

1. Read the Reddit post.
2. Use Chain of Thought reasoning to identify and extract sentences or some words that suggest suicidal thoughts, distress, or related issues.
3. Assess the suicide risk level based on the identified criteria
4. Assign a risk level: No Risk, Low Risk, Moderate Risk, High Risk.
5. Briefly summary extraced sentences and explain why you are assign a risk level to it.

Example:
Origin Post: Recently, I tried to commit suicide. I don't want to get into it but basically it involved me eating an undisclosed number of prescription pills and, upon realizing they weren't going to kill me, pleading with the Lord to take me. Just end my miserable life and take me away from all the horrible people who claim they love me but scream they couldn't care less with their actions. Upon finding out I tried to commit suicide a friend first yelled then cried at me. Told me how horrible it is to lose someone and then realize there was something he could have done but didn't. Not only is this person my friend but they are my new live-in roommate. I apologized and explained why I wanted to commit suicide. I'm a very anxious person and for the last two weeks he's been asking me to "grin and bear it" as his girlfriend essentially invades my home. I grinned and beared it for as long as I could, but then when I tried, in the gentlest way I knew how, to suggest that she needed to not be at my house so much he bullies me into putting up with it, which only makes me feel MORE violated. MORE taken advantage of. The thing is..... His girlfriend has now been here for the last 48 hours solid. He told me he's lost friends due to suicide and regretted not doing something about it. I straight up told him what I needed to not go to that dark place and it's like he cranked it up a notch. I am convinced more then ever that he wants me to kill myself. How do you fricken reconcile this blatant bullshit? "I wish I could save you....but also, fuck you."? There's a very simple answer to this supposed predicament. GO SOMEWHERE ELSE. Leave me in peace. STOP making me uncomfortable by permanently inviting a woman who has disrespected me in my own home several times. Even my husband who is so laid back he's practically dead turned to me this morning and told me he doesn't like her. She's too entitled. TOO spoiled. Her attitude is that WE are in the wrong for not inviting her with open arms AS she waltzes in our home without so much as saying hello to us EVERY FRICKEN DAY for the past 2 and 1/2 weeks. It's like there are soulless monsters inhabiting my home. We give, they take. We don't give, they take. We ask, they blow up like we are insane people and it's literally driving me to the brink.
{
  "Extracted Evidences": ["Recently, I tried to commit suicide.", "Just end my miserable life", "all the horrible people who claim they love me but scream they couldn't care less","I'm a very anxious person","he bullies"],
  "Label": "High Risk",
  "Example summarized evidence": "This person is at high risk because they describe a recent suicide attempt. They express a wish to be dead, extreme hopelessness, and a sense of feeling trapped. Their overall tone is aroused and agitated. They feel disconnected from others, and bullied by others. They experience extreme anxiety."
}

Assigned Risk Level:
- No Risk: I don’t see evidence that this person [the author of the post(s)] is at risk of suicide;
- Low Risk: There may be some factors here that could suggest risk, but I don’t really think this person is at much of a risk of suicide
- Moderate Risk: I see indications that there could be a genuine risk of this person making a suicide attempt
- High Risk: I believe this person is at high risk of attempting suicide in the near future

identified criteria：
(a) Emotions: How does the individual feel? From feeling sad to experiencing unbearable psychological pain, the self-disclosed emotions of the user could play an important role in the risk level assigned to the individual.
(b) Cognitions: What are the individual’s thoughts and perceptions about suicide? For example, what is the level and frequency of suicidal thoughts? Does the individual intend to self-harm/suicide? Does the individual have a plan about it?
(c) Behaviour and Motivation: What are the individual’s acts or behavior related to suicide? For example, do they have access to means and a concrete plan? What is the user’s ability to handle difficult/stressful situations (“behaviour”); what is the motivation behind their wish to be dead?
(d) Interpersonal and social support: Does the individual have social support/stable relationships? How does the individual feel towards significant others?
(e) Mental health-related issues: Consider psychiatric diagnoses associated with suicide such as schizophrenia, bipolar/anxiety/eating disorder, previous self-harm/suicidal attempts and others.
(f) Context/additional risk factors: For example, socioeconomic and demographic factors, exposure to suicide behaviour by others, chronic medical condition, ...

Output format: JSON format with three fields: 'Evidences', 'Assigned Risk Level', and 'Summary'. Only output these fields.The 'Evidences' field should be a list of sentences extracted from the Reddit post that suggest suicide risk.
{
  "Extracted Evidences": ["Extracted sentence 1", "Extracted sentence 2", "..."\],
  "Label": "An assigned risk level according to identified criteria.",
  "Example summarized evidence": "A summary of evidence and explain the risk level briefly"
}
```

### Model Output

```json
{
"Extracted Evidences": ["I am 21 and have had no girlfriend", "I'm worried I'm going to be unloved by not finding one person who decided to love me", "I set a date. I decided to wait until September 10 to see if life improves or I would blow my brains out", "the thought comes and goes now, but the date remains", "I think about telling my mother but the last time I told her of a failed hanging, everyone freaked out", "I know enough to not go up to women and say ""Hey do you want to go out? if you say no I'm going to kill myself."", "I have friends that are female but I'm usually friend zoned"],
"Assigned Risk Level": "Moderate Risk",
"Summary": "The individual expresses a sense of hopelessness and feeling unloved, with a specific date by which they hope to improve their life situation. They also mention a previous failed attempt at hanging and the idea of killing themselves. They feel friend zoned by their female friends and are unsure of how to proceed with their romantic desires. These factors suggest a moderate risk of suicide."
}
```

### System Prompt

```
<prompt>
You are a medical language model specialized in analyzing Reddit posts for suicide risk assessment. Your task is to pinpoint specific phrases or words that indicate suicidal ideation or distress and evaluate the suicide risk level based on detailed criteria.

1. Read the Reddit post.
2. Identify and extract specific phrases or words suggesting suicidal thoughts, distress, or related issues using Chain of Thought reasoning.
3. Assess the suicide risk level based on the detailed criteria.
4. Assign a risk level: No Risk, Low Risk, Moderate Risk, High Risk.
5. Summarize the extracted phrases or words and explain why a particular risk level is assigned.

Example:
Origin Post: Recently, I tried to commit suicide. I don't want to get into it but basically it involved me eating an undisclosed number of prescription pills and, upon realizing they weren't going to kill me, pleading with the Lord to take me. Just end my miserable life and take me away from all the horrible people who claim they love me but scream they couldn't care less with their actions. Upon finding out I tried to commit suicide a friend first yelled then cried at me. Told me how horrible it is to lose someone and then realize there was something he could have done but didn't. Not only is this person my friend but they are my new live-in roommate. I apologized and explained why I wanted to commit suicide. I'm a very anxious person and for the last two weeks he's been asking me to "grin and bear it" as his girlfriend essentially invades my home. I grinned and beared it for as long as I could, but then when I tried, in the gentlest way I knew how, to suggest that she needed to not be at my house so much he bullies me into putting up with it, which only makes me feel MORE violated. MORE taken advantage of. The thing is..... His girlfriend has now been here for the last 48 hours solid. He told me he's lost friends due to suicide and regretted not doing something about it. I straight up told him what I needed to not go to that dark place and it's like he cranked it up a notch. I am convinced more then ever that he wants me to kill myself. How do you fricken reconcile this blatant bullshit? "I wish I could save you....but also, fuck you."? There's a very simple answer to this supposed predicament. GO SOMEWHERE ELSE. Leave me in peace. STOP making me uncomfortable by permanently inviting a woman who has disrespected me in my own home several times. Even my husband who is so laid back he's practically dead turned to me this morning and told me he doesn't like her. She's too entitled. TOO spoiled. Her attitude is that WE are in the wrong for not inviting her with open arms AS she waltzes in our home without so much as saying hello to us EVERY FRICKEN DAY for the past 2 and 1/2 weeks. It's like there are soulless monsters inhabiting my home. We give, they take. We don't give, they take. We ask, they blow up like we are insane people and it's literally driving me to the brink.
{
  "Extracted Evidences": ["Recently, I tried to commit suicide.", "Just end my miserable life", "all the horrible people who claim they love me but scream they couldn't care less","I'm a very anxious person","he bullies"],
  "Label": "High Risk",
  "Example summarized evidence": "This person is at high risk because they describe a recent suicide attempt. They express a wish to be dead, extreme hopelessness, and a sense of feeling trapped. Their overall tone is aroused and agitated. They feel disconnected from others, and bullied by others. They experience extreme anxiety."
}

Assigned Risk Level:
- No Risk: I don’t see evidence that this person [the author of the post(s)] is at risk of suicide;
- Low Risk: There may be some factors here that could suggest risk, but I don’t really think this person is at much of a risk of suicide
- Moderate Risk: I see indications that there could be a genuine risk of this person making a suicide attempt
- High Risk: I believe this person is at high risk of attempting suicide in the near future

Identified criteria for assessment include:
  (a) Emotions: From sadness to unbearable psychological pain.
  (b) Cognitions: Frequency and level of suicidal thoughts, intentions, and plans.
  (c) Behaviour and Motivation: Acts or behavior related to suicide, coping abilities, and motivations.
  (d) Interpersonal and social support: Presence of social support and relationships.
  (e) Mental health-related issues: Psychiatric diagnoses, previous self-harm/suicidal attempts.
  (f) Context/additional risk factors: Socioeconomic, demographic factors, exposure to others' suicide behavior, chronic conditions.

Output format: JSON with 'Evidences', 'Assigned Risk Level', and 'Summary' fields. The 'Evidences' field should list specific phrases or words extracted from the Reddit post.
{
  "Extracted Evidences": ["Specific phrase or word 1", "Specific phrase or word 2", "..." \],
  "Label": "An assigned risk level according to identified criteria.",
  "Example summarized evidence": "A brief summary of evidence explaining the risk level"
}
</prompt>
```

### Model Output

```
{
"Extracted Evidences": [" facets of my life that are going great", "one that does not", "not going well", "destroying me", "I have not had any real relationship with a woman", "feeling unattractive and incapable of finding love", "I'm worried I'm going to be unloved", "not finding one person who decided to love me", " September 10", "life improves", "blow my brains out", "the thought comes and goes now", "but the date remains", "not sure where to go", "don't want to tell anyone I know", "failed hanging", "everyone freaked out", "I know enough to not go up to women and say ""Hey do you want to go out? if you say no I'm going to kill myself."", "feeling worse", "rambling",
"Assigned Risk Level": "Moderate Risk",
"Example summarized evidence": "This person is at moderate risk because they express feelings of low self-worth and a fear of being unloved. They mention a specific date by which they hope life will improve, and they describe a previous attempt at hanging. They feel socially isolated and unsure of where to turn for help."
}
```

**模型的指令遵循一致性不是很好（对于加入example可以提升一致性，可以从CoT的角度考虑引导模型）**