import os
import random
import json
import datetime
import yaml
import re
import traceback
from groq import Groq

# Constants
TOPICS_FILE = 'scripts/topics.json'
POSTS_DIR = '_posts'
API_KEY = os.environ.get("GROQ_API_KEY")

if not API_KEY:
    print("Error: GROQ_API_KEY not found in environment variables.")
    exit(1)

client = Groq(api_key=API_KEY)

def load_topics_data():
    if not os.path.exists(TOPICS_FILE):
        return {"topics": [], "used_topics": []}
    with open(TOPICS_FILE, 'r') as f:
        return json.load(f)

def save_topics_data(data):
    with open(TOPICS_FILE, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def generate_post_content(topic_data):
    title = topic_data['title']
    category = topic_data['category']
    keywords = ', '.join(topic_data['keywords'])
    
    prompt = f"""
    Buatkan artikel blog teknis yang lengkap dan mendalam tentang topik: "{title}".
    Kategori: {category}
    Kata Kunci Fokus: {keywords}
    
    Bahasa: Indonesia.
    Target audiens: Pemula hingga Menengah di bidang Geospasial/GIS.
    Format: Markdown.
    
    Struktur artikel:
    1. Pendahuluan (Apa dan Mengapa)
    2. Konsep Dasar / Teori
    3. Tutorial / Langkah-langkah (jika teknis) atau Studi Kasus
    4. Kesimpulan
    
    PENTING:
    - Jangan gunakan h1 (#), mulai dari h2 (##).
    - Sertakan contoh kode jika relevan (misal Python, JS, SQL).
    - Gaya bahasa santai tapi profesional.
    - Output HANYA isi artikel markdown, tanpa frontmatter.
    """
    
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "Anda adalah ahli GIS dan Geospatial Developer yang berpengalaman. Anda menulis artikel teknis yang jelas, akurat, dan mudah dipahami dalam Bahasa Indonesia."
            },
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    
    return chat_completion.choices[0].message.content

def create_post_file(topic_data, content):
    date_str = datetime.date.today().strftime("%Y-%m-%d")
    title = topic_data['title']
    
    # Generate slug from title
    slug = title.lower().replace(" ", "-")
    slug = re.sub(r'[^a-z0-9-]', '', slug)
    filename = f"{date_str}-{slug}.md"
    filepath = os.path.join(POSTS_DIR, filename)
    
    # Use category from data and add standard tags
    categories = [topic_data['category']]
    
    # Add extra categories based on keywords if needed, or just keep simple
    # But let's rely on the predefined category for the main one.
    
    tags = ["AI", "Auto-Generated"] + topic_data['keywords']
    
    frontmatter = {
        "layout": "post",
        "title": title,
        "date": f"{date_str} 00:00:00 +0700",
        "categories": categories,
        "tags": tags,
        "author": "Kodibot"
    }
    
    with open(filepath, "w") as f:
        f.write("---\n")
        yaml.dump(frontmatter, f, default_flow_style=False, allow_unicode=True)
        f.write("---\n\n")
        f.write(content)
        
    return filepath, frontmatter

def main():
    data = load_topics_data()
    topics = data.get('topics', [])
    used_topics = data.get('used_topics', [])
    
    if not topics:
        print("No topics available in topics.json")
        exit(0)
        
    # Select random topic
    topic_data = random.choice(topics)
    print(f"Selected topic: {topic_data['title']}")
    
    # Generate content
    try:
        content = generate_post_content(topic_data)
        
        # Save file
        filepath, fm = create_post_file(topic_data, content)
        print(f"Post saved: {filepath}")
        print(f"Category: {', '.join(fm['categories'])}")
        
        # Calculate and print URL for workflow
        slug = os.path.basename(filepath).split('-', 3)[-1].replace('.md', '')
        cat_slugs = [c.lower().replace(' ', '-') for c in fm['categories']]
        cat_path = '/'.join(cat_slugs)
        print(f"Post URL: https://hi-spatial.github.io/{cat_path}/{slug}/")
        
        # Deduplication: Move to used_topics
        topics.remove(topic_data)
        used_topics.append(topic_data)
        
        data['topics'] = topics
        data['used_topics'] = used_topics
        save_topics_data(data)
        print("Topic moved to used_topics.")
        
    except Exception as e:
        print(f"Error generating post: {e}")
        print("Full traceback:")
        traceback.print_exc()
        exit(1)

if __name__ == "__main__":
    main()
