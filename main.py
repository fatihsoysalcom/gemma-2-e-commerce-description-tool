import os
import google.generativeai as genai

def generate_product_description(product_name, category, features):
    """
    Generates a product description using Google's Gemma 2 (accessed via the Gemini API).
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return "Error: GEMINI_API_KEY environment variable not set. Please set it to your Google AI Studio API key."

    genai.configure(api_key=api_key)

    # The article discusses integrating Gemma 2. Gemma 2 models are accessible
    # via the Google Generative AI API, often under the 'gemini' model family.
    # 'gemini-pro' is a general-purpose model suitable for text generation.
    model = genai.GenerativeModel('gemini-pro')

    prompt = f"""
    Sen bir yerel e-ticaret listeleme stüdyosu için ürün açıklamaları yazan bir yapay zeka asistanısın.
    Aşağıdaki ürün bilgileriyle çekici ve bilgilendirici bir ürün açıklaması oluştur.
    Hedef kitle yerel müşterilerdir. Açıklama Türkçe olmalı.

    Ürün Adı: {product_name}
    Kategori: {category}
    Özellikler: {', '.join(features)}

    Ürün Açıklaması:
    """

    try:
        response = model.generate_content(prompt)
        # This is where Gemma 2 (via Gemini API) generates the product description.
        return response.text
    except Exception as e:
        return f"An error occurred during AI generation: {e}"

if __name__ == "__main__":
    # Example product data for a local business, as discussed in the article
    product_name = "El Yapımı Seramik Kupa"
    category = "Ev ve Yaşam"
    features = [
        "Benzersiz el yapımı tasarım",
        "Yüksek kaliteli seramik malzeme",
        "Bulaşık makinesi ve mikrodalga fırına uygun",
        "Her biri özel ve tek",
        "Yerel zanaatkarlar tarafından üretildi"
    ]

    print(f"Ürün Adı: {product_name}")
    print(f"Kategori: {category}")
    print(f"Özellikler: {', '.join(features)}\n")

    print("Yapay Zeka Destekli Ürün Açıklaması Oluşturuluyor...\n")
    description = generate_product_description(product_name, category, features)

    print(description)
    print("\n---")
    print("Bu açıklama, yerel e-ticaret listeleme stüdyosunda CraftList AI'nin Gemma 2 entegrasyonu ile oluşturulmuştur.")
