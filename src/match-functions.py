import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity



df = pd.read_csv('../resume-data/jobs.csv')

# Step 1: Load the pre-trained model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Step 2: Encode job descriptions into embeddings
job_embeddings = model.encode(df['Job Description'].tolist(), convert_to_tensor=True)

# Step 3: Example resume data
resume = "Experienced Data Scientist skilled in Python, machine learning, and data analysis."

# Step 4: Encode resume into an embedding
resume_embedding = model.encode([resume], convert_to_tensor=True)

# Step 5: Calculate cosine similarities
# Convert embeddings to numpy arrays first
resume_embedding_cpu = resume_embedding.cpu().detach().numpy()
job_embeddings_cpu = job_embeddings.cpu().detach().numpy()
similarities = cosine_similarity(resume_embedding_cpu, job_embeddings_cpu)

# Step 6: Get the indices of the top 5 most similar job descriptions
top_3_indices = similarities[0].argsort()[-3:][::-1]  # Sort in descending order and get top 5

# Step 7: Retrieve the top 5 matching job titles and descriptions
top_3_matches = df.iloc[top_3_indices]

# Step 8: Print the results
print("Top 3 matching job descriptions:")
for idx, row in top_3_matches.iterrows():
    print(f"Title: {row['Job Title']}\nDescription: {row['Job Description']}\n")
