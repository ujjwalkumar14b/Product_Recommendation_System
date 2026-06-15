from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)
df = pd.read_csv("Product_Recommendation_System.csv", encoding="latin1")

products = sorted(df["Description"].dropna().astype(str).unique().tolist())

model_popular = joblib.load("model_popular.pkl")
model_cf_item = joblib.load("model_cf_item.pkl")
model_content = joblib.load("model_content.pkl")
model_hybrid = joblib.load("model_hybrid.pkl")

product_details = {}

for _, row in df.iterrows():
    product = str(row["Description"])
    if product not in product_details:
        product_details[product] = {
            "price": round(float(row["UnitPrice"]), 2),
            "country": str(row["Country"])
        }

# POPULARITY
def popularity_recommend(top_n=10):
    return list(model_popular[:top_n])

# ITEM BASED
def item_based_recommend(product_name, top_n=10):
    try:
        if product_name not in model_cf_item.index:
            return []

        recommendations = (
            model_cf_item[product_name]
            .sort_values(ascending=False)
            .iloc[1:top_n + 1]
            .index
            .tolist()
        )
        return recommendations

    except Exception as e:
        print("Item CF Error:", e)
        return []

# CONTENT BASED
def content_recommend(product_name, top_n=10):
    try:
        if product_name not in model_content.index:
            return []

        recommendations = (
            model_content[product_name]
            .sort_values(ascending=False)
            .iloc[1:top_n + 1]
            .index
            .tolist()
        )
        return recommendations

    except Exception as e:
        print("Content Error:", e)
        return []

# HYBRID
def hybrid_recommend(product_name, top_n=10):
    try:
        if (product_name not in model_cf_item.index or product_name not in model_content.index):
            return []

        item_scores = model_cf_item[product_name]
        content_scores = model_content[product_name]
        hybrid_scores = (item_scores * 0.6 + content_scores * 0.4)

        recommendations = (
            hybrid_scores
            .sort_values(ascending=False)
            .iloc[1:top_n + 1]
            .index
            .tolist()
        )
        return recommendations

    except Exception as e:
        print("Hybrid Error:", e)
        return []

# HOME
@app.route("/")
def home():
    return render_template(
        "index.html",
        products=products,
        selected_product=None,
        popular_recommendations=[],
        item_recommendations=[],
        content_recommendations=[],
        hybrid_recommendations=[],
        product_details=product_details
    )

# RECOMMEND

@app.route("/recommend", methods=["POST"])
def recommend():
    selected_product = request.form.get("product")
    popular_recommendations = popularity_recommend()
    item_recommendations = item_based_recommend(selected_product)
    content_recommendations = content_recommend(selected_product)
    hybrid_recommendations = hybrid_recommend(selected_product)

    return render_template(
        "index.html",
        products=products,
        selected_product=selected_product,
        popular_recommendations=popular_recommendations,
        item_recommendations=item_recommendations,
        content_recommendations=content_recommendations,
        hybrid_recommendations=hybrid_recommendations,
        product_details=product_details
    )

# RUN
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)