# app/voucher_search_app.py

import streamlit as st
import random
from typing import List, Dict

# --- Mock function to simulate voucher search ---
def search_vouchers(platform: str, keyword: str) -> List[Dict]:
    mock_data = [
        {
            "title": f"{platform} - {keyword.title()} 50% OFF",
            "discount": random.randint(10, 90),
            "cashback": random.choice([0, 5, 10, 15, 20]),
            "free_shipping": random.choice([True, False]),
            "link": f"https://{platform.lower()}.com/search?q={keyword}"
        }
        for _ in range(random.randint(3, 7))
    ]
    return mock_data

# --- Ranking logic ---
def rank_vouchers(vouchers: List[Dict]) -> List[Dict]:
    def score(v):
        return v['discount'] * 2 + v['cashback'] * 1.5 + (20 if v['free_shipping'] else 0)
    return sorted(vouchers, key=score, reverse=True)

# --- Streamlit UI ---
st.set_page_config(page_title="Voucher Search Tool", layout="wide")
st.title("🔎 Internet Voucher Hunter")

keyword = st.text_input("Enter product or category to search for vouchers:", "laptop")

st.markdown("Select platforms to search:")
platforms_selected = []
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.checkbox("Shopee", True): platforms_selected.append("Shopee")
with col2:
    if st.checkbox("Lazada", True): platforms_selected.append("Lazada")
with col3:
    if st.checkbox("Amazon", True): platforms_selected.append("Amazon")
with col4:
    if st.checkbox("Temu", True): platforms_selected.append("Temu")

search_btn = st.button("Search Vouchers")

if search_btn and keyword:
    all_results = []
    for platform in platforms_selected:
        results = search_vouchers(platform, keyword)
        all_results.extend(results)

    ranked = rank_vouchers(all_results)

    st.subheader(f"🎯 Top Voucher Results for '{keyword}'")
    for voucher in ranked:
        with st.container():
            st.markdown(f"### [{voucher['title']}]({voucher['link']})")
            col1, col2, col3 = st.columns(3)
            col1.metric("Discount", f"{voucher['discount']}%")
            col2.metric("Cashback", f"{voucher['cashback']}%")
            col3.metric("Free Shipping", "✅" if voucher['free_shipping'] else "❌")
            st.markdown("---")
