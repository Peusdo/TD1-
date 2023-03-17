import plotly.graph_objects as go
from wordcloud import WordCloud
import en_core_web_sm
import plotly.io as pio
import plotly
import json
from collections import Counter
import re


text = """Online learning is an important technical means for sketching massive real-time and high-speed data. 
Although this direction has attracted intensive attention, most of the literature in this area ignore the following 
three issues: they think little of the underlying abstract hierarchical latent information exist- ing in examples, 
even if extracting these abstract hierarchical latent representations is useful to better predict the class labels of 
examples; the idea of preassigned model on unseen datapoints is not suitable for modeling streaming data with 
evolving probability distribution. This challenge is referred as model flexibility. And so, with this in minds, 
the online deep learning model we need to design should have a variable underlying structure; moreover, 
it is of utmost importance to fusion these abstract hierarchical latent representations to achieve better 
classification performance, and we should give different weights to different levels of implicit representation 
information when dealing with the data streaming where the data distribution changes. To address these issues, 
we propose a two-phase Online Deep Learning based on Auto-Encoder (ODLAE). Based on auto-encoder, considering 
reconstruction loss, we extract abstract hierarchical latent representations of instances; Based on predictive loss, 
we devise two fusion strategies: the output-level fusion strategy, which is obtained by fusing the classification 
results of en- coder each hidden layer; and feature-level fusion strategy, which is leveraged self-attention 
mechanism to fusion every hidden layer output. Finally, in order to improve the robustness of the algorithm, 
we also try to utilize the denoising auto-encoder to yield hierarchical latent representations. Experimental results 
on different datasets are presented to verify the validity of our proposed algorithm (ODLAE) outperforms several 
baselines."""


def get_most_frequent_words(texte):
    """
    Get the most frequent words
    :return: list of tuples (word, number of occurences)
    """
    # Get the more frequent words
    words = re.findall(r'\w+', texte.lower())
    return Counter(words).most_common()


def plot_wordcloud_most_frequent_words_len_more_6(texte):
    fig = None
    try:
        words = get_most_frequent_words(texte)
        # only keep the most frequent words that have more than 6 letters and no special characters
        words = [(word, freq) for word, freq in words if len(word) >= 6 and word.isalpha()]
        words = words[:30]

        # create a word cloud with the most frequent words with wordcloud, given a list of tuples (word, frequency)
        wordcloud = WordCloud(width=1200, height=600, background_color="white").generate_from_frequencies(dict(words))

        # create a plotly figure and return its JSON representation
        fig = go.Figure(data=[go.Image(z=wordcloud.to_array())])
        fig.update_layout(xaxis_title=None,
                          yaxis_title=None,
                          xaxis_visible=False,
                          yaxis_visible=False)
        fig = pio.to_json(fig)
    except Exception as e:
        print("Error in plot_wordcloud_most_frequent_words_len_more_6: ", e)
    return [fig, "Nuage de mots des mots les plus fréquents de taille supérieure ou égale à 6"]


def adjectives(texte):
    """
    Get the adjectives of the text
    :return: list of adjectives
    """
    nlp = en_core_web_sm.load()
    doc = nlp(texte)
    adjectives_list = [token.text for token in doc if token.pos_ == "ADJ"]
    return adjectives_list


def plot_wordcloud_most_frequent_adjectives_last_30(texte):
    fig = None
    try:
        adjectives_list = adjectives(texte)
        # count the number of occurences of each adjective
        adjectives_occur = Counter(adjectives_list)
        # only keep the 30 most frequent adjectives that have no special characters
        adjectives_occur = [x for x in adjectives_occur.most_common() if x[0].isalpha()][:30]
        wordcloud = WordCloud(width=1200, height=600, background_color="white").generate_from_frequencies(
            dict(adjectives_occur))
        fig = go.Figure(data=[go.Image(z=wordcloud.to_array())])
        fig.update_xaxes(showticklabels=False)
        fig.update_yaxes(showticklabels=False)
        fig = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    except Exception as e:
        print("Error in plot_wordcloud_most_frequent_adjectives_last_30: ", e)
    return [fig, "Nuage de mots des 30 adjectifs les plus fréquents"]


if __name__ == '__main__':
    plot_wordcloud_most_frequent_words_len_more_6(text)
    plot_wordcloud_most_frequent_adjectives_last_30(text)