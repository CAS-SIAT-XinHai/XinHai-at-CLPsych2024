# Copyright 2020 The HuggingFace Datasets Authors and the current dataset script contributor.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datasets
import pandas as pd

_CITATION = """\
Han-Chin Shing, Suraj Nair, Ayah Zirikly, Meir Friedenberg, Hal Daumé III, and Philip Resnik, "Expert, Crowdsourced, and Machine Assessment of Suicide Risk via Online Postings", Proceedings of the Fifth Workshop on Computational Linguistics and Clinical Psychology: From Keyboard to Clinic, pages 25–36, New Orleans, Louisiana, June 5, 2018.
@inproceedings{shing2018expert,
  title={Expert, crowdsourced, and machine assessment of suicide risk via online postings},
  author={Shing, Han-Chin and Nair, Suraj and Zirikly, Ayah and Friedenberg, Meir and {Daum{\'e} III}, Hal and Resnik, Philip},
  booktitle={Proceedings of the Fifth Workshop on Computational Linguistics and Clinical Psychology: From Keyboard to Clinic},
  pages={25--36},
  year={2018}
}

Ayah Zirikly, Philip Resnik, Özlem Uzuner, and Kristy Hollingshead. 2019. CLPsych 2019 shared task: Predicting the degree of suicide risk in Reddit posts. In Proceedings of the Sixth Workshop on Computational Linguistics and Clinical Psychology (CLPsych'19), Minneapolis, June 6, 2019.
@inproceedings{zirikly2019clpsych,
  title={{CLPsych} 2019 Shared Task: Predicting the Degree of Suicide Risk in {Reddit} Posts},
  author={Zirikly, Ayah and Resnik, Philip and Uzuner, {\"O}zlem and Hollingshead, Kristy}, 
  booktitle={Proceedings of the Sixth Workshop on Computational Linguistics and Clinical Psychology},
  location="Minneapolis",
  month="June",
  day="6",
  year={2019}
}
"""

_DESCRIPTION = """\
The University of Maryland Reddit Suicidality Dataset Version 2

********************************************************************************
THIS DATASET IS NOT PUBLICLY AVAILABLE. PLEASE DO NOT USE IT WITHOUT PERMISSION.

To request permission to use to the dataset, please see
http://users.umiacs.umd.edu/~resnik/umd_reddit_suicidality_dataset.html or
contact Philip Resnik, resnik@umd.edu
********************************************************************************

The University of Maryland Reddit Suicidality Dataset has been constructed using
data from Reddit, an online site for anonymous discussion on a wide variety of
topics, in order to facilitate research on suicidality and suicide prevention.
The dataset was constructed from the 2015 Full Reddit Submission Corpus, using
postings in the r/SuicideWatch subreddit to identify (anonymous) users who might
represent positive instances of suicidality.

As we discuss in Shing et al. (2018) and Zirikly et al. (2019), annotation of
users in this dataset for level of suicide risk (on a four-point scale of no
risk, low, moderate, and severe risk) has yielded what is, to our knowledge, the
first demonstration of reliability in risk assessment by clinicians based on
social media postings. The paper also introduces and demonstrates the value of a
new, detailed rubric for assessing suicide risk, compares crowdsourced with
expert performance, and presents baseline predictive modeling experiments using
the new dataset.

## Reference:
When using the dataset, please cite these two papers:

* Han-Chin Shing, Suraj Nair, Ayah Zirikly, Meir Friedenberg, Hal Daumé III, and
Philip Resnik, "Expert, Crowdsourced, and Machine Assessment of Suicide Risk via
Online Postings", Proceedings of the Fifth Workshop on Computational Linguistics
and Clinical Psychology: From Keyboard to Clinic, pages 25–36, New Orleans,
Louisiana, June 5, 2018.

* Ayah Zirikly, Philip Resnik, Özlem Uzuner, and Kristy Hollingshead. CLPsych
2019 Shared Task: Predicting the Degree of Suicide Risk in Reddit Posts.
Proceedings of the Sixth Workshop on Computational Linguistics and Clinical
Psychology, pages 24–33, Minneapolis, Minnesota, June 6, 2019.

#### Tasks
- **Task A**: Risk Assessment for SuicideWatch posters based *only* on their
SuicideWatch postings.

- **Task B**: Risk Assessment for SuicideWatch posters based on their
SuicideWatch postings *and* other Reddit postings.

- **Task C**: Screening. This task looks at posts that are *NOT* on
SuicideWatch, and determine the user's level of risk.

For both annotations, possible values include *a*, *b*, *c*, *d* or *None*. *a*
means *No Risk*, *b* means *Low Risk*, *c* means *Moderate Risk*, and *d* means
*Severe Risk*. If a user is a control user, they automatically receive a *None*
label, since we did not use human annotators to label control users.

"""

_HOMEPAGE = "http://users.umiacs.umd.edu/~resnik/umd_reddit_suicidality_dataset.html "

_LICENSE = "THIS DATASET IS NOT PUBLICLY AVAILABLE. PLEASE DO NOT USE IT WITHOUT PERMISSION."

_URL = "umd_reddit_suicidewatch_dataset_v2.zip"

task_list = [
    "A",
    "B",
    "C"
]


class UMDRedditSuicidewatchConfig(datasets.BuilderConfig):
    def __init__(self, **kwargs):
        super().__init__(version=datasets.Version("1.0.0"), **kwargs)


class UMDRedditSuicidewatch(datasets.GeneratorBasedBuilder):
    BUILDER_CONFIGS = [
        UMDRedditSuicidewatchConfig(
            name=task_name,
        )
        for task_name in task_list
    ]

    def _info(self):
        features = datasets.Features(
            {
                "user_id": datasets.Value("int32"),
                "posts": datasets.Value("string"),
                "A": datasets.Value("string"),
                "B": datasets.Value("string"),
                "C": datasets.Value("string"),
                "D": datasets.Value("string"),
                "answer": datasets.Value("string"),
            }
        )
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=features,
            homepage=_HOMEPAGE,
            license=_LICENSE,
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        data_dir = dl_manager.download_and_extract(_URL)
        task_name = self.config.name

        df_expert_labels = pd.read_csv(f'{data_dir}/expert/expert.csv')
        df_expert_posts = pd.read_csv(f'{data_dir}/expert/expert_posts.csv')

        df_train_labels_with_control = pd.read_csv(f'{data_dir}/crowd/train/crowd_train.csv')
        df_train_posts_with_control = pd.read_csv(f'{data_dir}/crowd/train/shared_task_posts.csv')

        # df_test_labels_with_control = pd.read_csv(f'{data_dir}/crowd/test/crowd_test.csv')
        df_test_posts_with_control = pd.read_csv(f'{data_dir}/crowd/test/shared_task_posts_test.csv')

        df_train_posts = pd.read_csv(f"{data_dir}/crowd/train/task_{task_name}_train.posts.csv")
        # df_train_labels = pd.read_csv(f"{data_dir}/crowd/train/crowd_train_{task_name}.csv")

        df_test_posts = pd.read_csv(f"{data_dir}/crowd/test/task_{task_name}_test.posts.csv")
        df_test_labels = pd.read_csv(f"{data_dir}/crowd/test/crowd_test_{task_name}.csv")

        df_train_task_with_posts = pd.merge(df_train_posts, df_train_posts_with_control, on='post_id', how='inner',
                                            suffixes=("", "_y"))
        df_test_task_with_posts = pd.merge(df_test_posts, df_test_posts_with_control, on='post_id', how='inner',
                                           suffixes=("", "_y"))

        return [
            datasets.SplitGenerator(
                name=datasets.Split.TEST,
                gen_kwargs={
                    "merged_df": pd.merge(df_test_task_with_posts, df_test_labels, on='user_id', how='inner')
                },
            ),
            datasets.SplitGenerator(
                name=datasets.Split.VALIDATION,
                gen_kwargs={
                    "merged_df": pd.merge(df_expert_posts, df_expert_labels, on='user_id', how='inner',
                                          suffixes=("", "_y"))
                },
            ),
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN,
                gen_kwargs={
                    "merged_df": pd.merge(df_train_task_with_posts, df_train_labels_with_control, on='user_id',
                                          how='inner',
                                          suffixes=("", "_y"))
                },
            )
        ]

    def _generate_examples(self, merged_df):
        merged_df.sort_values(['user_id', 'timestamp'], inplace=True)
        # label_columns = ['EmotionalPolarity', 'Emotion', 'Empathy']
        for i, (user_id, group_df) in enumerate(merged_df.groupby('user_id')):
            group_df.fillna("", inplace=True)
            posts = '\n\n'.join([f"{s}: {t}" for s, t in
                                 zip(group_df.post_title.tolist(), group_df.post_body.tolist())])
            instance = {
                'user_id': user_id,
                'posts': posts,
                "A": "No Risk",
                "B": "Low Risk",
                "C": "Moderate Risk",
                "D": "High Risk",
                "answer": group_df.label.unique().tolist()[0].upper()
            }
            yield i, instance
