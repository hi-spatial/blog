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
GENERATED_POSTS_FILE = 'scripts/generated_posts.json'
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

def load_generated_posts():
    """Load the generated posts tracking file"""
    if not os.path.exists(GENERATED_POSTS_FILE):
        return {"generated_posts": []}
    with open(GENERATED_POSTS_FILE, 'r') as f:
        return json.load(f)

def save_generated_posts(data):
    """Save the generated posts tracking file"""
    with open(GENERATED_POSTS_FILE, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def post_exists(title):
    """Check if post with similar title already exists in _posts/ directory"""
    # Generate expected filename patterns
    slug = title.lower().replace(" ", "-")
    slug = re.sub(r'[^a-z0-9-]', '', slug)

    # Check for any date-prefixed file with this slug
    if os.path.exists(POSTS_DIR):
        for filename in os.listdir(POSTS_DIR):
            if filename.endswith('-' + slug + '.md'):
                return True
    return False

def is_post_generated(title, generated_data):
    """Check if title already exists in generated posts tracking"""
    for post in generated_data.get("generated_posts", []):
        if post["title"] == title:
            return True
    return False

def record_generated_post(metadata):
    """Record a newly generated post in the tracking file"""
    data = load_generated_posts()
    data["generated_posts"].append(metadata)
    save_generated_posts(data)

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
    # Calculate WIB time (UTC+7)
    utc_now = datetime.datetime.now(datetime.timezone.utc)
    wib_now = utc_now + datetime.timedelta(hours=7)
    
    date_str = wib_now.strftime("%Y-%m-%d")
    time_str = wib_now.strftime("%H:%M:%S")
    
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
        "date": f"{date_str} {time_str} +0700",
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
    generated_data = load_generated_posts()

    # Stop if no topics available (no recycling)
    if not topics:
        if not used_topics:
            print("No topics available in topics.json")
            exit(0)
        print("All topics exhausted. No more posts to generate.")
        print(f"Total unique posts generated: {len(generated_data.get('generated_posts', []))}")
        exit(0)

    # Find a topic that hasn't been generated yet
    available_topics = []
    for topic in topics:
        if not post_exists(topic['title']) and not is_post_generated(topic['title'], generated_data):
            available_topics.append(topic)

    if not available_topics:
        print("All available topics have already been generated.")
        print(f"Total unique posts generated: {len(generated_data.get('generated_posts', []))}")
        exit(0)

    # Select random topic from available ones
    topic_data = random.choice(available_topics)
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

        # Record in generated_posts.json for deduplication tracking
        # Calculate WIB time for metadata
        utc_now = datetime.datetime.now(datetime.timezone.utc)
        wib_now = utc_now + datetime.timedelta(hours=7)
        date_str = wib_now.strftime("%Y-%m-%d")

        record_generated_post({
            "title": topic_data['title'],
            "slug": slug,
            "date": date_str,
            "category": topic_data['category'],
            "keywords": topic_data['keywords'],
            "generated_at": wib_now.strftime("%Y-%m-%d %H:%M:%S")
        })

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
