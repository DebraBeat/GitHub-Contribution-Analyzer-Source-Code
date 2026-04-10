import git_parser
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import re
from wordcloud import WordCloud
from sklearn.tree import DecisionTreeClassifier
from datetime import datetime

# --- 1. ACTIVITY HISTOGRAMS ---
def generate_histogram(username: str) -> plt.Figure:
    """Generates a combined figure with Time of Day and Day of Week histograms."""
    commits = git_parser.get_user_activity(username, pages=2)

    if not commits:
        raise ValueError(f"No recent activity found for user {username}.")
        
    df = pd.DataFrame([c.to_dict() for c in commits])
    df['date'] = pd.to_datetime(df['timestamp'])
    
    # Setup Figure with 2 subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    
    # Plot 1: Time of Day
    df['hour'] = df['date'].dt.hour
    bins = [0, 6, 12, 18, 24]
    labels = ['Late Night (0-6)', 'Morning (6-12)', 'Afternoon (12-18)', 'Evening (18-24)']
    df['time_block'] = pd.cut(df['hour'], bins=bins, labels=labels, right=False)
    
    sns.countplot(data=df, x='time_block', ax=ax1, palette='Blues_d', order=labels)
    ax1.set_title("Contributions by Time of Day")
    ax1.set_xlabel("Time Block")
    ax1.set_ylabel("Number of Commits")
    ax1.tick_params(axis='x', rotation=45)

    # Plot 2: Day of Week
    df['day'] = df['date'].dt.day_name()
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    sns.countplot(data=df, x='day', ax=ax2, palette='viridis', order=day_order)
    ax2.set_title("Contributions by Day of the Week")
    ax2.set_xlabel("Day of Week")
    ax2.set_ylabel("Number of Commits")
    ax2.tick_params(axis='x', rotation=45)

    fig.tight_layout()
    return fig

# --- 2. WORD CLOUD ---
def generate_wordcloud(username: str) -> plt.Figure:
    """Generates a word cloud from a user's commit messages."""
    commits = git_parser.get_user_activity(username, pages=2)
    if not commits:
        raise ValueError(f"No recent activity found for user {username}.")

    # Extract all messages
    full_text = " ".join([c.message for c in commits])
    
    # Filter out non-alphabetic characters (per requirements)
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', full_text)

    if not cleaned_text.strip():
         raise ValueError("No valid English words found in commit messages.")

    # Generate Word Cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='tab20').generate(cleaned_text)

    # Plot
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    ax.set_title(f"Commit Message Word Cloud for {username}", fontsize=16)
    
    return fig

# --- 3. TOP USERS BAR CHART (REPO) ---
def generate_top_users_barchart(repo_url: str, top_n: int = 10) -> plt.Figure:
    """Generates a positive/negative bar chart of lines added and deleted."""
    try:
        url_type, owner, repo = git_parser.parse_github_url(repo_url)
        if url_type != "repo":
            raise ValueError("Please provide a valid repository URL.")
            
        df = git_parser.get_repo_contributor_stats(owner, repo)
    except Exception as e:
        raise ValueError(f"Error fetching repo stats: {e}")

    if df.empty:
        raise ValueError("No contributor data found for this repository.")

    # Sort by Additions and get top N
    df = df.sort_values(by='Additions', ascending=False).head(top_n)

    fig, ax = plt.subplots(figsize=(8, 4))

    # Plot Positive Y (Additions)
    ax.bar(df['Author'], df['Additions'], color='green', label='Lines Added')
    
    # Plot Negative Y (Deletions)
    ax.bar(df['Author'], -df['Deletions'], color='red', label='Lines Deleted')

    # Formatting
    ax.set_title(f"Top {top_n} Contributors for {repo}", fontsize=16)
    ax.set_xlabel("Top Users (Sorted by Additions)")
    ax.set_ylabel("Lines of Code")
    ax.axhline(0, color='black', linewidth=1) # Center line
    ax.legend()
    ax.tick_params(axis='x', rotation=45)
    
    fig.tight_layout()
    return fig

# --- 4. SENTIMENT SCATTER PLOT ---
def generate_sentiment_scatter(username: str) -> plt.Figure:
    """Shows Deleterious vs Contributory and Informal vs Formal sentiment."""
    commits = git_parser.get_user_activity(username, pages=2)
    if not commits:
        raise ValueError(f"No recent activity found for user {username}.")
        
    df = pd.DataFrame([c.to_dict() for c in commits])
    
    fig, ax = plt.subplots(figsize=(4, 4))
    
    # Polarity (Negative=Deleterious, Positive=Contributory)
    # Subjectivity (Low=Formal/Objective, High=Informal/Subjective)
    sns.scatterplot(data=df, x='polarity', y='subjectivity', ax=ax, alpha=0.7, color='purple')
    
    # Add quadrants
    ax.axhline(0.5, color='gray', linestyle='--', alpha=0.5)
    ax.axvline(0, color='gray', linestyle='--', alpha=0.5)
    
    ax.set_title(f"Commit Message Sentiment for {username}")
    ax.set_xlabel("Polarity (Deleterious <---> Contributory)")
    ax.set_ylabel("Subjectivity (Formal <---> Informal)")
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-0.1, 1.1)
    
    return fig