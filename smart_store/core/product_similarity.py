
from gensim.models import Word2Vec
import os
from django.conf import settings

# مسار المودل
MODEL_PATH = os.path.join(settings.BASE_DIR, "product_similarity.model")

# تحميل المودل
model = Word2Vec.load(MODEL_PATH)


def get_similar_products(product):
    similar_products = model.wv.most_similar(product, topn=5)

    return [
        {
            "name": name,
            "score": score,
            "image": f"images/{name}.jpg"
        }
        for name, score in similar_products
    ]